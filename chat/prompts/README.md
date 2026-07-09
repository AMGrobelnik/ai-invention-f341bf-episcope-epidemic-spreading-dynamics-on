# Prompts

Complete, auto-generated record of **every prompt the AI Inventor system gave each agent** across this run — generated at repository-upload time so it captures all steps. For the full conversation (assistant turns, thinking, tool calls and results) see the sibling `../messages/` folder.

- Run: `run_PJcQ6RjRK3Db` — Neuro Symbolic Logic

Each prompt is labelled by type and timestamped, with its full untruncated body:

- **SYSTEM-USER** — the pipeline-generated role/instruction prompt placed in the user slot.
- **HUMAN-USER** — the task / human-typed message into the agent stream.
- **SKILL-INPUT** — a skill the agent loaded; its `SKILL.md` instructions, verbatim.

Layout mirrors the run's module tree: one folder per high-level phase, a `round_N/` per iteration where the phase iterates, then each module — a single-task module is one `.md` file, a parallel module (gen_plan / gen_art / gen_viz / gen_demo_art) is a folder with one `.md` per task.

## Index

- **1. create_idea** — `hypo_loop`
  - round_1
    - `chat/prompts/1_create_idea/round_1/1_gen_hypo.md` — 1 prompt
    - `chat/prompts/1_create_idea/round_1/2_review_hypo.md` — 1 prompt
  - round_2
    - `chat/prompts/1_create_idea/round_2/1_gen_hypo.md` — 3 prompts
    - `chat/prompts/1_create_idea/round_2/2_review_hypo.md` — 1 prompt
- **2. test_idea** — `invention_loop`
  - round_1
    - `1_gen_plan/` — 2 task(s)
      - `chat/prompts/2_test_idea/round_1/1_gen_plan/gen_plan_dataset_1.md` — 1 prompt
      - `chat/prompts/2_test_idea/round_1/1_gen_plan/gen_plan_experiment_1.md` — 1 prompt
    - `chat/prompts/2_test_idea/round_1/2_gen_paper_text.md` — 3 prompts
- **3. report_results** — `gen_paper_repo`
  - `chat/prompts/3_report_results/1_gen_full_paper.md` — 2 prompts
