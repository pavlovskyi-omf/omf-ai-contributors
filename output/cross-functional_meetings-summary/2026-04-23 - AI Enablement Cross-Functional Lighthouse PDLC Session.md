# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 23, 2026
**Duration:** 1h 5m 27s
**Presenters:** Nikita Kumar, Vlad Grubman, Oleksandr Tsyganok

---

## Meeting Title

AI Enablement: Confluence Integration & Hands-On Agent Enhancement — Connecting Agents to Live Knowledge Bases

---

## Short Description

This session marked a strategic shift in the program: moving from pure CodeMie tool training to use-case-driven, hands-on implementation. Oleksandr led a practical exercise adding a Confluence integration to the existing Jira Story Readiness Checker agent, enabling it to dynamically load the Definition of Ready and Definition of Done from a live Confluence page and include referenced citations in its output. The session covered integration setup, API token management, and prompt engineering for dynamic knowledge retrieval.

---

## Key Points / Topics

### Program Direction Change

- Teams will no longer receive generic CodeMie training sessions; instead, each Lighthouse team is expected to bring use cases for their specific PDLC context.
- AI enablement team will help implement those use cases hands-on, using CodeMie, Rovo, or any other suitable tool.
- Ask for next week: each team prepares cross-functional use cases spanning digital, dev, and QA roles.
- Vlad's framing: "reverse learning — give us the use case and we'll show you how to solve it with AI."

### Confluence Integration Setup

- Added a new **user integration** of type Confluence in CodeMie (mirroring the earlier Jira integration setup).
- Key configuration: Confluence Cloud URL, email address, and a freshly generated API token (Atlassian account → Security → API tokens).
- Confluence Cloud checkbox must be enabled for cloud instances.
- Important distinctions covered:
  - **User integration**: runs on behalf of the authenticated user; best for manual, interactive sessions.
  - **Project integration**: shared bot account; best for automated, unattended flows (e.g., PR triggers).
  - **Global integration**: available cross-project; useful when the same credentials are reused across many projects.
- Common issue resolved: incorrect Confluence URL (full wiki path instead of just the domain) caused test failures.
- API tokens can be scoped for limited permissions (production best practice) or reused across multiple integrations.

### Enhancing the Jira Story Readiness Agent

- Goal: make the agent dynamically load the Definition of Ready and Definition of Done from Confluence at runtime, ensuring it always uses the most current version of the document.
- Steps followed:
  1. Cloned the existing Jira Story Readiness agent.
  2. Enabled the generic Confluence tool in the agent's tool settings.
  3. Updated the system prompt to instruct the agent to always load the Definition of Ready / Done page from a specific Confluence URL before running its analysis.
  4. Modified the output constraints to allow a compliance summary section (in addition to the standard markdown table).
- Result: agent output now includes a **compliance summary** with direct citations from the Confluence page, highlighting specific criteria that were not met and referencing the original source.
- Observed behavior: the agent may use different numbers of Confluence API calls across runs (search, parent lookup, direct load) — this is expected non-deterministic behavior; narrow the instructions if consistency is critical.

### Hands-On Participant Notes

- Several participants successfully completed the integration and tested it end-to-end (posting results as Jira comments).
- Common issues: expired API tokens, incorrect URL format, missing Cloud checkbox, default model not detecting the correct integration.
- Recommendation: prefer explicit integration selection over the default resolution mechanism when building personal or shared agents.

### Session Notes

- No homework assigned.
- Next session: teams bring use cases for their Lighthouse teams to begin hands-on implementation.
- Friday open hours available for additional troubleshooting.
