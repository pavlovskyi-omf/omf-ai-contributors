# Score Meeting Participants

Score AI Champions session participants from a meeting transcript using the OMF Phase 2 Recognition Program rules, then output a structured table ready to copy into the Confluence Engineering Phase 2 page.

## How to use this skill

Invoke with: `/score-meeting`

You will be asked to paste (or provide the path to) a meeting transcript. The skill will:
1. Identify all named participants and their contributions
2. Classify each contribution and assign points using the scoring rules below
3. Produce two formatted tables — **AI Champions Sessions** and **Lighthouse - AI Hours Sessions** — matching the Engineering Phase 2 Confluence template

---

## Scoring Rules (from [WiP] Recognition Program for Phase 2+)

### Point Values

| Category | Points | Who grants |
|---|---|---|
| Active participation (spoke up, moved session forward) | 1 | auto |
| Use-case sharing / working on a use case between sessions | 1 | auto |
| Demo **D1 — Explored** (hands-on attempt on own real work, may be rough) | 2 | coach |
| Demo **D2 — Working** (functioning end-to-end, reproducible, concrete output) | 5 | coach |
| Demo **D3 — Impactful/Reusable** (D2 + reuse, adoption, or measured metric) | 10 | coach |
| Solved-Problem (D3 + real named problem resolved, needs second validator) | 15 | coach + validator |

### Demo Level Criteria

**D1 — Explored**
- Genuine hands-on attempt on the person's own real work (not a generic tool tour)
- Shown live or recorded; builder explains approach and what they learned
- May be rough, partial, or unsuccessful — the attempt counts

**D2 — Working**
- Functioning use case that does a real task end-to-end and is reproducible by the builder
- Shows concrete output; another person could follow the steps

**D3 — Impactful / Reusable**
- Clears D2 AND value extends beyond the builder via at least one of:
  - **Reuse** — published artifact others can run
  - **Adoption** — at least one teammate is using it
  - **Measured impact** — a real metric (time saved, defects, cycle time, etc.)

**Solved-Problem**
- Clears D3 AND resolved a real, named problem (merged PR, resolved ticket, manual process replaced, measurable outcome)
- Requires a second validator who is NOT the builder

### Key Rules
- Grade to the **highest** level whose bar is cleared
- Evidence required for D-level and Solved-Problem (no evidence → not qualified)
- Demos must be witnessed live or submitted as recording — not self-asserted
- Grade to the bar, not the person — seniority/role does not raise a demo's level
- When in doubt, grade down and invite a level-up next session

---

## Output Template

Produce output in this exact structure (matches Engineering Phase 2 Confluence page):

### Session Type Detection
- **AI Champions Sessions / Sync Up** → use the "AI Champions Sessions" table format
- **Lighthouse / AI Hours** → use the "Lighthouse - AI Hours Sessions" table format
- If the session contains both types of contributions, produce both tables

---

### AI Champions Sessions Table Format

```
| Name | Date | Activity | Score |
|---|---|---|---|
| [Full Name] | [Session Date] | **Why they stood out:** [1-2 sentences]<br><br>**Significant contributions:**<br>- [contribution point 1]<br>- [contribution point 2]<br>- [contribution point 3]<br><br>**Contribution:** [Use case sharing activity / Demo / Use Case — brief one-line summary] | [score] |
```

### Lighthouse - AI Hours Sessions Table Format

```
| Name | Date | Contribution | Score |
|---|---|---|---|
| [Full Name] | [Session Date] | **Why they stood out:** [1-2 sentences]<br><br>**Significant contributions:**<br>- [contribution point 1]<br>- [contribution point 2]<br>- [contribution point 3]<br><br>**Contribution:** [Demo / Use Case — brief one-line summary] | [score] |
```

---

## Instructions for Claude

When this skill is invoked:

1. **Ask the user** to paste the meeting transcript or provide a file path.
2. **Parse the transcript** to extract:
   - Session date and session type (Champion Sync Up, Lighthouse, AI Hours, etc.)
   - Every named participant who spoke or contributed
   - The nature of each person's contribution
3. **Score each participant** using the rules above:
   - If they only asked questions or commented → 1 pt (active participation)
   - If they shared a use case idea or work-in-progress → 1 pt (use-case sharing)
   - If they showed/described a hands-on attempt on real work → D1 = 2 pts
   - If they demoed a working end-to-end reproducible use case → D2 = 5 pts
   - If the demo is reusable/adopted/has measured impact → D3 = 10 pts
   - If it solved a real named problem with evidence → Solved-Problem = 15 pts
   - When a participant both shared AND demoed, award the **higher** score only (demo levels are additive to participation only when they are separate events)
4. **Write the Activity/Contribution cell** following the template format:
   - Start with "**Why they stood out:**" — one or two sentences on their unique value
   - Then "**Significant contributions:**" — three distinct contribution points from the transcript
   - Then "**Contribution:**" — a short label: `Use case sharing activity`, `Demo / Use Case`, etc., followed by a one-line summary
5. **Output** the completed table(s) in markdown, ready to paste into Confluence.
6. **Flag** any participants where evidence was unclear and the score could be upgraded with more evidence (e.g., "Note: [Name] may qualify for D2 if a recording is available").

---

## Example Output

**Session:** AI Champion Sync Up: Engineering — 2026-04-13

**AI Champions Sessions**

| Name | Date | Activity | Score |
|---|---|---|---|
| Patrick Behnke | 4/13/2026 | **Why he stood out:** Shared multiple practical engineering use cases across platform, code, docs, and testing.<br><br>**Significant contributions:**<br>- Shared AI-assisted JIRA ticket creation workflows.<br>- Described OpenShift config generation with validation and secret handling.<br>- Highlighted AI-based plugin, documentation, and test generation for NTS2.<br><br>**Contribution:** Use case sharing activity: shared ideas for PR change summaries, onboarding doc updates, and incident dashboard creation. | 1 |
| Anjali Pabbareddy | 4/8/2026 | **Why she stood out:** Delivered a practical engineering demo with clear time savings and reuse potential.<br><br>**Significant contributions:**<br>- Built an impersonation feature for non-prod testing using GitHub agent prompts.<br>- Reduced build time from 2–3 days to ~1.5 hours.<br>- Generated reusable documentation for rollout to other apps.<br><br>**Contribution:** Demo / Use Case: demoed an AI-built impersonate-user feature for faster testing across portfolio applications. | 2 |
