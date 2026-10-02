# Advantage

Public Claude Code plugin marketplace for StoreAdOps.

The `storeadops` plugin connects Claude Code to the production StoreAdOps MCP
service through the separately versioned, ten-tool ads-v3 interface. Google
Ads, Meta, Microsoft Advertising, TikTok, and OpenAI Ads operations are available
only when the selected account, permissions, feature gates, and campaign type
support them. Shopify commerce access is read-only. Four portable workflows
cover connection setup, performance review, daily briefs, and exact campaign
change previews. No provider is considered ready merely because it is listed.

## Install

In Claude Code, run:

```text
/plugin marketplace add nickdanger554/advantage
/plugin install storeadops@advantage
/reload-plugins
```

Open `/mcp` and complete the StoreAdOps browser OAuth flow. Never paste an API
key, OAuth token, advertising credential, or store credential into a prompt.

Verify the installation:

```bash
claude plugin details storeadops@advantage
claude mcp list
```

## Use

StoreAdOps skills are namespaced under `storeadops`:

- `/storeadops:storeadops-get-started`
- `/storeadops:storeadops-performance-review`
- `/storeadops:storeadops-daily-profit-brief`
- `/storeadops:storeadops-campaign-draft`

Example prompts:

1. `Check which providers and advertising accounts are connected. Do not switch accounts.`
2. `Review the last seven days of advertising performance and prioritize wasted-spend opportunities. Make no changes.`
3. `Prepare a paused Meta campaign draft for the selected account. Show me the exact budget, currency, targeting, and creative preview, but do not write anything until I explicitly confirm it.`
4. `Explain which Microsoft Advertising and TikTok operations my selected accounts support. Do not create report jobs or make changes.`

The live StoreAdOps server remains authoritative for authentication, account
selection, authorization, validation, confirmation, idempotency, and provider
writes. The plugin must not silently switch advertising accounts. A change
requires an exact `prepare_change` preview and explicit confirmation of that
preview before `execute_change`. New advertising objects are created paused.
The write path uses durable idempotency and provider readback; a timeout is not
permission to retry blindly. Report creation may be a separate non-spending
provider effect and must not be described as an ordinary read.

Data gaps are explicit. Missing revenue, costs, margin, attribution, or currency
must not be filled with invented figures, and an empty account is not an error
or proof of production readiness.

## Version 0.6.1 scope

This package migrates the declared endpoint and four core skills to ads-v3.
The old growth-action-graphs workflow requires V1-only tools and is not bundled
in the ads-v3 plugin. Its source is retained under `legacy/growth-action-graphs`
for reference, not loaded as a skill, and not claimed as an ads-v3 capability.
No server or provider capability is implemented or removed by this package.
Do not use legacy graph grants or tool names as substitutes for ads-v3 plans.

The four workflows share the same canonical guidance as the current StoreAdOps
OpenAI package, with a Claude-specific namespacing overlay. They use exact
discovered operation names and request envelopes, bounded reads, explicit
permission for provider report jobs, and in-chat confirmation of an exact change
preview. Missing data, stale account references, unsupported settings and
uncertain write outcomes are handled explicitly.

GitHub availability, directory acceptance, OAuth connectivity and successful
Claude conversations are separate checks. Package validation does not establish
marketplace approval or conversation-level E2E certification. See
[release validation and limitations](docs/releases/0.6.1.md).

## Data and network access

The plugin makes one declared external connection to
`https://app.storeadops.ai/mcp/packs/ads-v3`. StoreAdOps accesses only the
advertising and Shopify accounts the user has connected and authorized. Depending
on the requested operation, this may include account metadata, campaigns,
performance metrics, products, inventory and orders, a provider report job, or
an explicitly confirmed advertising change. This package does not provide
Shopify mutations, payment actions or autonomous spending.

The plugin ships no hooks, executables, background monitors, telemetry, package
installers, or credential readers. Browser OAuth is handled by Claude Code and
StoreAdOps. See the privacy policy below for collection, use, retention, and
deletion details.

## Troubleshooting

- **Needs authentication:** open `/mcp` and complete StoreAdOps browser OAuth.
- **Upgrading from 0.5.1:** the MCP resource URL changes to ads-v3. Complete
  OAuth for the new resource when prompted; an old connection is not proof
  that the new resource is authorized. Do not paste tokens into configuration.
- **Wrong or ambiguous account:** stop and select the intended account in
  StoreAdOps; the plugin must not switch accounts silently.
- **Write rejected:** inspect the returned issues and live operation contract.
  A terminal refusal requires a corrected new plan, not replay of a rejected
  plan. Never turn an uncertain outcome into a fresh-key retry.
- **Timeout or `outcome_unknown`:** do not retry the write. Read provider state
  back or reconcile by idempotency key first.
- **Installation or account support:** contact
  [support@storeadops.ai](mailto:support@storeadops.ai) or open a GitHub issue
  that contains no credentials, account identifiers, or customer data.

## Update

```bash
claude plugin marketplace update advantage
claude plugin update storeadops@advantage --scope user
```

Restart Claude Code or run `/reload-plugins`, then recheck `/mcp`.

## Remove

```bash
claude plugin uninstall storeadops@advantage --scope user
claude plugin marketplace remove advantage --scope user
```

## Service policies

- [Privacy policy](https://app.storeadops.ai/privacy)
- [Terms of service](https://app.storeadops.ai/terms)
- [Support](https://app.storeadops.ai/support)
- [Security](https://app.storeadops.ai/security)

Report security vulnerabilities privately through this repository's GitHub
Security Advisories.
