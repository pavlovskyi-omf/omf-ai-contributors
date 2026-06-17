# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** April 30, 2026
**Duration:** 57m 19s
**Presenters:** Nikita Kumar, Eugene Semenyuk, Oleksandr Pavlovskyi

---

## Meeting Title

AI Enablement: Understanding Cross-Functional Use Cases — Framework, Patterns, and PDLC Collision Points

---

## Short Description

Eugene Semenyuk delivered an interactive presentation defining what cross-functional AI use cases are and how to identify them. The session introduced a practical framework built around PDLC handoffs, collision points, and two core strategies: connecting existing functional use cases into a shared flow, or expanding a single use case to incorporate multiple team perspectives. Teams engaged in guided discussion to identify quick wins and a pattern for turning functional ideas into cross-functional pilots.

---

## Key Points / Topics

### What Is a Cross-Functional Use Case?

- Definition: an AI output that helps more than one function make a better or shared decision.
- Three lenses: **Digital** (business intent, acceptance criteria), **Engineering** (implementation, architecture, technical risk), **QA** (testability, coverage, quality risk).
- Key phrase: multiple perspectives + shared decision + better handoff.

### Two Strategies for Cross-Functional Value

1. **Connect existing functional use cases into a PDLC flow**
   - Example: requirements hardening → implementation plan → test case creation.
   - Each use case is useful alone; connecting them produces a smoother handoff and less rework.
   - Starter pattern: story analyzer used by digital to check requirements can also feed engineering subtask creation and QA scenario generation.

2. **Shape one use case with multiple perspectives**
   - Example: requirements hardening reviewed by all three functions simultaneously.
   - Digital asks: is the intent clear? Engineering asks: is it feasible? QA asks: is it testable?
   - Turns a single functional check into a consolidated readiness decision.

### Three Complexity Levels

| Level | Description | Example |
|---|---|---|
| Simple | One artifact, multiple perspectives | Requirements readiness reviewed by digital, engineering, and QA |
| Medium | Multiple artifacts, one workflow step | PR review using diff, linked stories, and task context |
| Complex | Multiple PDLC steps connected end-to-end | Requirements → implementation subtasks → test cases → release readiness |

### PDLC Handoff Points (Best Opportunities)

- Handoffs between functions (idea → requirement → dev → PR → QA → release → production) are where context gets lost and problems appear.
- Common pain point identified by team: requirements stage (ambiguous acceptance criteria causing rework downstream).
- Key insight: "Instead of asking 'what AI idea can we invent?', ask 'where do we lose context in the PDLC?'"

### Existing Building Blocks (Already Available)

- **Pattern 1 — Requirements to Plan to Test:** story analyzers, definition of ready/done validation, implementation plans as subtasks, test design.
- **Pattern 2 — PR Review + Task Recommendation:** code review, PR checklist, Jira updates, PR analysis, recommended follow-up tasks.
- **Pattern 3 — Release Readiness:** release notes, demo scripts, Jira-based docs, version linking, deployment validation.

### Identification Framework (5 Questions)

For any existing functional use case, ask:
1. Who consumes the output?
2. Is there a handoff?
3. What is found too late?
4. What artifacts are needed?
5. Whose perspective is missing?

If two or more answers point beyond one function → treat it as a cross-functional candidate.

### Collision Points

- A collision point is where multiple functions care about the same artifact but ask different questions.
- Example — **requirements hardening**: digital (is it unclear?), engineering (is scope feasible?), QA (is it testable?) → shared decision: is this story ready to build?
- Example — **PR review**: engineering (is code sound?), digital (what behavior may change?), QA (what tests are needed?) → shared decision: is this PR ready to merge and test?

### Discussion Highlights

- **Joshua Smith**: Requirements hardening before dev starts is the single biggest cross-functional opportunity because so many downstream activities depend on it.
- **Jason Daggs**: Requested the slide deck to present the framework to his Guardians team as a use-case solicitation tool.
- **Heath Fest + Jason Daggs**: Argued that documentation and system context (a "constitution") must come before requirements hardening — if processes aren't documented, AI cannot understand them.
- **Alfredo Achecar**: Noted that digital teams also have large customer discovery / voice-of-customer use cases that extend beyond the digital-dev-QA triangle; acknowledged these will be addressed in individual Lighthouse sessions.
- **Patrick Behnke**: Raised concern about forcing AI into places where it doesn't add value; Filippo Morelli responded that the goal is reimagining work, not adding AI for its own sake.

### Next Steps

- Champions call to follow: AI champions in each team will work with the enablement team to identify pain points and propose cross-functional pilots.
- Requirements hardening flagged as the most accessible quick win across all teams.
- Eugene's presentation deck to be shared with all participants.
