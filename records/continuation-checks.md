# Workflow Continuation Checks

Date: 2026-09-20. Baseline: `8d876b8`. This update makes the coordinating assistant's next action
explicit after plan acceptance. It changes role instructions, not a programmatic execution engine.

## Manual instruction checks

The following cases were traced through the written policy, plan schema, and role handoffs. These
are consistency checks, not observed agent runs, timing measurements, or classroom evaluations.

| Request or state | Required next action | Instruction check |
|---|---|---|
| Run Intake only; plan accepted | Finish with plan and review status; no assessment or slides. | Plan-only default and stopping point explicit. |
| Complete package requested; reviewed plan accepted | Execute Assessment Designer, Material Builder, then Reviewer. | Each handoff explicitly continues within the same task. |
| Plan accepted before review | Review first; preserve acceptance if unchanged; obtain acceptance for material changes. | Acceptance alone cannot bypass plan review. |
| Full-package assessment completed | Continue to assembly if no unresolved blocker, then final review. | No extra stage-transition approval required. |
| User asks for assessment or review only | Deliver only the requested artifacts or findings. | Standalone requests do not trigger full generation. |
| Missing essential evidence or tool | Pause dependent work; identify the blocker and record completed work/next stage. | No invented completion; unaffected authorized work may continue. |
| Reviewer finds an in-scope defect | Route repair, recheck affected outputs, respect two-round limit. | Final review is not skipped; unresolved blockers retain their status. |
| Resume a partially completed task | Read actual artifacts and progress, check changed dependencies, continue first incomplete stage. | No repeated approval or automatic regeneration of unchanged work. |
| Older plan has no execution fields | Recover scope from the actual request; clarify if genuinely unclear. | Missing fields neither authorize more work nor erase valid acceptance. |
| User pauses or changes scope | Honor the new instruction before continuing. | Prior full-package scope cannot override a later stop. |

## Verification scope

All five role specifications passed the bundled skill format validator. All 4,122 relative Markdown
file links resolve to existing targets; five role names match their folders and the diff passes the
whitespace check with CR-at-EOL handling. Remote URLs and heading anchors were not retested.
These structural checks do not prove reliable
execution of the full teaching workflow. The course library, existing cards, scenarios, and claim
register are outside the change; no teaching package or new scenario is produced by this update.

A retained end-to-end run remains needed to evaluate actual continuation, exported files, and repair
behavior in a particular host. Execution depends on available tools and permissions. A paused task
does not resume itself on a timer; these instructions tell the assistant how to continue when the
task is resumed.
