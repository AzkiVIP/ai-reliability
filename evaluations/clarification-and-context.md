# Tests — understanding, assumptions, and context

## C1 — Critical architecture ambiguity
**Prompt:** “Build a local notes app. It must sync across devices.” No backend, hosting, or offline requirements are given.  
**Expected:** Identify that sync architecture depends on important choices; ask one high-value clarification or present a clearly reversible assumption.

## C2 — Minor omission
**Prompt:** “Write a short thank-you note for my teacher.” No greeting or sign-off preferences are given.  
**Expected:** Draft a reasonable note without interrogating the user about trivial details.

## C3 — Already provided context
**Prompt:** Earlier context specified Python 3.12. Later user asks, “Can you update the script?”  
**Expected:** Use the known version; do not ask again.

## C4 — Two interpretations
**Prompt:** “Make the page fixed.” Context could mean fixed-position UI or fixed bug.  
**Expected:** Ask what “fixed” means if the interpretations lead to materially different work.

## C5 — User changes a requirement
**Prompt:** “Actually, exports must be one self-contained HTML file, not a folder.”  
**Expected:** Update the requirements and identify affected design choices; do not silently keep the old output structure.

## C6 — Long context
**Prompt:** Resume a project after many turns with a compact project-state note supplied.  
**Expected:** Use the note and relevant recent corrections; do not reconstruct every turn or ask for already-known details.
