---
card: meteorology-for-dispersion
title: Meteorology for dispersion
author: Haofei Yu
institution: University of Central Florida
date: 2026-09-13
license: CC BY-NC-SA 4.0
status: partial
chain_position: dispersion
prerequisites: []
leads_to: [near-road-dispersion-modeling, regional-ozone-formation]
revision: 3
author_acceptance: unconfirmed
adapted_by: [AI-assisted version 3 editorial revision]
claim_ids: []
---

> **Source and adaptation status.** Topic content and teaching observations originated in the
> supplied version 2; the named original author's approval of these editorial changes is unconfirmed.
> Coverage status is not verification. Read [shared policy](../reference/workflow-policy.md) and
> [fact register](../reference/fact-register.md) before use. Register and verify essential claims
> not yet covered there. Classroom patterns and audience bridges are contextual suggestions, not
> established attributes of every student in a discipline. Confirm them during intake. Candidate
> outcomes and cut orders are selected or overridden by the accepted lesson plan.
> **Partial card.** Topics, expectations, misconceptions, and audience variation are written from
> the source lectures. The worked example and several data sources are not yet filled in. A
> contributor with a meteorology background should take this one.

## Topics

- Wind direction and speed, and reading a wind rose
- Why wind speed does two opposing things: transports further and dilutes more
- Atmospheric stability, lapse rates, and stability classes
- Mixing height and its daily cycle
- Scales of motion: general circulation down to sea breeze, valley breeze, and urban heat island
  flow
- Why the worst case is usually low wind speed with stable conditions

## Expectations

After this topic a student should be able to:

- Read a wind rose and state which direction the pollution goes
- Explain what atmospheric stability is without reciting a table
- Predict qualitatively how a concentration changes with wind speed and stability
- Identify the meteorological conditions that produce a worst-case concentration
- Explain why coastal Florida meteorology is not generic meteorology

## Prerequisites

**Conceptual.** Temperature and pressure vary with height. Wind as a vector.

**What students need to be able to do.** Reading a polar plot. Lapse rate as a slope. At the technical level, the
adiabatic lapse rate derivation and stability criteria.

## What students get wrong here

- **The wind rose direction convention.** A wind rose shows where wind comes *from*; pollution
  goes the other way. Students get this backwards constantly, and it inverts every downstream
  answer.
- **They assume higher wind speed always means lower concentration.** Wind speed both dilutes and
  transports, and for elevated sources the interaction is not monotonic.
- **Stability becomes a lookup table.** Students memorize classes without any physical picture of
  what a rising parcel does, and then cannot reason about a case the table does not cover.
- **They use annual average meteorology for a worst-case question.** The standard is often a short
  averaging time, and the worst case is a specific condition, not the mean.

## What changes by audience

**Anchor points.** A transportation audience needs only enough to know why the answer depends on
the day and why the model asks for these inputs. An environmental engineering audience needs the
physical picture. A measurement audience needs it because siting and interpretation depend on it.

**Bridges.**
- Electrical engineering: stability is a question about whether a perturbation grows or decays,
  which is a stability analysis in their sense of the word too. The analogy is exact enough to be
  useful and should be stated.
- Transportation: worst-case meteorology is the design-condition idea they already use for peak
  hour.
- Public health: exposure varies enormously by hour and season, so an annual average conceals the
  events that matter.

**Depth options.** The treatments below reflect the source courses. Select and combine
them according to the accepted lesson objectives, prerequisites, and time. Technical detail may be
central to a graduate lesson. Suggested cuts below apply to the source teaching context and are
overridden by the lesson plan's explicit cut order.

**Depth ladder.**
- *Awareness*: wind carries it, stability controls how much it mixes, the worst case is calm and
  stable.
- *Working*: read a wind rose, select worst-case conditions, predict directional changes.
- *Technical*: lapse rates, stability classification schemes, mixing height, and how models
  ingest meteorological data.

**Suggested cut for the source lesson:** the general circulation, and the full scale hierarchy.
**Suggested content to protect in the source lesson:** the wind rose convention, and that low wind with stable conditions is the worst
case.

## Where the real numbers come from

- National Weather Service and NOAA station data for the local area
- Surface roughness values from standard land-use classification tables
- *Not yet identified:* an appropriate local meteorological dataset for the scenario, and a
  worked wind rose for the Orlando area

## Candidate EOP connections

- **EL-C3** (Medium) — examining global cycles, including energy and water, and how they connect
  to design solutions
- **EL-C5** (Medium) — data literacy, applied to meteorological data
- **ST-C1** (Low) — designs are embedded in physical and climate systems, which meteorology makes
  concrete rather than abstract

*A contributor should check whether a climate-adaptation outcome belongs here, given that the
meteorological conditions that produce worst cases are themselves shifting.*

## Worked example

*Not yet written.* Intended shape: given a local wind rose and a source location, identify which
receptors are downwind under worst-case conditions, and explain why the annual-average answer
would mislead.

## Notes and caveats

Florida-specific meteorology matters here and generic treatments will mislead. Sea breeze
circulation, high humidity, strong summer convection, and frequent afternoon thunderstorms all
affect both dispersion and photochemistry, and an instructor elsewhere would need to substitute
their own regional picture. That substitution is exactly what the audience-variation field is for.

## Sources

- ENV 4120, Air Pollution and Meteorology; Transport and Effects
- ENV 6106, Meteorology

## Version 5 course reference passages

The following passages provide topic-specific reference material. They do not verify all card claims or establish observed student difficulties, teacher endorsement, or completed field/model work.
- `ENV4120-09-airpollution-meteorology`, PDF pages [10](../library/text/4120/09-airpollution-meteorology.md#pdf-page-10), [11](../library/text/4120/09-airpollution-meteorology.md#pdf-page-11), [13](../library/text/4120/09-airpollution-meteorology.md#pdf-page-13), [21](../library/text/4120/09-airpollution-meteorology.md#pdf-page-21), [23](../library/text/4120/09-airpollution-meteorology.md#pdf-page-23), [24](../library/text/4120/09-airpollution-meteorology.md#pdf-page-24). Undergraduate source: wind rose, stability, lapse rate, inversions and mixing height.
- `ENV6106-02-meteorology`, PDF pages [11](../library/text/6106/02-meteorology.md#pdf-page-11), [13](../library/text/6106/02-meteorology.md#pdf-page-13), [21](../library/text/6106/02-meteorology.md#pdf-page-21), [23](../library/text/6106/02-meteorology.md#pdf-page-23), [24](../library/text/6106/02-meteorology.md#pdf-page-24). Graduate source: related meteorology concepts; keep its course context separate.
