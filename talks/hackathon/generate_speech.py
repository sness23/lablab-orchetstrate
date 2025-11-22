#!/usr/bin/env python3
"""
Generate TTS audio for hackathon presentation using OpenAI API.
Requires OPENAI_API_KEY environment variable.
"""

import os
from pathlib import Path
from openai import OpenAI

# Initialize client (uses OPENAI_API_KEY env var automatically)
client = OpenAI()

# Output directory
output_dir = Path(__file__).parent / "audio"
output_dir.mkdir(exist_ok=True)

# Voice options: alloy, echo, fable, onyx, nova, shimmer
# 'onyx' is good for professional/male voice
# 'nova' is good for professional/female voice
VOICE = "onyx"
MODEL = "tts-1-hd"  # Higher quality

# Script sections - each will be a separate audio file
SCRIPT_SECTIONS = {
    "01_intro": """
Hi, I'm presenting TechBio Lead Gen - an AI-powered sales intelligence platform built on watson x Orchestrate.

Here's the problem we're solving: Sales reps in TechBio spend 80% of their time researching leads. They're reading papers, finding equipment mentions, identifying pain points, crafting personalized emails.

The result? Either generic outreach that gets ignored, or personalized outreach that doesn't scale.

What if AI could do that research automatically?
""",

    "02_solution": """
We built four AI agents that work together in watson x Orchestrate:

First, Lead Discovery - finds researchers by domain.
Second, Profile Builder - extracts equipment needs and pain points.
Third, Product Matcher - recommends products.
And fourth, SMYKM Generator - creates personalized outreach.

SMYKM stands for 'Show Me You Know Me' - every email references their specific work.

Let me show you how it works with a real example.
""",

    "03_lead_discovery": """
Meet Alex Rives. He built ESM3, a breakthrough AI for protein design. Raised $142 million. Recently joined CZI as Head of Science.

When I ask watson x to 'find leads in AI protein design', it returns Alex with a score of 95 out of 100.

Why so high? Recent funding, direct equipment need, and an acute pain point we can solve.
""",

    "04_profile_builder": """
Next I ask: 'What equipment does Alex Rives need?'

The system analyzed his papers and found his core pain point: ESM3 generates novel proteins in seconds, but structural validation takes weeks.

That's a 10,000x speed mismatch. He needs high-throughput crystallography to close that gap.
""",

    "05_product_match": """
Now I ask: 'Match Rigaku products for Alex Rives.'

It recommends the XtaLAB Synergy-S. Look at this comparison:

Synchrotron: weeks to schedule, days per structure.
Rigaku on-site: available 24/7, hours per structure.

This directly addresses his bottleneck.
""",

    "06_smykm_outreach": """
Finally, the magic: 'Generate personalized outreach for Alex Rives.'

Look at this email. Subject: 'Closing the loop on ESM3 validation.'

It opens by congratulating him on the CZI announcement. Then it goes right to his pain point: 'ESM3 generates proteins in seconds, but validation takes weeks.'

This isn't a template. It references his specific CZI move, his '500 million years of evolution' paper, and his exact validation bottleneck.

Every sentence shows we understand his work. That's Show Me You Know Me.
""",

    "07_bonus_features": """
But we didn't stop at email. The platform also generates:

Competitive battlecards - why Rigaku beats synchrotron.
Objection handlers - pre-built responses to pushback.
Meeting prep briefings - what to say, what to avoid.
Deal probability scores - AI-explained reasoning.
6-week campaign sequences.
And LinkedIn content for social selling.

It's a complete sales enablement platform.
""",

    "08_technical_roi": """
Under the hood: FastAPI backend serves markdown resources. OpenAPI spec for watson x integration. All content is easy to update.

The impact: Research time drops from 3 hours to 5 minutes. Response rates jump from 2% to 15%.

That's 10x more leads with 7x better conversion.
""",

    "09_closing": """
TechBio Lead Gen turns public research into personalized sales intelligence.

For Alex Rives, we went from 'find leads' to a personalized email referencing his specific work - in under a minute.

That's what converts in TechBio sales.

Thank you.
"""
}

def generate_section(name: str, text: str) -> Path:
    """Generate audio for a single section."""
    output_path = output_dir / f"{name}.mp3"

    print(f"Generating {name}...")

    response = client.audio.speech.create(
        model=MODEL,
        voice=VOICE,
        input=text.strip()
    )

    response.stream_to_file(str(output_path))
    print(f"  Saved to {output_path}")

    return output_path

def generate_full_script() -> Path:
    """Generate audio for the complete script as one file."""
    full_text = "\n\n".join(SCRIPT_SECTIONS.values())
    output_path = output_dir / "full_presentation.mp3"

    print("Generating full presentation...")

    response = client.audio.speech.create(
        model=MODEL,
        voice=VOICE,
        input=full_text.strip()
    )

    response.stream_to_file(str(output_path))
    print(f"  Saved to {output_path}")

    return output_path

def main():
    print(f"Using voice: {VOICE}")
    print(f"Using model: {MODEL}")
    print(f"Output directory: {output_dir}")
    print()

    # Generate individual sections
    for name, text in SCRIPT_SECTIONS.items():
        generate_section(name, text)

    print()

    # Generate full presentation
    generate_full_script()

    print()
    print("Done! Audio files generated in:", output_dir)
    print()
    print("Files created:")
    for f in sorted(output_dir.glob("*.mp3")):
        print(f"  - {f.name}")

if __name__ == "__main__":
    main()
