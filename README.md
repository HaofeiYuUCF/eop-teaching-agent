# EOP Air Quality Teaching Agent Version 5

Version 5 adds a traceable three-course reference library to the supplied version 4 framework.
It remains a portable instruction framework, not an installed application or hosted service.

Start with [Contribute and use teaching resources](CONTRIBUTING.md) for plain-language examples of
reference lookup, card/scenario contributions, lesson adaptation, and feedback. No programming is
required to prepare a contribution; the assistant can organize supplied material into readable drafts.

- [Course library](library/index.md): 38 unchanged PDFs and 1,050 page-level references.
- [Topic index](library/topics.md): cross-course navigation.
- [Library guide](reference/library-guide.md): lookup, citation, evidence and reuse rules.
- [Card source map](reference/course-card-map.md): selected course passages linked to existing cards.
- [Validation report](reference/v5-validation.md): checks actually performed and remaining limits.
- [Revision notes](REVISION-NOTES.md) and [imported-material rights](library/RIGHTS.md).

Keep this complete folder together. Ask your assistant to read the library guide and find material on
a specified topic; a reference request does not launch course redesign or generate teaching materials.
No programming is required to browse these resources. Open the [course index](library/index.md),
choose a lecture, and click a page number; or start with the [topic index](library/topics.md).
Source records and check summaries are provided as readable Markdown documents.

The library is an initial domain resource, not evidence of educational effectiveness, independent
scientific validation, teacher endorsement, or multi-instructor co-design. Original course labels,
versions, credits and uncertainty are preserved. All page images are included to support visual lookup.

## Purpose and architecture

Adapt an instructor's teaching materials to the knowledge, goals, and practical resources of a
particular class, using Engineering for One Planet (EOP) learning outcomes where they are taught
and assessed. The same topic can support a planning decision exercise, an engineering calculation,
or a graduate modeling investigation.

This package contains five skill specifications and a reference library. It is a portable
instruction framework, not a standalone application or an installed service. A capable assistant
coordinates the stages and uses available document, presentation, computation, and source tools.
If a required tool is unavailable, it reports the affected output or check as incomplete.

## Five roles and their workflow

Role folders use the names shown below. If upgrading an older copy, see the
[role naming changes](REVISION-NOTES.md#role-naming-update--2026-09-20).

| Role | Specification | Responsibility |
|---|---|---|
| Card Builder | [eop-card-builder](skills/eop-card-builder/SKILL.md) | Prepare or revise reusable cards and scenario resources from supplied material and instructor knowledge. |
| Intake Agent | [eop-intake](skills/eop-intake/SKILL.md) | Clarify instructor goals, student preparation, and constraints; select suitable resources and develop the lesson plan. Planning is part of Intake. |
| Assessment Designer | [eop-assessment-designer](skills/eop-assessment-designer/SKILL.md) | Develop tasks, solutions, criteria, and verification records from the accepted, reviewed plan. |
| Material Builder | [eop-material-builder](skills/eop-material-builder/SKILL.md) | Assemble student and instructor materials around the plan and canonical assessment. |
| Reviewer | [eop-reviewer](skills/eop-reviewer/SKILL.md) | Review cards, scenarios, plans, assessments, and final materials; route defects to the responsible role. |

For lesson adaptation, prepare sources as needed, then use Intake to develop a plan. Reviewer checks
the plan, and the instructor accepts the resulting revision before dependent generation. Assessment
Designer produces the canonical assessment and its Word exports; Material Builder reuses that content
in separate student and instructor decks. Reviewer checks the actual exported package and produces
a coverage and assessment alignment memo. It can also review a scenario or assessment on its own,
reporting only the checks performed. Review modes are not additional roles. After at most two revision
rounds, report unresolved blockers under the shared policy; retain valid prior instructor acceptance.

Review may revise the plan or sources; affected downstream outputs must then be rebuilt and
rechecked. The five roles do not require five simultaneous agents. Delegate only when the host and
user permit it. Reviewing or installing this package does not authorize running a teaching session.

## Shared rules and library

### Continue after accepting a plan

Intake distinguishes **plan-only** from **teaching-package** requests. For a complete teaching
package, the coordinating assistant continues after the current plan passes review and is accepted:
Assessment Designer creates the assessment, Material Builder assembles the materials, and Reviewer
checks the outputs and routes needed corrections. You do not need to invoke each role separately.
The assistant pauses dependent work for blockers or important decisions, retaining a record for resumption.

For a request only to run Intake or prepare a plan, delivery ends with the plan and its review status.
Accepting that plan does not by itself request additional materials. Say what you want at the start:

- "Prepare and review a lesson plan only. Do not generate teaching materials."
- "Develop a complete teaching package. Let me accept the reviewed plan, then continue through
  assessment, materials, and final review without asking me to invoke each role."

These are instructions for the assistant executing the workflow, not a background service. See the
[continuation check record](reference/continuation-checks.md) for what has and has not been tested.

Read [workflow-policy.md](reference/workflow-policy.md) whenever using a role. It defines shared
assessment, evidence, precedence, and release rules. The [blueprint schema](reference/blueprint-schema.md)
defines lesson decisions; the [review rubric](reference/review-rubric.md) defines their checks.

- `skills/`: the five roles, each with a `SKILL.md` entrypoint.
- `cards/`: topic content, source teaching observations, and suggested adaptations.
- `reference/`: shared policy, schemas, EOP outcome catalog, and claim register.
- `scenario/`: a case catalog, the hypothetical I-4/SR 408 case, and the dated Sunshine Corridor case.

To use the package, make the complete library accessible to the assistant and identify the role
or request a teaching package. Keep the directory structure when moving it. Installing only the
five skill folders does not install their shared references; also provide the library location.
No installation or teaching-agent execution is performed by opening this ZIP.

## Output package

Default editable outputs are PowerPoint and Word, unless the instructor requests other formats:
student deck, instructor deck with notes and solutions, student problems, instructor solutions and
rubrics, lecture plan, review report, and alignment memo. Modeling lessons can additionally include
student datasets, starter code, and setup instructions. Instructor verification code remains separate.

The alignment memo describes intended coverage and assessment opportunities. It does not establish
student attainment, institutional accreditation, or EOP endorsement.

## Status and contributions

Version 4 extends the supplied version 3 demonstration specification. The inherited topic library
originated in version 2. Coverage, author acceptance, and evidence verification remain separate.
Sunshine source statements and synthetic arithmetic were checked during v4 development; inherited
claims have not been independently reverified. See the
[fact register](reference/fact-register.md). A complete card can still contain unverified claims.
See [revision notes](REVISION-NOTES.md) for changes, validation, and remaining limitations.

Use the [card template](reference/card-template.md) to contribute. Preserve original authorship and
identify adapters. An AI-assisted draft bearing an instructor's name is not evidence of their
approval. Record teaching observations in their course context and allow other instructors to adapt them.

For a case contribution, use the [scenario template](reference/scenario-template.md). Faculty may
contribute scenarios as well as cards and source materials. The optional
[faculty use record](reference/faculty-use-record.md) captures reported experience and revision needs;
it is not a completed trial or a research instrument. See the
[faculty workflow checks](reference/faculty-workflow-checks.md) for this documentation update's scope.

## Attribution and license

Based on the [Engineering for One Planet Framework](https://engineeringforoneplanet.org/eop-framework/).
Original package attribution and license are retained: see [LICENSE.md](LICENSE.md).
Check permissions for third-party material separately; the package license does not establish its rights.

## Choosing a project example

The default is **recommend with lecturer override**. The agent reads the supplied lecture and
student/audience information, then uses the [case catalog](scenario/catalog.md) to recommend a
fit and explain it in the lesson plan. Explicit lecturer choices take priority. A genuine tie
prompts one preference question; neither case is compulsory. The existing lesson-plan review
accepts the choice without a separate approval step.

- I-4/SR 408 supports roadway operations, intersection emissions and near-road dispersion.
- Sunshine Corridor supports mode shift, net emissions accounting and uncertainty, using an
  April 2024 study as context and separately labeled synthetic calculation data.

Example request: "Use this package to adapt my lecture for students who know ratios but have
not used an emissions model. Recommend a case, explain the fit, and plan supported practice."
To choose directly, add: "Use the Sunshine Corridor case." The agent still asks for essential
missing lecture, audience, objectives or time information rather than inventing a class.
You can also say: "Use my supplied case instead" or "Do not use a scenario."

Start with [the Sunshine case](scenario/sunshine-corridor.md), its
[transit-emissions card](cards/transit-emissions-accounting.md), and the
[instructor activity patterns](reference/sunshine-activities.md). Patterns include interpretation,
calculation and sensitivity exercises with solutions; select only what fits the lesson. Their
synthetic results are not predictions of corridor effects. STAR is optional, separately attributed
policy context. The source report itself and third-party figures are not bundled.

See [v4 validation](reference/v4-validation.md) for performed checks and limits. This delivery is
the portable framework, not an installed service or a generated classroom slide/Word package.
Keep the complete folder together; the new selection metadata is optional for existing plans.
