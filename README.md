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
repository is set up for **Claude Code** first: a `CLAUDE.md` file tells it how the roles, folders,
and tools fit together, and the five roles are registered as Claude Code skills. The prototype was
originally developed and checked with OpenAI Codex, which still works as described below. The
repository does not require one specific model or include an API key; accounts, available tools, and
service charges are managed by your chosen provider.

| Tool | Provide the resources | Practical fit |
|---|---|---|
| Claude Code (recommended) | Clone or extract the repository and start `claude` in its folder. | Reads the whole library, runs calculations, writes Word and PowerPoint files, and keeps outputs in `outputs/`. |
| Claude.ai Projects | Upload the instruction files and the sources for your topic. | Planning and drafting without a terminal; no file generation or whole-library search. |
| OpenAI Codex (local or cloud) | Open the folder as a project, or connect the repository to a cloud environment. | The original development setup; ask it to read the role files explicitly. |
| ChatGPT in a browser | Upload the relevant instructions and sources. | Focused lookup or drafting; exports depend on the tool. |

### Claude Code

1. Install Claude Code and sign in ([quickstart](https://code.claude.com/docs/en/quickstart)).
2. Clone the repository (`git clone https://github.com/HaofeiYuUCF/eop-teaching-agent`) or download
   and extract the ZIP, keeping the subfolders together.
3. Open a terminal in the repository folder and start `claude`. It reads `CLAUDE.md` automatically,
   which points it to `reference/workflow-policy.md` and the role specifications. The roles also
   appear as skills (`/eop-intake`, `/eop-reviewer`, `/eop-assessment-designer`,
   `/eop-material-builder`, `/eop-card-builder`), each a short wrapper around the full
   specification in `skills/`.
4. Paste a starter request from the next section. Claude Code will ask permission before running
   Python or writing files; it writes plans, review reports, and exports under `outputs/<plan_id>/`.

Word and PowerPoint files are produced with Claude Code's document skills when they are available,
otherwise with `python-docx` and `python-pptx`. Visual inspection of exports needs a renderer such as
LibreOffice; without one, the assistant records visual review as unverified, as the shared policy
requires. A plan-only run in Claude Code was checked on 2026-10-25 (see `outputs/README.md` for
where results land); a complete teaching package with exports has not yet been checked on Claude Code.

### Claude.ai Projects

Create a project and add these files as project knowledge: `README.md`, `reference/workflow-policy.md`,
`reference/blueprint-schema.md`, `reference/review-rubric.md`, `reference/fact-register.md`,
`reference/eop-outcomes.md`, the `SKILL.md` of each role you will use (rename each on upload, since
all five share the file name), the cards and scenario for your topic, and the Markdown page
references under `library/text/` for the lectures you want it to draw on. The page images and
original PDFs are too large to upload in full; add the few pages you need as images. Paste the
starter request with paths replaced by the uploaded file names. Claude Projects can draft plans,
assessments, and slide text but cannot write `.pptx` or `.docx` files; request text drafts and treat
export and visual review as incomplete. See the [Claude project guide](https://support.claude.com/en/articles/9517075-what-are-projects).

### OpenAI Codex

Open or attach the extracted repository folder, start a task, and paste the starter request. Ask
Codex to confirm it can read `reference/workflow-policy.md`, `skills/eop-intake/SKILL.md`, and a
relevant library entry before proceeding ([local project guidance](https://learn.chatgpt.com/docs/projects),
[cloud setup](https://learn.chatgpt.com/docs/cloud)). The `skills/` folder is not installed
automatically in Codex; asking it to read the role files is enough. In a cloud environment, files on
your computer are not available; supply additional materials through the environment and request
downloadable outputs. Before requesting exports, ask which tools are available to create and render
PowerPoint and Word files and to check calculations.

### ChatGPT in a browser

Create a chat or project and upload the same file set listed for Claude.ai Projects. A GitHub link
alone does not guarantee the assistant has read the repository. Ask it to identify missing files
before drafting, and keep source IDs and PDF page numbers in the request even when local links no
longer work. If it cannot create or inspect actual `.pptx` or `.docx` files, request a text draft and
treat export or visual review as incomplete.

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

One assistant can execute all five roles sequentially. Reviewer is one role used at multiple stages.
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

- [Course library](library/index.md): 38 PDFs and 1,050 pages from ENV 4120, ENV 5128, and ENV 6106.
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

The [course-library checks](reference/v5-validation.md), [scenario checks](reference/v4-validation.md),
[development records](reference/development-check-records.md), [faculty workflow checks](reference/faculty-workflow-checks.md),
and [continuation checks](reference/continuation-checks.md) describe their actual scope and limits.
These are retained evidence records, not new tests of every current instruction or platform.
Consult the [fact register](reference/fact-register.md) for claim status. Resource revisions and
source identifiers remain necessary for attribution, review, and resuming work.

## Attribution and license

See [LICENSE.md](LICENSE.md) for the package and [imported-material rights](library/RIGHTS.md) for the
course collection. Preserve credits and original course labels, including documented ENV 5128/6128
differences. The package license does not automatically cover third-party teaching materials. Share
only materials you are authorized to provide to the chosen AI service.
