# StoreAdOps for Claude Code

StoreAdOps connects Claude Code to Google Ads, Meta Ads, and Shopify through the
production StoreAdOps MCP service. It can read connected account data and
perform explicit, user-confirmed advertising and commerce operations supported
by the live server.

After installation, open `/mcp` and complete browser OAuth. Start with
`/storeadops:storeadops-get-started` to verify connections and select the
intended account before requesting analysis or a campaign draft.

This plugin contains no credentials and does not enforce server policy. The live
server controls identity, authorization, confirmation, idempotency, and provider
writes. Never paste credentials into Claude Code.

The plugin makes one declared external connection to
`https://app.storeadops.ai/mcp`. It ships no hooks, executables, background
monitors, telemetry, package installers, or credential readers.

- [StoreAdOps](https://app.storeadops.ai)
- [Privacy policy](https://app.storeadops.ai/privacy)
- [Terms of service](https://app.storeadops.ai/terms)
- [Support](https://app.storeadops.ai/support)
- [Security](https://app.storeadops.ai/security)
- [Email support](mailto:support@storeadops.ai)
