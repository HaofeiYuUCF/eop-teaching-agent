---
card: near-road-dispersion-modeling
title: Modeling near-road dispersion of primary pollutants
author: Haofei Yu
institution: University of Central Florida
date: 2026-09-13
license: CC BY-NC-SA 4.0
status: full
chain_position: dispersion
prerequisites: [traffic-related-primary-pollutants, meteorology-for-dispersion]
leads_to: [air-quality-regulation, regional-ozone-formation]
revision: 4
author_acceptance: unconfirmed
adapted_by: [AI-assisted version 3 editorial revision, AI-assisted version 4 case routing clarification]
claim_ids: [GEO-01, HYP-02]
---

> **Source and adaptation status.** Topic content and teaching observations originated in the
> supplied version 2; the named original author's approval of these editorial changes is unconfirmed.
> Coverage status is not verification. Read [shared policy](../reference/workflow-policy.md) and
> [fact register](../reference/fact-register.md) before use. Register and verify essential claims
> not yet covered there. Classroom patterns and audience bridges are contextual suggestions, not
> established attributes of every student in a discipline. Confirm them during intake. Candidate
> outcomes and cut orders are selected or overridden by the accepted lesson plan.
## Topics

- The Gaussian plume idea: what it assumes and what those assumptions buy
- Roadways as line sources, and why an intersection is not a line
- CALINE3 and CAL3QHC: a steady-state Gaussian model with an intersection queuing algorithm
- Link geometry: queue links and running links, and why the split exists
- Receptors, averaging time, surface roughness, wind angle search
- The screening ladder: categorical finding, then screening, then refined modeling
- What the model cannot do: inert pollutants only, no chemistry, no hourly meteorology in
  CAL3QHC

## Expectations

After this topic a student should be able to:

- Explain what a steady-state Gaussian dispersion model assumes, in plain language
- Set up a roadway as a series of links with appropriate queue and running segments
- Interpret a modeled concentration, including what its averaging time means
- Identify at least three assumptions that would fail at a real intersection
- Decide, for a given pollutant, whether this class of model is the right tool at all

## Prerequisites

**Conceptual.** Primary versus secondary pollutants. Wind direction and speed as vectors.
Atmospheric stability as a concept, though not its derivation. Emissions as an input, from the
primary pollutants card.

**What students need to be able to do.** Algebra, exponentials, and reading a dispersion curve or
table. Students can interpret and even run a screening model on that basis.

**Confirm programming and model-configuration experience.** The source course reports that
students needed support with control files, paths, and configuration failures. Record whether this
applies to the current class; it is not a general claim about environmental engineering students.
Plan guided practice or more advanced work according to actual experience and learning objectives.

The plume equation, dispersion coefficients, and line source superposition can all be **shown** to
any audience that will be told what they mean. Showing is not requiring.

## What students get wrong here

**The errors here are scattered, not concentrated, and they are mostly about model
configuration.** There is no single misconception to trap. Students make a different small
configuration mistake each time: a wrong unit flag, a path that does not resolve, a receptor in
the wrong coordinate system, a link entered in feet when the scaling factor says metres. The
errors are individually trivial and collectively fatal, and they are the reason a student's run
produces a number that is wrong in a way nothing flags.

**Source-course teaching response.** A complete walkthrough was used to address the reported
configuration errors. Select that approach when students need to operate the workflow and sufficient
time is available. Other objectives may call for focused demonstrations or targeted debugging practice.

Conceptual confusions worth watching for, though they are not what usually goes wrong:

- Reading a modeled concentration as a measurement. A model output is a consequence of its inputs
  and assumptions, and carries no error bar unless one is supplied.
- Assuming more model detail means more accuracy. A refined run with wrong meteorology is worse
  than a screening result with conservative assumptions.
- Ignoring the averaging time, and comparing a one-hour number to an eight-hour standard.
- Treating queue links versus running links as bookkeeping. Idling and moving vehicles emit very
  differently, and the split is where that physics enters.

## What changes by audience

**Anchor points.** A planner enters at the project and the finding, and needs to know what the
model can support, not how to run it. An environmental engineering student enters at the physics.
An electrical engineer entering here should be pointed at the assumption structure, since they
will compare it against a measurement.

**Bridges.**
- Transportation: the link-and-node structure is the same abstraction as a traffic network. They
  already think in links; the emissions and the dispersion attach to those links.
- Electrical engineering: ask whether students have studied steady-state assumptions and whether
  that prior work helps them examine this model's assumptions. Do not equate a steady-state
  dispersion model with a frequency-domain formulation. Confirm the analogy before using it.
- Public health: the model output is their exposure input, and its assumptions propagate directly
  into their health estimate.

**Depth options.** A conceptual lesson can emphasize why modeling is useful and what its
outputs mean. An applied lesson can teach data preparation, configuration, execution, and output
interpretation with guided practice. A graduate lesson may focus on formulations, assumptions,
numerical methods, sensitivity, or validation. Select the cut order from those objectives.

The source course favored a complete walkthrough because configuration errors were scattered.
Retain that approach when independent operation is a goal and sufficient time exists. For other
objectives, use a bounded demonstration or selected steps and identify what is omitted.

## Where the real numbers come from

- CAL3QHC user guide, for model structure and input requirements
- CO Florida screening model and its 2012 report, FDOT, developed at UCF
- FHWA categorical finding technical document, for the screening ladder
- Local meteorological data for wind and stability inputs
- Surface roughness values from standard land-use tables

## Candidate EOP connections

- **EIA-C1** (Low) — explaining what an assessment is, what it requires, and why it matters, is
  precisely the framing of a screening ladder.
- **EIA-C3** (Medium) — interpreting an assessment metric, which is what a modeled concentration
  compared against a standard is.
- **ST-C1** (Low, rescalable) — the model is a designed system embedded in physical and social
  systems, and its boundaries are choices.
- **CT-S4** (Medium) — the precautionary principle, which is what conservative screening
  assumptions institutionalize.
- **EL-C5** (Medium) — data literacy, including knowing what a number's provenance is.

## Worked example

**Source-course walkthrough option.** A complete example was used because the
errors this topic produces are scattered configuration errors rather than one conceptual mistake.
A student who has watched a complete correct run has seen the shape of the thing; a student shown
only the interesting parts has not.

Use a site the students can picture. A campus or local example works better than a textbook case,
and current meteorological data works better than the dataset printed in a textbook years ago.
For the original I-4/SR 408 demonstration only, the [hypothetical geometry](../scenario/i4-sr408-expansion.md)
has 27 links across four approaches, 100 m queue links and 330 m running links for through
movements, and turn lanes at their storage lengths. Use the selected case's appropriate inputs
for other lessons. This geometry does not describe Sunshine Corridor; that case needs separate
geometry, receptors, meteorology and a suitable model before a dispersion exercise can run.

The five steps:

1. Where the data comes from. Traffic volumes, meteorology, geometry, background concentration.
   Name the actual source for each.
2. How it is processed into what the model wants.
3. How it is loaded: the control file, the link definitions, the receptors.
4. How the run is executed, and what it looks like when it fails.
5. How the output is processed and interpreted, including against which averaging time.

An optional closing question asks whether the specific model used can represent the processes
needed for an ozone analysis. Establish its capabilities from the model documentation before
selecting a handoff to the regional ozone topic.

## Notes and caveats

**Provenance of this card's teaching content.** The misconception pattern, the priority ordering
of the depth ladder, the five-step example structure, and the cut order come from the instructor
directly, not from inference over slide decks. Retain them as reported observations from that course; confirm their relevance for another audience.

CAL3QHC is for carbon monoxide analysis and is explicitly not to be used for particulate hot-spot
analysis. Do not let generated material blur that.

The source demonstration does not account for acceleration lanes. That simplification should be
named in any material that uses the geometry, as an example of a modeling choice students should
learn to notice.

## Sources

- ENV 6106, Gaussian Model; CAL3QHC; Project-level demonstration
- ENV 4120, Gaussian Dispersion Model; Introduction to Air Quality Models
- CAL3QHC v2.0 user guide

## Version 5 course reference passages

The following passages provide topic-specific reference material. They do not verify all card claims or establish observed student difficulties, teacher endorsement, or completed field/model work.
- `ENV4120-10-gaussiandispersionmodel`, PDF pages [14](../library/text/4120/10-gaussiandispersionmodel.md#pdf-page-14), [19](../library/text/4120/10-gaussiandispersionmodel.md#pdf-page-19), [23](../library/text/4120/10-gaussiandispersionmodel.md#pdf-page-23). Gaussian formulation, assumptions and an existing stack example. This is not a near-road project result.
- `ENV6106-03-gaussian-model`, PDF pages [14](../library/text/6106/03-gaussian-model.md#pdf-page-14), [19](../library/text/6106/03-gaussian-model.md#pdf-page-19). Graduate Gaussian-model foundation and assumptions.
- `ENV6106-10-cal3qhc`, PDF pages [3](../library/text/6106/10-cal3qhc.md#pdf-page-3), [4](../library/text/6106/10-cal3qhc.md#pdf-page-4), [19](../library/text/6106/10-cal3qhc.md#pdf-page-19), [20](../library/text/6106/10-cal3qhc.md#pdf-page-20). Roadway model scope, receptor placement and queue-link notes; current applicability is unverified.
- `ENV6106-11-project-level-demo`, PDF pages [2](../library/text/6106/11-project-level-demo.md#pdf-page-2), [3](../library/text/6106/11-project-level-demo.md#pdf-page-3), [4](../library/text/6106/11-project-level-demo.md#pdf-page-4). Source teaching demonstration and link geometry; not verified site measurements or a complete runnable dataset.
