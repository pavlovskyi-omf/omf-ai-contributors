| Name | Total Score |
| --- | --- |
| Sukalya Rajendran | 55 |
| Bandana Sriramka | 52 |
| Deepti Pathak | 46 |
| Jurijs Markelovs | 46 |
| Jason Daggs | 40 |
| Jatin Bagga | 35 |
| Alfredo Achecar | 23 |
| Patrick Behnke | 21 |
| Dhanalakshmi Chinnasamy | 20 |
| Debamitra Bhattacharjee | 18 |
| Chantal Justamond | 17 |
| Mia (Xiaoling) Zhou | 15 |
| Amit Kumar | 14 |
| Eric Trenz | 14 |
| Shoaib Naseem | 12 |
| Amit Sharma | 11 |
| Sanjay Kumar Parui | 11 |
| Anjali Pabbareddy | 10 |
| Hai Le | 10 |
| Joshua Smith | 10 |
| Loquen MeyersJones | 10 |
| Sanjay Parsi | 10 |
| Uda, Balanarasimha Rao | 10 |
| Vazgen Ayrapetyan | 10 |
| Divya Ramkumar | 8 |
| Doug Ball | 8 |
| Muhammad Adnan Farooq | 8 |
| Ravi Nachimuthu | 8 |
| Swathy Lokula | 8 |
| Ashwin Jain | 7 |
| Denis Platonov | 7 |
| Sam Jayavelan | 7 |
| Kai Jei | 6 |
| Nicholas Crowley | 6 |
| Shai Eilat | 6 |
| Altaf Shariff | 5 |
| Anu Perera | 5 |
| John Zimmerman | 5 |
| Mauezatur Khan | 5 |
| Moses Song | 5 |
| Oleksandr Tsyganok | 5 |
| Swetha Koppula | 5 |
| Heath Fest | 4 |
| JT Tabencki | 4 |
| Praveen Lakshman | 4 |
| Brooke Borowiak | 3 |
| Byron Purdy | 3 |
| Haris Khan | 3 |
| Matt Nobles | 3 |
| Nicole Davis | 3 |
| Alice Merrill | 2 |
| Allen Truban | 2 |
| Biniam Wubyeshaw | 2 |
| Guru Pitty | 2 |
| Lisa Ruby | 2 |
| Monique Braxton | 2 |
| Oleg Kharlamov | 2 |
| Vin Underwood | 2 |
| Akash Gupta | 1 |
| Bertha Cadena | 1 |
| Chandra Willett | 1 |
| Dhiraj Shrivastava | 1 |
| Filippo Morelli | 1 |
| Gayathri Venkataraman | 1 |
| Iryna Pashko | 1 |
| Jamie Hayes | 1 |
| Joaquin Martinez Valdepenas | 1 |
| Karly Bolger | 1 |
| Kevin Yang | 1 |
| Manaswini Kaligotla | 1 |
| Mikhail Makarov | 1 |
| Prachi Chati | 1 |
| Ramakrishnan Varadhan | 1 |
| Raymond Gralewski | 1 |
| Rohit Sehdev | 1 |
| Sadananda Mondal | 1 |
| Saravanan Ganeshan | 1 |
| Sean Monaghan | 1 |
| Stuart Sharp | 1 |
| Sujan Shrestha | 1 |
| Xavier Ferguson | 1 |
| Yury Yastrabtsou | 1 |

---

## Use Cases: Production vs. Experimentation

### Used for Production

Use cases where AI tools were applied to complete actual work tasks — features delivered, automations running, Jira tickets closed.

1. **AI-built impersonate-user feature** (Anjali Pabbareddy, 4/8) — GitHub Copilot agent reduced a 2–3 day manual task to ~1.5 hours; reusable README rolled out across 20+ apps. [APE-110]
2. **Test account extraction from indicator file** (John Zimmerman, 4/15) — Copilot natural-language prompts generated filtered CSV files for bankruptcy and direct-pay accounts. [APE-113, Done]
3. **Autonomous parquet dummy data generation for Snowflake Iceberg tables** (Amit Sharma, 4/15) — End-to-end agent parses DDL, generates a Glue job, deploys to S3, and validates output in 91 seconds. [APE-264, Done]
4. **Automated Catalyst DDL change tracking workflow** (Sukalya Rajendran, 4/22) — CodeMie workflow monitors Jira labels and auto-creates follow-up tasks for DO, DPG, and DFP teams. [APE-266]
5. **GitHub Actions Dependabot vulnerability analysis workflow** (Chantal Justamond, 4/22) — 4-step agentic pipeline classifies PR risk level and merge priority; actively merged into all payment service repos. [APE-285]
6. **AI-assisted Kubernetes/OpenShift config generation and validation** (Patrick Behnke, 4/29) — VS Code prompt suite covering new app creation, secret management, GitCrypt encryption, and kustomization validation. [APE-126]
7. **Automated Prisma schema governance agent** (Sukalya Rajendran, 4/29) — GitHub Actions detects schema changes, generates ERD and Snowflake DDL, triggers DBT developer agent for pipeline creation. [APE-281]
8. **EKS governance automation** (Deepti Pathak, 5/6) — Scheduled GitHub Actions workflow scans cluster/add-on version drift, auto-creates Jira tickets, and sends Slack alerts. [APE-294]
9. **AI enablement curriculum for CodeMie and GitHub Copilot** (Jason Daggs, 5/6) — 7-session hands-on curriculum for non-developer team members; published to Confluence for cross-team adoption. [APE-278]
10. **PR reviewer and code optimizer agent for Python/Spark/Snowflake** (Sanjay Parsi, 5/13) — Four review modes (quality, performance, cost, combined) with severity-ranked summary tables; published in shared GitHub repo. [APE-308]
11. **Custom MCP server for Jira integration in Claude Code** (Jason Daggs, 5/13) — FastMCP server exposes Jira tools (active sprint, open issues, JQL search) callable via natural language in Claude Code. [APE-1058]
12. **AI-powered L1 support pipeline failure alert system** (Uda, Balanarasimha Rao, 5/20) — Event-driven Lambda + Azure OpenAI pipeline running live in production: detects Step Function failures, generates structured RCA, caches repeat errors, sends SNS email reports. [APE-282]
13. **Slack webhook integration for operational notifications** (Deepti Pathak, 5/20) — Webhook integrated into EKS alerting pipeline with full Confluence setup guide; used in production. [APE-1057]
14. **Figma MCP multi-repo code generation with CX design system enforcement** (Vazgen Ayrapetyan, 5/27) — Workspace skill pulls Jira ticket → reads Figma designs → maps CX design tokens → generates code and PRs across multiple repos with Optimizely A/B flag. [APE-1465]
15. **GitHub release notes generation workflow** (Shoaib Naseem, 6/3) — CodeMie workflow batches PR/Jira diff between tags and publishes formatted release notes directly to GitHub Releases; used for real SIAM production release. [APE-1028]
16. **GitHub MCP in IntelliJ for local AI-driven PR code review** (Amit Kumar, 6/3) — Pulls PR review comments into IDE, applies Copilot fixes locally, then pushes; team instructions shared via private GitHub repo. [APE-112]
17. **Multi-agent changelog workflow linking PRs, commits, and Jira tickets** (Jason Daggs, 6/10) — 4-node CodeMie workflow generates auditable markdown changelogs for multi-team release communication.
18. **JIRA-triggered audit documentation automation** (Deepti Pathak, 6/10) — JIRA transition triggers CodeMie assistant and GitHub Actions to generate and commit four mandatory audit documents per ticket; resolves a recurring compliance gap.
19. **Dependabot risk classification agent** (Loquen MeyersJones, 6/10) — Slash-command agent for Cursor and GitHub Copilot analyzes dependency upgrade PRs and outputs structured risk assessments with evidence for 48 open tickets.

---

### Used for Experimentation

Use cases where AI tools were explored to investigate capabilities or validate approaches — proofs of concept and work-in-progress investigations not yet applied to production tasks.

1. **Spec-driven development pattern and reusable GitHub Copilot agent repository** (Ravi Nachimuthu, 4/8) — Explored the shift from prompt-based to specification-driven development; shared a private repo with custom agents (MuleSoft-to-GraphQL migration agents were still work in progress at time of demo).
2. **Slack MCP server proof of concept** (Deepti Pathak, 5/20) — POC of a local Slack MCP server in VS Code demonstrating bot token scopes, channel messaging, and AI-assisted interactive notification potential — not yet integrated into a production workflow.
