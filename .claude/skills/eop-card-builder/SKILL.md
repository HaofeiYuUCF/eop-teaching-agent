---
name: eop-card-builder
description: Draft or revise EOP topic cards and optional teaching scenarios from supplied materials and instructor knowledge, preserving source locations, context, and evidence limits. Use for resource contributions without requiring lesson generation.
---

# Card Builder (wrapper)

This skill is the Claude Code entry point for the **Card Builder** role of the EOP Air Quality Teaching
Prototype. The full specification lives in `skills/eop-card-builder/SKILL.md`; this file exists so the role
appears in the skill list and is not a second copy of the rules.

When this skill is invoked:

1. Read `CLAUDE.md` at the repository root if you have not already this session.
2. Read `reference/workflow-policy.md`, the shared policy for all roles.
3. Read `skills/eop-card-builder/SKILL.md` in full and follow it, including the files it links to.
4. Write outputs under `outputs/<plan_id>/` as described in `CLAUDE.md`.

If the user's request fits a different role, say which one and read that role's specification
instead of forcing the request into this role.
