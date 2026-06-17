# AI Enablement: Cross-Functional Lighthouse PDLC Session

**Date:** May 7, 2026
**Duration:** 1h 31m 4s
**Presenters:** Nikita Kumar, Eugene Semenyuk

---

## Meeting Title

AI Enablement: Building the Cross-Functional Requirements Review Flow — Jira Automation with Rovo Agents (Part 1)

---

## Short Description

Eugene Semenyuk led the first hands-on session building a cross-functional automated requirements review flow directly in Jira Automation. The flow triggers when a user story transitions from "To Do" to "In Progress" and invokes a digital story reviewer Rovo agent, posting the review as a Jira comment. Participants followed along creating their own automation flows in the training Jira sandbox. The session ended with the digital review step working end-to-end; QA and engineering review steps were deferred to the next session.

---

## Key Points / Topics

### Session Goals

- Build a cross-functional user story review flow that automatically reviews a story from three perspectives (digital, QA, engineering) when it moves to in-progress.
- Make the review fully autonomous: triggered by a Jira status change, no manual initiation required.

### Live Demo of the Completed Flow

Eugene demonstrated the finished target state before rebuilding it from scratch:
- **Trigger**: work item transitions from "To Do" to "In Progress."
- **Step 1 (Digital review)**: a Rovo agent reviews the story from a business/digital perspective and posts a comment.
- **Step 2 (QA review)**: a testability analysis Rovo agent reviews and posts a comment.
- **Step 3 (Engineering review)**: a webhook call to a CodeMie agent analyzes technical feasibility against the actual codebase and posts a comment.
- **Step 4 (Cross-functional summary)**: a final Rovo agent reads all three comments and produces a consolidated recommendation with an executive summary, key concerns, and a readiness verdict.

Sample output observed: verdict "Proceed with Caution," confidence 75%, with impacted modules, required changes, and critical assumptions listed.

### Hands-On: Building the Flow from Scratch

**Trigger configuration**
- Navigate to Jira Space Settings → Automation → Create Flow → Create from Scratch.
- Select trigger: **Work Item Transitioned** (from To Do → In Progress).

**Adding a User Condition**
- Condition: Reporter = current user (limits the flow to only items you created, preventing accidental triggering on others' work).
- User ID must be pasted as a raw identifier (found in Jira profile URL); dropdown search available for users in the same domain.

**Adding the First Agent Step**
- Action: **Use Agent** → select the Digital Story Reviewer agent.
- Prompt: "Review this user story."
- Agent response is stored in the `{{agentResponse}}` variable automatically.

**Adding the Comment Step**
- Action: **Comment on Work Item**.
- Paste `{{agentResponse}}` into the comment body using the "copy response" button.
- Recommendation: uncheck "Prevent duplicates" to allow reruns during testing.

**Saving and Naming the Flow**
- Flow details → provide a personal name (e.g., "Requirements Review Flow — [Name]") to distinguish from others in the shared sandbox.

### Key Concepts Clarified

- **Variables in Jira Automation**: `{{agentResponse}}` is a built-in variable; the last agent's output always overwrites it. Use a **Create Variable** step immediately after each agent if you need to preserve multiple responses independently.
- **No Actions Performed** in audit log = workflow triggered but condition evaluated false for that item (expected behavior when others change their items).
- **Rovo agents in Jira Automation cannot use skills** — they can analyze and respond, but cannot take actions. The comment step bridges this limitation.
- **Step counter (2/65)**: Jira Automation limits flows to 65 steps per rule.

### Participant Issues and Resolutions

- Missing "Space Settings" in sidebar → user not yet added as project admin; Nikita added participants in real time via email.
- Profile page navigation opening new tab and losing unsaved flow → use right-click "open in new tab" for profile lookups.
- User ID not found in dropdown → paste raw ID from Jira profile URL; available to all.
- Flow not found after navigation away → Jira auto-saves drafts; click "New Automation" and the draft appears.
- Question about Power Automate vs Jira Automation → deferred to Friday office hours.

### Session Notes

- Session ended at the one-hour mark with the digital review step working.
- Next session (Thursday): add QA agent and engineering agent (CodeMie webhook) steps to complete the flow.
- Friday open hours: available for debugging and troubleshooting.
- Participants who missed this session: clone Eugene's existing flow from the sandbox and change the reporter condition to your own user ID before resuming.
