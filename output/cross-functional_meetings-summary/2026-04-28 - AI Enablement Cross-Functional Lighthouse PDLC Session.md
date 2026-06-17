# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 28, 2026
**Duration:** 56m 2s
**Presenters:** Nikita Kumar, Vlad Grubman, Svetlana Stogni

---

## Meeting Title

AI Enablement: Cross-Functional Use Case Collection — Teams Share Pain Points and Priorities

---

## Short Description

This session was a structured collection exercise where Lighthouse team members presented the AI use cases they identified since the previous session. The conversation focused on understanding what problems AI should solve rather than prescribing tools, with Vlad and Nikita guiding teams away from siloed, function-specific ideas toward cross-functional workflows spanning digital, dev, and QA. Several concrete use cases were captured, ranging from product prioritization signals to data pipeline automation and documentation standardization.

---

## Key Points / Topics

### Program Context

- Teams were explicitly asked to think cross-functionally — use cases should flow across at least two functions (e.g., product → QA, dev → testing, digital → dev).
- Emphasis on crawl-walk-run: start with simple, high-value use cases before tackling large-scale automation.
- Vlad: "We want to give you the tools to go build it yourselves — we can't always access your PII or financial data, but we can teach you the agentic patterns."

### Use Cases Presented

**Joshua Smith — Product Prioritization "Second Brain"**
- Synthesize signals from analytics, customer research, and product reviews to prioritize what to build next.
- Recognized as a compelling but complex goal; agreed to break it down: start with a single data source agent before connecting multiple sources.
- Vlad confirmed this is an ideal long-term agentic use case but requires understanding agent orchestration first.

**Lisa Ruby — QA Test Case Generation (Cross-Functional Clarification)**
- Already using Rovo + Copilot to generate test cases from Jira stories; reducing manual test case creation from ~2 days to ~1 day.
- Struggling with non-standard processes across different product types.
- Identified use case: a **requirements hardening agent** that pre-validates stories before they reach QA — checking completeness, acceptance criteria, and testability.
- Lisa is working toward a standardized QA workflow using CodeMie for story readiness and definition of done checking.

**Sukalya Rajendran — Data Factory Platform Team (Multiple Use Cases)**
- **Data validation agent**: post-pipeline execution, fires off custom validation rules per task type.
- **L1 support agent**: analyzes pipeline failure logs, identifies root cause, suggests action items — human-in-the-loop required before any action.
- **End-to-end automated development flow**: Jira creator → CodeMie orchestrator → DBT Developer Agent (GitHub Copilot custom agent) → DBT compile check → PR creation.
- **Code optimization agent**: connects to GitHub repos, suggests optimizations based on OMF standards.
- **AI use case registry and AI mentor chatbot**: indexes all AIPDLC Confluence documentation; allows new Lighthouse teams to query it like a chatbot during onboarding.

**Jason Daggs — Guardians Team CodeMie Training Curriculum**
- Created a 7-session CodeMie training program for the Guardians team covering all major platform features.
- Goal: ensure all team members (including non-coders and QA) can use CodeMie to automate their own tasks.
- Designed to generate additional use case ideas organically as team members learn the tool.
- Posted the internal Confluence page in chat for feedback.

**Bandana Sriramka — Sprint Regression Prioritization Agent**
- Proposes an agent to predict which components or features are most likely to fail during a sprint.
- Inputs: code review diffs, historical defect data.
- Output: prioritized list of areas for QA to focus on.
- Cross-functional: bridges development (code changes) and QA (test prioritization).

**Debamitra Bhattacharjee — Middleware & ETL Automation**
- Automate regression testing for middleware services as part of the CI/CD pipeline (benefits both QA and dev).
- Snowflake ETL data validation agent: no current CodeMie–Snowflake integration; team exploring alternatives.
  - Playwright noted as an upcoming CodeMie integration; Snowflake not yet on the priority list (GitHub, Figma, Atlassian prioritized first).
- Observation: team is succeeding with AI for documentation but struggling with execution/automation; seeking help bridging that gap.

**Heath Fest — Standardized Documentation as AI Foundation**
- Proposes standardizing documentation for (1) data facts/dimensions/measurements, (2) processes, and (3) system interactions as a prerequisite for AI to be effective.
- Argues that scattered, undocumented processes prevent AI agents from understanding business context — "you can't AI what you can't explain."
- Advocates for a shared, living documentation standard that could later feed into a "second brain" or system-context hub.

**Jatin Bagga — MCP/Atlassian Integration for Jira Story Push**
- Asked whether ChatGPT or CodeMie can push generated content (stories, epics) directly into Jira.
- Vlad: MCP servers for Atlassian will enable this bidirectional flow; CodeMie already supports it today; Cursor lacks the connector.
- CodeMie confirmed: can create and modify Jira content including assigning to existing epics.

### Session Notes

- All use cases noted and will be organized from simple to complex for upcoming hands-on sessions.
- Goal for Thursday: more cross-functional use cases covering at least two functions.
- Cross-functional use case identification guide shared in chat.
