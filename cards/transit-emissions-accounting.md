---
card: transit-emissions-accounting
title: Conditional emissions accounting for a transit alternative
author: AI-assisted teaching draft; instructor author not assigned
institution: Not assigned
date: 2026-09-15
revision: 1
adapted_by: [AI-assisted version 4 development]
ai_assistance: Original instructional synthesis and synthetic exercise; report context is attributed separately
license: CC BY-NC-SA 4.0 for original teaching content
status: full
author_acceptance: unconfirmed
source_contexts: [Sunshine Corridor TCAR April 2024; no classroom trial]
prerequisites: []
leads_to: [near-road-dispersion-modeling, health-burden-of-traffic-pollution]
claim_ids: [SC-03, SC-04, SC-06, SC-HYP-01, SC-DER-01]
---

## Scope and candidate objectives

Define an emissions accounting boundary; distinguish journeys from boardings; calculate a
conditional change; and explain sensitivity and missing evidence. Air quality stays central.
Mobility and access can frame the decision but do not automatically add assessed planning topics.

## Prerequisites and support

Interpretation needs a supplied source summary and explanations of forecast and assumption.
Calculation needs ratios, multiplication and g-to-kg conversion; teach these before assessment
when unfamiliar. Advanced work needs algebra or a supported spreadsheet. No specialized model
software is required for the synthetic example. The
[road-emissions card](traffic-related-primary-pollutants.md) is optional supporting content.

## Student difficulties

Classroom observations are unknown. Hypotheses to check include equating boardings with cars
removed, omitting added transit/access emissions, mixing daily and annual values, and equating an
emissions decrease with an exposure benefit. SC-04 documents counting transfers, not the
prevalence of a student misconception.

## Content, model and example

SC-HYP-01 **defines a synthetic daily tailpipe NOx balance**, not a validated prediction model:

```
avoided_vehicle_km = J * f * d / o
avoided_road_g = avoided_vehicle_km * e_road
added_transit_g = T * e_transit
delta_g = added_transit_g + access_g - avoided_road_g
```

J is new-to-transit, one-way passenger journeys/day (each transfer-linked journey counted once);
f is the fraction replacing automobile travel; d is displaced road km/vehicle trip; o is mean
persons/displaced vehicle; e_road is g NOx/vehicle-km; T is added train-km/day relative to the
baseline; e_transit is stipulated g NOx/train-km. `access_g` is added daily access/egress road NOx.
Negative delta means lower emissions **inside this stipulated boundary**.

The displaced travel parties are assumed to remove whole vehicle trips, making division by
occupancy appropriate. If a former passenger switches but their car still travels, this assumption
fails; use actual avoided vehicle trips instead. Train-km counts trains, not cars in a train.
Access emissions are incremental and separate from avoided line-haul travel. No existing transit
reallocation is included in this exercise. All quantities share the same day and pollutant basis.

For positive J, d and e_road, with fixed added emissions and occupancy:

```
f_break_even = (T * e_transit + access_g) * o / (J * d * e_road)
```

If the threshold exceeds 1, the stipulated model cannot break even at feasible f. If the avoided
emissions coefficient is zero, do not divide: compare the fixed added emissions directly; zero
added emissions then gives equality for all f. Changing service with demand requires a revised
model; the fixed-service sensitivity formula no longer suffices. This is arithmetic bookkeeping
under SC-HYP-01; SC-DER-01 records its executed checks, not empirical validation.

See [the case](../scenario/sunshine-corridor.md) and
[activities with solutions](../reference/sunshine-activities.md). Do not use forecast annual system
boardings as J. Reported forecasts SC-03/04 are for interpretation, separate from synthetic inputs.

## Adaptations and cuts

- Interpretation: annotate a claim and propose needed evidence; no algebra.
- Applied: supply a units table, show one calculation, then ask for the balance and its limits.
- Advanced: derive the threshold, test sensitivity and propose an evidence collection/modeling plan.
- Mixed backgrounds: use a shared question with a ratio refresher and optional spreadsheet extension.

Select by objectives and actual support. For a calculation lesson protect units, boundaries and
assumptions; cut optional policy/cost discussion before cutting supported practice.

## Data, EOP and review

Use [fact-register records](../reference/fact-register.md) SC-03/04/06 for dated source statements,
SC-HYP-01 for all numerical inputs and SC-DER-01 for conditional answers. Local factors and
real avoided trips are not established. Distinguish emissions from concentrations, exposure and
health outcomes; a mass balance establishes none of the latter.

Candidate EOP connections are deliberately unassigned until intake selects the observable work
and checks the [outcome catalog](../reference/eop-outcomes.md). Evidence appraisal and defended
boundary choices may support outcomes; multiplication alone does not establish systems feedback,
teamwork or attainment. This card's complete teaching coverage does not establish instructor
endorsement or classroom effectiveness. See [validation](../reference/v4-validation.md).
