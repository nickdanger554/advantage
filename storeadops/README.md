# StoreAdOps for Claude

StoreAdOps connects Claude to the ten-tool production ads-v3 interface.
Google Ads, Meta, Microsoft Advertising, TikTok, and OpenAI Ads operations are
subject to account-specific capability, permission and feature gates. Shopify
commerce access is read-only. The four included skills cover onboarding,
performance review, daily briefs with explicit data gaps, and campaign changes.

In Claude chat, enable the StoreAdOps connector and complete browser OAuth.
In Claude Code, after installation, open `/mcp` and complete browser OAuth. Start with
`/storeadops:storeadops-get-started` to verify connections and select the
intended account before requesting analysis or a campaign draft.

This plugin contains no credentials and does not enforce server policy. The live
server controls identity, authorization, confirmation, idempotency, and provider
writes. Never paste credentials into Claude Code.

The plugin makes one declared external connection to
`https://app.storeadops.ai/mcp/packs/ads-v3`. Upgrades from the old MCP resource
may require OAuth again. The plugin never asks for tokens in a prompt.
It ships no hooks, executables, background
monitors, telemetry, package installers, or credential readers.

Read account-specific contracts before using an operation. Preparing a plan
does not execute a provider write. Execution requires explicit confirmation of
the exact preview, accepted effects, idempotency and provider readback. New
advertising objects stay paused; enabling delivery requires a separate request
and its own preview and confirmation. Never retry ambiguous writes blindly.

Legacy growth action graphs are not exposed by this ten-tool package. Report
unsupported operations honestly instead of inventing tools or outcomes.

## Package license

The files in this public plugin directory are distributed under the
[MIT License](LICENSE). This license does not cover the private StoreAdOps
server, account data, provider data, or access to the hosted service.

- [StoreAdOps](https://app.storeadops.ai)
- [Privacy policy](https://app.storeadops.ai/privacy)
- [Terms of service](https://app.storeadops.ai/terms)
- [Support](https://app.storeadops.ai/support)
- [Security](https://app.storeadops.ai/security)
- [Email support](mailto:support@storeadops.ai)
