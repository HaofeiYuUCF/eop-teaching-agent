# Lecture Plan Schema

Use [workflow-policy.md](workflow-policy.md) for shared rules. Write a readable Markdown lecture plan
with structured fields below. Explain decisions in ordinary language and expose identifiers when useful.
Fields can be concise; do not collect information that does not change this lesson.

```yaml
plan_id: near-road-example
revision: 1
title: Interpreting near-road project impacts
prepared_for: Instructor name or role
framework_edition: EOP 2026, as cataloged in reference/eop-outcomes.md
acceptance:
  status: draft  # draft | accepted | changes-pending
  accepted_revision: null
  evidence: null # actual instructor response/date; never invent acceptance
plan_review:
  status: pending # pending | passed | revision-required | awaiting-verification
  reviewed_revision: null
source_cards:
  - id: near-road-dispersion-modeling
    revision: source date or revision
scenario: null # optional; identify file and revision when selected
scenario_selection: # optional v4 metadata; omission is valid for older plans
  mode: recommend-with-override # recommend-with-override | lecturer-selected | none
  rationale: null # fit to objectives, capabilities, time, tools and usable evidence
  source_date_context: null # e.g., April 2024 TCAR study; 2026/2040 forecasts, not observed status
```

Keep `scenario` in its existing representation (null or the plan's file/revision identification).
The new metadata supplements it; it does not replace it or require migration. An explicit older
selection or null remains valid. For a Sunshine plan, identify `scenario/sunshine-corridor.md`,
revision 1. The case choice is reviewed with the whole plan; there is no separate acceptance gate.
When adapting a plan, follow the [catalog](../scenario/catalog.md), and record any changed case
and its consequences before rebuilding affected assessments and exports.

## 1. Audience and instructor

- Discipline(s), course purpose, and relevant educational/institutional context.
- Prior coursework, recently used knowledge, air-quality experience, and next professional task.
- Entry capabilities: mathematics and tools students already use, including variation across the class.
- Target capabilities: what students should be able to do after supported instruction.
- Permitted tools and available access: software/version, computing, data, lab facilities, installation
  constraints, and accessibility/format needs that affect this lesson.
- Instructor background and desired explanatory support.
- Instructor notes: preserve supplied constraints and distinguish them from inferred assumptions.

Do not infer proficiency from a major. Record unresolved assumptions and their consequences.

## 2. Lesson objectives and EOP connections

Each objective describes an observable action, its conditions, and adequate performance. Include
technical objectives whether or not they independently map to EOP. The example below is illustrative.

```yaml
lesson_objectives:
  - id: LO-1
    action: Compare two hypothetical emissions scenarios and explain the result using stated inputs.
    evidence: A comparison with units and reasoning consistent with the assumptions.
    cognitive_demand: analyze
    prerequisite_support: Worked example plus guided practice.
    assessed_by: [P1]
eop_connections:
  - id: EIA-C3
    published_wording: Copy the selected outcome exactly from the catalog.
    published_level: Medium
    adapted_objective_ids: [LO-1]
    scope: State which part of the published outcome this lesson supports.
    evidence_items: [P1]
    attainment_claim: not evaluated
```

EOP mappings are optional per objective, and there is no fixed number. Use exact cognitive demand
(remember, understand, apply, analyze, evaluate, create), rather than relying only on the catalog's
Low/Medium/High grouping. Do not equate a technical exercise with evidence of an entire broad outcome.

## 3. Teaching approach and sequence

Record a recognizable starting question and any confirmed connections to prior knowledge, with analogy
limits. Audience roles can combine interpretation, production, and decision-making.

For each selected topic, specify depth in words, planned minutes, purpose, and integration with other
topics. Labels such as primary/supporting/brief are optional. Equal emphasis and single-topic lessons
are valid when justified by objectives. Choose background-led, example-led, or balanced treatment,
or describe a different structure suited to the lesson.

List ordered segments with minutes, objective IDs, source/card IDs, activities, and assessment IDs.
Count opening, explanations, demonstrations, practice, discussion, and transitions once each. Lecture
segments plus buffer must equal the session budget. Record lab and homework minutes separately; do
not force a take-home project into the lecture or count its full duration as an in-class activity.

Specify what this lesson omits and any next topic. A recap or exit task is allowed alongside a handoff.

## 4. Assessment and tools

```yaml
assessment:
  requested_item_count: 3
  items:
    - id: P1
      objectives: [LO-1]
      form: analysis # recognition | calculation | analysis | design | project | other
      use: in-class # in-class | lab | homework | optional extension
      estimated_minutes: 8
      student_tools: [spreadsheet]
      deliverable: Comparison table and explanation
      criteria: Units, supported comparison, and acknowledgment of stipulated inputs
      scaffold: Example table supplied in the lecture
  student_resources: State datasets, starter files, versions, access, and setup support.
  instructor_resources: Solutions, rubrics, and separate verification files.
```

Select form per item and permit mixed formats. Specify observable evidence for reasoning, design,
communication, and teamwork claims; a short individual response does not evidence team performance.
Creating/designing objectives require a bounded product and quality criteria. Item count is a
preference to reconcile with objectives and time, not a reason to fabricate alignment.

## 5. Cut order, sources, and gaps

- Cut first: named optional segments or details, with minutes saved.
- Protect: content and practice essential to the objectives; this can include derivations or model code.
- If a cut removes required learning/assessment evidence, revise the objective or plan and flag the change.
- Claim IDs, scenario assumptions, and essential source dependencies from the fact register.
- Known gaps, whether each blocks generation/release, and the action needed to resolve it.

## 6. Deliverables and handoff

Specify requested formats, student and instructor versions, accessible alternatives as needed, and
assessment package location. Record downstream artifact revisions and review status in the final
handoff. Follow the acceptance and revision rules in the shared policy.
