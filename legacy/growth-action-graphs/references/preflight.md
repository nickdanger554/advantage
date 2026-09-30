# Client-side preflight

This preflight is non-authoritative. Passing it is not server validation.

## Before submitting a draft

- Use the live manifest's `schema_version` and closed vocabularies.
- Include `reassessment` on every draft, including action and experiment graphs.
- Give a no-action draft evidence references or explicit missing inputs.
- Give an action or experiment at least one node; use no-action when no change is warranted.
- Keep every `action_id` unique and every edge acyclic with valid `from_action_id` and `to_action_id` values.
- Put `name` and `capability_version` inside each MCP tool node's `capability` object.
- Represent money as integer minor units plus explicit currency.
- Use only server-issued opaque references, never raw provider identifiers.
- Keep evidence references attached to the claims they support.
- For experiments, provide the manifest-required experiment fields and leave assignment with the server.

Prefer no-action or request-input when an authoritative input is missing, no active merchant objective defines "better," measurement is broken before a spend increase, or evidence supports only a hypothesis.

## Findings and execution

- A rejection cannot be repaired by rewording.
- A repair creates a new draft and invalidates approval for the old revision.
- A finding is binding even when the agent disagrees.
- Read durable status from `storeadops://action-runs/{run_id}`.
- Never retry `outcome_unknown` or treat a timeout as proof that no effect occurred.
- Never mark manual, request-input, or wait nodes complete.
