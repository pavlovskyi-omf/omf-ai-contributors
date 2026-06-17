# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** May 12, 2026
**Duration:** 1h 0m 11s
**Presenters:** Eugene Semenyuk, Svetlana Stogni

---

## Meeting Title

AI Enablement: Building the Cross-Functional Requirements Review Flow — QA and Engineering Agents via Webhook (Part 2)

---

## Short Description

Eugene Semenyuk continued the hands-on build of the automated cross-functional requirements review flow, expanding it with a QA testability analysis agent and an engineering technical feasibility agent. The engineering review introduced a new integration pattern: calling an external CodeMie agent from Jira Automation via an HTTP webhook. By the end of the session, all three review perspectives (digital, QA, engineering) were posting comments automatically to a Jira story upon status transition. A final summarization step combining all three reviews was identified as the next milestone.

---

## Key Points / Topics

### Session Recap and Starting Point

- Previous session established: trigger (To Do → In Progress), user condition, digital story review agent, and comment step.
- Today's goal: add QA and engineering perspectives to produce a three-way cross-functional review.

### Adding the QA Review Step

- Action: **Use Agent** → select **Test Analysis Without Context** (Rovo agent).
- Prompt: "Review this user story."
- Add a **Comment on Work Item** action immediately after, using `{{agentResponse}}`.
- Note: `{{agentResponse}}` is overwritten by each subsequent agent; for complex flows requiring multiple stored values, use a **Create Variable** step after each agent to save the response under a named variable (e.g., `digitalReview`). Nodes are draggable to reorder.
- Result observed: QA review posted as a separate Jira comment identifying testability issues and assumptions.

### Adding the Engineering Review via CodeMie Webhook

The engineering review requires a CodeMie agent with access to the actual codebase, making it an external integration:

**Step 1 — Create a CodeMie Webhook (Project Integration)**
- Navigate to CodeMie → Integrations → Project Integrations → Create.
- Credentials type: **Webhook**.
- Configure:
  - Alias/name (e.g., "Technical Review — [Name]")
  - Webhook ID
  - Secure header name and value (acts as a shared password; use a strong value in production)
  - Resource type: **Assistant**
  - Resource ID: copied from the Technical Feasibility agent's URL in CodeMie
- Admin permissions required for project integrations; request via ServiceNow ticket if not available.
- Participants without admin access: use Eugene's shared webhook for the training session.

**Step 2 — Add Send Web Request Action in Jira Automation**
- Action: **Send Web Request**.
- URL: CodeMie webhook URL (pattern: `https://[codeme-domain]/api/v1/webhooks/[webhook-id]`).
- Body type: **Issue Data Automation Format** (sends the full Jira story context automatically).
- Headers: add `x-secure: [password]` matching what was configured in the webhook.
- Validate configuration using the built-in "Validate" button with an issue key before going live.

**Result observed**
- CodeMie agent analyzed the codebase, identified impacted modules and files, produced a feasibility verdict (75% confidence, "Feasible"), listed required changes, estimated development effort, and flagged risks.
- Agent also added an **AI Reviewed** label to the Jira issue automatically.
- References to specific repository files included in the comment.

### Three-Perspective Review Working End-to-End

With all three steps in place:
1. User story transitions to In Progress.
2. Rovo digital agent reviews and comments (business/digital perspective).
3. Rovo QA agent reviews and comments (testability perspective).
4. CodeMie engineering agent reviews via webhook and comments (technical feasibility perspective).

The flow demonstrated in the sandbox with the self-service team's backend user story (CS184).

### Issues and Resolutions

- **Comment too long error (32,767 character limit)**: Jira Automation rejects comments exceeding this limit. Potential mitigation: split large responses across multiple comments or truncate in the prompt. "Prevent duplicates" checkbox also highlighted as a common source of skipped steps.
- **Webhook URL incorrect in chat**: Eugene corrected a typo (I vs. V) — participants advised to copy from the materials page rather than from chat.
- **Project integration not visible**: user lacks admin permissions; must request via ServiceNow before creating own webhooks.
- **No Actions Performed in audit log**: expected when another user's item triggers the flow but the reporter condition filters it out.

### Next Steps

- **Final summarization step**: add a cross-functional summary agent that reads all three comments and produces a consolidated recommendation — proceed/blocked verdict, key concerns, and executive summary.
- **Conditional branching**: if the cross-functional review returns "Not Ready," automatically transition the story back to a blocked/to-do state and assign it for clarification.
- **Next Thursday**: dedicated session on MCP servers.
- **After MCP session**: continue with cross-functional use case expansion.
- Eugene to publish a detailed step-by-step guide for the full flow after the session.
- Friday office hours available for debugging and further assistance.
