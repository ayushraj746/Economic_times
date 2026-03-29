# AI Story Arc Tracker

Transforming news from static articles into structured intelligence.

---

## Problem

Today’s news consumption is broken.

* Static articles
* Same format for every user
* No continuity across updates
* No clarity on why a story matters

Even after reading multiple articles, users still struggle to understand:

* What actually changed
* Why it matters
* What happens next

---

## Solution

AI Story Arc Tracker converts raw news into structured, actionable intelligence.

Instead of just summarizing news, it provides:

* Deep insights (non-obvious interpretation)
* Timeline (past → present → future)
* Intelligent follow-up questions
* “Why this matters” (decision layer)
* Meta-analysis (impact, winners, signal strength)
* Story evolution across multiple updates

---

## Core Features

### 1. Single Article Intelligence

Input a news article and get:

* Bullet-point summary
* Deep insights
* Timeline (past, present, future)
* Key questions
* Why this matters
* Meta analysis:

  * story_type
  * impact_level
  * winners / losers
  * signal_strength

---

### 2. Story Evolution Tracker (Key Feature)

Track how a story evolves across multiple updates:

* Trigger → Reaction → Impact phases
* Narrative shift detection
* Overall trend analysis
* Cross-update insights

This goes beyond traditional news reading.

---

### 3. Perspective-Based Personalization

The system adapts based on user role:

| Mode     | Focus                      |
| -------- | -------------------------- |
| General  | Balanced understanding     |
| Investor | Market impact, risks       |
| Founder  | Opportunities, competition |
| Student  | Simplified explanations    |

---

## Architecture

```
User Input
   ↓
Streamlit UI
   ↓
LangGraph Workflow
   ↓
Main Agent
   ↓
Groq LLM (LLaMA 3.1)
   ↓
Structured JSON Output
   ↓
Rendered UI
```

---

## Tech Stack

* Frontend: Streamlit
* Backend: LangGraph
* LLM: Groq (LLaMA 3.1-8B-Instant)
* Language: Python

---

## How to Run

```bash
git clone <your-repo-link>
cd ai-news-tracker
pip install -r requirements.txt
streamlit run app.py
```

---

## Environment Variables

Create a `.env` file:

```bash
GROQ_API_KEY=your_api_key_here
```

---

## Impact

Traditional news:

* ~15 minutes per story

AI Story Arc Tracker:

* ~2 minutes

This results in ~85% time savings per story.

At scale (10,000 users/day):

* ~130,000 minutes saved daily
* Increased engagement and retention

---

## What Makes This Unique

* Not just summarization
* Structured intelligence system
* Story evolution tracking
* Perspective-aware outputs
* Decision-focused insights

---

## Future Scope

* Real-time news ingestion
* Story memory using vector databases
* Long-term narrative tracking
* Multi-modal outputs (video, charts)

---

## Author

Ayush Raj

---

## Final Note

AI Story Arc Tracker is designed to move beyond information delivery and focus on understanding, context, and decision-making.
