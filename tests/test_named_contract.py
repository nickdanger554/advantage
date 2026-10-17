"""Offline contract regressions, not model-behavior or provider E2E claims."""
import copy
import json
from pathlib import Path
import re
import unittest

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "storeadops/skills"
REF = "SYNTHETIC_SELECTED_ACCOUNT_REFERENCE"


class NamedContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads((ROOT / "tests/fixtures/named-contract.json").read_text())
        cls.schemas = json.loads((ROOT / "tests/fixtures/input-schemas.json").read_text())

    def assert_valid(self, tool, request):
        Draft202012Validator(self.schemas[tool], format_checker=FormatChecker()).validate(request)

    def assert_invalid(self, tool, request):
        self.assertTrue(list(Draft202012Validator(self.schemas[tool], format_checker=FormatChecker()).iter_errors(request)))

    def test_all_four_manifests_use_current_public_names(self):
        paths = list(SKILLS.glob("*/manifest.json"))
        self.assertEqual(len(paths), 4)
        self.assertFalse({"query", "prepare_change", "execute_change"} & set(self.contract["tools"]))
        for path in paths:
            manifest = json.loads(path.read_text())
            with self.subTest(skill=manifest["name"]):
                self.assertEqual(manifest["version"], "0.3.0")
                self.assertLessEqual(set(manifest["required_tools"]), set(self.contract["tools"]))
                self.assertEqual(manifest["authority"], "none")

    def test_every_schema_is_valid(self):
        for name, schema in self.schemas.items():
            with self.subTest(tool=name):
                Draft202012Validator.check_schema(schema)

    def test_every_documented_named_tool_has_a_schema_fixture(self):
        documented = set()
        for path in SKILLS.rglob("*.md"):
            documented.update(set(re.findall(r"`([a-z][a-z0-9_]+)`", path.read_text())) & set(self.contract["tools"]))
        self.assertLessEqual(documented, set(self.schemas))

    def test_google_shopping_discovery_does_not_use_microsoft_merchant_tool(self):
        self.assert_valid("query_google_ads", {"channel": "google", "account_ref": REF, "gaql": "SELECT product_link.merchant_center.merchant_center_id FROM product_link LIMIT 10"})
        self.assert_valid("resolve_locations", {"channel": "google", "account_ref": REF, "locations": ["United States"]})
        self.assert_invalid("get_merchant_stores", {"channel": "google", "account_ref": REF, "campaign_type": "shopping"})

    def test_readiness_and_metadata_for_all_six_channels(self):
        self.assert_valid("get_connections_status", {})
        for channel in ("google", "meta", "microsoft", "tiktok", "openai", "shopify"):
            with self.subTest(channel=channel):
                self.assert_valid("get_capabilities", {"channel": channel, "account_ref": REF, "tool_name": "verify_connection", "limit": 5})
                self.assert_valid("verify_connection", {"channel": channel, "account_ref": REF})

    def test_old_discovery_parameters_are_rejected(self):
        for key, value in (("operation", "campaign.create"), ("public_tool", "prepare_change"), ("detail", "contract")):
            with self.subTest(key=key):
                self.assert_invalid("get_capabilities", {"channel": "google", key: value})

    def test_compact_performance_variants(self):
        cases = [
            {"channel": "google", "projection": "campaigns", "start_date": "2026-10-14", "end_date": "2026-10-15", "limit": 2},
            {"channel": "meta", "projection": "account", "since": "2026-10-14", "until": "2026-10-15"},
            {"channel": "tiktok", "campaign_type": "auction", "entity_type": "account", "dimensions": ["account"], "metrics": ["spend", "conversions"], "start_date": "2026-10-14", "end_date": "2026-10-15"},
            {"channel": "openai", "campaign_type": "chat", "entity_type": "account", "dimensions": ["account"], "metrics": ["spend", "conversions"], "start_date": "2026-10-14", "end_date": "2026-10-15"},
        ]
        for request in cases:
            with self.subTest(channel=request["channel"]):
                self.assert_valid("get_performance", {"account_ref": REF, **request})
        self.assert_invalid("get_performance", {"channel": "meta", "account_ref": REF, "projection": "invented"})

    def test_shopify_dated_reads_not_sample_substitution(self):
        self.assert_valid("get_store", {"channel": "shopify", "account_ref": REF})
        self.assert_valid("get_order_report", {"channel": "shopify", "account_ref": REF, "start_date": "2026-10-14", "end_date": "2026-10-15"})
        self.assert_invalid("get_order_report", {"channel": "shopify", "account_ref": REF, "view": "recent"})

    def test_report_start_and_poll_have_distinct_contracts(self):
        for campaign_type in ("search", "audience", "performance_max", "shopping"):
            with self.subTest(campaign_type=campaign_type):
                request = {"channel": "microsoft", "account_ref": REF, "campaign_type": campaign_type, "start_date": "2026-10-14", "end_date": "2026-10-15", "idempotency_key": "synthetic-report-intent"}
                self.assert_valid("start_performance_report", request)
                self.assert_invalid("get_report", request)
        self.assert_valid("get_report", {"report_ref": "SYNTHETIC_EXISTING_REPORT_REFERENCE"})
        self.assert_invalid("start_performance_report", {"report_ref": "SYNTHETIC_EXISTING_REPORT_REFERENCE"})

    def test_reference_examples_use_real_schemas(self):
        content = (SKILLS / "storeadops-campaign-draft/references/call-shapes.md").read_text()
        cases = [json.loads(text) for text in re.findall(r"```json\n(.*?)\n```", content, re.S)]
        self.assertEqual(len(cases), 2)
        for case in cases:
            with self.subTest(tool=case["tool"]):
                self.assert_valid(case["tool"], case["arguments"]["request"])

    def test_shopping_optional_bid_and_execution_binding_shape(self):
        content = (SKILLS / "storeadops-campaign-draft/references/call-shapes.md").read_text()
        change = json.loads(re.findall(r"```json\n(.*?)\n```", content, re.S)[1])["arguments"]["request"]
        self.assertNotIn("cpc_bid", change["google_shopping"])
        self.assertEqual(change["google_shopping"]["initial_status"], "paused")
        request = {"change": change, "plan_ref": "SYNTHETIC_PREPARED_PLAN_REFERENCE", "confirmed": True, "accepted_effects": ["provider_write"], "idempotency_key": "synthetic-plan-intent"}
        # Effect membership/consent/plan identity are enforced at runtime, not by this fixture.
        self.assert_valid("create_google_campaign", request)
        for field in ("change", "plan_ref", "confirmed", "accepted_effects", "idempotency_key"):
            bad = copy.deepcopy(request)
            del bad[field]
            with self.subTest(field=field):
                self.assert_invalid("create_google_campaign", bad)
        self.assert_invalid("create_google_campaign", {**request, "change": {"request": change}})
        self.assert_invalid("prepare_create_google_campaign", {"operation": "campaign.create", "input": change})


if __name__ == "__main__":
    unittest.main()
