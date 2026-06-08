# AI Enablement ENGINEERING — Lighthouse Session Scores
**Session:** AI Enablement ENGINEERING Lighthouse Session
**Date:** April 15, 2026
**Duration:** 37m 10s
**Scored by:** score-meeting skill (OMF Phase 2 Recognition Rules)
**Evidence tickets:** [APE-113](https://onemainfinancial.atlassian.net/browse/APE-113) · [APE-264](https://onemainfinancial.atlassian.net/browse/APE-264)

---

## Lighthouse - AI Hours Sessions

| Name | Date | Contribution | Score |
|---|---|---|---|
| John Zimmerman | 4/15/2026 | **Why he stood out:** Demonstrated how AI can replace domain expertise for navigating complex data files — used Copilot to discover field names and extract targeted test account sets without any prior knowledge of the indicator file's schema.<br><br>**Significant contributions:**<br>- Uploaded the integration/UAT indicator file to Copilot and used natural-language prompts to identify bankruptcy fields (BK-CH07) and direct-pay flags (DP) without knowing any column names in advance — confirmed accurate live.<br>- Generated two complete filtered CSV files: one for Chapter 7/13 bankruptcy accounts, one for non-direct-pay accounts with balance > 0; output validated and Jira ticket APE-113 closed as Done.<br>- Identified a path toward a reusable script/agent that can serve recurring test data needs across releases, reducing effort for common regression scenarios.<br><br>**Contribution:** Demo / Use Case: demoed AI-assisted extraction of targeted test accounts from the indicator file using Copilot natural-language prompts ([APE-113](https://onemainfinancial.atlassian.net/browse/APE-113), Done). | 5 |
| Amit Sharma | 4/15/2026 | **Why he stood out:** Built a fully autonomous end-to-end agent that eliminates the manual Glue job bottleneck for Snowflake Iceberg table testing — going from DDL input to validated parquet output in S3 without manual steps.<br><br>**Significant contributions:**<br>- Designed an agent workflow that parses a Snowflake CREATE TABLE statement, maps Snowflake-to-Spark types, generates a Glue job script, deploys it to S3, and executes and monitors it via Boto3 — all autonomously, demonstrated live to completion (91 seconds, 10 parquet rows validated).<br>- Used CodeMe to generate and refine the agent prompt, incorporating a prior manually-created Glue job as reference to ensure realistic output; ran the agent live end-to-end with Glue job creation, execution, and S3 parquet validation shown.<br>- Eliminated the per-table manual effort of creating individual Glue jobs for dummy data generation; Jira ticket APE-264 closed as Done with documentation linked.<br><br>**Contribution:** Demo / Use Case: demoed an agent that generates parquet dummy data for Snowflake Iceberg tables from CREATE TABLE statements ([APE-264](https://onemainfinancial.atlassian.net/browse/APE-264), Done). | 5 |
| Sukalya Rajendran | 4/15/2026 | **Why she stood out:** Added immediate practical value to John's demo by connecting it to a Snowflake-native alternative — offering a simpler path for data-adjacent teams already working in Snowflake Dev.<br><br>**Significant contributions:**<br>- Suggested loading the indicator CSV into Snowflake and using Snowflake Cortex — the platform's NLP/AI feature — to query the data directly without writing SQL.<br>- Highlighted that Cortex enables natural-language questions on the data, mirroring the Copilot experience but inside the Snowflake environment.<br>- Offered to share the Snowflake Dev access role name to help John's team try the approach.<br><br>**Contribution:** Use case sharing activity: shared Snowflake Cortex as a data-native alternative for natural-language querying of test account data. | 1 |
| Praveen Lakshman | 4/15/2026 | **Why he stood out:** Raised a critical data security question that established the compliance guardrails for AI-assisted data workflows in front of the full group.<br><br>**Significant contributions:**<br>- Asked whether the indicator file contained real customer data or scrambled test data, drawing a clear data security boundary for using Copilot with this file type.<br>- Highlighted that data could become public when processed through tools like Copilot, prompting explicit confirmation from the presenter.<br>- Reinforced the compliance-first mindset relevant to anyone considering similar approaches with customer-adjacent data.<br><br>**Contribution:** Active participation: raised the data security clarification confirming all data used was scrambled test data, not real customer data. | 1 |
| Jason Daggs | 4/15/2026 | **Why he stood out:** Actively engaged during Amit's demo and explicitly named how the use case was generating ideas for his own team's work — an early adoption signal for the dummy data agent approach.<br><br>**Significant contributions:**<br>- Affirmed the practical value of Amit's agent implementation and noted it was giving him concrete ideas.<br>- Engaged during the live Q&A phase of the demo, contributing to the discussion.<br>- Signaled interest in applying similar agent-based approaches within his own team context.<br><br>**Contribution:** Active participation: engaged with Amit's dummy data agent demo and cited specific relevance for his own team's use cases. | 1 |
| Allen Truban | 4/15/2026 | **Why he stood out:** Engaged directly when asked about his team's workflow, providing honest context about their Snowflake usage to help assess applicability of the session's approaches.<br><br>**Significant contributions:**<br>- Responded to direct questions about his team's Snowflake usage, clarifying they run queries but not Glue-style workflows.<br>- Contributed context that helped frame the scope of applicability for Amit's dummy data agent.<br>- Stayed engaged through both demo discussions.<br><br>**Contribution:** Active participation: engaged with session discussion about team's Snowflake query workflows in relation to the demos presented. | 1 |

---

## Score Summary

| Name | Score | Level | Evidence |
|---|---|---|---|
| John Zimmerman | **5** | D2 — Working | APE-113 (Done), live demo |
| Amit Sharma | **5** | D2 — Working | APE-264 (Done), live demo |
| Sukalya Rajendran | **1** | Use-case sharing | Transcript |
| Praveen Lakshman | **1** | Active participation | Transcript |
| Jason Daggs | **1** | Active participation | Transcript |
| Allen Truban | **1** | Active participation | Transcript |

---

## Upgrade Flags

- **Amit Sharma** — Currently D2 (5 pts). Jason Daggs explicitly said the demo was giving him ideas; if his team adopts the agent or a time-saved metric is documented, this qualifies for **D3 (10 pts)**. Track adoption in APE-264 or a follow-up ticket.
- **John Zimmerman** — Currently D2 (5 pts). If the Copilot-generated script is saved and generalized into a reusable agent/tool for common test data scenarios, this could qualify for **D3 (10 pts)** with reuse evidence.
