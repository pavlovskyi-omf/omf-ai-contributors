# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 14, 2026
**Duration:** 1h 0m 53s
**Presenters:** Nikita Kumar, Oleksandr Tsyganok

---

## Meeting Title

AI Enablement: Homework Show & Tell — Custom Assistants and CodeMie Platform Overview

---

## Short Description

Session three was a homework show-and-tell where participants demonstrated custom CodeMie assistants they had built since the previous Thursday. Multiple teams showcased real use cases ranging from Jira story quality checks and automated follow-up task creation to blocked issue monitoring and automated test generation workflows. The second half of the session provided a guided overview of the CodeMie platform's core features: chat history, assistant management, skills, workflows, integrations, data sources, and spending controls.

---

## Key Points / Topics

### Homework Demonstrations

**Jason Daggs — PR Code Review Agent**
- Built a GitHub PR review agent using a publicly available prompt template.
- Agent reviews PRs across 5 dimensions: correctness, readability, architecture, security, and performance.
- Blocked by missing GitHub organization authorization (personal GitHub lacked access to the OMF org).
- Resolution: ensure the correct GitHub organization is authorized and the VCS tool is enabled in the agent's tool settings.

**Swetha Koppula — Jira Story Quality Checker**
- Created a requirements hardening assistant based on the session demo.
- Successfully ran analysis on a Jira story and posted a structured quality review comment covering clarity, completeness, and testability.
- Initially created the story in production Jira (not training); resolved by using the training instance.

**Sukalya Rajendran — Catalyst DDL Watcher**
- Advanced use case: monitors Jira for stories labeled **"Catalyst DDL update"** (indicating a data pipeline impact from a front-end change).
- Automatically creates follow-up tasks across three downstream Jira boards: domain review, data modeling, and DFP data pipeline.
- Follow-up tickets include all relevant context from the source story; downstream teams do not need to reference the original ticket.
- Tracks upstream/downstream dependencies via links.
- Next step: schedule the agent to run automatically once the scheduler feature is enabled.
- CodeMie tip received: use native Jira link functionality and add a "processed" label to avoid re-processing tickets on each run.

**Jurijs Markelovs — Automated Test Generator Workflow**
- Built a multi-agent **workflow** (not a single assistant) targeting tickets that reach "Testing" status with a specific label.
- Agent 1: fetches Jira ticket details via JQL query.
- Agent 2: clones the automation test repository, analyzes the Playwright framework structure, and creates placeholder test cases on a new branch.
- Reported a UI bug: selected integrations disappear from the workflow editor after saving (flagged to the CodeMie team).
- Next step: add a scheduled cron trigger to run automatically.

**Deepti Pathak — Jira Blocked Issue Monitor**
- Monitors all tickets in "Blocked" status across the DFP project.
- Rules: informational if blocked < 24h; follow-up if blocked > 24h; escalation comment if blocked > 3 days.
- Posts a summary comment on the blocked ticket including the blocker reason, risk level, and time blocked.
- Future enhancement: post daily summaries to a Confluence page or Slack/Teams channel.

**Angela (Speaker 1) — Jira TDM Intake Agent**
- Built an agent to automate Jira ticket intake.
- Issue encountered: **Refine with AI** button spun indefinitely and never returned a result (confirmed CodeMie bug; team to investigate logs).
- Workaround: used VS Code + Claude to refine the prompt externally and pasted the result back into CodeMie.

### CodeMie Platform Overview

**Chat Features**
- All chats are private by default; use **Share Chat** to generate a read-only link for troubleshooting or collaboration.
- Chat history is organized per assistant and supports custom folders, pinning, and moving items.
- Per-message controls: copy, edit and resend (clears history forward), view usage/token stats, download transcript.

**Assistants**
- Filter by project; access a **Marketplace** to share production-ready agents across all OMF teams.
- **Clone** an assistant to customize without modifying the shared original.
- **Skills**: extract reusable prompt logic (e.g., a meeting summary format) and attach it to multiple assistants.
- In-chat model switching: override the default model for a specific conversation without editing the assistant.

**Workflows**
- Orchestrate multiple agents in automated sequences; trigger via events, webhooks, or scheduled jobs.
- Dedicated deep-dive session planned.

**Integrations & Data Sources**
- Integrations connect agents to external tools (Jira, GitHub, Confluence, etc.).
- Data sources add knowledge bases: indexed repositories, uploaded files, exported backlogs, Confluence spaces.

**Spending & Usage**
- Per-user spending visible in the profile page (current limit: ~$500/month).
- Platform-wide analytics available (24h / weekly / per-project / per-user breakdowns).
- Admins can adjust budgets per user, team, or role.

**Tutorials**
- Built-in hands-on challenges available (15-minute intro through advanced workflow labs).

### Upcoming Sessions
- **Thursday**: next hands-on session with new homework assignment.
- **Friday open hours**: optional drop-in for troubleshooting and Q&A.
