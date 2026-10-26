---
name: eop-assessment-designer
description: Build an assessment package with problems, solutions, rubrics, and numerical checks from an accepted and reviewed EOP lecture plan. Use before assembling the lecture slides.
---

# Assessment Designer (wrapper)

This skill is the Claude Code entry point for the **Assessment Designer** role of the EOP Air Quality Teaching
Prototype. The full specification lives in `skills/eop-assessment-designer/SKILL.md`; this file exists so the role
appears in the skill list and is not a second copy of the rules.

When this skill is invoked:

1. Read `CLAUDE.md` at the repository root if you have not already this session.
2. Read `reference/workflow-policy.md`, the shared policy for all roles.
3. Read `skills/eop-assessment-designer/SKILL.md` in full and follow it, including the files it links to.
4. Write outputs under `outputs/<plan_id>/` as described in `CLAUDE.md`.

If the user's request fits a different role, say which one and read that role's specification
instead of forcing the request into this role.
