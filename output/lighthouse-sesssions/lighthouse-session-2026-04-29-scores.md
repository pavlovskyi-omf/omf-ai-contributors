# Lighthouse - AI Hours Session Scores
**Session:** AI Enablement: ENGINEERING Lighthouse Session — 2026-04-29
**Jira Tickets Showcased:** [APE-281](https://onemainfinancial.atlassian.net/browse/APE-281) | [APE-126](https://onemainfinancial.atlassian.net/browse/APE-126)

---

## Lighthouse - AI Hours Sessions

| Name | Date | Contribution | Score |
|---|---|---|---|
| Patrick Behnke | 4/29/2026 | **Why he stood out:** Built a comprehensive AI-assisted Kubernetes/OpenShift configuration management system in VS Code with prompts covering the full lifecycle — new app creation, secret management, encryption/decryption, and validation — designed to onboard new team members and reduce manual YAML errors.<br><br>**Significant contributions:**<br>- Created a suite of prompts for the NTS2 and OpenShift repos covering: new application creation (with guided Q&A), secret creation with GitCrypt encryption, and config validation with automatic kustomization file updates.<br>- Demonstrated live: creating a new secret, which was encrypted via GitCrypt AND automatically added to the kustomization resources list — a common step developers forget.<br>- The system is explicitly built for team adoption: "I've just been making a whole bunch of instructions and prompts to try to lighten the load of new person coming in" (incoming intern).<br><br>**Contribution:** Demo / Use Case — AI-assisted Kubernetes/OpenShift config generation and validation system for VS Code with team onboarding focus (APE-126). | **5** |
| Sukalya Rajendran | 4/29/2026 | **Why she stood out:** Presented the next iteration of her data platform work — an automated Prisma schema governance agent that generates ERD diagrams and Snowflake DDLs from GitHub PRs, with a clear end-to-end workflow toward fully automated data pipeline development.<br><br>**Significant contributions:**<br>- Showed the full agent workflow: PR merge triggers GitHub Actions → agent detects Prisma schema changes → generates ERD (mermaid) and Snowflake raw DDL → human reviews → DBT developer agent generates data pipeline and PR automatically.<br>- Ran a live session showing the agent pulling 3 weeks of Prisma changes (multiple CAT tasks), generating ERD diagrams with table relationships and Snowflake DDL with column-level comments.<br>- Demonstrated iterative improvement: discovered formatting issues with mermaid files during development and fixed the agent instructions to handle hyphens/quotes correctly.<br><br>**Contribution:** Demo / Use Case — Automated Prisma schema governance agent for ERD and Snowflake DDL generation via GitHub Actions (APE-281). | **5** |
| Muhammad Adnan Farooq | 4/29/2026 | **Why he stood out:** Provided critical business context that framed both demos' real-world value and confirmed the production urgency behind the Prisma schema automation.<br><br>**Significant contributions:**<br>- Explained the pain that motivated the Prisma agent: teams have broken pipelines in the past by making schema changes without notifying downstream data teams.<br>- Confirmed the scale: 18+ subgraphs teams whose changes all need to be tracked.<br>- Connected Sukalya's work to the broader goal of end-to-end automated pipeline delivery.<br><br>**Contribution:** Active participation — provided the business incident history and scale context that justified both the Prisma and OpenShift automation demos. | **1** |
| Guru Pitty | 4/29/2026 | **Why he stood out:** Asked substantive validation questions that probed the practical readiness of the Prisma agent for real use.<br><br>**Significant contributions:**<br>- Asked whether the agent is in active daily use (vs. just demonstrated).<br>- Probed how generated Snowflake DDL is validated before production deployment.<br>- Confirmed understanding of the SDLC cycle for AI-generated artifacts.<br><br>**Contribution:** Active participation — drove a quality discussion about validation practices and production readiness of AI-generated database artifacts. | **1** |

---

## Scoring Notes

| Participant | Jira Ticket | Demo Level | Rationale |
|---|---|---|---|
| Patrick Behnke | APE-126 | D2 — Working (5 pts) | Functioning system in a real repo; live demo showed secret creation, encryption, and kustomization update working end-to-end. Demo had some model compatibility hiccups but the underlying system works. Potential D3 upgrade if intern adoption is confirmed in next session. |
| Sukalya Rajendran | APE-281 | D2 — Working (5 pts) | Live demo produced real ERD and Snowflake DDL artifacts from actual Prisma changes; end-to-end workflow demonstrated. Running locally pending buy-in from subgraph repo owners for production deployment. |
| Muhammad Adnan Farooq | — | Active participation (1 pt) | — |
| Guru Pitty | — | Active participation (1 pt) | — |
