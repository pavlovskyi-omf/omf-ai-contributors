## Meeting Title
AI Enablement: Cross-Functional Lighthouse PDLC Session — May 21, 2026

## Short Description
Introduction of the multi-repo system intelligence use case in CodeMie, and a live demo of GitHub webhooks triggering CodeMie agents from pull request events. The session explored how autonomous agents can be invoked by developer actions in GitHub without any manual intervention.

## Key Points / Topics
- **Multi-repo system intelligence** concept introduced: a single CodeMie agent that can reason across multiple GitHub repositories simultaneously, enabling cross-repo Q&A, impact analysis, and dependency tracing
- Use case examples: "which service owns this API endpoint?", "what would break if I change this shared library?", "where is this business rule implemented?"
- **GitHub webhooks** demonstrated as an event-driven trigger mechanism for CodeMie agents:
  - Webhook fires on PR events (created, labeled, updated, merged)
  - Payload sent to CodeMie agent endpoint
  - Agent processes the PR diff and executes a configured task (e.g., code review, test coverage check)
- Webhook configuration walkthrough: GitHub repo settings → Webhooks → payload URL (CodeMie endpoint), content type, event selection
- **Comparison of trigger types**: manual (user invokes agent in chat), scheduled (cron-style), event-driven (webhook from GitHub or Jira)
- Discussion of authentication: webhook secrets used to verify payloads; CodeMie validates the signature before processing
- **Practical integration**: combining Jira automation (for ticket-lifecycle events) with GitHub webhooks (for code-lifecycle events) creates a full SDLC event loop for autonomous agents
- Upcoming sessions to cover hands-on CodeMie agent setup and data source configuration
