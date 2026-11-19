# Maintenance notes

## What must remain true

- The main skill remains a router and behavioural core, not a copy of every reference.
- A reference is loaded only when its trigger applies.
- Learning and creative ideation remain first-class capabilities.
- Anti-sycophancy must not become reflexive disagreement.
- Clarification must be based on materiality, not a demand for certainty.
- Verification claims must match actual evidence.
- Platform compatibility must be tested, not inferred from file format alone.

## When adding a module

Create a new module only if it represents a distinct workflow that cannot be kept clearer inside an existing reference. Add a trigger to the module router, one or more evaluation cases, and update the validator's expected file list. Avoid fragmenting the system into tiny files that increase routing overhead.

## When changing behaviour

1. Identify the failing evaluation case.
2. Determine whether the problem is a missing rule, poor routing, conflicting instructions, or host limitation.
3. Change the smallest responsible file.
4. Re-run validation and the affected evaluation cases.
5. Check for regressions in token efficiency and other task types.
6. Record meaningful changes in a changelog.

## Known limitation

This package has been structurally checked but has not yet been benchmarked across target models/hosts. Do not claim measured gains until comparative tests are run.
