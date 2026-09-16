---
card: low-cost-sensors
title: Low-cost air quality sensors and community monitoring
author: Haofei Yu
institution: University of Central Florida
date: 2026-09-13
license: CC BY-NC-SA 4.0
status: full
chain_position: measurement (spans the chain)
prerequisites: [reference-measurement]
leads_to: []
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
## Topics

- What a low-cost sensor actually measures, by sensing principle: optical scattering for
  particles, electrochemical and metal oxide for gases, non-dispersive infrared and photoacoustic
  for carbon dioxide
- Building one: microcontroller, I2C and UART, wiring, libraries, logging
- Behind the hype: can the data be trusted, and by what evidence
- Accuracy, inter-unit variability, cross-sensitivity, temperature and humidity effects,
  long-term drift
- Collocation against a reference monitor, and correction derived from it
- The coverage-versus-credibility trade, and how a network is designed around it
- Who maintains a deployed network, and what happens when nobody does
- Sensor lifetime, replacement cadence, and the waste stream of a deployed network

## Expectations

After this topic a student should be able to:

- Build and log data from a working particle or gas sensor
- Name the sensing principle of a given unit and predict its characteristic failure modes
- Design a collocation study and explain what it would and would not establish
- Judge whether a low-cost dataset can support a specific claim
- Argue, with evidence, why a community dataset should or should not be believed alongside a
  regulatory monitor
- State the maintenance and end-of-life burden of a deployed network

## Prerequisites

**Conceptual.** What a reference measurement is and why it exists, from the reference measurement
card. Accuracy versus precision. Basic circuit and microcontroller familiarity for the build.

**What students need to be able to do.** Linear regression and correlation for the collocation analysis. Reading a
scatter plot critically. Spreadsheet level throughout; no programming beyond copying and modifying
a sketch.

## What students get wrong here

- **They trust the number on the screen.** The unit prints three decimal places and students read
  that as precision. Inter-unit variability between two identical devices sitting side by side is
  the fastest cure, and the evidence for it already exists in published evaluations.
- **They think calibration is a one-time factory event.** Drift is continuous, and a correction
  derived in one season at one site may not hold in another.
- **They attribute a difference from the reference monitor to the reference monitor.** When a
  cheap sensor disagrees with a regulatory instrument, students' first instinct is often that the
  official number is wrong.
- **They confuse a high correlation coefficient with agreement.** Two instruments can track each
  other beautifully and differ by a factor of two.
- **They forget humidity.** Optical particle measurement responds to the particle's wet size, and
  a humidity-driven artifact looks exactly like a pollution event.
- **They do not think about who maintains it.** A fifty-node network is a fifty-node maintenance
  obligation, and student projects almost never plan for the second year.
- **They assume more nodes means better data.** More nodes means more coverage and the same
  per-node uncertainty.

## What changes by audience

**Anchor points.** An electrical engineer enters at the instrument and the build, which is where
they are strongest, and learns outward to what the measurement means and who uses it. A community
audience enters at the question "can I measure my own air," which is the honest and answerable
version of what they came to ask.

**Bridges.**
- Electrical engineering: drift, cross-sensitivity, baseline, inter-unit variability, calibration
  against a traceable standard. They already own every one of these concepts. What is new is that
  the analyte is a reactive gas or a hygroscopic aerosol in an uncontrolled environment, which
  breaks assumptions that hold in a lab.
- Environmental engineering: a low-cost network is a sampling design problem with a
  measurement-error budget.
- Public health: exposure misclassification is the reason spatial coverage is worth wanting, and
  measurement error is the reason it may not deliver.

**Depth options.** The treatments below reflect the source courses. Select and combine
them according to the accepted lesson objectives, prerequisites, and time. Technical detail may be
central to a graduate lesson. Suggested cuts below apply to the source teaching context and are
overridden by the lesson plan's explicit cut order.

**Depth ladder.**
- *Awareness*: these devices exist, they are cheap, here is what they can and cannot support.
- *Working*: build one, log data, collocate it, derive and apply a correction, state what the
  corrected data can support.
- *Technical*: sensing principle physics, characterization across temperature and humidity,
  network design under a measurement-error budget.

**Suggested cut for the source lesson:** the wiring detail and the code walkthrough, if there is no lab time.
**Suggested content to protect in the source lesson:** the collocation step. A build without a collocation teaches students to trust a
number they should not, which is worse than not teaching the topic.

## Where the real numbers come from

- AQ-SPEC laboratory and field evaluations, South Coast AQMD, for instrument-specific performance
- Published field evaluation literature for collocation results
- Manufacturer datasheets for the Plantower, Sensirion, Sensirion SCD4x, and Bosch BME680 families,
  read as claims rather than as measurements
- EPA guidance on air sensor performance targets and evaluation protocols
- Reference monitor data from the Florida DEP network for a collocation site

## Candidate EOP connections

- **EL-C5** (Medium) — assessing, critiquing, and verifying air quality data without
  greenwashing. This card is the most direct instance of that outcome in the library.
- **MAT-C1** (Low, rescalable to Medium) — sensor lifetime, replacement cadence, and the waste
  stream of a deployed network are genuine materials impacts across a life cycle.
- **DES-C2** (High) — designing for durability, repairability, and serviceability, which for a
  field-deployed enclosure in a hot humid climate is a real constraint rather than a slogan.
- **RBE-C5** (High) — weighing the short and long term costs of the work, which is exactly the
  question of who maintains the network in year three.
- **COM-C1** (Medium) — communicating a technical result to a non-expert audience, if the
  community-data scenario is used.
- **SR-C2** (Low) — recognizing the justice implications of who gets measured and who does not.

## Worked example

Two parts.

First, the build: wire an optical particle sensor to a microcontroller, log data, and observe two
identical units disagreeing.

Second, the judgment: a community group deploys sensors along the scenario corridor and reports
values higher than the nearest regulatory monitor. Students are asked what would have to be true
for the community data to be right, what would have to be true for the monitor to be right, and
what further investigation would best distinguish the cases under the stated constraints.
Collocation is a candidate approach to evaluate. Accept other justified investigations and specify
enough context before treating any one approach as uniquely correct.

## Notes and caveats

This card deliberately joins two things that are usually taught apart: the build and the
skepticism. A course that teaches students to assemble a sensor without teaching them what it does
in the field has taught them to produce numbers they cannot defend.

On the community-data scenario: it is genuinely two-sided and should stay that way. Community
measurements have revealed real problems that official networks missed, and have also produced
alarming artifacts. Material generated from this card must not resolve the tension in advance.

## Sources

- ENV 5128, IoT in Air Quality Monitoring; Ambient gas measurement, "Behind the hype"; Aerosol
  Measurement 1, sampling issues in low-cost sensors
- AQ-SPEC evaluations, South Coast AQMD
- Lewis et al., low-cost sensor assessment, WMO

## Version 5 course reference passages

The following passages provide topic-specific reference material. They do not verify all card claims or establish observed student difficulties, teacher endorsement, or completed field/model work.
- `ENV5128-07-ambient-gas-measurement`, PDF pages [11](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-11), [15](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-15), [16](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-16), [18](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-18), [19](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-19), [20](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-20), [21](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-21), [22](../library/text/5128/07-ambient-gas-measurement.md#pdf-page-22). Sensor types, data-quality limitations, environmental response, cross-sensitivity and calibration.
- `ENV5128-env-6128-iot-in-air-quality-monitoring-10222024`, PDF pages [1](../library/text/5128/env-6128-iot-in-air-quality-monitoring-10222024.md#pdf-page-1), [18](../library/text/5128/env-6128-iot-in-air-quality-monitoring-10222024.md#pdf-page-18), [19](../library/text/5128/env-6128-iot-in-air-quality-monitoring-10222024.md#pdf-page-19), [22](../library/text/5128/env-6128-iot-in-air-quality-monitoring-10222024.md#pdf-page-22), [23](../library/text/5128/env-6128-iot-in-air-quality-monitoring-10222024.md#pdf-page-23), [26](../library/text/5128/env-6128-iot-in-air-quality-monitoring-10222024.md#pdf-page-26), [27](../library/text/5128/env-6128-iot-in-air-quality-monitoring-10222024.md#pdf-page-27). IoT and sensor examples; retain the cover contributor credit and course label ENV 6128.
