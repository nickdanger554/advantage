# Authority boundary

This skill is guidance and client-side preflight. It has no authority.

## Never

- Decide that policy passed; only the server evaluator and constraint tools can do that.
- Mint evidence, approval, grants, references, or validation receipts.
- Override or reinterpret a server finding.
- Mark a manual, request-input, or wait node complete.
- Claim execution or outcome success from a returned call alone.
- Store credentials, tenant data, account identifiers, or provider snapshots.
- Become required for correctness; the typed server workflow must remain complete without it.

The skill contains no executable code and cannot call a tool, hold credentials, or alter a request. Server enforcement is identical whether the skill is installed or absent. When a client-side preflight fails, describe it as guidance—not validation, approval, or a safety guarantee.
