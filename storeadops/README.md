# StoreAdOps for Claude

StoreAdOps connects Claude to the production ads-v3 named-tool interface.
Four skills cover selected-account setup, performance review, daily profit
briefs and exact campaign-change previews. Google Ads, Meta, Microsoft
Advertising, TikTok and OpenAI Ads depend on account-specific gates; Shopify
commerce access is read-only.

In Claude chat, enable the StoreAdOps connector and complete browser OAuth.
In Claude Code, use `/mcp` after installation, then start with
`/storeadops:storeadops-get-started`. Never paste credentials into chat.

The complete schemas come from the host's live named tools. Readiness uses
`get_capabilities` with `tool_name`. Preparation uses matching `prepare_*`
tools and saves a preview without provider writes. Execution requires the
returned named action, unchanged typed change, exact plan/effects, explicit
in-chat confirmation, durable idempotency and verified provider readback.
Draft delivery objects remain paused; activation needs a separate request and
its own preview/confirmation. Never retry an uncertain write blindly.

`start_performance_report` creates an explicitly approved report job;
`get_report` polls an existing job only. Revenue samples are not exact revenue,
and revenue or ROAS is not profit. Unknown coverage is unavailable, not zero.
Legacy generic dispatchers and growth action graphs are not callable tools.

This plugin declares one external connection:
`https://app.storeadops.ai/mcp/packs/ads-v3`. It ships no hooks, executables,
monitors, telemetry, installers or credential readers. The server, not the
skills, enforces identity, authorization, input validation and effects.

## Package license and policies

The public plugin directory is distributed under the [MIT License](LICENSE).
This does not license private server code, account/provider data or hosted access.

- [StoreAdOps](https://app.storeadops.ai)
- [Privacy policy](https://app.storeadops.ai/privacy)
- [Terms of service](https://app.storeadops.ai/terms)
- [Support](https://app.storeadops.ai/support)
- [Security](https://app.storeadops.ai/security)
- [Email support](mailto:support@storeadops.ai)
