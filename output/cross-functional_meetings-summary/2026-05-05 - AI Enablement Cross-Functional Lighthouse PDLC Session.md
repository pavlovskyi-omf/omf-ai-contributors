# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** May 5, 2026
**Duration:** 1h 3m 30s
**Presenter:** Eugene Semenyuk

---

## Meeting Title

AI Enablement: Moving to Event-Driven PDLC Automation with Webhooks and AI Agents

---

## Short Description

The session introduced the concept of shifting from manually triggered AI assistance to event-driven automation across the PDLC. Eugene Semenyuk presented how Jira automations and webhooks can automatically invoke Rovo and CodeMie agents when PDLC events occur (e.g., ticket status changes, pull request creation), reducing coordination overhead. A live demo showed a working Jira automation that triggers a Rovo testability agent when a ticket moves from "To Do" to "In Progress," posting an analysis as a comment. The follow-up hands-on session is planned for Thursday.

---

## Key Points / Topics

### Problem Statement
- Most current AI usage is manually triggered — team members must remember to run agents, copy context, and pass results between tools.
- This creates friction at handoffs between Digital, Engineering, and QA tracks.
- Goal: reduce repetitive coordination, not remove human judgment.

### Event-Driven Automation Concepts
- **Semi-autonomous**: a human manually starts the agent.
- **Autonomous**: an event starts the agent; humans supervise and review the output.
- The human role shifts from *initiating every action* to *reviewing and approving results*.

### Four Ingredients for Autonomy
1. **Events** — status changes, PR creation, branch pushes, etc.
2. **Rules** — Jira Automations, GitHub Actions.
3. **Agents** — Rovo agents, CodeMie agents.
4. **Integrations / Webhooks** — connecting events to agents across platforms.

### Key Automation Scenarios Discussed
- **Jira + Rovo agents**: ticket moves to a status → Rovo agent checks requirements readiness (testability, PRD quality, technical feasibility) → result posted as a comment.
- **GitHub + CodeMie agent**: pull request opens → CodeMie agent reviews code, assesses product impact, recommends test cases → cross-functional PR review output.
- **Release event**: release created → agent produces a readiness summary with changes, tasks, and risks.

### Live Demo: Jira Automation → Rovo Agent
- Created a Jira automation rule in the CodeMie Sandbox project.
- **Trigger**: work item transitions from *To Do* → *In Progress*.
- **Action**: Rovo Test Analyst agent runs, analyzes testability of the user story, result stored in a variable, then posted as a comment on the work item via the "Comment on Work Item" action.
- Demo succeeded: testability verdict and identified issues were added as an automatic comment.

### Tool Capabilities Highlighted
- **Jira Automation triggers**: field value change, work item status transition, PR created, branch created, version released, and more.
- **JQL conditions**: filter automations by priority, assignee, work item type (e.g., exclude Spikes), and other criteria to avoid unintended triggering.
- **Rovo agents**: available directly inside Jira Automation actions; output can be written back as comments.
- **CodeMie agents via webhooks**: supported but will be covered in depth in the next session. CodeMie agents can also pick up instruction files (e.g., `agent.md`) from repositories to dynamically adapt their behavior.

### Discussion: Multi-Agent Workflows (Ravi's Use Case)
- Proposal: parallel agents for code writing, architecture alignment, coding standards, test coverage, and code review — all validating before the developer sees the output.
- Eugene confirmed this is feasible with CodeMie workflows (multi-agent sequences with branching).
- A similar workflow for implementation plan creation across multiple repositories is already in development.
- **Alternative approach noted (Chantal)**: GitHub Actions cron-scheduled workflows can orchestrate existing GitHub-based agents without CodeMie.
- Limitation: CodeMie cannot natively invoke external agents (e.g., from cursor/Claude `agent.md`) but can mimic them by loading instructions from repository files.

### Access and Next Steps
- Participants who shared their emails will be added as Jira Admins on the CodeMie Sandbox project.
- CodeMie access must be self-requested (link shared in chat).
- **Thursday session**: hands-on workshop to expand the automation with multiple cross-functional agents and explore GitHub + CodeMie webhook integrations.
