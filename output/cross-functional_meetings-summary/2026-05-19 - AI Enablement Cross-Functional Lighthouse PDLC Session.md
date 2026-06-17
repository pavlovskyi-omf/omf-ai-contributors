## Meeting Title
AI Enablement: Cross-Functional Lighthouse PDLC Session — May 19, 2026

## Short Description
Continuation and completion of the Jira automation requirements readiness workflow. The session added a cross-functional summary agent, a delay-until mechanism triggered by a Jira label, and an if/else decision step that automatically blocks stories not ready for development.

## Key Points / Topics
- **Recap of the requirements readiness workflow** built in previous sessions: a Jira automation pipeline that uses AI to assess whether a story is ready to move to development
- **Cross-functional summary agent** added to the workflow: aggregates input from multiple stakeholders (PM, design, QA, engineering) into a single structured summary before the readiness check
- **Delay-until mechanism**: the automation pauses and waits until a specific Jira label ("AI reviewed") is applied before proceeding — enables human review as a gate in the flow
- **If/else condition step**: after the AI assessment, a branch decides the outcome:
  - If the story passes the readiness criteria → moves to "Ready for Development"
  - If the story fails → automatically transitions to "Blocked" status with a comment explaining what is missing
- Discussion of token limits and prompt design: keeping prompts focused to avoid exceeding Jira automation's context window
- **Practical outcomes**: the workflow reduces manual readiness review effort and creates a consistent, auditable record of why each story was approved or blocked
- Next steps identified: extend the workflow to handle epic-level readiness and explore GitHub webhook triggers as an alternative entry point
