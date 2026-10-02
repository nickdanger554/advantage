# ads-v3 call shapes

Use these envelopes to avoid mixing public tools, operations, and legacy source
names. These are illustrative inputs, not permission to create a campaign.
The live contract is authoritative. Replace `<selected_account_ref>` with the
opaque reference from the intended selected account, never a guessed ID.

## Discover one exact contract

Tool: `get_capabilities`

```json
{
  "request": {
    "channel": "google",
    "account_ref": "<selected_account_ref>",
    "operation": "campaign.create",
    "detail": "contract"
  }
}
```

Read `input_schema` and the matching `campaign_types` entry. Its `example` is
the inner `input`, not a whole tool call. Copy the advertised `operation`;
do not copy the legacy `create_campaign` name from migration metadata.

## Prepare a campaign-only Search shell

Only use this example after the user has chosen this account, campaign name,
USD 10/day, United States targeting and Maximize Clicks, and the current contract
supports them. The location value is a provider location code, not an account ID.
No Manual CPC cap, ads, keywords or landing page are represented by this call.
Never replace a requested unsupported bidding strategy with Maximize Clicks
without the user's agreement.

Tool: `prepare_change`

```json
{
  "request": {
    "operation": "campaign.create",
    "input": {
      "channel": "google",
      "account_ref": "<selected_account_ref>",
      "campaign_type": "search",
      "name": "Example Search draft",
      "budget": {"amount": "10.00", "currency": "USD", "period": "daily"},
      "bidding": {"strategy": "max_clicks"},
      "google_target_location_ids": ["2840"]
    }
  }
}
```

Require successful preparation and inspect the returned paused-state preview.
If no `plan_ref` was returned, report an unsaved proposal or a preparation error,
not a created draft. Do not send `confirmed`, `accepted_effects` or
`idempotency_key` inside this preparation input.

## Confirmation and result

For preview-only requests, stop here. Otherwise show the returned preview in
chat and obtain approval. Build `execute_change.request` from the returned
`plan_ref`, `execution.accepted_effects`, a fresh idempotency key for the new
intent, and `confirmed=true`. Never invent acceptance codes or reuse a sample
plan reference. No extra website approval step is needed.

After an uncertain response, use `get_change_status.request.plan_ref` for that
same plan; retain the original idempotency key. A successful transport response
is not sufficient: inspect the tool envelope, final change status and provider
readback before reporting success.
