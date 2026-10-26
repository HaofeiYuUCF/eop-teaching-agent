# Version 4 validation record

Date: 2026-09-15. Scope: the portable framework, added Sunshine evidence summary and illustrative
activities. This is not a release review of a generated lecture or evidence of classroom effectiveness.

## Executed checks

- **Skill metadata:** all five SKILL.md files passed the bundled skill-creator `quick_validate.py`
  validator. Python 3.12.14 with PyYAML 6.0.3 was used for validation; PyYAML is not a runtime
  dependency of this teaching package.
- **Structure:** all 16 card/scenario/skill frontmatter blocks parsed as YAML. All 36 distinct
  frontmatter claim IDs resolve to the fact register. Internal Markdown file links were checked
  for existing targets, including the new revision notes and this validation record.
- **Preservation:** LICENSE.md is byte-identical to the original archive. The I-4 scenario is
  content-identical after normalizing inherited excess blank lines/carriage returns. Original
  archive SHA256 matches the value in revision notes.
- **Source checks:** read the April 2024 report's relevant sections and visually inspected PDF
  pages 11, 12, 14, 93, 94 and 95, including the complete Table 13 continuation and Table 14 notes.
  Verified source attribution/qualifications for SC-01 through SC-06, not their current-world truth.
  Read the STAR page on 2026-09-15 and checked STAR-01 as an attributed advocacy statement.
- **Arithmetic:** during development, executed a numerical verification helper using Python 3.12.14. Exact rational
  calculations, independent kg regrouping, zero shift, altered train factor, zero avoided-emissions
  coefficient, infeasible threshold and invalid fraction checks passed.
  The helper was subsequently removed at the lecturer's request; the worked calculations and
  historical check results remain in the activity guide and this record.
- **Archive:** reopened the final ZIP, checked its CRCs and compared every member byte-for-byte
  with the delivered folder. Only package files are included; temporary validation dependencies,
  source-page images and local helper scripts are excluded.

### Numerical results

SC-HYP-01 is the input record; SC-DER-01 is the conditional result record. Base avoided travel:
64,000 vehicle-km/day. Road emissions avoided: 32 kg NOx/day. Added emissions: 20 kg/day. Net:
**-12 kg/day**. Units check: vehicle-km/day x g/vehicle-km = g/day, divided by 1,000 for kg/day;
train-km/day x g/train-km has the same output basis. Occupancy removes whole vehicle trips only
under the explicit full-party displacement premise.

For f = 0, 0.20, 0.25, 0.40, 0.80, net results are +20, +4, 0, -12, -44 kg/day. Break-even is
0.25. Raising the synthetic train factor to 30 g/train-km gives break-even 0.35 and -4 kg/day at
f=0.40. Independently, each removed trip accounts for 10 g NOx; 3,200 trips avoid 32 kg, compared
with 16 kg train plus 4 kg access. No local measurements, STOPS/MOVES or dispersion runs were used.

## Case-selection walkthroughs

Method: manually apply the updated intake/catalog instructions to the concrete requests below,
then trace the resulting choice into the plan, assessment and review rules. These are reasoning
walkthroughs by the editing assistant, not independent agent executions or automated LLM tests.

| Request and relevant facts | Walkthrough result | Acceptance criterion checked |
|---|---|---|
| A 50-minute intersection emissions lecture; students know activity x factor, calculator available; hypothetical inputs allowed | Recommend I-4, explain road-operations fit; use a supported calculation, no unsolicited rail extension | Objectives and data requirements control selection |
| A 60-minute lecture on mode shift and emissions; students know ratios, calculator available; synthetic example acceptable | Recommend Sunshine; SC-P2 with its demonstration and boundary discussion is feasible; record April 2024 context | Transit case selected with supported prerequisite/time needs |
| A mixed planning/engineering class on transit evidence; no common algebra prerequisite, 40 minutes | Recommend Sunshine SC-P1; explain forecast/assumption terms; do not automatically assign SC-P3 because some students are engineers | Capability is not inferred from major; scaffold matches assessed work |
| Lecturer explicitly selects Sunshine for interpreting monitoring needs despite a roadway-oriented lecture | Retain Sunshine and identify missing spatial/local data; use a bounded evidence-design task if consistent with the stated objective, or ask about an essential gap | Explicit choice wins; no imported I-4 geometry or silent objective change |
| Lecturer explicitly selects I-4 for a general emissions comparison using synthetic factors | Keep I-4 and its hypothetical status | Override works in both directions |
| A sensor calibration lecture requiring a bench calibration exercise, with no project preference | Neither project materially supports the objective; propose no case and retain the sensor lesson | No forced transportation case |
| Both cases suit a broad emissions comparison equally; no other context | Ask one preference question; if unanswered, identify the catalog's provisional continuity default in the plan, without fabricating acceptance | Tie handling is bounded and reviewable |
| An accepted v3 plan names I-4 and lacks scenario_selection metadata | Preserve selection; do not require a metadata-only interview or reapproval | Backward compatibility |
| Lecturer changes an accepted I-4 lesson to Sunshine | Revise affected inputs, geometry, items/solutions, exports and review records; obtain normal acceptance for changed lesson decisions | Case change is substantive, not a project-name replacement |
| Lecturer requires measured local avoided-car trips and real emissions estimates | Neither case supplies those inputs; identify the evidence gap before dependent generation rather than calling synthetic inputs measured | Evidence requirements outrank ease of generation |

## Misuse and consistency review

- SC-P1 classifies the 2026 boardings value as a dated forecast, not observed service or car removal.
  SC-P2's J is explicitly separate, new-to-transit, transfer-linked passenger journeys.
- The hypothetical train factor makes no claim about actual propulsion. Access emissions and the
  displacement premise are visible in the student prompt, not hidden in instructor notes.
- The STAR page is separately attributed and optional. Its embedded campaign requests do not
  become agent actions or grading criteria. TCAR's recommendation is attributed, not prescribed.
- Cost notes distinguish full-route and station-only figures and overlapping O&M coverage.
- Net emissions are not relabeled as concentrations, exposure or health outcomes. Rubrics accept
  alternative defensible conclusions and give credit for stated limits.
- The I-4 demonstration geometry is conditional in the dispersion card; Sunshine has an explicit
  geometry/data gap for real dispersion work.
- SC-P1's supplied numeric result could reveal SC-P2's answer. The resource and lecture-builder
  instructions require replacing that number with qualitative wording when SC-P2 is an unseen
  assessment. Complete instructor resources/verification scripts are excluded from student exports.

## Remaining limits

All required checks for this framework update are complete. No classroom decks or Word exports
were generated, so export rendering, student-file inspection and actual lesson alignment review
are not applicable to this delivery. Those checks remain required for a later teaching package.
New content has no claimed instructor endorsement. Existing unresolved regulatory, scientific,
local-data and EOP-catalog claims retain their original limitations. Current Sunshine project
status was not researched; this case deliberately uses the April 2024 study. Behavioral reliability
across models and student learning outcomes have not been empirically tested.
