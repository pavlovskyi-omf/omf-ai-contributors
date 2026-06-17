## Meeting Title
AI Enablement: Cross-Functional Lighthouse PDLC Session — May 28, 2026

## Short Description
Introduction to ChatGPT Agents as a new capability for cross-tool automation and productivity. The session demoed a morning planner agent integrating Teams, Jira, and Calendar, and a QA testability agent built with reusable skills. Key differences between ChatGPT Agents and Custom GPTs were clarified.

## Key Points / Topics
- **ChatGPT Agents** introduced as OpenAI's new agentic capability within ChatGPT (distinct from the API-level Assistants)
- **Morning planner demo**: agent reads the user's calendar, pulls assigned Jira tickets, checks Teams messages, and generates a prioritized daily plan — all in one automated run
- **Available app integrations** for ChatGPT Agents: Microsoft Teams, SharePoint, Jira and Confluence (via Atlassian Robo connector), GitHub, and others
- **Skills concept**: reusable task instructions that act as sub-agents within a larger agent flow; each skill has a name, description, and prompt defining what it does
  - Example skills built in session: "Testability Review" (assesses whether a story is testable), "Test Idea Generator" (produces test scenarios from acceptance criteria)
- **QA testability agent demo**: agent receives a Jira story, runs the Testability Review skill, conditionally runs Test Idea Generator if the story passes, and posts results back to Jira
- **ChatGPT Agents vs. Custom GPTs**:
  - Agents: can be scheduled, can write/act autonomously, can chain skills, integrate live apps
  - Custom GPTs: conversational only, no scheduling, no autonomous write actions, suitable for document Q&A and persona-based chat
- **Human-in-the-loop**: agents can be configured to pause and request approval before taking write actions (posting to Jira, sending Teams messages)
- Next session to cover deeper Custom GPT comparison and scheduling via the ChatGPT Tasks feature
