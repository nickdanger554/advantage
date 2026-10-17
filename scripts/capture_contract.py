"""Capture public JSON schemas from the pinned local server; no network I/O."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-root", type=Path, required=True)
    args = parser.parse_args()
    expected = json.loads((ROOT / "tests/fixtures/named-contract.json").read_text())
    actual = subprocess.check_output(["git", "-C", str(args.server_root), "rev-parse", "HEAD"], text=True).strip()
    assert actual == expected["source"]["commit"], "server checkout does not match contract pin"
    sys.path.insert(0, str(args.server_root / "src"))
    from advantage_mcp.ads_v3.public_tools import BY_NAME, TOOL_NAMES
    from advantage_mcp.ads_v3.server import ConnectionsRequest, CapabilitiesRequest, GetReportRequest, ChangeStatusRequest
    from advantage_mcp.ads_v3.models import MerchantProfileRequest, RecordRecommendation, RecommendationHistoryRequest
    from pydantic import TypeAdapter
    controls = {"get_connections_status": ConnectionsRequest, "get_capabilities": CapabilitiesRequest,
                "get_report": GetReportRequest, "get_change_status": ChangeStatusRequest,
                "get_merchant_profile": MerchantProfileRequest, "record_recommendation": RecordRecommendation,
                "get_recommendation_history": RecommendationHistoryRequest}
    names = set(controls)
    for path in (ROOT / "storeadops/skills").glob("*/manifest.json"):
        names.update(json.loads(path.read_text())["required_tools"])
    for path in (ROOT / "storeadops/skills").rglob("*.md"):
        names.update(set(re.findall(r"`([a-z][a-z0-9_]+)`", path.read_text())) & set(TOOL_NAMES))
    schemas = {name: TypeAdapter(controls[name] if name in controls else BY_NAME[name].request_model).json_schema()
               for name in sorted(names)}
    assert set(expected["tools"]) == set(TOOL_NAMES)
    (ROOT / "tests/fixtures/input-schemas.json").write_text(json.dumps(schemas, sort_keys=True, separators=(",", ":")) + "\n")
    print(f"Captured {len(schemas)} real input schemas from {actual[:7]}; no calls executed")


if __name__ == "__main__":
    main()
