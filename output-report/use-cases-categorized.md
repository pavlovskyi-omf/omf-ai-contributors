# AI Champions Use Cases — Production vs. Experimentation

**Source:** AI Enablement: ENGINEERING Champion Sync (April–June 2026)

---

## 1. Production Use Cases
*AI used to deliver real work — features, automation, or processes actively in use*

1. **Anjali Pabbareddy (4/8)** — AI-built impersonation feature; cut 2–3 day task to ~1.5 hours, with rollout docs for 20+ apps (APE-110)
2. **John Zimmerman (4/15)** — Copilot-assisted test account extraction from indicator file; Jira APE-113 closed Done
3. **Amit Sharma (4/15)** — Autonomous agent: CREATE TABLE → Glue job → S3 parquet validation, eliminating per-table manual effort (APE-264, Done)
4. **Sukalya Rajendran (4/22)** — CodeMie workflow auto-creating Catalyst DDL cross-team follow-up tasks in Jira (APE-266)
5. **Chantal Justamond (4/22)** — Agentic GitHub Actions Dependabot analysis pipeline; actively rolled out across all payment repos (APE-285)
6. **Patrick Behnke (4/29)** — AI-assisted K8s/OpenShift config generation and validation system for team adoption (APE-126)
7. **Sukalya Rajendran (4/29)** — Prisma schema governance agent: automated ERD + Snowflake DDL generation from GitHub PRs (APE-281)
8. **Deepti Pathak (5/6)** — Automated EKS version drift scanning → Jira ticket creation → Slack alerts; live in production (APE-294)
9. **Sanjay Parsi (5/13)** — PR reviewer and code optimizer for Python/Spark/Snowflake SQL; published in shared GitHub repo (APE-308)
10. **Jason Daggs (5/13)** — Custom Python/FastMCP Jira server for Claude Code: daily issue and sprint management via natural language (APE-1058)
11. **Bala Uda (5/20)** — AI-powered L1 pipeline failure alerts: EventBridge → Lambda → Azure OpenAI RCA → SNS email; running in production (APE-282)
12. **Deepti Pathak (5/20)** — Slack webhook integration for operational EKS alerting, already embedded in the production pipeline (APE-1057)
13. **Vazgen Ayrapetyan (5/27)** — Figma MCP + Atlassian MCP multi-repo code generation with CX design system enforcement and Optimizely A/B feature flag (APE-1465)
14. **Shoaib Naseem (6/3)** — CodeMie workflow generating structured release notes for a real SIAM production release with batched PR/Jira processing (APE-1028)
15. **Amit Kumar (6/3)** — GitHub MCP in IntelliJ for local AI-driven PR review and fix implementation; shared via team agent repo (APE-112)
16. **Jason Daggs (6/10)** — CodeMie 4-step multi-agent workflow generating structured markdown changelogs linking GitHub PRs, commit IDs, and Jira tickets for CAPS/Domain Gateway release communication
17. **Deepti Pathak (6/10)** — Jira automation + GitHub Actions pipeline auto-generating four mandatory audit documents (project analysis, deployment checklist, backout plan, test cases) per Jira ticket; eliminates a real recurring compliance gap
18. **Loquen MeyersJones (6/10)** — Cross-tool Dependabot risk classification agent (Cursor + GitHub Copilot) producing structured risk assessments with evidence trail; applied to a live 48-PR open backlog

---

## 2. Experimentation Use Cases
*AI used primarily to investigate capabilities, explore approaches, or build POCs — not yet delivering production work*

1. **Ravi Nachimuthu (4/8)** — Spec-driven development pattern + MuleSoft-to-GraphQL migration agents; explicitly described as work-in-progress, exploring the architectural approach
2. **Chantal Justamond (4/8)** — Early-stage agentic Dependabot security review flow; still under active refinement at the time ("as I'm going through my repos and improving this script") — later graduated to production by 4/22
3. **Sukalya Rajendran (4/15)** — Snowflake Cortex for natural-language querying of test data; a capability suggestion/demo, not a built or deployed solution
4. **Jason Daggs (5/6)** — 7-session CodeMie enablement curriculum investigating and documenting what AI tools can do for non-developer audiences (APE-278)
5. **Deepti Pathak (5/20)** — Slack MCP server POC in VS Code; explicitly a proof of concept to evaluate AI-assisted interactive notifications
