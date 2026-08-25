# Advantage

Public Claude Code plugin marketplace for StoreAdOps.

The `storeadops` plugin connects Claude Code to the production StoreAdOps MCP
service. It includes portable workflows for connection setup, performance
review, daily profit reporting, reviewable campaign drafts, and approved growth
action graphs.

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

The live StoreAdOps server remains authoritative for authentication, account
selection, authorization, validation, confirmation, idempotency, and provider
writes. The plugin must not silently switch advertising accounts. Campaign
writes require an exact preview and explicit confirmation, create drafts in
`PAUSED` state, and require provider readback. A timeout is not permission to
retry a write blindly.

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

Report security vulnerabilities privately through this repository's GitHub
Security Advisories.
