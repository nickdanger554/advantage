# Advantage

Public Claude Code plugin marketplace for StoreAdOps.

The `storeadops` plugin connects Claude Code to the production StoreAdOps MCP
service. It can read data from connected Google Ads, Meta Ads, and Shopify
accounts and can perform explicit, user-confirmed advertising and commerce
operations supported by the live server. Its portable workflows cover
connection setup, performance review, daily profit reporting, reviewable
campaign drafts, and approved growth action graphs.

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
- `/storeadops:growth-action-graphs`

Example prompts:

1. `Check which providers and advertising accounts are connected. Do not switch accounts.`
2. `Review the last seven days of advertising performance and prioritize wasted-spend opportunities. Make no changes.`
3. `Prepare a paused Meta campaign draft for the selected account. Show me the exact budget, currency, targeting, and creative preview, but do not write anything until I explicitly confirm it.`
4. `Build a proposed growth action graph from the current evidence and validate it without executing it.`

The live StoreAdOps server remains authoritative for authentication, account
selection, authorization, validation, confirmation, idempotency, and provider
writes. The plugin must not silently switch advertising accounts. Campaign
writes require an exact preview and explicit confirmation, create drafts in
`PAUSED` state, and require provider readback. A timeout is not permission to
retry a write blindly.

## Data and network access

The plugin makes one declared external connection to
`https://app.storeadops.ai/mcp`. StoreAdOps then accesses only the Google Ads,
Meta Ads, and Shopify accounts the user has connected and authorized. Depending
on the requested tool, this may include account metadata, campaigns,
performance metrics, products, inventory, and orders, or an explicitly
confirmed provider change.

The plugin ships no hooks, executables, background monitors, telemetry, package
installers, or credential readers. Browser OAuth is handled by Claude Code and
StoreAdOps. See the privacy policy below for collection, use, retention, and
deletion details.

## Troubleshooting

- **Needs authentication:** open `/mcp` and complete StoreAdOps browser OAuth.
- **Wrong or ambiguous account:** stop and select the intended account in
  StoreAdOps; the plugin must not switch accounts silently.
- **Write rejected:** provide the exact account and parameters, review the
  preview, explicitly confirm it, and use a fresh idempotency key.
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
