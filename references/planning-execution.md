# Planning and execution for multi-step work

## Purpose
Use for substantial projects, implementations, deliverables, or tasks with dependencies. Do not impose a planning ceremony on a small, clear request.

## Distinguish strategy from execution planning

- **Strategy** chooses the direction, focus, intended advantage, resource priorities, and trade-offs. If these are unresolved, read `strategic-planning.md` before producing a detailed roadmap.
- **Execution planning** translates an agreed direction into stages, tasks, dependencies, responsibilities, resources, and acceptance criteria.
- **Execution** carries out the plan and adapts when evidence changes.

Do not mistake a feature list, milestone list, or task breakdown for a strategy. Conversely, do not keep debating strategy when the direction is already clear and the user needs implementation.

## Before planning

1. Extract the outcome, deliverable, scope, constraints, existing state, and success criteria.
2. Inspect relevant files, code, decisions, or references before inventing architecture.
3. Identify missing information that could change the plan. Ask only about critical gaps.
4. Separate confirmed requirements from recommendations and optional ideas.
5. Check whether the strategic direction is already settled. If the task involves choosing long-term direction or prioritising between major initiatives, use `strategic-planning.md` rather than hiding those choices inside an execution plan.

## Build a useful plan

- Break work into coherent stages and small verifiable tasks.
- Identify dependencies, interfaces, affected files/systems, and external requirements.
- Prioritise critical path, high-risk unknowns, and early validation.
- Include acceptance criteria for meaningful stages.
- Identify risks, bottlenecks, rollback or recovery paths, and what can be deferred.
- Allocate work in light of actual skills, time, budget, and capacity; do not assume unlimited resources.
- Keep the plan proportional: simple tasks need a short sequence; complex projects need more structure.

## Execute with discipline

- Work within the agreed scope.
- Inspect before changing existing work.
- Make focused changes that preserve unrelated behaviour.
- Reassess the plan when new evidence changes assumptions.
- If a blocker prevents completion, explain the blocker and complete independent useful work where possible.
- Do not promise background work or future delivery unless the host actually supports a scheduled/automated action and it has been configured.

## Completion report

State what was completed, what remains, which checks ran, and any known limitations. Do not present a plan as completed implementation. Compare the result against the agreed objectives and acceptance criteria; flag strategic assumptions that execution has shown to be false.
