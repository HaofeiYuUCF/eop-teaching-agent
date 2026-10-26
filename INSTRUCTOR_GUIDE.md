# Instructor guide

This guide is for instructors who want to use the prototype to adapt one of their own teaching
activities. It tells you what to prepare, what to ask for, what happens, and what you get back. You
do not need to read the assistant's rule files; the assistant reads them.

## What the prototype does

You bring one activity you already teach: a lecture, a problem set, a lab, or a project. The
assistant interviews you, proposes ways to connect the technical content to an environmental or
societal question, drafts a lesson plan for you to accept, and then, if you ask for it, produces the
assessment items, slides, and teaching notes that carry the plan out. You decide every change. The
assistant records what it suggested, what you decided, and why.

The subject coverage today is air quality: nine topic cards, two planning scenarios from Central
Florida, and the lecture material from three UCF courses. You can work on another topic; the
assistant will tell you where the library runs out and will rely on the material you supply.

## What to prepare

- The activity as you teach it now: slides, handout, problem statement, or assignment text.
- Your learning objectives for it, even if informal.
- Who the students are: course level, prerequisites, class size, the tools they can use.
- The time you have: class minutes, lab time, homework expectations.
- One sentence on what you want this revision to resolve. The assistant will ask for it first.

Supply only material you are allowed to share with the AI service you use.

## How to start

1. Set up Claude Code (see the README for the tool options). Download this repository, extract it,
   keep the folders together, and start Claude Code in the extracted folder.
2. Paste the starter request below and fill in the brackets. Attach or name your files.
3. Answer the interview questions. Expect six to eight questions in two or three rounds. Say when
   something does not matter to you; the assistant will stop asking.

Starter request:

> Use this prototype to help me adapt [course and activity]. My students are [level, prerequisites,
> class size]. I have [class minutes, lab time, homework]. Here are my current materials: [files].
> I want this revision to [one sentence]. Propose connections to environmental or societal questions
> and explain why each would help my students. Show me the plan and a short review summary before
> producing anything else.

Add "Then produce the assessment items, slides, and teaching notes as editable Word and PowerPoint
files" if you want the complete package. Leave it out to stop at the plan.

## What happens

1. **Interview.** The assistant asks about your students, goals, time, and tools.
2. **Proposals.** It proposes two to four connections between your content and an environmental or
   societal question, each with a possible student activity. You choose, adapt, defer, or decline.
3. **Plan.** It writes a lesson plan: objectives, sequence with minutes, assessment items, what to cut
   if time runs short, and the sources it relied on.
4. **Review.** It checks its own plan against a rubric and gives you a one-page summary: what was
   checked, what was changed, what remains open, and what it needs you to decide.
5. **Your acceptance.** Nothing further is produced until you accept the plan.
6. **Package** (if requested). Assessment items with solutions and scoring criteria, student and
   instructor versions of the slides, teaching notes, and a final review. Student files never
   contain answers.

A plan takes about an hour of your time. A complete package adds assistant working time and a final
check by you of the exported files.

## What you get back

Everything is saved in the `outputs` folder, in a subfolder named after your plan.

- `plan.md`: the lesson plan, including the record of suggestions and your decisions.
- `plan-review.md`: the review summary and the detailed check record.
- Student and instructor subfolders with the Word and PowerPoint files, if you requested a package.
- A verification subfolder with every calculation the assistant ran.

Open the exported files yourself before class. The assistant inspects them when it can, and it will
tell you when it could not.

## What the assistant will not do

- It will not change your plan without recording your decision.
- It will not present a number it did not calculate, or a claim it did not source.
- It will not contact anyone, publish anything, or put your material online.
- It will not tell you that students learned something; that is for you to find out in class.

## Contributing material

If you want to add a topic card or a scenario so others can use your material, see
[CONTRIBUTING.md](CONTRIBUTING.md). Contributing is optional and separate from adapting your lesson.
