# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 7, 2026
**Duration:** 59m 21s
**Presenters:** Eugene Semenyuk, Oleksandr Tsyganok

---

## Meeting Title

AI Enablement: End-to-End Agentic PDLC Flow — From Requirements to Testing

---

## Short Description

Eugene Semenyuk introduced the concept of a connected agentic PDLC flow where AI agents operate at every stage — from requirements intake through development to testing — passing context seamlessly instead of working in isolation. Oleksandr Tsyganok delivered a live end-to-end demo using CodeMie to orchestrate multiple agents across Jira, Confluence, and GitHub, covering requirements hardening, QA testability analysis, test case generation, engineering implementation planning, PR risk analysis, and smart test selection.

---

## Key Points / Topics

### Problem Statement
- Current PDLC suffers from disconnected steps: each team uses AI tools independently, losing context at every handoff.
- Goal: replace isolated point solutions with one **connected agentic flow** spanning Digital, QA, and Engineering.
- Each team's implementation will differ, but the shared goal is aligned context and reduced rework.

### The Agentic Flow Concept
- A continuous flow from requirements → implementation → testing, treated as a **team activity**.
- Agents are connected so output from one step becomes input for the next — context is never lost.
- CodeMie orchestrates existing agents (including Rovo agents) across Jira, Confluence, and GitHub with **human control at each step**.

### Demo Walkthrough (End-to-End)

1. **Requirements Hardening Agent**
   - Input: Jira user story.
   - Validates quality: acceptance criteria, NFRs, estimates, clarity.
   - Acts as a "Definition of Ready" gate; posts results as a Jira comment.
   - Demonstrated event-driven execution on Jira ticket status transition.

2. **QA Testability Analysis**
   - Analyzes the story for testability gaps.
   - Searches linked Jira items and Confluence for additional context.
   - Posts analysis as a Jira comment; can be iterated with human input.

3. **Test Condition & Test Case Generation**
   - **Test Conditions Agent**: generates low-level test conditions from acceptance criteria.
   - **Test Case Composer Agent**: converts conditions into formatted test cases (target: X-Ray integration, pending approval).
   - Agents share context within a single chat; no need to re-provide Jira ID.

4. **Implementation Plan Architect Agent**
   - Analyzes connected code repositories before creating a plan.
   - Identifies affected components (backend-for-frontend, mobile, frontend).
   - Creates a specification markdown file and opens a GitHub pull request branch.
   - Reduces "assumption-based" development; supports multi-repo specs for parallel dev.

5. **PR Risk Analysis Workflow**
   - Triggered automatically via GitHub webhook on pull request creation.
   - Orchestrates specialized agents: one reads GitHub diffs, another reads Jira context, a third synthesizes and assesses risks.
   - Outputs a structured risk report (impacted components, user journeys, deployment recommendations) as a PR comment — zero manual interaction required.

6. **Smart Test Selection** *(in active development)*
   - Takes a PR and user story as input.
   - Identifies affected components and maps them to existing test cases.
   - Highlights test coverage gaps and recommends new test cases to create.
   - Reuses the Test Case Composer agent modularly.

### Tools & Features Highlighted
- **CodeMie**: orchestrates multiple agents, connects to Jira, Confluence, GitHub; supports webhooks and event-driven execution.
- **Rovo agents**: can be orchestrated by CodeMie as sub-agents within workflows.
- **X-Ray integration**: planned native integration for test case management (pending security approval).
- **OpenAPI tool**: allows connecting any REST API with an OpenAPI spec as a custom tool.
- **MCP connectors**: path to Slack/Teams integration, pending organizational approval.

### Q&A Highlights
- **Slack/Teams integration**: technically possible via approved MCP server; approval process still in progress at OMF.
- **Anthropic/Claude models**: planned for CodeMie but not yet approved; only Azure-hosted models currently available.
- **CodeMie vs. Power Automate**: CodeMie is better suited for engineering-specific tasks and internal OMF tooling; Power Automate is better for Office/Microsoft ecosystem tasks.
- **Snowflake integration**: no native support yet; possible via REST API + OpenAPI spec if Snowflake provides documented endpoints.
- **Token budgets**: CodeMie uses Azure-hosted LLMs with configurable per-user spending limits (~$200/month default); budgets are adjustable by project admins.
