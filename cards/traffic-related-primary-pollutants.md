---
card: traffic-related-primary-pollutants
title: Primary pollutants from road traffic
author: Haofei Yu
institution: University of Central Florida
date: 2026-09-13
license: CC BY-NC-SA 4.0
status: full
chain_position: emissions
prerequisites: []
leads_to: [near-road-dispersion-modeling, regional-ozone-formation, health-burden-of-traffic-pollution]
revision: 3
author_acceptance: unconfirmed
adapted_by: [AI-assisted version 3 editorial revision]
claim_ids: [EF-01, EF-02, EF-03, EF-04, ORL-03, ORL-04]
---

> **Source and adaptation status.** Topic content and teaching observations originated in the
> supplied version 2; the named original author's approval of these editorial changes is unconfirmed.
> Coverage status is not verification. Read [shared policy](../reference/workflow-policy.md) and
> [fact register](../reference/fact-register.md) before use. Register and verify essential claims
> not yet covered there. Classroom patterns and audience bridges are contextual suggestions, not
> established attributes of every student in a discipline. Confirm them during intake. Candidate
> outcomes and cut orders are selected or overridden by the accepted lesson plan.
## Topics

- Criteria pollutants and hazardous air pollutants, and why traffic matters for both
- Primary versus secondary, and why that distinction decides everything downstream
- Source classification: stationary and mobile; point, area, volume, and line
- The emission calculation `E = A x F x adj`, activity times emission factor times adjustment
- Speed dependence of emission factors, and why it differs by pollutant
- Exhaust versus non-exhaust particulate

## Expectations

After this topic a student should be able to:

- Distinguish primary from secondary pollutants and predict which analytical approach each needs
- Compute emissions from activity data and an emission factor, carrying units correctly
- Explain why a roadway is modeled as a line source rather than a point
- Predict the direction, not just the magnitude, of an emissions change when traffic speed and
  volume both change
- Identify which pollutants a congestion-relief project could plausibly make worse

## Prerequisites

**Conceptual.** What an air pollutant is. That concentration and emission are different
quantities. Basic familiarity with how traffic is described: volume, speed, level of service.

**What students need to be able to do.** Unit conversion and multiplication. That is the whole floor for the awareness
and working levels. Nothing above algebra is required anywhere in this card.

## What students get wrong here

- **Emissions and concentrations get used interchangeably.** Students will say "emissions went
  up" when the data shows a concentration, and vice versa. Worth a deliberate correction early,
  because every later confusion in the sequence traces back to this one.
- **They assume faster traffic is always cleaner.** Test this proposed reasoning error with
  the factors actually supplied in the exercise. Do not assign a universal speed relationship
  or transfer the imported study's threshold to a local fleet; see EF-01/02.
- **They forget non-exhaust particulate exists.** Brake, tire, and road dust emissions are
  invisible in most introductory treatments, so students conclude that an electric fleet solves
  particulate matter. It does not.
- **They treat the emission factor as a property of the vehicle** rather than of the vehicle
  operating at a particular speed, load, temperature, and age.
- **Sign errors in the combined effect.** Given both a speed increase and a volume increase,
  students compute each correctly and then guess at the combination instead of working it.

## What changes by audience

**Anchor points.** A transportation audience enters at activity data, which they already own, and
learns outward to what an emission factor is. An environmental engineering audience enters at the
pollutant and learns outward to where the activity data comes from. A public health audience
should be brought here only briefly, as the upstream origin of the concentrations they care about.

**Bridges.**
- Transportation and planning: `E = A x F x adj` is structurally the trip-generation logic they
  already use, with a different factor. Their AADT and level of service are the `A`.
- Electrical engineering: an emission factor is a transfer function with operating-point
  dependence. They have seen this shape before.
- Public health: activity times factor is the same arithmetic as exposure times a unit risk
  coefficient, one step earlier in the chain.

**Depth options.** The treatments below reflect the source courses. Select and combine
them according to the accepted lesson objectives, prerequisites, and time. Technical detail may be
central to a graduate lesson. Suggested cuts below apply to the source teaching context and are
overridden by the lesson plan's explicit cut order.

**Depth ladder.**
- *Awareness*: qualitative. Which pollutants come from traffic, primary versus secondary, why the
  answer is not obvious. No calculation.
- *Working*: compute emissions for a link from volume, length, and an emission factor table.
  Compare two scenarios and get the sign right for three pollutants.
- *Technical*: engage with the emission model itself, operating mode distributions, fleet
  composition, temperature and fuel effects.

**Suggested cut for the source lesson:** hazardous air pollutants, and the source-shape taxonomy beyond line sources.
**Suggested content to protect in the source lesson:** why any of this matters, primary versus secondary, and the pollutant-specific
direction of the speed effect. Those carry the entire rest of the sequence.

## Where the real numbers come from

- A documented MOVES run is a candidate source for a US modeling exercise; record version and
  applicable inputs. Other suitable measured/model data require explicit scope and justification.
  Synthetic factors are allowed for labeled hypothetical exercises. See EF-04.
- Gao et al. (2022), *Atmospheric Pollution Research* 13, 101421, is an imported candidate
  source for comparing fleet-specific findings. EF-01/02 record the required source check and
  applicability limits; neither local direction nor magnitude is established by this citation alone.
- **Non-exhaust particulate behaviour is currently unsourced.** Do not state it as fact until it is.
- FDOT traffic count data for Florida activity data.
- EPA National Emissions Inventory for sector shares.
- EPA air trends reports for national emission and concentration trends over time.

If an actual factor cannot be retrieved, record the gap. An explicitly labeled hypothetical
exercise may use a stipulated factor; do not present that value as an observed or executed-model result.

## Candidate EOP connections

- **ST-C2** (Medium) — a task that explicitly analyzes a feedback mechanism, such as an
  appropriately evidenced or stipulated response of travel demand to a capacity change. Two inputs
  changing in opposite directions do not by themselves demonstrate feedback.
- **EL-C5** (Medium) — data literacy, specifically air quality data, is what reading an emission
  factor table well amounts to.
- **EIA-S1** (Low) — relative versus absolute impact reduction. The framework's own example is
  vehicle emissions per mile versus total emissions, which is exactly this card's tension.
- **CT-C1** (Low, rescalable to Medium) — defining the problem with attention to unintended
  consequences.

## Worked example

Two scenarios for the same roadway link: before, congested at a low average speed; after,
free-flowing at a higher speed with more vehicles. Students compute emissions for carbon
monoxide, nitrogen oxides, and particulate matter under sourced or visibly stipulated factors.
Let the computed results determine their directions. Ask which comparisons and assumptions a
decision maker needs and what would make a selective presentation misleading.

## Notes and caveats

Check speed relationships for the selected fleet, operating conditions, pollutant and source
version before predicting signs or magnitudes. EF-01 through EF-04 are unresolved source dependencies.
Do not assert a quantified or growing non-exhaust share without appropriate evidence.

## Sources

- ENV 6106, Mobile Source Overview and introduction to MOVES
- ENV 4120, Air Pollution Sources
- MOVES user guide
- EPA air emissions inventories

## Version 5 course reference passages

The following passages provide topic-specific reference material. They do not verify all card claims or establish observed student difficulties, teacher endorsement, or completed field/model work.
- `ENV4120-03-airpolltuionsource`, PDF pages [4](../library/text/4120/03-airpolltuionsource.md#pdf-page-4), [8](../library/text/4120/03-airpolltuionsource.md#pdf-page-8), [9](../library/text/4120/03-airpolltuionsource.md#pdf-page-9), [10](../library/text/4120/03-airpolltuionsource.md#pdf-page-10), [13](../library/text/4120/03-airpolltuionsource.md#pdf-page-13). Primary/secondary categories and selected pollutant descriptions; not local emission factors.
- `ENV6106-07-mobile-source-overview`, PDF pages [2](../library/text/6106/07-mobile-source-overview.md#pdf-page-2), [6](../library/text/6106/07-mobile-source-overview.md#pdf-page-6), [9](../library/text/6106/07-mobile-source-overview.md#pdf-page-9). Mobile-source lecture context and emissions calculation introduction; no new MOVES execution.
