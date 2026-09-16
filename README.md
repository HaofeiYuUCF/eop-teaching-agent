# EOP Air Quality Teaching Agent Version 5

Version 5 adds a traceable three-course reference library to the supplied version 4 framework.
It remains a portable instruction framework, not an installed application or hosted service.

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

## Inherited version 4 documentation

The following describes the earlier framework. Historical validation statements refer to v4;
use the version 5 report for checks performed in this delivery.

# EOP Air Quality Teaching Agent — Version 4

Adapt an instructor's teaching materials to the knowledge, goals, and practical resources of a
particular class, using Engineering for One Planet (EOP) learning outcomes where they are taught
and assessed. The same topic can support a planning decision exercise, an engineering calculation,
or a graduate modeling investigation.

This package contains five skill specifications and a reference library. It is a portable
instruction framework, not a standalone application or an installed service. A capable assistant
coordinates the stages and uses available document, presentation, computation, and source tools.
If a required tool is unavailable, it reports the affected output or check as incomplete.

## Roles and order

1. **Prepare sources — eop-card-builder.** Draft or revise topic cards from supplied text, slides,
   notes, and instructor observations. Compare new materials with existing cards, including when
   a graduate and undergraduate course cover the same topic. Preserve attribution and source locations.
2. **Plan — eop-intake.** Ask only for missing information that changes the lesson. Produce a
   lecture plan covering technical objectives, EOP connections, activities, assessment, and time.
3. **Check the plan — eop-review, plan mode.** Resolve blocking design problems and obtain the
   instructor's acceptance of the resulting plan. Existing explicit acceptance remains valid for
   that revision; do not request it repeatedly.
4. **Design assessment — eop-problem-set.** Create a canonical assessment package with student
   prompts, instructor solutions, criteria, and verification records.
5. **Assemble materials — eop-lecture-builder.** Build separate student and instructor decks around
   the plan and assessment. Collect and check the problem role's Word exports; request regeneration
   from that role if the canonical assessment changes.
6. **Review and revise — eop-review, material mode.** Check content, evidence, assessment, and the
   actual exported files. Route defects to their cause. After at most two revision rounds, report
   unresolved blockers. Produce a coverage and assessment alignment memo with an explicit status.

Review may revise the plan or sources; affected downstream outputs must then be rebuilt and
rechecked. The five roles do not require five simultaneous agents. Delegate only when the host and
user permit it. Reviewing or installing this package does not authorize running a teaching session.

## Shared rules and library

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
Sunshine source statements and synthetic arithmetic were checked in this revision; inherited
claims have not been independently reverified. See the
[fact register](reference/fact-register.md). A complete card can still contain unverified claims.
See [revision notes](REVISION-NOTES.md) for changes, validation, and remaining limitations.

Use the [card template](reference/card-template.md) to contribute. Preserve original authorship and
identify adapters. An AI-assisted draft bearing an instructor's name is not evidence of their
approval. Record teaching observations in their course context and allow other instructors to adapt them.

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

Start with [the Sunshine case](scenario/sunshine-corridor.md), its
[transit-emissions card](cards/transit-emissions-accounting.md), and the
[instructor activity patterns](reference/sunshine-activities.md). Patterns include interpretation,
calculation and sensitivity exercises with solutions; select only what fits the lesson. Their
synthetic results are not predictions of corridor effects. STAR is optional, separately attributed
policy context. The source report itself and third-party figures are not bundled.

See [v4 validation](reference/v4-validation.md) for performed checks and limits. This delivery is
the portable framework, not an installed service or a generated classroom slide/Word package.
Keep the complete folder together; the new selection metadata is optional for existing plans.
