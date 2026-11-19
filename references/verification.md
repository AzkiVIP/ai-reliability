# Verification before completion claims

## Purpose
Use whenever the assistant produces a deliverable or claims that a task, fix, analysis, or change is complete.

## Match verification to the claim

- **Code change:** inspect the diff; run relevant tests, build, or reproduction where possible.
- **Bug fix:** reproduce the original failure and verify the corrected behaviour after the final relevant change.
- **Research:** check that important claims map to accessible, relevant sources and that dates/scope are correct.
- **Document or file:** confirm the file exists, opens or parses where practical, and contains the requested sections/content.
- **Calculation:** recompute independently or use a reliable calculation method for consequential results.
- **Plan/specification:** compare against the user's requirements and acceptance criteria.

## Evidence ladder
Report only the level reached:

1. **Inspected:** reviewed the relevant output or change.
2. **Static check:** validated structure, syntax, or constraints without executing the full system.
3. **Executed:** ran the relevant command or workflow.
4. **Tested:** ran defined tests and observed results.
5. **End-to-end verified:** checked the actual user-facing flow in a representative environment.

These labels are illustrative; use the host's natural wording, but preserve the distinction.

## Rules

- Verify after the final relevant change, not only before it.
- Re-run a check when changed code or content could invalidate its previous result; do not repeat identical tests without a reason.
- State skipped tests and environment limitations.
- A passing test suite does not prove absence of all defects; report its actual scope.
- Do not use “complete”, “fixed”, “works”, or “verified” more broadly than the evidence allows.
