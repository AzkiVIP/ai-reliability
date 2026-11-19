#!/usr/bin/env python3
"""Validate the AI Reliability Agent Skill package using only Python's standard library."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
EXPECTED_REFERENCES = {
    "honesty.md", "uncertainty.md", "understanding-user.md",
    "assumption-clarification.md", "critical-thinking.md", "devils-advocate.md",
    "decision-making.md", "research-verification.md", "learning.md",
    "creative-ideation.md", "planning-execution.md", "systematic-debugging.md",
    "context-management.md", "token-efficiency.md", "error-recovery.md",
    "scope-discipline.md", "tool-discipline.md", "verification.md",
    "security.md", "action-boundaries.md", "outcome-oriented.md",
}
EXPECTED_EVALS = {
    "README.md", "honesty-and-sycophancy.md", "clarification-and-context.md",
    "reasoning-and-decisions.md", "research-and-verification.md",
    "learning-and-ideation.md", "execution-and-security.md", "token-efficiency.md",
}

errors = []
if not SKILL.is_file():
    errors.append("Missing SKILL.md")
    text = ""
else:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append("Malformed YAML frontmatter delimiters")
        else:
            fm = parts[1]
            name = re.search(r"^name:\s*([^\s]+)\s*$", fm, re.M)
            desc = re.search(r"^description:\s*(.+)$", fm, re.M)
            if not name:
                errors.append("Frontmatter missing name")
            else:
                skill_name = name.group(1)
                if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_name):
                    errors.append(f"Invalid skill name format: {skill_name}")
                if skill_name != ROOT.name:
                    errors.append(f"Skill name '{skill_name}' does not match folder '{ROOT.name}'")
            if not desc or not desc.group(1).strip():
                errors.append("Frontmatter missing non-empty description")
            elif len(desc.group(1).strip()) > 1024:
                errors.append("Description exceeds 1024 characters")

for filename in sorted(EXPECTED_REFERENCES):
    if not (ROOT / "references" / filename).is_file():
        errors.append(f"Missing reference: references/{filename}")

# Every .md filename explicitly mentioned in the router must exist in references/.
skill_body = SKILL.read_text(encoding="utf-8") if SKILL.exists() else ""
for filename in sorted(set(re.findall(r"`([a-z][a-z-]*\.md)`", skill_body))):
    if not (ROOT / "references" / filename).is_file():
        errors.append(f"SKILL.md references missing module: {filename}")
for filename in sorted(EXPECTED_EVALS):
    if not (ROOT / "evaluations" / filename).is_file():
        errors.append(f"Missing evaluation: evaluations/{filename}")

# Validate relative Markdown links inside SKILL.md and README.
for rel in ("SKILL.md", "README.md", "COMPATIBILITY.md"):
    file = ROOT / rel
    if not file.exists():
        errors.append(f"Missing required file: {rel}")
        continue
    content = file.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        candidate = (file.parent / target.split("#", 1)[0]).resolve()
        if not candidate.exists():
            errors.append(f"Broken relative link in {rel}: {target}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDATION PASSED")
print(f"- References: {len(EXPECTED_REFERENCES)}")
print(f"- Evaluation files: {len(EXPECTED_EVALS)}")
print("- Frontmatter and relative links: OK")
print("Note: this validates package structure, not model behaviour or host compatibility.")
