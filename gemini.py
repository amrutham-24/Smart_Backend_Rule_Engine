import os
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# -----------------------------------
# Load .env safely (absolute path)
# -----------------------------------
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found. Check your .env file.")

# -----------------------------------
# Create Gemini client
# -----------------------------------
client = genai.Client(api_key=API_KEY)

# -----------------------------------
# NLP → JSON rule generator
# -----------------------------------
def generate_rule_from_text(text: str) -> dict:
    """
    Converts natural language text into structured rule JSON.
    """

    if not text or not isinstance(text, str):
        raise ValueError("Input text must be a non-empty string.")

    prompt = f"""
You are a backend rule extraction engine.

Convert the sentence below into VALID JSON ONLY.
Do NOT add explanations.
Do NOT add markdown.
Return RAW JSON.

Sentence:
{text}

JSON format:
{{
  "rule_id": "auto_generated",
  "event": "attendance_updated",
  "conditions": [
    {{
      "field": "attendance",
      "operator": "<",
      "value": 75
    }}
  ],
  "action": "block_hall_ticket"
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        output_text = response.text.strip()

        return json.loads(output_text)

    except json.JSONDecodeError:
        raise ValueError(
            "❌ Gemini returned invalid JSON.\n"
            f"Raw output:\n{output_text}"
        )

    except Exception as e:
        raise RuntimeError(f"Gemini error: {e}")
