# EOP Air Quality Teaching Prototype

Based on the [Engineering for One Planet Framework](https://engineeringforoneplanet.org/eop-framework/).

Use existing course content to develop teaching materials that make relevant environmental and
societal connections explicit. Instructors choose the goals and resources; an AI assistant follows
five role instructions to prepare and review the work.

This repository contains readable instructions, topic cards, scenarios, and a course reference
library. Use it through an AI tool that can read the files. It is not a standalone application or
hosted service. You do not need to write code to contribute teaching knowledge or request materials;
the assistant may use code and document tools to generate files and check calculations.

## Start here

Instructors: the [instructor guide](INSTRUCTOR_GUIDE.md) is the short version of everything below.

1. On GitHub, choose **Code → Download ZIP** and extract the complete folder. Keep the subfolders
   together so that links and shared references remain accessible.
2. Choose an AI tool below and give it access to the folder or relevant files.
3. Copy a starter request below and add your course, topic, student preparation, and available time.
   You may supply your own teaching materials, but contribution is optional.
4. For a complete teaching package, review and accept the internally reviewed plan before the
   assistant proceeds to assessments, slides, teaching notes, and final review.

To browse without AI, start with the [course index](library/index.md) or [topic index](library/topics.md)
and follow the lecture and page links. See [Contribute and use teaching resources](CONTRIBUTING.md)
for examples of resource lookup, card/scenario contributions, and lesson adaptation.

## Choose your AI tool

The role instructions are plain text and work with any AI tool that can read the files. The
repository is set up for **Claude Code** first: a file named `CLAUDE.md` tells it how the roles,
folders, and tools fit together, and the five roles appear in its skill list. The prototype was
first developed and checked with OpenAI Codex, which still works as described below. No specific
model or API key is required. Accounts, available tools, and charges are handled by your provider.

| Tool | What you provide | What it can do |
|---|---|---|
| Claude Code (recommended) | Open the extracted repository folder in Claude Code. | Read the whole library, run calculations, write Word and PowerPoint files, keep outputs in one folder. |
| Claude.ai Projects | Upload the instruction files and the sources for your topic. | Plan and draft without a terminal. It cannot write Word or PowerPoint files or search the whole library. |
| OpenAI Codex (local or cloud) | Open the folder as a project, or connect the repository to a cloud environment. | The original development setup. Ask it to read the role files. |
| ChatGPT in a browser | Upload the relevant instructions and sources. | Focused lookup or drafting. Exports depend on the tool. |

### Claude Code

1. Install Claude Code and sign in, following the [quickstart](https://code.claude.com/docs/en/quickstart).
2. Download the repository as a ZIP file (on GitHub, **Code → Download ZIP**) and extract it, keeping
   the subfolders together. If you use Git, you can clone the repository instead.
3. Start Claude Code in the extracted folder. It reads `CLAUDE.md` on its own, which directs it to the
   shared policy and the role specifications. If you start it in a different folder, ask it to read
   `CLAUDE.md` in the repository folder first. The roles are also available as skills named
   `eop-intake`, `eop-reviewer`, `eop-assessment-designer`, `eop-material-builder`, and
   `eop-card-builder`; each is a short pointer to the full specification in the `skills` folder.
4. Paste a starter request from the next section. Claude Code asks for permission before it runs a
   calculation or writes a file. It saves plans, review reports, and exports in the `outputs` folder,
   one subfolder per plan.

Word and PowerPoint files are produced with Claude Code's document skills when they are available,
otherwise with a Python library, and the assistant says which. Checking how an exported file looks
requires a program that can render it; without one, the assistant records the visual review as
unverified, as the shared policy requires. A plan-only run in Claude Code was checked on
2026-10-25. A complete teaching package with exports has not yet been checked on Claude Code.

### Claude.ai Projects

Create a project and add these files as project knowledge: `README.md`;
`reference/workflow-policy.md`, `reference/blueprint-schema.md`, `reference/review-rubric.md`,
`reference/fact-register.md`, and `reference/eop-outcomes.md`; the `SKILL.md` file of each role you
will use (rename each when uploading, because all five share the same file name); the cards and the
scenario for your topic; and the Markdown page references under `library/text` for the lectures you
want it to draw on. The page images and original PDFs are too large to upload in full; add the few
pages you need as images. Paste the starter request with the file paths replaced by the uploaded file
names. Claude Projects can draft plans, assessments, and slide text but cannot write Word or
PowerPoint files; ask for text drafts and treat export and visual review as incomplete. See the
[Claude project guide](https://support.claude.com/en/articles/9517075-what-are-projects).

### OpenAI Codex

Open or attach the extracted repository folder, start a task, and paste the starter request. Ask
Codex to confirm it can read `reference/workflow-policy.md`, `skills/eop-intake/SKILL.md`, and one
library entry before it proceeds ([local project guidance](https://learn.chatgpt.com/docs/projects),
[cloud setup](https://learn.chatgpt.com/docs/cloud)). Codex does not register the `skills` folder on
its own; asking it to read the role files is enough. In a cloud environment, files on your computer
are not available; supply additional materials through the environment and ask for downloadable
outputs. Before requesting exports, ask which tools it has to create and render PowerPoint and Word
files and to check calculations.

### ChatGPT in a browser

Create a chat or project and upload the same set of files listed for Claude.ai Projects. A GitHub
link alone does not guarantee that the assistant has read the repository. Ask it to name any missing
files before drafting, and keep source identifiers and PDF page numbers in your request even when the
local links no longer work. If it cannot create or inspect actual Word or PowerPoint files, ask for a
text draft and treat export and visual review as incomplete.

## Copy a starter request

Replace the bracketed details with your teaching context:

> Use this EOP prototype to develop a complete teaching package for [course and topic]. First read
> README.md, reference/workflow-policy.md, and skills/eop-intake/SKILL.md, then follow their linked
> references as needed. Confirm which files and output tools you can access and identify missing
> dependencies. My students have [prior preparation], and I have [time and tools]. Use [my supplied
> materials / relevant repository resources]. Propose useful environmental or societal connections
> and explain their teaching value. I may choose an existing scenario, supply another context, or
> use none. Prepare and internally review the plan, then show me the plan and a concise review
> summary for acceptance. After acceptance and resolution of blocking issues, continue through
> Assessment Designer, Material Builder, and Reviewer. Produce editable PowerPoint slides, teaching
> notes, and Word assessment materials. Preserve source IDs and page references, separate student
> materials from solutions, and report incomplete checks.

For a smaller task:

- **Reference only:** "Read reference/library-guide.md. Find course material on sensor calibration
  and cross-sensitivity, with source IDs and PDF page numbers. Do not generate a lesson."
- **Contribute a resource:** "Read CONTRIBUTING.md and skills/eop-card-builder/SKILL.md. Help me turn
  these teaching notes into a draft card, preserving sources and identifying gaps for my review."
- **Plan only:** "Read reference/workflow-policy.md and skills/eop-intake/SKILL.md. Prepare and
  review a lesson plan for [topic]. Stop with the plan and review summary; do not generate materials."

Accepting a plan-only request does not start material generation. For a complete package, you do
not need to invoke each role separately. You can stop or change scope. If interrupted, ask the
assistant to resume from the saved plan, outputs, and review status.

## Five roles

| Role | Specification | Responsibility |
|---|---|---|
| Card Builder | [eop-card-builder](skills/eop-card-builder/SKILL.md) | Organize sources and teaching experience into draft cards and scenarios. |
| Intake Agent | [eop-intake](skills/eop-intake/SKILL.md) | Clarify needs, propose environmental or societal connections, and develop the plan with instructor choice. |
| Assessment Designer | [eop-assessment-designer](skills/eop-assessment-designer/SKILL.md) | Create tasks, solutions, scoring criteria, and calculation checks aligned with the accepted plan. |
| Material Builder | [eop-material-builder](skills/eop-material-builder/SKILL.md) | Produce slides and teaching notes using the plan and shared assessment content. |
| Reviewer | [eop-reviewer](skills/eop-reviewer/SKILL.md) | Review plans before acceptance and materials after assembly; route repairs, recheck, and summarize findings. |

One assistant coordinates the work and talks with the instructor. In Claude Code, the Reviewer, Assessment Designer, and Material Builder roles run as separate assistants with a fresh context, so that review is independent and long generation steps start clean; where that is not possible, one assistant runs all five roles in sequence. Reviewer is one role used at multiple stages.
The normal plan sequence is **Intake draft → internal review and revision → instructor acceptance**.
Important subsequent instructional changes may require renewed acceptance; routine repairs do not.
After at most two revision rounds, unresolved blockers are reported under the shared policy.

The plan records **technical content → environmental or societal question → student activity →
learning objective**. Materials explain the selected connections, and assessments address them when
they are assessed objectives. Reviewer checks explanations and activities, not just EOP labels.
Connections can be deferred when evidence, scope, or time is insufficient; a lesson may provide
technical preparation for later EOP learning. Neither a fixed number of connections nor a scenario
is required.

## Resources and outputs

- [Course library](library/index.md): 38 lectures and 1,050 pages from ENV 4120, ENV 6128 (formerly 5128), and ENV 6106, as page text and page images.
- [Topic index](library/topics.md), [card source map](reference/course-card-map.md), and
  [library guide](reference/library-guide.md): find and cite relevant pages, including visual content.
- [Scenario catalog](scenario/catalog.md): hypothetical I-4/SR 408 and Sunshine Corridor. Either case,
  another supplied context, or no scenario can be used. Sunshine uses a dated planning report and
  separate hypothetical calculation inputs; its exercises do not predict actual corridor outcomes.
- [Card template](reference/card-template.md), [scenario template](reference/scenario-template.md),
  and [optional faculty use record](reference/faculty-use-record.md): contribute resources and experience.
- [Plan schema](reference/blueprint-schema.md) and [review rubric](reference/review-rubric.md): organize
  instructional choices and inspect the resulting work.

Outputs can include student slides, instructor slides and notes, student problems, instructor
solutions and rubrics, the plan, review report, and alignment memo. Modeling lessons may also need
datasets, starter code, or setup instructions. Requested files depend on the host's capabilities;
a text outline is not an exported and visually checked presentation.

## Evidence and limitations

This is a prototype with scoped checks, not evidence of classroom effectiveness or general agent
reliability. Source ingestion does not verify every claim, and instructor acceptance does not replace
evidence checks. The alignment memo describes intended coverage and assessment opportunities, not
demonstrated learning, accreditation, or EOP endorsement.

The [course-library checks](records/v5-validation.md), [scenario checks](records/v4-validation.md),
[development records](records/development-check-records.md), [faculty workflow checks](records/faculty-workflow-checks.md),
and [continuation checks](records/continuation-checks.md) describe their actual scope and limits.
These are retained evidence records, not new tests of every current instruction or platform.
Consult the [fact register](reference/fact-register.md) for claim status. Resource revisions and
source identifiers remain necessary for attribution, review, and resuming work.

## Attribution and license

See [LICENSE.md](LICENSE.md) for the package and [imported-material rights](library/RIGHTS.md) for the
course collection. Preserve credits and original course labels, including documented ENV 5128/6128
differences. The package license does not automatically cover third-party teaching materials. Share
only materials you are authorized to provide to the chosen AI service.
