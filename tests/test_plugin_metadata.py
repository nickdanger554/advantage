"""Offline checks for public Claude directory metadata; no provider I/O."""

import json
from pathlib import Path
import unittest
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
PRIVACY_URL = "https://app.storeadops.ai/privacy"


class PluginMetadataTests(unittest.TestCase):
    def setUp(self):
        self.plugin = json.loads(
            (ROOT / "storeadops/.claude-plugin/plugin.json").read_text()
        )
        self.marketplace = json.loads(
            (ROOT / ".claude-plugin/marketplace.json").read_text()
        )

    def test_remote_plugin_declares_privacy_policy(self):
        self.assertEqual(self.plugin.get("privacyPolicyUrl"), PRIVACY_URL)
        url = urlsplit(self.plugin["privacyPolicyUrl"])
        self.assertEqual(url.scheme, "https")
        self.assertEqual(url.netloc, "app.storeadops.ai")
        self.assertFalse(url.query or url.fragment)

    def test_readmes_retain_privacy_link_fallback(self):
        for path in (ROOT / "README.md", ROOT / "storeadops/README.md"):
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(any(
                    "privacy" in line.lower() and f"]({PRIVACY_URL})" in line
                    for line in path.read_text().splitlines()
                ))

    def test_marketplace_and_plugin_versions_match(self):
        entries = [
            p for p in self.marketplace["plugins"]
            if p["name"] == self.plugin["name"]
        ]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["source"], "./storeadops")
        self.assertEqual(entries[0]["version"], self.plugin["version"])

    def test_directory_only_field_is_not_in_marketplace(self):
        # Anthropic supports this listing field in plugin.json, not an entry.
        for entry in self.marketplace["plugins"]:
            self.assertNotIn("privacyPolicyUrl", entry)

    def test_production_mcp_connection_is_unchanged(self):
        mcp = json.loads((ROOT / "storeadops/.mcp.json").read_text())
        self.assertEqual(mcp, {"mcpServers": {"storeadops": {
            "type": "http",
            "url": "https://app.storeadops.ai/mcp/packs/ads-v3",
        }}})


if __name__ == "__main__":
    unittest.main()
