# Review Rubric

Use [workflow-policy.md](workflow-policy.md) for shared rules and release states. Verdicts apply to
checks; severity applies to issues. Do not average away a blocking defect.

- **pass:** the stated check was completed and its criterion met.
- **fail:** checked and the criterion was not met.
- **unverified:** evidence or capability needed for checking was unavailable.
- **not-applicable:** the check does not apply, with a recorded reason.

## Defect record

```yaml
id: D-001
mode: material
dimension: numerical-validity
verdict: fail
severity: blocking # blocking | suggestion
where: P3, instructor solution, assessment revision 2
finding: The answer uses a different unit conversion from the prompt.
evidence: Reference to execution output and independent unit check.
target: eop-assessment-designer
acceptance_criterion: Prompt, method, computation, and displayed result use consistent units.
affected_artifacts: [assessment, instructor-solutions, instructor-deck]
round: 0
status: open # open | resolved
```

Other targets: `eop-intake`, `eop-material-builder`, or `eop-card-builder:card-or-claim-id`.
The card builder maintains source records; a change requiring author knowledge is reported to the
instructor rather than treated as an executable external contact. Preserve resolved defect history.

## Plan review

Check the current plan revision before generation:
- Objectives name observable actions and adequate performance; EOP mappings match the actual scope.
- Audience assumptions are supported, and new skills have instruction/practice before assessment.
- Tools, data, setup, accessibility, and instructor support are feasible.
- Formats and criteria can elicit evidence of each assessed objective; design/creation requires a
  suitable product, teamwork requires actual collaborative evidence, and reasoning requires evidence
  beyond a guessed correct choice.
- Session timing includes activities and transitions, with lab/homework separate and no double-counting.
- Depth and cut order protect this lesson's objectives. Single topics and equal emphasis are allowed.
- Source cards and claim records are sufficient for essential content, or a valid stipulated example
  is explicitly planned. Unresolved critical prerequisites, evidence, and tool dependencies are blockers.
- Record design-review findings independently of instructor acceptance. A sound plan can pass
  design review while acceptance is pending. Before generation, require both passed design review
  and instructor acceptance of that revision; existing acceptance of an unchanged revision counts.

## Material review

| Dimension | Check and failure conditions |
|---|---|
| Revision and plan fit | Correct accepted/reviewed plan and assessment revisions; no silent scope, tool, workload, or objective change. |
| Learning support | Required tasks are supported by entry skills or planned instruction and practice; audience bridges are justified rather than stereotypes. |
| Technical accuracy | Definitions, formulations, assumptions, units, interpretation, and applicability hold against available evidence. Unsupported essential claims are unverified blockers. |
| Numerical validity | Reproduce quantitative answers and perform appropriate independent checks of units, cases, magnitudes, or benchmarks. Incorrect checks fail; unavailable execution or essential checks are unverified. Qualitative items are not-applicable. |
| Assessment validity | Items elicit the claimed actions at the stated cognitive demand, with defensible criteria and alternatives. Being above the planned level is a mismatch if it exceeds support or time. |
| EOP alignment | Claimed EOP connections trace to lesson objectives and concrete evidence opportunities. Technical items without separate EOP IDs are valid. No attainment claim without evaluated student work. |
| Provenance | Inputs, claims, adaptations, and derived conclusions trace to sources/register entries; inherited limitations and assumptions remain visible. A citation or warning alone does not establish correctness. |
| Reasoning and decisions | Evidence and uncertainty are represented fairly; examples and rubrics allow defensible recommendations. Do not require a predetermined policy answer or fabricate balance between unsupported and supported claims. |
| Visual and access quality | Inspect actual exported/rendered slides and documents for legibility, equations, overflow, units/legends, contrast, non-color cues, relevant text alternatives, and practical access constraints. |
| Pacing | Actual slide content and learning activities fit the agreed session, with adequate practice and separate lab/homework workloads. |
| Student separation | No answer keys or private answer-bearing notes, comments, hidden slides, or attachments in student files; planned public criteria, datasets, and starter code are retained. |
| Package consistency | Canonical item content matches all exports; slide/page maps and manifest identify exact versions; instructor solutions and verification records are accessible. |

Classify a missing/failed check by consequence. Core numerical uncertainty, essential unsupported
scientific claims, invalid assessments, unreadable required figures, and answer leakage block release.
Optional enrichment that does not affect objectives can be removed or left as a clearly separated
research question. Aesthetic preferences are suggestions. State exclusions instead of claiming checks
were completed. Readiness does not imply educational effectiveness has been demonstrated in a classroom.

## Scenario checks for plans, cards and materials

- Selection respects explicit lecturer preferences and matches objectives, actual capabilities,
  support, time, tools and evidence; no automatic difficulty assignment by major.
- The selected case path/revision is consistent across dependent artifacts. Older absent metadata
  alone is not a defect; an unexplained case substitution or stale case-dependent result is.
- Report forecasts retain their source date, horizon, system boundary and forecast label. Sunshine
  boardings cannot be treated as unique journeys or displaced cars; synthetic J is a separate input.
- Emissions accounting states the baseline, pollutant, units/time basis, added transit/access,
  full-vehicle displacement premise and exclusions. Check zero shift and break-even when used.
- Cost comparisons reconcile station-only/full-route, cumulative/individual and capital/annual
  scopes. STAR claims remain attributed advocacy context, not TCAR findings or official approvals.
- No unsupported inference from emissions to concentrations, exposure or health; no I-4 geometry
  presented as Sunshine geometry; no implied current opening from the 2024 model's assumed year.
- Changed cases trigger downstream revision/review. Student outputs omit activity solutions and
  verification code, including answers inadvertently disclosed by another selected activity.

Errors affecting an answer, objective or real-world claim are blocking under the shared policy.

## Standalone scenario documentation review

Use the [scenario template](scenario-template.md) for new contributions. Review existing cases in
their current format; missing new headings alone are not defects.

- Teaching question, system boundaries, relevant cards, and intended systems relationships are clear.
- Recommendation, source provision, authorship, adaptation, and review credits are distinguished.
- Source locations, dates, evidence types, hypothetical inputs, and reuse limits are inspectable.
- Data/tool requirements and usable teaching options match the available evidence; unfinished
  calculations or missing local observations are not presented as ready model exercises.
- The catalog describes actual coverage and limits, and the revision can be tracked into later use.
- Review status, contributor acceptance, scientific verification, and classroom evaluation remain
  separate. A partial case can pass documentation review without supporting every proposed use.

Do not require a lesson plan or assessment to review a scenario contribution. Record the scope and
limits of review; apply the scenario checks above to the claims and examples actually present.

## Card documentation checks

- Scope, sources, locators, and assumptions are inspectable.
- Coverage, author acceptance, and claim verification are represented separately.
- Classroom observations identify their context/evidence; proposed misconceptions remain hypotheses.
- Audience bridges have limits; depth and cut order are suggestions for named contexts.
- Conflicts with other cards are recorded and routed; unsupported claims are registered.
- EOP candidates are plausible connections to activities, not guaranteed attainment claims.
- Third-party assets have known usage limits, and original author/adaptor attribution is retained.

A partial card can pass documentation review while remaining unsuitable for a particular primary
lesson. Record what was reviewed: completeness of documentation is not verification of all science.
