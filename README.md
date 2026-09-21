# EOP Air Quality Teaching Prototype

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

The prototype was developed and checked using **OpenAI Codex**, including local file access and
document/presentation tools. The role instructions are portable text, but equivalent behavior in
Claude Code, browser chat, or cloud environments has not been established by cross-platform tests.
The repository does not require one specific model or include an API key. Accounts, available tools,
and service charges are managed by your chosen provider.

| Tool | Provide the resources | Practical fit |
|---|---|---|
| Codex with local folder access | Open or attach the extracted repository as a project folder. | Closest to the development setup; preserves access to the complete library. |
| Claude Code | Start a session in the extracted repository folder. | A file-based alternative; explicitly request that it read the role instructions. |
| ChatGPT or Claude browser chat / Projects | Upload relevant instructions and source files. | Focused lookup or drafting; file access and exports depend on the tool. |
| Codex cloud | Configure a cloud environment with access to the repository. | Remote execution; required files and tools must be available there. |

### Codex with a local project

Open or attach the extracted repository folder, start a task, and paste the starter request below.
Ask Codex to confirm it can read `reference/workflow-policy.md`, `skills/eop-intake/SKILL.md`, and
a relevant library entry before proceeding. See the official [local project guidance](https://learn.chatgpt.com/docs/projects).

The `skills/` folder contains role specifications. Opening this repository does not automatically
install or register them as skills; explicitly asking the assistant to read them avoids a separate
installation. Do not move only the five role folders, because they link to shared resources elsewhere
in the repository. Before requesting exports, ask which tools are available to create and render
PowerPoint/Word files and check calculations. This repository does not install those tools.

### Claude Code

After setting up Claude Code, open a terminal in the extracted repository folder and start `claude`.
Paste the same starter request, explicitly asking it to read the named `SKILL.md` files. Do not
assume those files are automatically installed Claude skills. Ask it to confirm source access,
file generation, rendering, and calculation capabilities before beginning a full package.
Follow the official [Claude Code quickstart](https://code.claude.com/docs/en/quickstart) for setup
and sign-in. This is an adaptation path, not a tested EOP installation procedure.

### ChatGPT or Claude in a browser

Create a chat or project and upload the relevant files. A GitHub link alone does not guarantee that
the assistant has read the complete repository. Start with `README.md`, `reference/workflow-policy.md`,
and the selected role's `SKILL.md`; supply the shared references and sources it requests.
Each role file has the same filename, so identify its role and original folder when uploading.

For planning, also provide the plan schema, relevant EOP outcomes and fact-register entries, selected
cards, and any chosen scenario. For course lookup, provide the library guide, relevant index entries,
and the PDF or page images needed to verify the answer. Ask the assistant to identify missing files
before drafting. Upload limits and image-reading capabilities vary; provide a relevant subset and
retain original source IDs and PDF page numbers even when local links no longer work.

Use the starter request with paths replaced by uploaded filenames. Supply downstream role files and
references when proceeding to assessment and material creation. If the tool cannot create or inspect
actual `.pptx` or `.docx` files, request a text draft and treat export or visual review as incomplete.
See the official [ChatGPT project guide](https://learn.chatgpt.com/docs/projects) and
[Claude project guide](https://support.claude.com/en/articles/9517075-what-are-projects).

### Codex cloud and other remote environments

Connect a repository you can access, create its environment, and use the starter request there,
following the official [Codex cloud setup](https://learn.chatgpt.com/docs/cloud). Files on your local
computer are not automatically available remotely. Supply any additional teaching materials through
the environment's supported mechanism and confirm that PDFs, page images, export tools, rendering,
and calculation tools are accessible. Request downloadable outputs or an accessible output location;
do not assume a local desktop folder will receive them.

Cloud describes where work runs; **Claude** is a separate AI product. Repository access alone does
not establish that every workflow check can run. Publishing newly supplied materials remains a
separate instructor decision.

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

Based on the [Engineering for One Planet Framework](https://engineeringforoneplanet.org/eop-framework/).
See [LICENSE.md](LICENSE.md) for the package and [imported-material rights](library/RIGHTS.md) for the
course collection. Preserve credits and original course labels, including documented ENV 5128/6128
differences. The package license does not automatically cover third-party teaching materials. Share
only materials you are authorized to provide to the chosen AI service.
