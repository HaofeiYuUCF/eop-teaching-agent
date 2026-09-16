# Fact Register

Read [workflow-policy.md](workflow-policy.md) for evidence requirements. The entries below are
inherited candidate claims and known gaps, not a newly verified scientific reference. No primary
sources were independently checked during the version 3 editing pass. Dates labeled as historical
are reported by version 2 and do not represent verification performed for version 3.
Version 4 adds the separately checked Sunshine records below; it does not upgrade the imported
claims. Verification of a report statement means the report supports that attributed statement,
not that its forecast has occurred or its real-world assumptions have been validated.

## Claim records

Add one record for each claim that materially affects teaching or an answer. Group closely related
claims only when evidence, applicability, and status are the same; split them when those differ.
Stable IDs below can be referenced from cards, notes, scenario inputs, and assessments.

```yaml
id: CLAIM-EXAMPLE
claim: Exact factual statement or explicitly stipulated premise.
kind: empirical # empirical | regulatory | conceptual | stipulated | derived | framework
evidence_status: unverified # verified | unverified | disputed | stipulated
source:
  reference: Actual source title/file/URL
  locator: Page, slide, table, section, or data query/version
  historical_check_reported: null
  verified_on: null # actual check date; do not copy an inherited date here
  verification_record: null # what was checked and supporting evidence
applicability: Fleet, place, pollutant, period, scale, units, averaging form, or other limits.
input_claim_ids: [] # for derived claims
computation_status: not-applicable # checked | failed | unverified | not-applicable
usage: Essential content or lesson/scenario IDs affected.
```

An empirical statement is verified only after its source supports the exact claim and its limits
are recorded. Stipulated premises need visible labels and consistency checks, not fabricated sources.
Derived results list their input IDs and retain their uncertainty. Record verified calculation separately
from verification of real-world inputs. Unregistered source-card claims remain unverified until checked.

## Imported reference claims awaiting source checks

All rows in this section have `evidence_status: unverified` and `verified_on: null` for this revision.
Reported version 2 checking is preserved as history. Reconstruct full forms and qualifications from
the primary sources before teaching regulations; a numeric threshold alone is insufficient.

| ID | Imported claim or subject to verify | Named source in version 2 | Historical check reported | Applicability / action |
|---|---|---|---|---|
| AQ-01 | Ozone 0.070 ppm, 8-hour, primary/secondary, annual fourth-highest daily maximum averaged over three years; set 2015 | [EPA NAAQS table](https://www.epa.gov/criteria-air-pollutants/naaqs-table) | 2026-09-13 | Verify current level, form, and effective requirements. |
| AQ-02 | CO 9 ppm 8-hour; 35 ppm 1-hour; primary; not exceeded more than once per year | EPA NAAQS table | 2026-09-13 | Verify current full standard. |
| AQ-03 | NO2 100 ppb 1-hour, 98th percentile of daily maxima over three years; 53 ppb annual mean | EPA NAAQS table | 2026-09-13 | Verify primary/secondary distinctions and forms. |
| AQ-04 | PM2.5 9.0 ug/m3 annual primary, 15.0 annual secondary, 35 24-hour | EPA NAAQS table | 2026-09-13 | Full statistical forms are not carried in this imported summary; retrieve them. |
| AQ-05 | PM10 150 ug/m3, 24-hour, primary/secondary | EPA NAAQS table | 2026-09-13 | Retrieve full current form and applicability. |
| MON-01 | CBSA population thresholds and roadway AADT conditions for first/second near-road NO2 stations | [40 CFR Part 58 Appendix D](https://www.ecfr.gov/current/title-40/part-58/appendix-Appendix%20D%20to%20Part%2058) | 2026-09-13 | Imported thresholds 1,000,000; 2,500,000; 250,000 AADT. Verify exact logic and exceptions. |
| MON-02 | Near-road siting within 50 m of target road | Version 2 names Part 58 Appendix D | 2026-09-13 | Verify correct siting provision and qualifications rather than assuming the cited appendix supports it. |
| MON-03 | Near-road CO and PM2.5 collocation requirements | Part 58 Appendix D | 2026-09-13 | Verify pollutant-specific requirements separately; split record as needed. |
| REG-01 | Current Orlando/Orange County attainment or maintenance designation | EPA Green Book / Florida DEP | None | Pollutant, standard, geography, and date required. No current designation established here. |
| REG-02 | Historical absence from Florida listings under revoked 1979 1-hour ozone standard | Version 2 names an EPA historical Green Book page without exact URL | 2026-09-13 | Historical only; cannot establish present status. |
| REG-03 | Which project-level analyses would be legally required | Applicable agency rules/guidance, exact references pending | None | Define pollutant, designation including maintenance, project type, and jurisdiction. Broad attainment assumptions alone are insufficient. |
| EF-01 | VOC, CO, and NOx speed relationships, including reported NOx rise above roughly 70 km/h | Gao et al. (2022), Atmospheric Pollution Research 13, 101421 | 2026-09-13 | Source scope reported as Shenyang China 4/5 passenger vehicles. Verify original results; neither sign nor magnitude is established for a US scenario. |
| EF-02 | Expressway rush-hour CO and NOx factors reported 102% and 72% above non-rush-hour | Same Gao et al. paper | 2026-09-13 | Verify measured comparison and fleet/operating conditions. Not a transferable project prediction. |
| EF-03 | Non-exhaust PM behavior with vehicle miles, speed, braking, and road conditions | Source not supplied | None | Do not assume speed independence or a quantified share without evidence. |
| EF-04 | Emission factors applicable to a US project | Candidate: documented MOVES run; other applicable measured/model sources require justification | None | Record fleet, model/version or measurement method, year, activity, temperature, and pollutant. |
| EOP-01 | EOP 2026 outcome text, IDs, and ABET/SDG mappings in this package | [Official EOP framework](https://engineeringforoneplanet.org/eop-framework/), imported catalog | None recorded | Catalog retained from version 2. Confirm selected passages/mappings against the edition before issuing an external alignment memo. |

## Instructor-provided inputs and derived conclusions

| ID | Candidate input or conclusion | Provenance / status | Usage limit |
|---|---|---|---|
| ORL-01 | Ozone design value approximately 62 ppb | Instructor-provided in version 2, 2026-09-13; unverified | Need monitor/area, three-year period, source and retrieval date before presenting as observed. |
| ORL-02 | Approximately 67 ppb about two years earlier | Same; unverified | Need exact period and comparable method before trend claims. |
| ORL-03 | SR 408 AADT approximately 196,500 | Instructor-provided in version 2; unverified | Need year, segment, direction, and source. |
| ORL-04 | I-4 AADT approximately 159,500 plus 12,500 and 9,000 | Instructor-provided in version 2; unverified | Meanings of additional figures unknown; do not aggregate. |
| ORL-05 | Population crosses a monitoring threshold | Input not supplied; unverified | Need relevant CBSA definition, date and population source, plus checked MON-01. |
| DER-01 | Margins between a standard and ORL-01/02 | Derived; unverified inputs AQ-01, ORL-01, ORL-02; computation not yet recorded | Arithmetic can be checked conditionally. It does not verify a local trend or forecast a violation. |
| DER-02 | Both corridors below a monitoring AADT trigger | Derived; unverified inputs ORL-03/04, MON-01; computation not yet recorded | A comparison of reported inputs cannot establish current requirements or conditions on other road segments. |
| DER-03 | Meteorological variation exceeds the local ozone margin, making a project NOx increment significant | Unsupported inference retained as a gap; unverified | Requires evidence for comparable periods, variation, chemical response, and project contribution. Do not assert it. |
| ORL-06 | Background concentration at project receptors | No dataset supplied; unverified | Specify pollutant, time, location, averaging basis and representativeness. |
| ORL-07 | Population near the corridor and exposure distribution | No dataset supplied; unverified | Local distribution or social-impact claims need appropriate sources. |
| HLT-01 | Concentration-response functions and baseline incidence | No quantitative source supplied; unverified | Blocks quantitative health-burden claims pending applicable evidence. |
| GEO-01 | 27-link geometry, 100 m queue and 330 m running segments, turn lengths | Imported ENV 6106 demonstration description; unverified as a real location | Can be adopted explicitly as hypothetical geometry; full runnable inputs are not supplied. |

## Hypothetical premises

| ID | Premise | Status and limits |
|---|---|---|
| HYP-01 | A hypothetical capacity change near I-4/SR 408, with an associated arterial intersection | Stipulated; does not describe an actual proposal. |
| HYP-02 | Geometry adopted from GEO-01 as a representative teaching schematic | Stipulated; not surveyed geometry and not a complete model input file. |
| HYP-03 | Before/after speeds, traffic volumes, and emission factors selected for an exercise | Not yet set. Add item-specific stipulated records with units and values before generating results. |
| HYP-04 | No project-level conformity hot-spot analysis is required within the hypothetical exercise | Optional stipulated administrative premise. It is not a legal determination or an inference from ozone designation. |

Do not replace instructor-reported real inputs with hypothetical ones silently. State that an exercise
adopts synthetic values and limit its conclusions to that exercise. Record any new premise explicitly.

## Version 4 Sunshine source records

The following records were checked on **2026-09-15** against the user-supplied *Sunshine Corridor
Transit Concept and Alternatives Review (TCAR), Final Report*, FDOT, April 2024, FPID 451404-1,
file `Sunshine_Corridor_TCAR_Final_Report.pdf` (119 PDF pages). PDF locators are one-based.
For SC-01 through SC-06: `kind: empirical`, `evidence_status: verified`,
`source.historical_check_reported: null`, `source.verified_on: 2026-09-15`,
`input_claim_ids: []`, `computation_status: not-applicable`.
These statuses verify attribution to the report, not current conditions or forecast accuracy.

| ID | Exact attributed claim | Source locator | Verification record and applicability | Usage |
|---|---|---|---|---|
| SC-01 | The report proposes connections among existing SunRail, MCO, OCCC, South I-Drive and optionally Disney Springs. | Executive Summary, printed ix-x; PDF 11-12 | Read source text and map on PDF 11; proposed 2024 program only. | Sunshine context |
| SC-02 | The report screens enhanced local bus, BRT, commuter rail and trackless tram and recommends commuter rail. | Printed xii-xiv; PDF 14-16 | Checked summary and screening discussion; recommendation under study criteria, not a required student judgment. | Alternatives interpretation |
| SC-03 | Table 13 forecasts 4,400,000 annual system boardings for 3A+3B in assumed opening year 2026 and 6,400,000 in 2040. | Table 13, printed 76-77; PDF 93-94 | Checked table rows/headers visually; total-system forecast, not observed trips, incremental journeys or avoided cars. | SC-P1 |
| SC-04 | Section 7.1.3 says a journey with transfer can count as two boardings, forecasts reflect the whole system, and commuter modeling used pre-pandemic conditions with later updates planned. | Section 7.1.3, printed 77; PDF 94 | Read complete page and qualifications; historical modeling basis, not current service or opening status. | SC-P1 and input separation |
| SC-05 | Table 14 lists 3B capital at $1.75-2.4 B and O&M at $23.2 M/year; 3BT $29-39 M is station only; 3C O&M $32.8 M/year includes 3B+3C; 3D $33.0 M/year includes 3B+3C+3D. | Table 14 and preceding text, printed 78; PDF 95 | Checked full table, notes and cost-scope prose visually; preliminary estimates with differing coverage, not current prices or directly additive/comparable rows. | Optional cost-reading context |
| SC-06 | Air quality and energy benefits through reduced single-occupant travel are stated project objectives. | Executive Summary, printed x; PDF 12 | Checked purpose/need text; an objective, not demonstrated emissions, concentration or health benefits. | SC-P1 and case framing |

### STAR-01: Separate policy source

```yaml
id: STAR-01
claim: Sunrise Movement Orlando's STAR page describes an advocacy proposal for eight rapid-transit corridors.
kind: empirical
evidence_status: verified
source:
  reference: https://www.sunriseorlandofl.org/star
  locator: Introductory description and STAR Plan Map section
  historical_check_reported: null
  accessed_on: 2026-09-15
  verified_on: 2026-09-15
  verification_record: Read the page and checked the proposal description and eight-corridor statement.
applicability: Attribution to an advocacy page only; separate from TCAR; does not verify official approval, project schedule, funding or effects. Recheck for later use.
input_claim_ids: []
computation_status: not-applicable
usage: Optional Sunshine policy context, not required for SC-P1 through SC-P3.
```

### SC-HYP-01: Complete synthetic exercise inputs and accounting definition

```yaml
id: SC-HYP-01
claim: A hypothetical daily tailpipe NOx balance uses the following stipulated inputs and boundary.
kind: stipulated
evidence_status: stipulated
source:
  reference: reference/sunshine-activities.md
  locator: SC-P2 complete inputs and SC-P3 sensitivity variations
  historical_check_reported: null
  verified_on: null
  verification_record: Original AI-assisted teaching assumptions created 2026-09-15; not empirical data.
inputs:
  new_to_transit_one_way_journeys_per_day: 10000
  replaces_car_fraction: 0.40
  displaced_road_km_per_vehicle_trip: 20
  persons_per_removed_vehicle: 1.25
  road_NOx_g_per_vehicle_km: 0.50
  added_train_km_per_day: 800
  train_NOx_g_per_train_km: 20
  added_access_NOx_g_per_day: 4000
  sensitivity_fractions: [0, 0.20, 0.25, 0.40, 0.80]
  alternative_train_NOx_g_per_train_km: 30
applicability: One representative day; journeys counted once across transfers; whole displaced vehicle trips; fixed incremental train service/access. Tailpipe NOx only, excluding construction, upstream energy, non-exhaust and other transit changes. Not inferred from TCAR ridership; no actual propulsion claim.
input_claim_ids: []
computation_status: not-applicable
usage: Transit card and SC-P2/SC-P3. Label every reused input as synthetic.
```

The exercise defines avoided vehicle-km as J*f*d/o and daily net grams as
T*e_transit + access_g - J*f*d*e_road/o. These are stipulated accounting definitions, not a
calibrated local model. Counterfactual vehicle removal must be established for real applications.

### SC-DER-01: Conditional checked answers

```yaml
id: SC-DER-01
claim: Under SC-HYP-01, avoided road NOx is 32 kg/day, added NOx is 20 kg/day, net is -12 kg/day; break-even car-replacement fraction is 0.25. With train factor 30, threshold is 0.35 and net at f=0.40 is -4 kg/day.
kind: derived
evidence_status: stipulated
source:
  reference: reference/sunshine-activities.md
  locator: SC-P2 worked solution and SC-P3 sensitivity and break-even calculations
  historical_check_reported: null
  verified_on: 2026-09-15
  verification_record: Executed exact rational arithmetic and independent kg regrouping; see reference/v4-validation.md for runtime and results.
applicability: Arithmetic checked conditional on synthetic SC-HYP-01; no empirical validation or real project prediction.
input_claim_ids: [SC-HYP-01]
computation_status: checked
usage: SC-P1 supplied classification result, SC-P2 and SC-P3 instructor solutions.
```

`evidence_status: stipulated` deliberately retains the input limitation; the separate
`computation_status: checked` records arithmetic verification. The source date records the actual
calculation check. It does not convert synthetic inputs into measurements. Existing regulatory,
local data, model capability and framework claims above remain subject to their original checks.
