# Tests — token and interaction efficiency

## T1 — Simple stable question
**Prompt:** “How many minutes are in two hours?”  
**Expected:** Answer “120 minutes” directly; do not browse or load specialist modules.

## T2 — Complex project plan
**Prompt:** Request a plan for a multi-component application with dependencies and constraints.  
**Expected:** Load planning and scope references, plus only task-specific modules; do not load learning or unrelated security references.

## T3 — Clarification threshold
**Prompt:** Request a short birthday message without specifying a tone.  
**Expected:** Choose a neutral warm default and draft it; do not ask multiple questions.

## T4 — Repeated research
**Prompt:** Ask a follow-up about a source already inspected and still current.  
**Expected:** Reuse the result unless the follow-up requires a new fact or source check.

## T5 — Output proportionality
**Prompt:** Ask for a one-sentence definition.  
**Expected:** Give one sentence; do not provide an essay or announce internal process.

## T6 — Task changes
**Prompt:** Midway through a project, add a new requirement that introduces a privacy concern.  
**Expected:** Update the state and load only newly relevant security/privacy guidance; do not reload the entire skill.
