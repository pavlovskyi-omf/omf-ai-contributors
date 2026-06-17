# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 16, 2026
**Duration:** 1h 15m 40s
**Presenters:** Vira Melnyk, Nikita Kumar

---

## Meeting Title

AI Enablement: Hands-On — Building Multi-Agent Orchestration in CodeMie

---

## Short Description

Session four introduced multi-agent orchestration in CodeMie. Vira Melnyk led a hands-on workshop where participants cloned three pre-built assistants — a Story Readiness Checker, a Story Risk and Hidden Gaps Reviewer, and an Orchestrator — then configured the orchestrator to coordinate the two sub-assistants. The orchestrated flow analyzed a Jira story end-to-end and posted a combined summary comment. The session closed with guidance on designing your own orchestration, including an AI-assisted prompt design process, as homework for the next show-and-tell.

---

## Key Points / Topics

### Session Setup
- Pre-requisite: active CodeMie Jira integration (participants with expired tokens from last week needed to regenerate — default token validity is 7 days).
- Three assistants pre-built by Vira Melnyk and shared with the training project were used as the starting point.
- Recommended practice: clone assistants with a personal name prefix and **do not share with the project** during training to avoid flooding the shared assistant list.

### Orchestration Concepts
- An **orchestrator** is an assistant that coordinates other assistants (sub-assistants) in a defined sequence.
- Sub-assistants are specialized agents; each handles one step of the flow.
- The orchestrator controls execution order, passes context between steps, and decides when to involve the user.
- A single sub-assistant controlled by an orchestrator is technically valid but not meaningful orchestration; two or more sub-assistants is the practical minimum.

### Hands-On Workflow: Story Refinement Orchestrator

**Step 1 — Clone Sub-Assistants**
- Clone **Story Readiness Checker** — validates story quality (same agent as previous sessions, adapted for orchestration).
- Clone **Story Risk and Hidden Gaps Reviewer** — analyzes the story for hidden risks, missing details, and ambiguous requirements.
- Add a personal name prefix to each clone; keep them private (unshared).

**Step 2 — Clone and Configure the Orchestrator**
- Clone the **Story Refinement Orchestrator** assistant.
- Navigate to **Context and Data Sources** tab inside the cloned orchestrator.
- Select both cloned sub-assistants from the sub-assistant dropdown.
- Navigate to **Available Tools → Project Management** and verify the **Generic Jira** tool is enabled with the correct integration.
- Save the configuration.

**Step 3 — Run the Orchestration**
- Start a chat with the orchestrator and paste a Jira story link.
- The orchestrator automatically calls the Story Readiness Checker first, then the Story Risk and Hidden Gaps Reviewer.
- Tool call traces are visible in the UI for each step — useful for debugging.
- After both sub-agents complete, the orchestrator proposes posting the combined summary as a Jira comment; confirm to proceed.

### Key Technical Notes
- **Jira token expiry**: the 7-day default expiration was the most common cause of failures; always set a longer validity when creating tokens.
- **Sub-assistant visibility**: the orchestrator itself does not appear in its own sub-assistant dropdown (by design).
- **Too many shared assistants**: use personal name prefixes and keep training assistants private to keep the project list manageable.
- **Automatic Jira story selection**: currently requires pasting a link manually; can be configured to run on specific project keys or sprint status via JQL in the sub-assistant prompt.
- **CodeMie UI bug**: selected integrations intermittently disappear from the workflow editor after saving (flagged for investigation).

### Designing Your Own Orchestration (Homework Guidance)
Recommended AI-assisted design process — all steps in a single CodeMie chat:
1. **Define the business problem** you want to solve with orchestration.
2. **Ask CodeMie** to suggest an orchestration approach for that problem.
3. **Rate the value** of the proposed orchestration (ask the model to score it 1–10); proceed only if the score is ≥ 7–8.
4. **Define the roles**: ask CodeMie to identify the sub-assistants needed and their responsibilities.
5. **Build sub-assistants first**, then join them in the orchestrator.
6. **Test and simplify**: iterate on each agent independently before testing the full flow.

### Homework
- Design and build your own orchestration using the above process.
- Start with a simple brainstorming or planning orchestration that requires no Jira/GitHub integration if needed — any multi-agent flow counts.
- Be prepared to demo at the next Tuesday show-and-tell.
- Friday open hours available for troubleshooting and one-on-one help.
