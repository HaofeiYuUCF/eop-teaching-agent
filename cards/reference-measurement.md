---
card: reference-measurement
title: Regulatory-grade ambient measurement and monitoring networks
author: Haofei Yu
institution: University of Central Florida
date: 2026-09-13
license: CC BY-NC-SA 4.0
status: full
chain_position: measurement (spans the chain)
prerequisites: [traffic-related-primary-pollutants]
leads_to: [low-cost-sensors]
revision: 3
author_acceptance: unconfirmed
adapted_by: [AI-assisted version 3 editorial revision]
claim_ids: [MON-01, MON-02, MON-03, ORL-05]
---

> **Source and adaptation status.** Topic content and teaching observations originated in the
> supplied version 2; the named original author's approval of these editorial changes is unconfirmed.
> Coverage status is not verification. Read [shared policy](../reference/workflow-policy.md) and
> [fact register](../reference/fact-register.md) before use. Register and verify essential claims
> not yet covered there. Classroom patterns and audience bridges are contextual suggestions, not
> established attributes of every student in a discipline. Confirm them during intake. Candidate
> outcomes and cut orders are selected or overridden by the accepted lesson plan.
## Topics

- Why a legally defensible measurement is a different object from a good measurement
- Federal Reference Methods and Federal Equivalent Methods, and what the distinction buys
- The US monitoring networks and what each exists to answer: SLAMS, NCore, PAMS, CSN, NATTS,
  IMPROVE, CASTNET, NADP
- Siting: what a monitor is meant to represent, and how that decides where it goes
- Gravimetric filter measurement as the reference for particulate matter
- Continuous methods and their characteristic biases
- Calibration as a system property, not an instrument property

## Expectations

After this topic a student should be able to:

- Explain what makes a measurement usable for comparison against a standard
- Choose which network would answer a given question, and say why the others would not
- Justify a monitor location from the purpose the measurement is meant to serve
- Explain why a continuous instrument can be more useful and less authoritative than a filter
- Describe at least two systematic biases in a real instrument and what is done about them

## Prerequisites

**Conceptual.** What an ambient concentration is. That a standard has an averaging time.
Accuracy and precision as distinct ideas.

**What students need to be able to do.** Concentration as mass over volume, and unit conversion. Nothing beyond that at
the working level.

## What students get wrong here

- **They assume a monitor measures "the air quality here."** A monitor measures the air at one
  point, chosen to represent something specific: a maximum, a population-typical exposure, a
  background, a source impact. Which one it was chosen to represent determines what its number
  means, and students almost never ask.
- **They think the reference method is the most accurate method.** It is the method the standard
  is defined against, which is a different and more interesting claim. A filter measurement with
  known volatilization losses is still the reference.
- **They expect calibration to be done on the instrument alone.** Sampling systems are calibrated
  assembled, at operating flows and conditions. Calibrating a component in isolation can be
  worthless.
- **They ignore humidity.** It affects both the sampled aerosol and the instrument, and it is the
  most commonly overlooked variable in the whole topic.
- **They assume continuous means better.** Continuous instruments have their own biases,
  including losses of volatile material at elevated filter temperature.

## What changes by audience

**Anchor points.** An electrical engineer enters at the instrument and learns outward to what the
number is for. A planner or policy audience enters at the network, since "where does the official
number come from" is their real question. An environmental engineering audience enters at the
method.

**Bridges.**
- Electrical engineering: this is metrology, and they already own it. Traceability, calibration
  chains, systematic versus random error, the difference between a sensor and a measurement
  system. The novelty is the analyte, not the discipline.
- Transportation and planning: a monitoring network is a sampling design under budget constraint,
  the same problem as placing traffic counters.
- Public health: exposure assessment rests on these numbers, and the siting purpose determines
  whether a monitor represents the population they care about.

**Depth options.** The treatments below reflect the source courses. Select and combine
them according to the accepted lesson objectives, prerequisites, and time. Technical detail may be
central to a graduate lesson. Suggested cuts below apply to the source teaching context and are
overridden by the lesson plan's explicit cut order.

**Depth ladder.**
- *Awareness*: the networks exist, they answer different questions, and where a monitor sits is a
  deliberate choice.
- *Working*: select a network and a siting rationale for a stated question; read a monitoring
  network plan.
- *Technical*: method principles, bias mechanisms and corrections, quality assurance requirements.

**Suggested cut for the source lesson:** the full network roster. Three networks taught well beats ten listed.
**Suggested content to protect in the source lesson:** that a monitor represents a chosen thing, and that the reference method defines
rather than perfects the measurement.

## Where the real numbers come from

- EPA list of designated reference and equivalent methods
- Florida DEP ambient air monitoring network plan, for Orlando-area monitor locations and purposes
- EPA AMTIC pages for each network
- 40 CFR Parts 50, 53, 58 for method and network requirements
- 40 CFR Part 58, Appendix D, for near-road monitoring requirements — **reported checked in version 2 on 2026-09-13; recheck before use**. A
  CBSA of 1,000,000 or more requires a near-road NO2 station, sited within 50 m of the target road
  segment, with CO and PM2.5 collocated; a second NO2 station is required above 2,500,000 or where
  a roadway segment carries 250,000 or greater AADT. See [fact register](../reference/fact-register.md).
- **Still unverified:** the Orlando CBSA population and local AADT, which together decide how many
  near-road stations the area actually requires.

## Candidate EOP connections

- **EL-C5** (Medium) — data literacy specifically about air quality data, including assessing and
  verifying it. This card is where that outcome is most literally earned.
- **EIA-C3** (Medium) — interpreting assessment metrics and what they imply.
- **EIA-C2** (Low) — recognizing reporting standards and methods that could improve their work.
- **SR-C4** (Medium, optional) — whether a network represents the populations most affected is a
  real and answerable question about siting.

## Worked example

Given the scenario corridor, decide where you would site a monitor to answer each of three
different questions: is the standard being met, what is the population near the road breathing,
and what is the regional background. Ask students to justify locations and discuss whether any
purposes could share a site under the supplied constraints. Do not require three distinct locations
without a basis.

## Notes and caveats

MON-01/02/03 preserve the inherited regulatory topics for rechecking. Verify both the full
requirements and their local inputs before stating how many stations are required. An imported
check date or a comparison of unverified counts does not establish present obligations.

## Sources

- ENV 5128, Monitoring Network; Aerosol Measurement 1-3; Ambient gas measurement
- Florida DEP ambient air monitoring network plan
- EPA AMTIC

## Version 5 course reference passages

The following passages provide topic-specific reference material. They do not verify all card claims or establish observed student difficulties, teacher endorsement, or completed field/model work.
- `ENV5128-02-monitoringnetwork`, PDF pages [3](../library/text/5128/02-monitoringnetwork.md#pdf-page-3), [4](../library/text/5128/02-monitoringnetwork.md#pdf-page-4), [5](../library/text/5128/02-monitoringnetwork.md#pdf-page-5), [6](../library/text/5128/02-monitoringnetwork.md#pdf-page-6), [7](../library/text/5128/02-monitoringnetwork.md#pdf-page-7), [8](../library/text/5128/02-monitoringnetwork.md#pdf-page-8). Monitoring network purposes and siting considerations; not a current regulatory verification.
- `ENV5128-04-aerosolmeasurement-1`, PDF pages [8](../library/text/5128/04-aerosolmeasurement-1.md#pdf-page-8), [11](../library/text/5128/04-aerosolmeasurement-1.md#pdf-page-11), [15](../library/text/5128/04-aerosolmeasurement-1.md#pdf-page-15), [19](../library/text/5128/04-aerosolmeasurement-1.md#pdf-page-19). Sampling loss, calibration, inlet design and sample drying.
- `ENV5128-07-ambient-gas-measurement`, PDF pages [4](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-4), [5](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-5), [6](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-6), [7](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-7). Gas measurement methods; figures require visual inspection.
