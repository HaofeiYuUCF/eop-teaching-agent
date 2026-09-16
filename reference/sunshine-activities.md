# Sunshine Corridor activity patterns - instructor resource

These are reusable illustrations, not an accepted lecture or canonical classroom assessment.
Select and adapt them through intake, then create the lesson's
[canonical assessment package](assessment-package.md). Copy only student sections and approved
assets to student outputs. Keep solutions, private rubrics and verification code separate.
Source records are in the [fact register](fact-register.md); context is in the
[case](../scenario/sunshine-corridor.md).

## SC-P1: What does the evidence establish?

**Candidate objective:** distinguish a source forecast, a stipulated assumption and a derived result,
and identify evidence needed for an air-quality claim. Allow 12 minutes after introducing these terms.
Tools: the source summary below. No mathematical prerequisite.

### Student prompt

The April 2024 TCAR report's Table 13 (printed 76-77, PDF 93-94) forecasts 4.4 million annual
system boardings for option 3A+3B in its assumed 2026 opening year. Section 7.1.3 explains that
one trip with a transfer can count twice and that forecasts cover the entire system. The report
lists air quality as a project objective (Executive Summary, printed x / PDF 12).

Classify these statements and explain what each can establish:

1. "The report forecasts 4.4 million annual system boardings for this option."
2. "For our exercise, assume 40% of new-to-transit passenger journeys replace car travel."
3. "Using the exercise inputs, the computed emissions change is -12 kg NOx/day."
4. "The corridor has therefore removed 4.4 million cars and improved everyone's health."

Identify three additional types of evidence needed to move toward an actual air-quality evaluation.
Give a short, evidence-limited conclusion. The numeric result in statement 3 is supplied for
classification; you do not need to calculate it. If using this before SC-P2 as an unseen assessment,
replace its number with "a decrease" to avoid revealing SC-P2's answer.

### Instructor answer and grading (10 points)

1 is an attributed historical forecast, not observed ridership (2 points). 2 is a stipulated
assumption, not the report's mode-shift estimate (2). 3 is a derived conditional result, whose
arithmetic does not verify its inputs (2). 4 is unsupported: boardings are not avoided car trips,
and emissions do not establish health outcomes (2). Award 2 for three relevant evidence needs
and a bounded conclusion: e.g., actual avoided road travel/occupancy, incremental transit and
access activity with applicable NOx factors, and spatial emissions/meteorology/receptors for
concentrations. Other justified needs are valid. Health analysis would also need exposure and
applicable health evidence. Accept any defensible conclusion; do not grade support for rail.

Claim dependencies: SC-03, SC-04, SC-06, SC-HYP-01, SC-DER-01. Numerical verification is
not applicable to classification; the supplied result is checked separately for SC-P2.

## SC-P2: A conditional daily NOx balance

**Candidate objective:** calculate a net emissions change with units and state its boundary.
Allow 20 minutes after a 10-minute worked demonstration of activity times factor and g-to-kg
conversion. Tools: calculator or spreadsheet. All data below are **synthetic teaching assumptions
(SC-HYP-01), not TCAR forecasts, measurements or output from an emissions model**.

### Student prompt and complete inputs

Compare a baseline with a stipulated added transit service for one representative day. Account
only for tailpipe NOx from displaced road travel, added trains and added road access/egress.

| Input | Symbol | Stipulated value |
|---|---|---|
| New-to-transit one-way passenger journeys per day, counting each journey once despite transfers | J | 10,000 journeys/day |
| Fraction of these journeys replacing car travel | f | 0.40 |
| Displaced line-haul road distance | d | 20 km/vehicle trip |
| Occupancy of removed vehicle trips | o | 1.25 persons/vehicle |
| Avoided road tailpipe NOx factor | e_road | 0.50 g/vehicle-km |
| Additional train operation relative to baseline | T | 800 train-km/day |
| Added train tailpipe NOx factor | e_transit | 20 g/train-km |
| Additional road access/egress NOx, already calculated separately | access_g | 4,000 g/day |

Assume complete travel parties shift, so dividing displaced passenger journeys by occupancy
counts vehicles that no longer travel. Every journey is one-way; do not double for a return trip.
The other 60% of journeys replace no car travel in this exercise. The added train service and
access total are fixed. Unchanged baseline emissions cancel. Exclude construction, upstream
energy, non-exhaust emissions and changes in other transit services; do not claim lifecycle totals.
The train factor stipulates a hypothetical emitting service and makes no claim about actual propulsion.

Use `avoided_vehicle_km = J*f*d/o` and
`delta_g = T*e_transit + access_g - avoided_vehicle_km*e_road`.

Calculate avoided vehicle-km/day, avoided road NOx, added NOx and net change in kg/day.
Interpret the sign and state two limits on using this answer to describe Sunshine Corridor impacts.
Public criteria: correct units, transparent reasoning and conclusions confined to the assumptions.

### Instructor worked solution and rubric (10 points)

Displaced passenger journeys = 10,000 x 0.40 = 4,000/day. Removed vehicle trips = 4,000/1.25
= 3,200/day. Avoided distance = 3,200 x 20 = **64,000 vehicle-km/day** (2 points).
Avoided road NOx = 64,000 x 0.50 = 32,000 g/day = **32 kg/day** (2).
Added train NOx = 800 x 20 = 16,000 g/day; with access, **20 kg/day** added (2).
Delta = 20 - 32 = **-12 kg NOx/day**, a decrease within the stipulated boundary (2).
Award 2 for two material limits, such as synthetic mode shift/factors, full-vehicle displacement,
fixed service, omitted lifecycle sources, or no concentration/exposure inference. Accept equivalent
units and a clearly defined opposite sign convention. Give method credit after an arithmetic error.

Claim dependencies: SC-HYP-01 and SC-DER-01. Recheck the worked calculations above with a
calculator or spreadsheet; historical checks are recorded in [validation record](v4-validation.md).
This file is instructor-only when assembling a student package.

## SC-P3: When does the sign change?

**Candidate objective:** evaluate sensitivity, derive or numerically identify break-even, and defend
the model's limitations. Allow 35 minutes in a lab/homework after SC-P2; do not count that time
inside the lecture. Tools: supported algebra and calculator, or spreadsheet with a demonstrated
parameter table. Adapt the objective if independent algebra or computing has not been taught.

### Student prompt

Use the same synthetic inputs and boundary as SC-P2. Hold service, access and all other inputs
fixed while testing f = 0, 0.20, 0.25, 0.40 and 0.80. Tabulate the net NOx change. Derive the
break-even fraction or locate it with a spreadsheet. Then change the train factor from 20 to
30 g/train-km and find the new threshold and result at f = 0.40.

Explain whether each parameter combination supports a decrease inside the stated boundary.
Name a condition under which the fixed-service calculation would need revision, and propose the
additional data/model work needed before making a local concentration or exposure claim.
Submit a small table plus a 150-250 word explanation; a documented formula or spreadsheet is sufficient.

### Instructor worked solution and rubric (12 points)

With the original inputs, avoided road emissions = 80f kg/day and added emissions = 20 kg/day,
so delta = 20 - 80f. Results:

| f | Net kg NOx/day |
|---|---:|
| 0 | +20 |
| 0.20 | +4 |
| 0.25 | 0 |
| 0.40 | -12 |
| 0.80 | -44 |

Break-even f = 20/80 = **0.25** (25%). With 30 g/train-km, train emissions are 24 kg/day;
total added = 28 kg/day, threshold = **0.35** (35%), and at f=0.40 delta = **-4 kg/day**.
At zero car displacement the added service still emits. Higher f lowers delta only under the
stipulated fixed parameters; if service or access changes with f, recompute those terms.
If the threshold is greater than one, no feasible fraction yields a decrease in this model.

Award 3 points for the table and units, 3 for both thresholds with a transparent method, 2 for
the altered-factor result and interpretation, 2 for a justified boundary/parameter limitation,
and 2 for the additional evidence plan. Examples: spatial and time-resolved emissions,
meteorology and dispersion modeling for concentrations; time-location/population information
for exposure. Accept different defensible project recommendations supported by the analysis.
Do not infer improved health, current ridership, actual propulsion or an observed project outcome.

Dependencies and computation checks: SC-HYP-01, SC-DER-01 and
[verification record](v4-validation.md). No EOP outcome is automatically assigned; intake maps
the selected observable work to verified framework wording when preparing the actual lesson.
