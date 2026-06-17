# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 21, 2026
**Duration:** 1h 0m 42s
**Presenters:** Nikita Kumar, Vira Melnyk, Oleksandr Tsyganok

---

## Meeting Title

AI Enablement: Orchestrator Homework Show & Tell — Demos and Troubleshooting

---

## Short Description

This session was a homework show-and-tell focused on the orchestrator topic introduced the previous week. Participants demonstrated their orchestrator implementations in CodeMie, ranging from story refinement and BDD test generation to PR review automation. Vira Melnyk closed the session with a structured walkthrough of orchestration design principles — including structured vs. collaborative patterns — and introduced a live Decision Coordinator orchestrator for validating ideas.

---

## Key Points / Topics

### Homework Demonstrations

**Ashwin Jain — BDD Test Case Generator + PR Review Orchestrators**
- Extended the base story refinement orchestrator by adding a BDD test case generator agent that posts Gherkin scenarios as Jira comments.
- Noted that X-Ray integration was not yet available; results posted directly to Jira in the meantime.
- Built a second orchestrator: a PR review and updater that reviews a pull request, identifies issues, and attempts to apply fixes automatically on a new branch.

**Altaf Shariff — Story Refinement Orchestrator**
- Created the standard story refinement orchestrator with two sub-agents: readiness checker and story risk/hidden gap reviewer.
- Ran it against a real Jira story (CS179); the orchestrator assessed readiness and posted a structured update.

**Alice Merrill — Test Scenario + Readiness Orchestrator (Troubleshoot)**
- Built an orchestrator targeting test scenario generation and story readiness.
- Issue: only one sub-agent's output was posted; the second was silently skipped.
- Root cause identified by Vira: the orchestrator system prompt still referenced old sub-agent names, overriding the updated agent list.
- Key lesson: system prompts must explicitly name sub-agents and describe the full flow; relying on CodeMie's implicit resolution is unreliable with less-capable models.
- Tip shared: export a conversation as JSON and feed it back to a fresh assistant to troubleshoot agent behavior.

**Dhanalakshmi Chinnasamy — Rovo Agents via CodeMie**
- Attempted to run Rovo agents through a CodeMie orchestrator; encountered Confluence permissions issues (needed to grant page-creation access).
- Clarification from Oleksandr: Rovo agents can call CodeMie agents (agent-to-agent protocol supported), but the reverse — CodeMie calling Rovo agents directly — is currently limited; Jira Automation can serve as a bridge.

**Bandana Sriramka — Story Refinement Orchestrator**
- Ran the standard story refinement orchestrator against an internal story; confirmed it worked, with plans to further refine and customize for team needs.

**Jatin Bagga — Orchestrator Attempt with Issues**
- Showed an attempt to build an orchestrator combining Jira story creation, a backlog planning agent, and a team member persona sub-agent.
- Issue: the system prompt described individual tool behaviors but contained no orchestration logic — the assistant did not know it was an orchestrator.
- Root cause (Vira and Oleksandr): selecting sub-agents in the UI adds them to the roster, but the system prompt must explicitly describe roles, flow order, and how results should be collected and acted upon.
- Analogy offered: "hiring a team without giving the manager a brief" — the manager only knows addresses, not what to do.

### Orchestration Theory (Vira Melnyk)

- **Orchestration prompt structure:** must include (1) role and task, (2) flow/sequence, (3) decision logic for collecting results, (4) output instructions.
- **Structured orchestration:** orchestrator coordinates all agents; sub-agents are independent and unaware of each other. Easier to set up and scale.
- **Collaborative orchestration:** sub-agents are also aware of the orchestration context and of each other, enabling richer collaboration. Demonstrated in the story refinement example (where sub-agents were updated to know they were part of an orchestration).
- **Best practice:** keep orchestrators lean — avoid adding data sources and tools directly to the orchestrator; delegate those to sub-agents.
- **Decision Coordinator agent:** a live example orchestrator that validates orchestration ideas by running them through an evaluator, a critic, and an FAQ agent before returning a go/no-go recommendation. Available in the training project for participants to experiment with.

### Session Notes
- No homework assigned for this session.
- Next Thursday: new topic introduced.
- Friday open hours available for troubleshooting.
