# Lecture Plan Schema

Use [workflow-policy.md](workflow-policy.md) for shared rules. Write a readable Markdown lecture plan
with structured fields below. Explain decisions in ordinary language. The plan the instructor reads
carries no EOP outcome identifiers; those belong to the alignment memo (section 8).
Fields can be concise; do not collect information that does not change this lesson.

```yaml
plan_id: near-road-example
revision: 1
title: Interpreting near-road project impacts
prepared_for: Instructor name or role
execution:
  mode: plan-only # plan-only | teaching-package; derive from the actual request
  requested_outputs: [lecture-plan, plan-review] # replace with the requested deliverables/formats
  request_basis: null # actual request or concise reference; never invent authorization
revision_objective: null # one sentence from the instructor, recorded before any card, scenario, or suggestion is shown: what this revision should resolve
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

## 2. Lesson objectives and connections

Each objective describes an observable action, its conditions, and adequate performance. Include
technical objectives whether or not they relate to EOP. The example below is illustrative.

```yaml
lesson_objectives:
  - id: LO-1
    action: Compare two hypothetical emissions scenarios and explain the result using stated inputs.
    evidence: A comparison with units and reasoning consistent with the assumptions.
    cognitive_demand: analyze
    prerequisite_support: Worked example plus guided practice.
    assessed_by: [P1]
connections:
  - id: C-1
    question: Which of two project options leaves nearby residents with lower concentrations, and why?
    eop_topic: Environmental Impact Assessment # topic area in plain words; no outcome identifier here
    objective_ids: [LO-1]
    activity: Pairs compare the two scenarios and explain the difference to a non-specialist.
    assessed_by: [P1] # empty when the connection is taught but not assessed
    decision: pending # pending | selected | adapted | deferred | declined
```

Connections are optional per objective, and there is no fixed number. Use exact cognitive demand
(remember, understand, apply, analyze, evaluate, create) for objectives. Do not equate a technical
exercise with evidence of an entire broad outcome.

### Connection rationale

For each proposed environmental or societal connection, record a concise, readable chain:
technical content → environmental or societal question → student activity → lesson objective.
Explain the teaching value, supporting source locations, assumptions, and limits. Record whether
the instructor selected, adapted, deferred, or declined it; leave unresolved choices pending rather
than inferring acceptance. For selected connections, identify where the explanation and activity
will appear and whether the objective is assessed, with the relevant assessment item if applicable.
Name the EOP topic area a connection draws on when that helps the instructor see where the idea
comes from. Outcome identifiers and published wording are added after acceptance, in section 8.

For example, a dispersion-model lesson could connect predicted concentrations at different receptor
locations to a monitoring-site decision, using a comparison activity to support an objective about
interpreting model assumptions and siting trade-offs. This does not establish actual exposure or
health effects. This example is optional, not a required topic or activity.

If none is selected, record the reason and any role as technical preparation for later EOP learning.
Follow shared policy for older accepted plans; missing fields alone do not require reapproval.

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

## 6. Revision record

Record every suggestion the instructor receives while this plan and its materials are developed,
whether it comes from a partner in a co-design session, from the assistant, from the framework, or
from a facilitator. Source `framework` marks a "one step further" suggestion that the assistant or
the Reviewer drew from an EOP outcome (shared policy); `assistant` marks every other suggestion of
theirs. Write one entry per suggestion when the decision is made. An entry has a decision or does
not exist yet: an undecided suggestion stays in the plan's list of open decisions and is not applied.

```yaml
revision_record:
  - id: S-01
    stage: plan # plan | assessment | materials
    source: assistant # partner | assistant | framework | facilitator
    suggestion: Add a receptor-distance comparison before the averaging-time discussion.
    decision: modified # adopted as given | modified | rejected
    reason: Kept the comparison but limited it to two distances to fit the session budget.
    serves_revision_objective: yes # yes | no | unclear
    affects: [LO-2, P1] # objectives, items, or slides changed, if any
```

Changes the instructor introduces on their own are recorded as plan changes, not as entries here.
Later roles report proposed changes to accepted content to the coordinating assistant, which appends
the entries and keeps the record complete. The record travels with the plan at every handoff.
Reviewer notes any gap it sees for the coordinating assistant to repair; a gap does not block.

Corrections of errors are kept apart from suggestions, because they are not teaching choices and do
not wait for a decision (shared policy, "Corrections are not suggestions"):

```yaml
corrections:
  - id: K-01
    found_by: reviewer # reviewer | assistant | instructor
    kind: draft-error # draft-error | source-error | changes-teaching
    where: P2 instructor solution
    was: The draft answer was 176 µg/m³.
    why_wrong: Recalculating with the stated inputs gives 167 µg/m³; the draft used the wrong stability class.
    now: The solution and the comparison with the limit use 167 µg/m³.
    told_instructor: yes # every correction is reported in the review summary
```

A `source-error` leaves the source unchanged and records what the instructor decided the lesson will
say. A `changes-teaching` correction also has a revision-record entry for the instructor's decision.

## 7. Deliverables and handoff

Follow the shared policy's requested-scope and continuation rules. Explain the execution mode to
the instructor in ordinary language when presenting the plan: either delivery ends with the plan,
or acceptance of the reviewed plan will be followed by the requested assessment/material generation
and final review. Do not require the instructor to edit these fields or approve routine role changes.

Include the current instructor-facing review summary with the plan, as required by shared policy,
before any needed acceptance. Retain it with the plan-review evidence so the checked scope, completed
repairs, remaining issues, and instructor decisions can be recovered at handoff or resumption.

At handoff or interruption, record completed stages, artifact paths and revisions, actual acceptance
and review evidence, next stage, and unresolved blockers. Use those records when resuming; missing
fields in an older plan do not invalidate unchanged acceptance or authorize additional outputs.

Specify requested formats, student and instructor versions, accessible alternatives as needed, and
assessment package location. Record downstream artifact revisions and review status in the final
handoff. Follow the acceptance and revision rules in the shared policy.

## 8. Alignment memo (written after acceptance)

After the instructor accepts the plan, the coordinating assistant maps the selected and adapted
connections to published EOP outcomes and saves the result as `alignment-memo.md` beside the plan
(or presents it after the plan where files cannot be written). This is documentation, not a
decision: do not ask the instructor to choose between outcomes or to approve the memo.

```yaml
framework_edition: EOP 2026, as cataloged in reference/eop-outcomes.md
plan_revision: 3
eop_connections:
  - connection_id: C-1
    outcome_id: EIA-C3
    published_wording: Copy the outcome exactly from the catalog.
    published_level: Medium
    adapted_objective_ids: [LO-1]
    covered: State which part of the published outcome the lesson's items actually ask for.
    not_covered: State the part no item asks for, or "none".
    evidence_items: [P1]
    attainment_claim: not evaluated
framework_suggestions: # each revision-record entry with source framework
  - record_id: S-04
    outcome_id: ST-S1
    decision: rejected
```

Map a connection only to an outcome its activity or item actually develops; a connection with no
defensible outcome is listed as unmapped with one sentence of reason. When an item asks for less
than the outcome's wording, write the difference under `not_covered`; do not go back and change the
lesson. Keep the catalog's Low/Medium/High level separate from the objective's cognitive demand.
In a teaching-package request the Reviewer completes the memo in material review (reviewer role).
