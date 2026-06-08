# Lighthouse - AI Hours Session Scores
**Session:** AI Enablement: ENGINEERING Lighthouse Session — 2026-04-22
**Jira Tickets Showcased:** [APE-266](https://onemainfinancial.atlassian.net/browse/APE-266) | [APE-285](https://onemainfinancial.atlassian.net/browse/APE-285)

---

## Lighthouse - AI Hours Sessions

| Name | Date | Contribution | Score |
|---|---|---|---|
| Sukalya Rajendran | 4/22/2026 | **Why she stood out:** Delivered a working agentic automation that solves a real cross-team coordination pain point for the Catalyst project, demonstrating both the agent and its iterative evolution into a workflow.<br><br>**Significant contributions:**<br>- Built a CodeMie agent that monitors Catalyst Jira tasks with the `catalys-ddl-update` label and auto-creates downstream follow-up tasks for the DO, DPG, and DFP teams with pre-populated details.<br>- Evolved from three separate agents → a sequential workflow for deterministic execution order, explaining the key difference between orchestrators vs. deterministic workflows.<br>- Collaborated with Richard Weiss (DO team) to refine task templates based on reviewer feedback, making the output immediately actionable.<br><br>**Contribution:** Demo / Use Case — Working CodeMie workflow for automated Catalyst DDL change tracking and cross-team task generation (APE-266). | **5** |
| Chantal Justamond | 4/22/2026 | **Why she stood out:** Built a sophisticated 4-step GitHub Actions agentic workflow that goes beyond simple Copilot review to provide context-aware vulnerability exploitability analysis, and is actively rolling it out across all her repos.<br><br>**Significant contributions:**<br>- Created a multi-step pipeline: metadata extraction → codebase exploitability scan (production vs. test code) → risk summary + recommendation → optional issue creation — combining 4+ data sources intelligently with fallback strategies.<br>- Demonstrated the workflow on a live denial-of-service Dependabot alert, showing risk level (medium), merge priority (normal), and upgrade risk (low) in seconds instead of manual investigation.<br>- "Since this has been kind of like a work in motion, I'm merging this into all my repos" — confirmed active adoption across her entire payment service portfolio.<br><br>**Contribution:** Demo / Use Case — Agentic GitHub Actions workflow for Dependabot vulnerability analysis and automated PR risk scoring (APE-285). | **10** |
| Muhammad Adnan Farooq | 4/22/2026 | **Why he stood out:** Actively added strategic context and vision, connecting Sukalya's demo to the team's broader goal of building an end-to-end AI-powered PDLC.<br><br>**Significant contributions:**<br>- Articulated the team's north star: automating requirement gathering → coding → deployment as an end-to-end Gen AI workflow.<br>- Reinforced the value of deterministic-plus-LLM hybrid workflows.<br>- Engaged with both demos to encourage the broader team.<br><br>**Contribution:** Active participation — shared the team's strategic AI workflow vision and connected individual demos to the bigger goal. | **1** |
| Ravi Nachimuthu | 4/22/2026 | **Why he stood out:** Provided a sharp analytical observation that named the architectural pattern Sukalya demonstrated and articulated its broader applicability.<br><br>**Significant contributions:**<br>- Called out the LLM-plus-deterministic-workflow hybrid pattern as a key reusable architectural approach for the team.<br>- Noted the pattern's broader applicability beyond this specific use case.<br>- Moved the discussion forward with substantive technical commentary.<br><br>**Contribution:** Active participation — named and validated the deterministic workflow + LLM hybrid pattern as a generalizable design approach. | **1** |
| Jason Daggs | 4/22/2026 | **Why he stood out:** Engaged positively and contributed to the discussion momentum.<br><br>**Significant contributions:**<br>- Provided affirmative engagement during both demos.<br>- Expressed enthusiasm about his own upcoming use case submission.<br>- Participated actively in session flow.<br><br>**Contribution:** Active participation — engaged throughout the session and confirmed his own use case is in progress. | **1** |
| Deepti Pathak | 4/22/2026 | **Why she stood out:** Asked a technically precise question about Chantal's workflow that advanced understanding for the whole group.<br><br>**Significant contributions:**<br>- Asked whether the vulnerability analysis uses LLMs or pattern matching, clarifying the multi-source AI approach.<br>- Followed up on agent compartmentalization and reuse possibilities.<br>- Explored MCP integration potential for connecting Copilot to additional security tools.<br><br>**Contribution:** Active participation — engaged with targeted questions that deepened the group's understanding of Chantal's agentic security workflow. | **1** |

---

## Scoring Notes

| Participant | Jira Ticket | Demo Level | Rationale |
|---|---|---|---|
| Sukalya Rajendran | APE-266 | D2 — Working (5 pts) | Functioning end-to-end agent connected to production Jira; showed concrete task output; shared with team. Potential D3 upgrade if confirmed teammate adoption beyond builder. |
| Chantal Justamond | APE-285 | D3 — Impactful/Reusable (10 pts) | Clears D2; confirmed adoption/reuse: actively merging the workflow into all her repos; production payment service already using it. |
| Muhammad Adnan Farooq | — | Active participation (1 pt) | — |
| Ravi Nachimuthu | — | Active participation (1 pt) | — |
| Jason Daggs | — | Active participation (1 pt) | — |
| Deepti Pathak | — | Active participation (1 pt) | — |
