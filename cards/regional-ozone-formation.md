---
card: regional-ozone-formation
title: Tropospheric ozone formation and why it is a regional problem
author: Haofei Yu
institution: University of Central Florida
date: 2026-09-13
license: CC BY-NC-SA 4.0
status: full
chain_position: ambient concentration
prerequisites: [traffic-related-primary-pollutants, near-road-dispersion-modeling]
leads_to: [air-quality-regulation]
revision: 3
author_acceptance: unconfirmed
adapted_by: [AI-assisted version 3 editorial revision]
claim_ids: [AQ-01, ORL-01, ORL-02, DER-03]
---

> **Source and adaptation status.** Topic content and teaching observations originated in the
> supplied version 2; the named original author's approval of these editorial changes is unconfirmed.
> Coverage status is not verification. Read [shared policy](../reference/workflow-policy.md) and
> [fact register](../reference/fact-register.md) before use. Register and verify essential claims
> not yet covered there. Classroom patterns and audience bridges are contextual suggestions, not
> established attributes of every student in a discipline. Confirm them during intake. Candidate
> outcomes and cut orders are selected or overridden by the accepted lesson plan.
## Topics

- Ozone as a secondary pollutant, and what that means operationally
- The photostationary state: nitrogen dioxide photolysis, ozone formation, and titration by
  nitric oxide
- The role of reactive organic gases in breaking the null cycle
- Why roadside ozone is often lower than regional ozone
- Spatial and temporal scale: why the peak is downwind and in the afternoon
- Why a dispersion model cannot answer an ozone question, and what can
- Cross-scale consequences: conditions and evidence needed to compare local and regional responses

## Expectations

After this topic a student should be able to:

- Explain why ozone is not emitted and what follows from that
- Sketch the null cycle and explain what reactive organic gases do to it
- Predict where and when the ozone peak occurs relative to a source
- Explain why nitrogen oxide emissions can lower ozone locally and raise it regionally
- Determine that a dispersion model is the wrong tool for an ozone question, and say what class of
  model is right

## Prerequisites

**Conceptual.** Primary versus secondary pollutants. Basic reaction kinetics, rate and rate
constant, at a refresher level. Transport and dilution from the dispersion card, since the
contrast with a primary pollutant is the point.

**What students need to be able to do.**
- *Awareness*: none. The qualitative story is complete and correct without equations.
- *Working*: rate expressions, and the algebra of a steady state.
- *Technical*: the photostationary state relation, isopleth interpretation, sensitivity regimes.

## What students get wrong here

- **They look for an ozone source.** Students search for what emits ozone and are genuinely
  disoriented when told nothing does. This confusion is productive and worth sitting in rather
  than resolving quickly.
- **They expect the worst ozone at the busiest road.** The opposite is often true, and the reason,
  titration by fresh nitric oxide, is counterintuitive enough that stating it once is not enough.
- **They assume reducing nitrogen oxides always reduces ozone.** Whether it does depends on the
  chemical regime, and the wrong assumption has produced real policy errors.
- **They apply dispersion intuition to a secondary pollutant.** Dilution reduces a primary
  pollutant; for ozone, dilution of the titrating species can raise the concentration.
- **They collapse the timescales.** Formation takes hours, which is why the peak is downwind of
  the city rather than in it.

## What changes by audience

**Anchor points.** A transportation audience arrives here at the end of a dispersion lecture, as
the pollutant their analysis could not see. A chemistry-capable audience enters at the mechanism.
A policy audience enters at the regional and multi-jurisdictional character of the problem.

**Bridges.**
- Transportation: ozone is the reason a project's air quality consequence is not confined to the
  project's footprint, which reframes what the analysis boundary should be.
- Electrical engineering: the null cycle is a feedback loop with a forcing term, and the
  photostationary state is a steady-state solution. Familiar structure, unfamiliar variables.
- Public health: the exposure surface for ozone is regional and time-shifted, which means a
  near-road exposure estimate does not transfer.

**Depth options.** The treatments below reflect the source courses. Select and combine
them according to the accepted lesson objectives, prerequisites, and time. Technical detail may be
central to a graduate lesson. Suggested cuts below apply to the source teaching context and are
overridden by the lesson plan's explicit cut order.

**Depth ladder.**
- *Awareness*: ozone is made, not emitted; it peaks downwind in the afternoon; roadside values are
  often low; the local analysis cannot see it. This is complete and honest with no chemistry.
- *Working*: the null cycle, the role of reactive organic gases, qualitative regime reasoning.
- *Technical*: photostationary state algebra, isopleth reading, regime diagnosis.

**Suggested cut for the source lesson:** the detailed mechanism and rate constants.
**Suggested content to protect in the source lesson:** secondary formation, titration near the road, and that a dispersion model cannot
answer the question. Those three carry the entire pedagogical payload.

## Where the real numbers come from

- EPA air trends for regional ozone concentrations and trends
- Florida DEP monitoring network for local ozone data
- PAMS network data for ozone, nitrogen oxides, and volatile organic compound relationships
- The current 8-hour ozone standard is 0.070 ppm, set in 2015 — **reported checked in version 2 on 2026-09-13; recheck before use**, see
  [fact register](../reference/fact-register.md).
- ORL-01/02 retain reported design values as unverified inputs. DER-03 records the unsupported
  meteorological-margin inference. Do not teach a local trend or significance claim until the
  relevant periods, observations, and interpretation are supported.

## Candidate EOP connections

- **ST-C2** (Medium) — an activity explicitly tracing dynamic interactions or feedback across
  scales under supported assumptions. Do not assume a local-versus-regional sign reversal.
- **ST-C1** (Low, rescalable) — interconnectedness, including synergies and rebound effects.
- **EL-C3** (Medium) — global cycles and how they interconnect and affect design solutions.
- **CT-C1** (Low, rescalable to Medium) — defining problems with attention to uncertainties and
  unintended consequences, which here means recognizing that the problem boundary was drawn wrong.

## Worked example

Take the scenario project's estimated change in nitrogen oxide emissions. Ask two questions: what
happens to ozone at a receptor beside the roadway, and what happens to ozone in the region
downwind. Ask what determines each response and whether the information is sufficient to
predict its sign. Accept a justified conclusion that more evidence is needed.

Second turn: what tool would you need to answer the regional question properly, and why is it not
the model you used last week?

## Notes and caveats

The regime question, whether an area is limited by nitrogen oxides or by organic compounds, is
genuinely local and genuinely contested. Material generated from this card should present it as a
question requiring local evidence, not as a fact about the area.

## Sources

- ENV 4120, Tropospheric Ozone
- ENV 5128, Monitoring Network, PAMS section

## Version 5 course reference passages

The following passages provide topic-specific reference material. They do not verify all card claims or establish observed student difficulties, teacher endorsement, or completed field/model work.
- `ENV4120-05-troposphericozone`, PDF pages [6](../library/text/4120/05-troposphericozone.md#pdf-page-6), [14](../library/text/4120/05-troposphericozone.md#pdf-page-14), [20](../library/text/4120/05-troposphericozone.md#pdf-page-20), [21](../library/text/4120/05-troposphericozone.md#pdf-page-21), [24](../library/text/4120/05-troposphericozone.md#pdf-page-24), [25](../library/text/4120/05-troposphericozone.md#pdf-page-25). Ozone chemistry, precursor relationships and control diagrams.
- `ENV5128-01-airpollutionbasics-2`, PDF pages [7](../library/text/5128/01-airpollutionbasics-2.md#pdf-page-7), [13](../library/text/5128/01-airpollutionbasics-2.md#pdf-page-13), [19](../library/text/5128/01-airpollutionbasics-2.md#pdf-page-19), [20](../library/text/5128/01-airpollutionbasics-2.md#pdf-page-20), [23](../library/text/5128/01-airpollutionbasics-2.md#pdf-page-23), [24](../library/text/5128/01-airpollutionbasics-2.md#pdf-page-24). Related graduate-course refresher; preserve the source-specific sequence.
