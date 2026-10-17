# Named tool call shapes

Read this when constructing a preparation or resolving an input error. The live
host tool schema wins; examples below are synthetic, not account discoveries.
Replace every placeholder with an authorized read or a confirmed user input.
Never send placeholder references or synthetic merchant/location IDs to a provider.

## Readiness versus schema

`get_capabilities` accepts `request.channel`, `request.account_ref`, optional
`request.tool_name`, `request.limit` and `request.offset`. It reports readiness.
The complete input schema comes from the named tool exposed by the host, not
from `detail="contract"` or an `operation` selector.

```json
{"tool":"get_capabilities","arguments":{"request":{"channel":"google","account_ref":"REPLACE_WITH_SELECTED_ACCOUNT_REF","tool_name":"prepare_create_google_campaign"}}}
```

## Google Standard Shopping preview

Read `query_google_ads` on `product_link` for linked Merchant Center IDs and
`resolve_locations` with their actual schemas before filling identifiers.
`get_merchant_stores` is Microsoft-only. The amount is a decimal string in account
currency; this is not Meta's minor-unit budget format. Maximize Clicks can omit
the optional manual child `cpc_bid`. Do not invent a strategy CPC cap. A Merchant
Center `feed_label` is separate from location targeting; omit it unless verified
from the intended feed or explicitly supplied by the user.

```json
{"tool":"prepare_create_google_campaign","arguments":{"request":{"channel":"google","account_ref":"REPLACE_WITH_SELECTED_ACCOUNT_REF","campaign_type":"shopping","name":"Synthetic paused Shopping draft","budget":{"amount":"10","currency":"USD","period":"daily"},"bidding":{"strategy":"max_clicks"},"google_target_location_ids":["2840"],"google_shopping":{"merchant_id":"1234","initial_status":"paused"}}}}
```

This example is not authorization to create a campaign. Preparation stores a
plan but makes no provider write. Keep the exact typed `request` and inspect the
returned preview, `plan_ref`, `execution_tool` and `execution.accepted_effects`.
Reject an unexpected active status or scope expansion, including nested objects.

## Execution after explicit approval only

Use the execution tool returned by preparation, not a guessed generic name.
Its `request` contains `change` (the unchanged preparation request), `plan_ref`,
`confirmed: true`, `accepted_effects` copied exactly from that plan, and a fresh
`idempotency_key` for the new intent. Do not wrap `change` in another `request`.
Changing a budget, target, projection or account requires a new preview and
approval. A paused draft request never authorizes activation.

For a preview-only request, do not execute even if a host permission dialog
allows the tool. For an uncertain execution, retain the original plan/key and
use `get_change_status`; do not manufacture a fresh-key retry or roll back
successful steps without direction.

## Read and report variants

Google campaign `get_performance` uses `projection="campaigns"`; Meta account
performance uses `projection="account"`. Other variants have their own selectors.
Use `start_performance_report` only for an approved report-job batch, then
`get_report` with its returned `report_ref`. Polling never requires a new job.
