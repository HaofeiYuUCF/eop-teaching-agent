---
card: health-burden-of-traffic-pollution
title: Health burden of traffic-related air pollution
author: unassigned
institution: unassigned
date: 2026-09-13
license: CC BY-NC-SA 4.0
status: header-only
chain_position: effect
prerequisites: [traffic-related-primary-pollutants, near-road-dispersion-modeling]
leads_to: []
revision: 3
author_acceptance: unconfirmed
adapted_by: [AI-assisted version 3 editorial revision]
claim_ids: [HLT-01, ORL-07]
---

> **Source and adaptation status.** Topic content and teaching observations originated in the
> supplied version 2; the named original author's approval of these editorial changes is unconfirmed.
> Coverage status is not verification. Read [shared policy](../reference/workflow-policy.md) and
> [fact register](../reference/fact-register.md) before use. Register and verify essential claims
> not yet covered there. Classroom patterns and audience bridges are contextual suggestions, not
> established attributes of every student in a discipline. Confirm them during intake. Candidate
> outcomes and cut orders are selected or overridden by the accepted lesson plan.
> **Header-only card, and deliberately so.**
>
> The source course material for this library covers health *effects* qualitatively but does not
> cover quantified health impact assessment: concentration-response functions, baseline incidence,
> attributable burden. Rather than generate that content and present it as grounded, this card is
> shipped with its required fields empty.
>
> **This card is the recruitment ask made concrete.** It needs an author with a public health or
> environmental epidemiology background. It is what one contributed card would look like before a
> contributor fills it, and the three empty fields below are exactly the three that matter.
>
> A lesson depending on missing essential content should report the gap and request source
> preparation or propose a supported scope. A warning does not make ungrounded content ready to teach.

## Topics

- Health endpoints associated with traffic-related air pollution
- Concentration-response functions: what they are and where they come from
- From a modeled concentration change to an attributable health burden
- Population at risk, baseline incidence, and why both are needed
- Health impact assessment tools and what they assume
- Uncertainty propagation from the concentration estimate into the health estimate

## Expectations

*To be written by the card's author.* Intended shape: a student should be able to take a modeled
concentration change, combine it with a concentration-response function and population data, and
produce an attributable burden estimate while stating the assumptions that estimate inherits.

## Prerequisites

**Conceptual.** What a modeled concentration is, and crucially that it is not a measurement.
Exposure as distinct from ambient concentration. Risk as a population-level quantity.

**What students need to be able to do.** *To be specified by the author.* Expected floor: proportional reasoning and
spreadsheet arithmetic for a basic burden calculation. Higher levels would involve log-linear
response functions and uncertainty propagation.

## What students get wrong here

*Empty. Requires an author who has taught this.*

The one contribution from the modeling side of the library: **the health estimate inherits every
assumption made upstream.** Students treat a concentration input as given data and carry no
uncertainty forward, so a health number arrives with three significant figures and no error bar.
That is the teach-backward hook that makes this card belong in an air quality sequence rather
than a public health one.

## What changes by audience

**Anchor points.** A public health audience enters here, where they are strongest, and learns
backward along the chain toward where a concentration estimate comes from and why its provenance
matters to them. An engineering audience enters here last, as the reason the modeling was worth
doing.

**Bridges.**
- Public health: this is health impact assessment, which they know. What is new is the origin and
  uncertainty of the exposure input, not the method.
- Transportation and planning: attributable burden is a project impact expressed in a currency
  decision makers respond to, alongside travel time and cost.
- Electrical engineering: *unwritten.*

**Depth options.** The treatments below reflect the source courses. Select and combine
them according to the accepted lesson objectives, prerequisites, and time. Technical detail may be
central to a graduate lesson. Suggested cuts below apply to the source teaching context and are
overridden by the lesson plan's explicit cut order.

**Depth ladder.** *To be written by the author.*

**Suggested cut order by lesson purpose.** *Not yet supplied by a subject contributor.*

## Where the real numbers come from

*Largely empty, and the agent is instructed to say so rather than invent.* Starting points a
contributor should evaluate:

- EPA BenMAP and its underlying function library
- Published concentration-response literature, with attention to which populations the functions
  were derived in
- CDC and state health department baseline incidence data
- US Census for population within a distance buffer of the corridor

**Until this field is filled, no problem generated from this card may contain a numeric health
estimate.** A qualitative treatment is acceptable; a fabricated quantitative one is not.

## Candidate EOP connections

*Provisional, to be confirmed by the author.*

- **SR-C3** (Medium) — analyzing how engineering activities cause social and health impacts across
  the life cycle, to communities and to workers
- **SR-C4** (Medium) — examining which populations are disproportionately affected
- **EIA-C3** (Medium) — interpreting assessment metrics and their broader implications
- **EL-C5** (Medium) — data literacy, applied to health and exposure data

## Worked example

*Not written.*

## Notes and caveats

Health effects of air pollution are a settled area of science with genuinely contested edges,
particularly around low-concentration response and the attribution of specific outcomes.
Generated material must distinguish the two and must not present a contested estimate as settled.

The source version deferred research into the corridor's demographic context. This is a historical
scope choice, not an instruction from the current user. A requested extension requires appropriate
sources and review; see the selected scenario and its fact-register entries.

## Sources

- ENV 4120, Transport and Effects, for the qualitative health effects treatment
- Everything else: to be supplied by the card's author

## Version 5 course reference passages

The following passages provide topic-specific reference material. They do not verify all card claims or establish observed student difficulties, teacher endorsement, or completed field/model work.
- `ENV4120-04-transport-effects`, PDF pages [11](../library/text/4120/04-transport-effects.md#pdf-page-11), [12](../library/text/4120/04-transport-effects.md#pdf-page-12), [13](../library/text/4120/04-transport-effects.md#pdf-page-13). Health-effects teaching context, not a local burden estimate or supplied incidence dataset.
- `ENV4120-11-introductiontoairqualitymodel`, PDF pages [25](../library/text/4120/11-introductiontoairqualitymodel.md#pdf-page-25), [26](../library/text/4120/11-introductiontoairqualitymodel.md#pdf-page-26), [33](../library/text/4120/11-introductiontoairqualitymodel.md#pdf-page-33), [37](../library/text/4120/11-introductiontoairqualitymodel.md#pdf-page-37). Exposure estimation and model context; not validation of health outcomes.
