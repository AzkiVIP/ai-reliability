# Systematic debugging

## Purpose
Use when diagnosing bugs, failed commands, incorrect output, build failures, regressions, or unexpected system behaviour.

## Evidence-first process

1. **Capture the symptom.** Record exact error text, observed behaviour, environment, versions, recent changes, and reproduction steps.
2. **Inspect before editing.** Read the relevant code, logs, configuration, documentation, and known working examples.
3. **Reproduce when practical.** Establish a minimal reliable reproduction. If reproduction is impossible, state what evidence is available.
4. **Locate the failure boundary.** Determine which component or stage first behaves incorrectly.
5. **Form a hypothesis.** Explain the evidence supporting it and what observation would disprove it.
6. **Test one meaningful change at a time.** Avoid simultaneous speculative edits that obscure causality.
7. **Verify the fix.** Re-run the reproduction and relevant regression tests after the final relevant change.
8. **Report residual risk.** Mention untested paths, environment limits, or likely follow-up checks.

## Rules

- Do not guess a fix from the error's wording alone when source or logs are available.
- Do not repeatedly change code without updating the hypothesis.
- Compare with known-working examples or version-specific official documentation when useful.
- Distinguish root cause from workaround or mitigation.
- In urgent situations, a safe containment step may be appropriate before full root-cause analysis; document that it is a mitigation, not a confirmed fix.
- Do not claim the issue is solved unless the relevant behaviour has been checked.
