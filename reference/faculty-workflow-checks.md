# Faculty Contribution Workflow Checks

Date: 2026-09-20. Baseline: repository commit `32c8a64`, fetched from origin/main before editing.

This update improves readable instructions for faculty contributions and resource use. It adds no
application, database, role, course source, completed scenario, or classroom trial. The library's
original [v5 checks](v5-validation.md) and [v4 checks](v4-validation.md) remain historical records.

## Changes and rationale

| Area | Baseline finding | Change |
|---|---|---|
| Role explanation | Intake already performs planning, but README listed six workflow steps without a five-role mapping. | Five-role table and explicit Intake/Planning relationship. |
| Faculty entry point | Card contribution instructions existed mainly in agent-facing files. | Plain-language contribution guide with examples and separate lookup, contribution, and teaching requests. |
| Scenario preparation | Existing cases had detailed records, but no common contribution template or explicit scenario-review mode. | Scenario template; existing Card Builder prepares it and Reviewer checks it. |
| Assessment review | Final material review included assessment checks. | Explicit standalone assessment-review scope, with no claim that final slide checks were performed. |
| Instructor choice | Existing catalog and Intake already allowed a supplied case or no case. | Exposed these options in the faculty guide and README; preserved selection behavior. |
| Feedback after use | Revision rules existed, but there was no short faculty-facing record. | Optional use/revision record separating actual observations, interpretations, and changes. |

## Manual instruction walkthrough

These are desk checks of routing and requirements in the written instructions. They are not
independent agent executions, benchmark results, completed teaching packages, or faculty usability tests.

| Illustrative request | Path and boundary checked | Desk-check result |
|---|---|---|
| Find course pages on sensor calibration | Library lookup only; do not start a lesson interview. | Consistent with contribution guide and all role library sections. |
| Turn supplied slides into a card only | Card Builder, card template, card review; no lesson generation. | Explicit route and scope boundary present. |
| Draft a scenario from a supplied report | Card Builder, scenario template, catalog update, scenario review. | New preparation/review route present; sources, gaps and attribution required. |
| Adapt a lecture without a scenario | Intake keeps no case; plan review precedes generation. | Existing catalog and shared policy preserve this choice. |
| Use an instructor-supplied case | Honor the choice; surface missing evidence/tools rather than silently switch cases. | Existing catalog rule retained and linked from the guide. |
| Recommend a case, then change it in plan review | Recommend by fit; instructor override; rebuild affected outputs if the case changes. | Catalog, Intake, and shared policy remain consistent. |
| Review assessment tasks and scoring before slide assembly | Reviewer assessment mode checks the accepted plan and applicable assessment dimensions. | Scope explicitly excludes uninspected final slides and whole-package claims. |
| Report a classroom difficulty after using a scenario | Optional use record; distinguish report from inference; route resource or plan corrections. | Feedback path present without treating the report as demonstrated learning. |

## Structural verification

The check results below are maintained with this update after checking the final changed files.
They concern file structure and instruction consistency, not scientific or educational validity.

- All five role SKILL.md files pass the bundled skill-creator quick validator.
- All 4,114 relative Markdown file links across 81 Markdown files resolve to existing targets; heading anchors and remote URLs
  are outside this check's scope.
- The course-source inventory remains 38 PDFs and 1,050 JPEG page images; course library files, existing
  cards, existing case files, and fact-register entries are unchanged from the baseline commit.
- Whitespace/diff checks are performed. No executable or JSON files are added to the public package.

## Remaining evidence needs

Faculty must still try the contribution process to establish whether it is understandable and useful.
A retained end-to-end adaptation run with checked outputs would provide evidence beyond instruction
inspection. Actual classroom use, sustained faculty adoption, student learning, and comparative
effectiveness remain unevaluated here. Complete further scenarios only when actual contributions and
sources are supplied; do not count a template or recommended case as an implemented case.

The Sunshine source report is not bundled. Its existing source locators support retrieval when that
report is available, but this update does not independently verify its contents or current project status.
