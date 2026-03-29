from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def main_agent(state):
    perspective = state.get("perspective", "General")

    if "input_texts" in state:
        texts = state["input_texts"]
        return {"output": handle_evolution(texts, perspective)}
    else:
        text = state["input_text"]
        return {"output": handle_single(text, perspective)}


# -------------------- SINGLE --------------------
def handle_single(text, perspective):

    prompt = f"""
User type: {perspective}

Avoid obvious statements.
Each insight must add new interpretation or meaning.
Focus on implications, not description.

Return ONLY valid JSON.

{{
  "summary": [],
  "insights": [],
  "timeline": {{
    "past": "",
    "present": "",
    "future": ""
  }},
  "questions": [],
  "why_it_matters": "",
  "meta_analysis": {{
    "story_type": "",
    "impact_level": "",
    "stakeholders": {{
      "winners": [],
      "losers": []
    }},
    "signal_strength": ""
  }}
}}

News:
{text}
"""

    return call_llm(prompt, text)


# -------------------- EVOLUTION --------------------
def handle_evolution(texts, perspective):

    combined = "\n\n".join(
        [f"Update {i+1}: {t}" for i, t in enumerate(texts) if t.strip()]
    )

    prompt = f"""
User type: {perspective}

Analyze how this story evolves across updates.

Avoid obvious statements.
Each insight must add interpretation.
Focus on narrative shift and implications.

Return ONLY valid JSON.

{{
  "summary": [],
  "insights": [],
  "story_evolution": {{
    "phases": [
      "Initial trigger",
      "Reaction phase",
      "Impact phase"
    ],
    "shift": "",
    "trend": ""
  }},
  "questions": [],
  "why_it_matters": "",
  "meta_analysis": {{
    "story_type": "",
    "impact_level": "",
    "stakeholders": {{
      "winners": [],
      "losers": []
    }},
    "signal_strength": ""
  }}
}}

Updates:
{combined}
"""

    return call_llm(prompt, combined)


# -------------------- SAFE LLM CALL --------------------
def call_llm(prompt, fallback_text):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )

        content = response.choices[0].message.content

        if not content:
            return fallback_response(fallback_text)

        content = content.strip()
        content = content.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(content)
        except:
            print("Bad JSON received:")
            print(content)
            return fallback_response(fallback_text)

    except Exception as e:
        print("API Error:", e)
        return fallback_response(fallback_text)


# -------------------- FALLBACK --------------------
def fallback_response(text):
    return {
        "summary": [text[:100]],
        "insights": ["Fallback response"],
        "timeline": {"past": "", "present": "", "future": ""},
        "questions": [],
        "why_it_matters": "Unable to analyze importance",
        "meta_analysis": {},
        "story_evolution": {}
    }