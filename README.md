# Advantage

Public Claude Code plugin marketplace for StoreAdOps.

The `storeadops` plugin connects Claude Code to production StoreAdOps ads-v3
through named, typed tools. Four skills cover account setup, performance reviews,
daily profit briefs and exact campaign-change previews. Google Ads, Meta,
Microsoft Advertising, TikTok and OpenAI Ads depend on selected-account,
permission, feature and campaign-type gates. Shopify commerce is read-only.

## Install and update

```text
/plugin marketplace add nickdanger554/advantage
/plugin install storeadops@advantage
/reload-plugins
```

For an existing installation:

```bash
claude plugin marketplace update advantage
claude plugin update storeadops@advantage --scope user
```

Restart Claude Code or run `/reload-plugins`, then check `/mcp`. Complete browser
OAuth if requested; never paste a credential into a prompt. The MCP URL remains
`https://app.storeadops.ai/mcp/packs/ads-v3`. OAuth connectivity, package
installation and successful conversations are separate checks.

## Four workflows

- `/storeadops:storeadops-get-started`: verify selected accounts and available actions.
- `/storeadops:storeadops-performance-review`: explain performance with bounded evidence.
- `/storeadops:storeadops-daily-profit-brief`: dated store/ads coverage with honest profit gaps.
- `/storeadops:storeadops-campaign-draft`: prepare exact previews; execute only after explicit confirmation.

Try: "Check which accounts are connected. Do not switch accounts."
Or: "Review the last completed week's performance. No changes or report jobs."
For a preview: "Prepare a paused Google Shopping proposal. Ask for missing
inputs; do not execute."

## Version 0.6.5

All four skills now use the live named-tool contract. The generic dispatchers
are retired; readiness uses `get_capabilities(tool_name=...)`, not hidden
operation discovery. Reports start only through `start_performance_report`
with approval for the exact batch; `get_report` only polls existing jobs.
Preparation uses a matching `prepare_*` tool; its returned named execution tool
requires the unchanged typed `change`, plan, exact effects, explicit
confirmation and durable idempotency. A preview is not a provider write.

This release also declares the existing privacy-policy URL to address the
directory's metadata finding. The endpoint, OAuth configuration, logo and
license are unchanged. No backend deployment or OpenAI submission is included.
See [validation, provenance and rollback](docs/releases/0.6.5.md). Older release
notes are historical and do not describe the current tool contract.

## Boundaries

No silent account switching, invented identifiers, autonomous spending or
Shopify mutations. New delivery objects in the draft workflow remain paused.
Activation, resuming or budget increases require a separate explicit request
and their own exact preview/confirmation. An uncertain write is reconciled with
its original plan/key, never blindly retried with a new key.

Report-job creation is a non-spending provider effect, not an ordinary read.
Incomplete pagination, unknown timezone, in-progress days, missing costs and
incompatible attribution/currency remain explicit gaps. Revenue is not profit.
Live server schemas and authorization always take precedence over this guidance.

## Data and network access

The package declares only the production StoreAdOps MCP connection above.
StoreAdOps accesses the advertising and Shopify accounts the user connected
and authorized, for the requested reads, approved report jobs or confirmed
changes. The package ships no hooks, executables, background monitors,
telemetry, installers or credential readers. Repository tests and release
utilities are outside the installed `storeadops/` package.

## Support and removal

For authentication, use `/mcp`; for wrong/ambiguous selection, choose the intended
account in StoreAdOps. Do not reconnect to bypass a gate. Report sanitized errors
to [support@storeadops.ai](mailto:support@storeadops.ai); never include credentials,
opaque references or customer data in a public issue.

```bash
claude plugin uninstall storeadops@advantage --scope user
claude plugin marketplace remove advantage --scope user
```

## Service policies

- [Privacy policy](https://app.storeadops.ai/privacy)
- [Terms of service](https://app.storeadops.ai/terms)
- [Support](https://app.storeadops.ai/support)
- [Security](https://app.storeadops.ai/security)

Report vulnerabilities privately through GitHub Security Advisories. The public
plugin is MIT-licensed; private backend code and provider/account data are not
licensed by this package.
