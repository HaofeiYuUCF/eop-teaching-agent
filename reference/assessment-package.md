# Canonical Assessment Package

Use one structured YAML/JSON file or equivalently structured Markdown as the authoritative assessment
content. Store rich figures, datasets, and code as referenced assets. Export documents and slide inserts
from these records; reflow is permitted, but silently changing inputs, questions, or solutions is not.

```yaml
assessment_id: near-road-assessment
revision: 1
plan_id: near-road-example
plan_revision: 1
scenario: null # optional v4 provenance; carry the plan's case path/revision when selected
items:
  - id: P1
    objective_ids: [LO-1]
    eop_ids: [] # populated only when this item supports the stated EOP connection
    cognitive_demand: analyze
    use: in-class
    estimated_minutes: 8
    student:
      prompt: Complete prompt with inputs, units, instructions, and requested product.
      options: null
      public_criteria: Criteria the instructor intends students to see.
      assets: []
      assumptions: [] # explicitly labeled and linked to claim records
      source_labels: []
    instructor:
      solution: Worked method with units, or expected reasoning.
      answer: Result or range of defensible conclusions.
      grading_criteria: Observable criteria and partial-credit guidance.
      alternative_answers: []
      distractor_rationales: []
      private_notes: null
    evidence:
      claim_ids: []
      computation: not-applicable # checked | failed | unverified | not-applicable
      verification_files: []
      independent_checks: []
      limitations: []
    placement:
      after_segment: Segment ID in lecture plan
exports:
  student_problems: null
  instructor_solutions: null
  student_deck: null
  instructor_deck: null
```

Record exported filenames, assessment revision, and item-to-slide/page maps when available. Student
and instructor decks can have different slide numbers, so map them separately. Only the student
branch and student-approved assets may enter student exports. Public criteria may guide the work
without revealing instructor answers. Verify separation in the final files, including notes,
comments, hidden slides, attachments, and other retained answer-bearing content.

For model exercises, distinguish starter templates and student datasets from complete solution files
and instructor verification runs. Record required software, versions, setup steps, expected student
access, and fallback treatment if access fails. A demonstration-only fallback changes the assessment
when independent model execution was an objective; route that change to the plan.
