# Topic Card Template

Use [workflow-policy.md](workflow-policy.md) for evidence and adaptation rules. Keep the card compact
enough to maintain; include the detail needed for its scope rather than enforcing a page count.

```yaml
---
card: topic-slug
title: Plain-language topic title
author: Original author or authors
institution: Source institution if provided
date: Source date or unknown
revision: 1
adapted_by: []
ai_assistance: Describe extraction or adaptation if applicable
license: Established license or permission status
status: partial # full | partial | header-only; coverage only
author_acceptance: unconfirmed # unconfirmed | accepted; identify revision/evidence in notes
source_contexts: [] # courses/audiences and versions represented
prerequisites: [] # card IDs where available
leads_to: []
claim_ids: [] # factual claims relevant to this card, including unresolved ones
---
```

## Scope and candidate objectives

Concepts and boundaries, followed by observable technical/professional actions this topic could teach.
The lesson plan selects among these; a card is not a requirement to teach everything it contains.

## Prerequisites and support

Concepts, mathematics, and tools needed for each kind of task. Identify what can be introduced during
the lesson, prerequisite refreshers, and access constraints. Separate interpreting a demonstration
from independently operating a model.

## Student difficulties

Specific recurring misconceptions, scattered configuration mistakes, or unknown patterns. Identify
whether each is instructor-reported in a course, source-supported, or a hypothesis. Unknown is valid.

## Adaptations by audience and objective

Starting points and connections to confirmed prior knowledge, including limits of analogies.
Describe conceptual, applied, and technical treatments as options; no rung is universally expendable.
Record suggested cut orders for specific lesson purposes. Graduate and introductory variants can
coexist without assigning capabilities solely from course level or discipline.

## Content, models, and example

Essential definitions, equations and their assumptions, model boundaries, source-located examples,
and simplifications. Link detailed source material rather than inventing omitted derivations.
Use claim IDs where statements affect teaching conclusions or assessment answers.

## Data and evidence

Source IDs with file/page/slide/section or URL/version/locator. Claim IDs in the fact register include
verification, applicability, and input provenance. Stipulated examples are permitted when visibly
labeled; missing actual data must not be presented as measurements or model outputs.

## Candidate EOP connections

EOP ID and the specific student activity/evidence that could support it. No fixed count; leave empty
where the topic is preparatory. Keep published wording/level separate from adapted objectives.

## Gaps, conflicts, and review

Unresolved claims, competing sources/card references, usage/asset permissions, author acceptance
evidence, adaptations, and review scope/status. Acceptance of text is distinct from verification.

## Course-library source map when applicable

Link only the relevant passage, using source ID, course context, and one-based PDF page. Record the
supported topic and limits of the connection. A related lecture does not substantiate every card claim,
classroom observation, or audience assumption. See the [library guide](library-guide.md).
