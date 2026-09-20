# Version 5 revision notes

## Role naming update — 2026-09-20

Folder names, SKILL.md names, headings, and current handoff references now match the role names
used in the architecture overview. This is a naming change, with five roles and their duties retained.

| Previous identifier | Current identifier | Role |
|---|---|---|
| `eop-problem-set` | `eop-assessment-designer` | Assessment Designer |
| `eop-lecture-builder` | `eop-material-builder` | Material Builder |
| `eop-review` | `eop-reviewer` | Reviewer |

`eop-card-builder` and `eop-intake` are unchanged. Historical validation records retain the names
used when those checks ran. Use this mapping when reading older handoff records; update the role
reference when continuing work without treating a name change as a new artifact revision or review.
Existing installations should replace the old skill folders with the renamed folders rather than
install both copies. Older external links to those folder paths must be updated; no alias roles were
added. Shared references and the source library must remain accessible as before.

Naming-update checks: all five role specifications pass the skill format validator; each declared
name matches its folder; all 4,116 relative Markdown file links resolve; obsolete identifiers occur
only in this migration table and historical check records. Remote URLs and heading anchors were not
retested. These checks establish naming and file-link consistency, not runtime or classroom performance.

## Faculty contribution workflow update — 2026-09-20

- Clarified the five role names and that lesson planning is part of the Intake Agent.
- Added a plain-language contribution guide, scenario template, and optional faculty use/revision record.
- Made scenario preparation and review explicit responsibilities of the existing Card Builder and
  Reviewer. Clarified standalone assessment review within Reviewer; no sixth role was added.
- Retained instructor choice of an existing case, a supplied alternative, or no scenario.
- Added a [scoped check record](reference/faculty-workflow-checks.md). These are documentation and
  workflow-specification improvements, not completed faculty co-design, classroom evaluation, or
  evidence of reliable autonomous execution. No new scenario or teaching package was generated.
- Original course resources, cards, scenarios, claim statuses, and historical checks are preserved.

## Original v5 delivery

The supplied v4 archive is the baseline. Its README referenced REVISION-NOTES.md, but that file was
not included in the supplied archive. This file supplies v5 notes; it does not reconstruct or certify
the unavailable earlier history. The original v4 validation record is retained as a historical report.

## Added

- Three-course library, original PDFs, checksums and metadata, 38 Markdown references and 1,050 page images.
- Course/topic indexes, page-level references, visual-reference notes and image-only navigation annotations.
- Library guide, rights notice, source map and readable source/check records.
- Shared and role-specific reference access instructions; selected source links in eight existing cards.

## Preserved

Original course files and v4 archive were not changed. Copies of course PDFs are byte-identical.
Existing card IDs, claim IDs, claim statuses, author-acceptance statuses and license file are preserved.
Scenario, assessment and teaching workflows retain their existing behavior outside source lookup.
The transit-emissions card retains its v4 source basis rather than receiving an invented course citation.

## Boundaries

No course redesign, new lecture package, new worked example, faculty trial, scientific update, model
run, public publication, or proposal prose was produced. Original course and third-party rights are
not replaced by the framework license. See [validation](reference/v5-validation.md) for actual checks.

## Instructor-facing repository simplification

At the owner's request, JSON/JSONL records were replaced by readable Markdown records where they
contained unique provenance or check information. The duplicate page index and two optional Python
helpers were removed. Course PDFs, 1,050 page images, 38 page-level references, topic cards and
role instructions are preserved. Browsing now uses the course/topic indexes and page links without
requiring a programming environment. Earlier development checks remain historical records.
