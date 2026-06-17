# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 9, 2026
**Duration:** 1h 0m 33s
**Presenters:** Oleksandr Tsyganok, Nikita Kumar

---

## Meeting Title

AI Enablement: Hands-On — Building a Requirements Hardening Assistant in CodeMie

---

## Short Description

The second session focused on a guided, hands-on workshop where participants built their first CodeMie assistant from scratch. Oleksandr Tsyganok walked the group step-by-step through creating a Jira API token, configuring a Jira integration in CodeMie, generating an assistant using AI, refining the system prompt, and successfully running the requirements hardening agent against a Jira user story. Homework was assigned: build your own custom assistant before the next session.

---

## Key Points / Topics

### Session Setup
- All participants needed active CodeMie access; a training Atlassian Jira instance was provided to avoid unintended changes in production.
- Materials, links, and the step-by-step guide were shared in the meeting chat.
- Thursday sessions = demo + hands-on; Tuesday sessions = homework show-and-tell.

### Step 1 — Create a Jira API Token
- Navigate to Atlassian account security settings and create a new API token.
- Set expiration to several months (not the 1-week default) to avoid frequent rotation.
- Copy the token immediately — it cannot be retrieved after closing the page.
- Best practice: store in a password manager; avoid plain-text documents.
- Tokens can be revoked and regenerated at any time.
- Scoped tokens (least-privilege) are possible and recommended for production agents.

### Step 2 — Configure Jira Integration in CodeMie
- Navigate to **Integrations → User Integrations → Create**.
- Select **Jira** from the dropdown; provide a friendly alias (e.g., "Jira Training OMF").
- Enter the training Jira URL and check the **Jira Cloud** checkbox.
- Provide email and paste the API token; click **Test** before saving.
- Integration must be created in the same CodeMie project as the assistant.

### Step 3 — Create an Assistant Using AI Generation
- Navigate to **Assistants → Create Assistant**.
- Describe the goal in plain language (e.g., "review Jira user story quality and post a comment with missing details").
- CodeMie generates a full system prompt, description, category tags, and conversation starters automatically.
- The AI-generated prompt includes: role definition, step-by-step checklist (personas, business value, acceptance criteria, NFRs, estimates), tool usage guidance, and constraints.

### Step 4 — Refine the System Prompt
- Review the generated steps and adapt them to your team's standards and processes.
- Key recommendation: add explicit **user confirmation** before the agent posts a Jira comment (to avoid autonomous posting under your account).
- Use the **Refine with AI** button to iterate on the prompt without manual editing.

### Step 5 — Connect the Jira Tool
- In the assistant's **Tools & Integrations** tab, enable **Generic Jira** and select the integration created in Step 2.
- This is the step that transforms a chat-only assistant into a real agent with Jira access.

### Step 6 — Test the Assistant
- Run the agent by providing a Jira story link.
- Confirm the agent calls the Jira tool (visible in the tool call trace).
- When prompted, confirm to post the analysis as a Jira comment.

### Prompt Quality Improvement
- A known issue: the AI-generated prompt did not specify Jira's **ADF (Atlassian Document Format)** for comments, causing repeated failures.
- Fix: add an example of a valid ADF payload to the system prompt — the agent immediately succeeded on the next attempt.
- Key lesson: providing concrete examples in the prompt dramatically improves reliability even with weaker models.
- A high-quality production prompt (used by the network team's story readiness checker) was shared for participants to adopt and adapt.

### Key Platform Notes
- **Model selection**: default is GPT mini; more powerful models can be selected per assistant based on task complexity and cost trade-offs.
- **GitHub integration**: available and approved but not covered in this session; participants can explore it independently.
- **API token scopes**: default tokens inherit all user permissions; scoped tokens can restrict agents to specific Jira actions.

### Homework
- Create at least one custom assistant of your own choosing.
- Be prepared to demo it during the Tuesday show-and-tell session.
