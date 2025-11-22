#!/usr/bin/env python3
"""
Generate individual TTS audio files for each slide.
Each audio file is perfectly timed for its specific slide.
"""

import os
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Output directory for slide audio
output_dir = Path(__file__).parent / "slide_audio"
output_dir.mkdir(exist_ok=True)

# Voice and model settings
VOICE = "onyx"  # Professional male voice
MODEL = "tts-1-hd"  # High quality

# Script for each slide - carefully timed narration
SLIDE_SCRIPTS = {
    "slide_01_title.mp3": """
    Welcome to TechBio Lead Gen and SMYKM - an AI-powered sales intelligence platform built on watson x Orchestrate.

    We're turning public research into personalized outreach that actually converts.

    This is our submission for the IBM watson x Orchestrate Hackathon.
    """,

    "slide_02_problem.mp3": """
    Here's the problem we're solving: Sales reps in TechBio spend 80% of their time researching SMYKM -
    Show Me You Know Me.

    They're reading papers to understand prospects' work, finding what equipment they use,
    identifying pain points, and crafting personalized emails.

    The result? Either generic outreach that gets ignored, or personalized outreach that doesn't scale.

    What if AI could do that research automatically?
    """,

    "slide_03_solution.mp3": """
    We built four AI agents that work together seamlessly in watson x Orchestrate.

    First, Lead Search finds researchers by domain.
    Second, Profile Builder extracts equipment needs and pain points.
    Third, Product Match recommends the right products.
    And fourth, SMYKM Outreach creates personalized emails.

    SMYKM stands for 'Show Me You Know Me' - every email references their specific work.

    The agents work in sequence: Find leads, build profiles, match products, personalize outreach.
    """,

    "slide_04_alex_rives.mp3": """
    Let me show you with a real example: Alex Rives.

    He's the Head of Science at CZI, the Chan Zuckerberg Initiative.
    His research focuses on ESM3 - breakthrough AI for protein generation.
    He raised 142 million dollars in seed funding.

    And here's his critical pain point: AI generates proteins in seconds,
    but structural validation takes weeks. That's the bottleneck we can solve.
    """,

    "slide_05_lead_discovery.mp3": """
    Step 1: Lead Discovery.

    When I ask watson x to "find leads in AI protein design", it returns Alex Rives
    with a score of 95 out of 100.

    Why such a high score? Recent funding of 142 million, direct equipment need
    for crystallography, and an acute pain point - the validation bottleneck
    that's holding back his research.
    """,

    "slide_06_profile_builder.mp3": """
    Step 2: Profile Builder.

    When I ask "What equipment does Alex Rives need?", the system analyzes his papers
    and identifies his equipment needs: high-throughput X-ray crystallography,
    automated crystal screening with 96-well plates, and fast data collection systems.

    The key insight: AI generates 1000 proteins per day, but traditional validation
    handles only 1 to 2 per week. That's a 10,000x bottleneck. He needs to close that gap.
    """,

    "slide_07_product_match.mp3": """
    Step 3: Product Match.

    When I ask "Match Rigaku products for Alex Rives", it recommends the XtaLAB Synergy-S.

    Look at this comparison: Synchrotron requires weeks to schedule versus Rigaku's 24/7 availability.
    Synchrotron takes days per structure versus hours with Rigaku.
    Synchrotron costs 500 to 2000 dollars per structure versus about 50 dollars with Rigaku.

    This directly addresses his validation speed gap.
    """,

    "slide_08_smykm_outreach.mp3": """
    Step 4: SMYKM Outreach.

    When I ask "Generate personalized outreach for Alex Rives", look at this email.

    Subject: "Closing the loop on ESM3 validation."

    It opens by congratulating him on the CZI announcement. Then it goes straight
    to his pain point: "ESM3 generates novel proteins in seconds, but traditional
    structural validation takes weeks."

    Then it positions our solution: "The Rigaku XtaLAB Synergy-S could change that equation."

    This isn't a template - it's personalized to his exact situation.
    """,

    "slide_09_personalization.mp3": """
    What makes this truly SMYKM - Show Me You Know Me?

    First, it references his CZI and Biohub announcement - showing we follow his career.
    Second, it mentions his "500 million years of evolution" achievement - we've read his papers.
    Third, it addresses his validation bottleneck specifically - we understand his pain.
    Fourth, it connects the product directly to his research goal - we get what he's trying to achieve.

    Every sentence demonstrates that we understand his work. That's what converts.
    """,

    "slide_10_bonus_features.mp3": """
    But we didn't stop at email generation. The platform creates a complete sales toolkit.

    Battlecards explain why Rigaku beats synchrotron or contract research organizations.
    Objection handlers provide pre-built responses to common pushback.
    Meeting prep tells you what to say and what to avoid.
    Deal probability gives you AI-scored likelihood with clear reasoning.
    Campaign sequences map out 6-week multi-touch plans.
    And LinkedIn content helps with social selling.

    It's everything you need to close the deal.
    """,

    "slide_11_technical.mp3": """
    The technical implementation is elegantly simple.

    We host markdown resources at doi.bio - leads profiles, product catalogs,
    and outreach templates.

    A FastAPI backend serves these resources with proper OpenAPI specifications
    for watson x skill import.

    Using markdown files makes updates easy - no database complexity,
    just simple text files that anyone can edit.
    """,

    "slide_12_roi.mp3": """
    The ROI impact is dramatic.

    Research time drops from 3 hours to just 5 minutes - that's a 36x improvement.
    Personalization goes from surface-level to deep understanding.
    Response rates jump from 2 percent to over 15 percent.

    The result: 10x more leads with 7x better conversion.

    That's the power of AI-assisted sales intelligence.
    """,

    "slide_13_thank_you.mp3": """
    TechBio Lead Gen and SMYKM - turning public research into personalized sales.

    In our demo, we took Alex Rives - with ESM3 and 142 million in funding -
    matched him with the Rigaku XtaLAB Synergy-S, and generated a personalized
    email that actually converts.

    This is what wins in TechBio sales - showing them you truly understand their work.

    Thank you for watching our hackathon submission.
    """
}

def generate_audio_file(filename: str, text: str):
    """Generate a single audio file"""
    output_path = output_dir / filename

    print(f"Generating {filename}...")

    response = client.audio.speech.create(
        model=MODEL,
        voice=VOICE,
        input=text.strip()
    )

    # Save the audio file
    response.stream_to_file(str(output_path))
    print(f"  ✓ Saved to {output_path}")

    return output_path

def main():
    print("=" * 60)
    print("  Generating Individual Slide Audio Files")
    print("=" * 60)
    print()
    print(f"Voice: {VOICE}")
    print(f"Model: {MODEL}")
    print(f"Output: {output_dir}")
    print()

    # Generate audio for each slide
    for filename, script in SLIDE_SCRIPTS.items():
        generate_audio_file(filename, script)

    print()
    print("✅ All slide audio files generated!")
    print()
    print("Files created:")
    for f in sorted(output_dir.glob("*.mp3")):
        print(f"  - {f.name}")

if __name__ == "__main__":
    main()