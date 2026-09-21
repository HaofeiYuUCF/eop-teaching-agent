# Version 5 validation report

## Scope and status

Version 5 imports the supplied courses as traceable reference resources. This report distinguishes
file integrity and source retrieval from scientific verification and educational evaluation.
See the readable [development check records](development-check-records.md). The technical checks below describe the original v5 build; optional scripts were later removed for simpler browsing.

| Course folder | Documents | PDF pages | User-reported audience |
|---|---:|---:|---|
| 4120 | 10 | 280 | Undergraduate |
| 5128 | 11 | 415 | Graduate |
| 6106 | 17 | 355 | Graduate |
| Total | 38 | 1,050 | |

Each PDF has an unchanged copy, a SHA-256 record, one Markdown reference, and one image per page.
All 1,050 pages have sections in the Markdown references, including pages with no extracted text.
The [source records](../library/source-records.md) preserve the actual UTC build time and the baseline v4 archive checksum.

## Extraction and visual inspection

Text was extracted with pypdf. Page images were rendered with pypdfium2 at 1.5 pixels per PDF point
and saved as JPEGs at quality 90. Original PDFs remain available for higher-resolution viewing.

The automated scan found **245 sparse-text pages**, including **10 with no extracted text**.
It found no replacement-character or `(cid:...)` flags under the configured checks. This is a
limited diagnostic, not proof of complete text extraction. Sparse covers, dividers, charts, maps,
photos and scanned tables account for the flagged pages; their visible content was not discarded.

The implementing assistant visually inspected all 245 flagged pages in 13 contact sheets to classify
their content and check that a visual fallback was present. This was thumbnail-level review, not
line-by-line transcription. Ten image-only pages received separate, generated visual-navigation
descriptions. Table identifiers on image-only filter pages were corrected after full-page inspection.

Full-page visual checks also covered these representative pages:

- ENV4120-10-gaussiandispersionmodel, PDF pp. 14, 19 and 23: equation, assumptions, worked example.
- ENV4120-06-atmospheric-pm, PDF p. 21: source-composition table and attribution.
- ENV5128-07-ambient-gas-measurement, PDF pp. 19 and 21: cross-sensitivity and calibration figures.
- ENV5128-05-aerosolmeasurement-2, PDF pp. 23-26 and 32: scanned filter tables and TEOM equation.
- ENV5128-env-6128-iot-in-air-quality-monitoring-10222024, PDF p. 19: wiring diagram and table.
- ENV6106-10-cal3qhc, PDF pp. 6 and 19: parameter table and receptor-placement text.
- ENV6106-11-project-level-demo, PDF p. 3: source geometry schematic.
- ENV6106-04-plume-rise-downwash, PDF p. 14: model equations and variable definitions.

Known limits remain visible: embedded equations and table contents are not reliably represented by
extracted text alone. Small source labels may require zooming the original PDF. The source geometry
schematic reaches the top page boundary; it was retained as supplied, not reconstructed. No OCR or
manual transcription of all visual content was claimed. Source typos and dated statements remain.

## Source-use checks

These are executed literal-retrieval checks plus source-inspection walkthroughs by the implementing
assistant, not independent agent trials or a cross-model behavioral benchmark.

| Request | Located evidence | Interpretation boundary |
|---|---|---|
| Find Gaussian-model assumptions | ENV4120-10-gaussiandispersionmodel, PDF p. 19; graduate counterpart ENV6106-03-gaussian-model, PDF p. 19 | Distinct course contexts retained; source statements are not newly validated science. |
| Find a Gaussian worked example | ENV4120-10-gaussiandispersionmodel, PDF p. 23 | Existing stack example; not an observed roadway impact or a newly executed model. |
| Find sensor cross-sensitivity | ENV5128-07-ambient-gas-measurement, PDF pp. 19-20 | Refer to original curves and attribution; do not infer universal sensor performance. |
| Find calibration discussion | Same source, PDF p. 21 | Source compares performance at several locations; no new calibration study was performed. |
| Find roadway receptor placement | ENV6106-10-cal3qhc, PDF p. 19 | Course guidance located; present-day regulatory applicability not checked. |
| Provide measured 2026 Sunshine Corridor emissions from these courses | No literal match for the test query; no such dataset identified in the inspected sources | Report that the requested measured dataset is not established by this library. The separate v4 synthetic activity is not a measured result. |

The original no-match helper produced no answer or citation. The shared guide instructs the assistant to
report the specific gap and examine visual/source context as needed. This demonstrates the local
lookup behavior and a bounded walkthrough, not a guarantee that any future model will follow it.

## Skill and file checks

All five role SKILL.md files passed the bundled skill-creator quick validator using a task-local
PyYAML 6.0.3 dependency. This validation dependency is not included in or required by the delivered
framework. See [recorded skill results](development-check-records.md). All 1,050 JPEG files passed image decoding
verification. The search helper also ran through its command-line entry point and returned the
expected no-match status without a generated answer.

## Preservation and metadata

Checks compare every copied PDF with its source checksum and inspect coverage and relative links.
Archive release checking also reopens the ZIP, checks CRCs, compares member bytes, and validates
the package after extraction into a separate location. The [development check records](development-check-records.md) retain the original archive hash and results. They describe the earlier ZIP, not a new archive of this simplified repository.

The original v4 license and fact register are preserved byte-for-byte. Existing claim IDs, card IDs
and author-acceptance fields were not changed. Related course links were appended to eight cards.

Eight source covers in folder 5128 display ENV 6128. Both labels are retained. The IoT cover includes
a contributor contact; original attribution is preserved. PDF metadata is recorded separately from
authorship claims. Importing these resources grants no new rights over third-party assets.

## What this delivery does not establish

Scientific and regulatory claims have **not been independently verified** by this import. Current
software instructions, policy and standards require checking before consequential teaching use.
Instructor endorsement of derived content, faculty co-design participation, classroom effectiveness,
student learning, workload reduction and cross-model reliability have not been evaluated.

This is a reference-library integration, not a released classroom teaching package. No course was
redesigned and no new lesson, worked solution, model run or proposal narrative was generated.
