## Meeting Title
AI Enablement: Cross-Functional Lighthouse PDLC Session — June 9, 2026

## Short Description
Deep dive into Custom GPTs vs. ChatGPT Agents — when to use each, key capability differences, and practical limitations. The session also covered using the ChatGPT Tasks feature as a scheduling workaround and addressed Slack integration approval requirements.

## Key Points / Topics
- **Custom GPTs deep dive**: hands-on build of a daily planner GPT using uploaded files and app integrations (SharePoint, Jira via Robo connector)
- **Custom GPTs vs. ChatGPT Agents — key differences**:
  - Custom GPTs: conversational persona, no scheduling, no autonomous write actions, no multi-agent composition, best for document Q&A and guided chat
  - ChatGPT Agents: can be scheduled (via Tasks), can take write actions autonomously, can combine multiple skills into a workflow, suitable for ongoing background automation
- **ChatGPT Tasks** introduced as the scheduling mechanism for Agents — allows setting a recurring schedule (e.g., every morning at 8 AM) for an agent to run automatically without user intervention
- **Limitations of Custom GPTs highlighted**:
  - Cannot initiate actions without a user message
  - Cannot combine multiple GPTs into a single orchestrated flow
  - File uploads are static — do not auto-refresh when source documents change
- **Slack integration**: ChatGPT Agents can post to Slack channels, but requires Slack admin approval to install the ChatGPT app in the workspace; teams should plan for this approval cycle
- Comparison to Robo agents: Robo is better for Atlassian-native tasks; ChatGPT Agents better when cross-platform orchestration (Teams + GitHub + Jira together) is needed
- **Recommendation guidance**: use Custom GPTs for onboarding new team members to domain knowledge; use ChatGPT Agents for recurring automated workflows that span multiple tools
