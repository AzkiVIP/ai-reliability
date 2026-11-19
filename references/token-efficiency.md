# Token and context efficiency

## Purpose
Use to reduce unnecessary context use, repetition, tool calls, and verbosity without reducing answer quality.

## Core principle
Optimise for **minimum sufficient context and output**, not minimum possible word count. Excessive compression can hide assumptions, omit caveats, or make instructions unusable.

## Practices

1. Load only the reference modules relevant to the present task.
2. Do not load evaluation files or the full research dossier during routine work.
3. Avoid restating facts, requirements, or conclusions already clear in the conversation.
4. Ask only material questions; do not turn every uncertainty into a question.
5. Do not browse, test, calculate, or call tools repeatedly without a clear information gain.
6. Reuse verified findings and existing files when current and applicable; re-check only when facts may have changed or the new task demands it.
7. Match response depth to complexity, risk, and the user's requested format.
8. Use tables only when they improve comparison; use prose for straightforward answers.
9. For long work, maintain a compact state summary instead of repeatedly reconstructing the entire history.
10. Keep long examples, templates, and specialist procedures in reference files rather than the main skill.

## Measure rather than promise
A Markdown reference file does not have zero token cost when read. Token cost depends on the host's loader and model context. Measure actual usage where possible. Compare baseline and skill-enabled runs on the same task, and remove low-value instructions or unnecessary module loads if overhead grows without corresponding quality gains.

## Do not optimise away
Never omit a material uncertainty, safety constraint, required clarification, or verification step solely to save tokens.
