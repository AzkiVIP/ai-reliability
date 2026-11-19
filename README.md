# AI Reliability Skill

**Version:** 0.1.0  
**Format:** Agent Skills-style folder (`SKILL.md` + on-demand references)  
**Status:** Initial implementation draft; cross-model behavioural evaluation is still required.

## What it is

A modular behaviour skill designed to help AI assistants be more honest, less sycophantic, more careful with assumptions, stronger at critical thinking, and more effective at learning, brainstorming, research, planning, and verification.

It is not a new model, a guarantee against hallucination, or a security boundary. Results depend on the model, host, tools, context, and how reliably the host loads the skill files.

## Package layout

```text
ai-reliability-skill/
├── SKILL.md
├── README.md
├── COMPATIBILITY.md
├── VERSION.md
├── references/          # 21 focused modules; read only when relevant
├── evaluations/         # test scenarios; not loaded during routine work
├── docs/
│   └── RESEARCH_BASELINE.md
└── scripts/
    └── validate_package.py
```

## Install/use

1. Extract the ZIP.
2. Install or register the **`ai-reliability` folder** with an Agent Skills-compatible host.
3. Keep the `references/` directory beside `SKILL.md`; do not upload only the main file if you expect modular loading.
4. Ask the AI to use `ai-reliability` for tasks involving analysis, learning, ideation, research, planning, or verification.
5. Check that the host can actually read sibling reference files. See `COMPATIBILITY.md`.

For Codex-style repository skills, the folder is commonly placed under `.agents/skills/ai-reliability/`. Other hosts may use a UI, API, or different skills directory. Follow the host's current installation instructions.

## How modules are loaded

`SKILL.md` is the entry point and contains the core rules plus a routing table. The assistant should read only the relevant files in `references/` for the current task. For example:

- Learning Python: `references/learning.md`; add `understanding-user.md` only if the user's level or goal is unclear.
- Brainstorming a product: `references/creative-ideation.md`; add `decision-making.md` when selecting concepts.
- Checking a factual claim: `references/honesty.md`, `references/uncertainty.md`, and `references/research-verification.md` when external verification is warranted.
- Debugging code: `references/systematic-debugging.md` and `references/verification.md`.

Do not load `evaluations/` or the research dossier during ordinary user tasks.

## Validation

Run:

```bash
python scripts/validate_package.py
```

This checks the package structure, required frontmatter, relative reference links, and expected evaluation files. It does not prove that a model follows the instructions or that a specific platform supports dynamic module loading.

## Evaluation

Use `evaluations/README.md` and the scenario files to compare the same model and tasks with/without the skill. Score not only answer correctness but also unjustified agreement, unsupported claims, wrong assumptions, missed/extra clarifications, completion honesty, and unnecessary context/tool overhead.

## Research provenance

`docs/RESEARCH_BASELINE.md` preserves the research dossier that informed this implementation. It records the reviewed public skills, analysis, source register, caveats, and initial test design. Its research snapshot is **18 November 2026**; re-check moving GitHub branches and current platform docs before making claims about their current contents.

## Important limits

- Agent Skills-style packaging is increasingly supported, but there is no guarantee that every AI product can install this format or dynamically read reference files.
- If a host only accepts one prompt or one Markdown file, use `SKILL.md` as the compact core and manually provide only the relevant module(s), or adapt the package to that host.
- Read module files only when relevant. Loading them costs context on hosts that insert their contents into the model context.
- The skill can improve instructions and workflows; it cannot guarantee truth, learning outcomes, safety, or perfect verification.
