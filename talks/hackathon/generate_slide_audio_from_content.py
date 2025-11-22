#!/usr/bin/env python3
"""
Generate individual audio files for each slide based on slide content.
Each audio file will contain ONLY the narration for that specific slide.
"""

import os
import json
import subprocess
from pathlib import Path
import tempfile

# Define narration text for each slide
SLIDE_NARRATIONS = [
    # Slide 1: Title
    """Welcome to our presentation on TechBio Lead Generation and Show Me You Know Me,
    or SMYKM. This is an AI-powered sales intelligence solution built for the
    IBM watsonx Orchestrate Hackathon. Our mission: turn public research into
    personalized outreach.""",

    # Slide 2: The Problem
    """Here's the problem. Sales reps spend 80% of their time researching for
    Show Me You Know Me personalization. They're reading papers to understand prospects' work,
    finding what equipment they use, identifying pain points, and crafting personalized emails.
    The result? Most of this effort produces generic outreach that gets ignored.""",

    # Slide 3: Our Solution
    """Our solution uses 4 AI agents in watsonx Orchestrate. First, Lead Search finds prospects.
    Then Profile Builder creates detailed profiles. Product Match identifies the right products.
    Finally, SMYKM Outreach generates personalized messages. It's a complete pipeline:
    find leads, build profiles, match products, personalize outreach.""",

    # Slide 4: Demo - Alex Rives
    """Let me demonstrate with Alex Rives, our target lead. He's Head of Science at CZI,
    researching ESM3 for AI protein generation. His company just raised 142 million dollars.
    His pain point? AI generates proteins in seconds, but validation takes weeks.""",

    # Slide 5: Lead Discovery
    """Step 1: Lead Discovery. We ask watsonx to find leads in AI protein design.
    It returns Alex Rives from EvolutionaryScale and CZI with a score of 95 and
    142 million in funding. Why the high score? Recent funding, direct equipment need,
    and an acute pain point.""",

    # Slide 6: Profile Builder
    """Step 2: Profile Builder. We ask what equipment Alex Rives needs.
    The system identifies high-throughput X-ray crystallography, automated crystal screening
    with 96-well plates, and fast data collection systems. The key insight:
    AI generates 1000 proteins per day, but traditional validation handles only 1 to 2 per week.
    That's a 10,000x bottleneck.""",

    # Slide 7: Product Match
    """Step 3: Product Match. We match Rigaku products for Alex Rives.
    The recommendation: XtaLAB Synergy-S. Compare it to synchrotron:
    Availability - weeks to schedule versus 24/7. Speed - days per structure versus hours.
    Cost - 500 to 2000 dollars per structure versus about 50 dollars.
    Why it fits: it closes the validation speed gap.""",

    # Slide 8: SMYKM Outreach
    """Step 4: SMYKM Outreach. Generate personalized outreach for Alex Rives.
    Subject line: Closing the loop on ESM3 validation. The message congratulates him
    on the CZI announcement and addresses his specific bottleneck - ESM3 generates
    novel proteins in seconds, but traditional structural validation takes weeks.
    Then introduces how Rigaku XtaLAB Synergy-S could change that equation.""",

    # Slide 9: Personalization Hooks
    """Key Personalization Hooks - what makes it Show Me You Know Me.
    It references the CZI Biohub announcement. Mentions the 500 million years of evolution achievement.
    Addresses the validation bottleneck specifically. Connects the product to his research goal.
    Every sentence shows we understand his work.""",

    # Slide 10: Bonus Features
    """Bonus Features - a complete sales toolkit. Battlecards explain why Rigaku beats synchrotron or CRO.
    Objection handlers provide pre-built responses to pushback. Meeting prep shows what to say
    and what to avoid. Deal probability gives AI-scored likelihood with reasoning.
    Campaign sequences provide 6-week multi-touch plans. LinkedIn content enables social selling.""",

    # Slide 11: Technical Implementation
    """Technical Implementation. The system uses a FastAPI backend serving resources.
    OpenAPI spec enables watsonx skill import. Content is stored as markdown files for easy updates.
    Resources are organized at doi.bio/resources with leads, products, and outreach directories.""",

    # Slide 12: ROI Impact
    """ROI Impact - the numbers speak for themselves. Research time drops from 3 hours to 5 minutes.
    Personalization goes from surface level to deep understanding. Response rate jumps from 2% to over 15%.
    The result: 10 times more leads with 7 times better conversion.""",

    # Slide 13: Thank You
    """Thank you for watching our TechBio Lead Gen and SMYKM demonstration.
    We've shown how to turn public research into personalized sales. Our demo featured
    Alex Rives with ESM3 and 142 million in funding, matched with Rigaku XtaLAB Synergy-S,
    resulting in personalized email that converts. Find the code on GitHub at
    github.com/sness23/lablab-orchestrate."""
]

def generate_audio(text, output_file, voice="nova", speed=1.3):
    """Generate audio using OpenAI TTS API."""
    # Create a temporary file for normal speed audio
    temp_file = output_file.parent / f"temp_{output_file.name}"

    # Generate audio at normal speed
    cmd = [
        "curl", "-s", "https://api.openai.com/v1/audio/speech",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {os.environ.get('OPENAI_API_KEY', '')}",
        "-d", json.dumps({
            "model": "tts-1",
            "input": text,
            "voice": voice,
            "speed": 1.0  # Generate at normal speed first
        }),
        "-o", str(temp_file)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0 or not temp_file.exists():
        print(f"✗ Failed to generate audio for {output_file.name}")
        return False

    # Speed up the audio using ffmpeg
    speed_cmd = [
        "ffmpeg", "-i", str(temp_file),
        "-filter:a", f"atempo={speed}",
        "-y", str(output_file)
    ]

    result = subprocess.run(speed_cmd, capture_output=True, text=True)

    # Clean up temp file
    if temp_file.exists():
        temp_file.unlink()

    if result.returncode == 0:
        print(f"✓ Generated: {output_file.name}")
        return True
    else:
        print(f"✗ Failed to speed up audio for {output_file.name}")
        return False

def main():
    # Check for OpenAI API key
    if not os.environ.get('OPENAI_API_KEY'):
        print("❌ Please set OPENAI_API_KEY environment variable")
        print("export OPENAI_API_KEY='your-api-key'")
        return

    # Create output directory
    slide_audio_dir = Path("slide_audio_new")
    slide_audio_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("GENERATING AUDIO FOR EACH SLIDE")
    print("=" * 60)
    print()

    # Slide filenames
    slide_files = [
        "slide_01_title.mp3",
        "slide_02_problem.mp3",
        "slide_03_solution.mp3",
        "slide_04_alex_rives.mp3",
        "slide_05_lead_discovery.mp3",
        "slide_06_profile_builder.mp3",
        "slide_07_product_match.mp3",
        "slide_08_smykm_outreach.mp3",
        "slide_09_personalization.mp3",
        "slide_10_bonus_features.mp3",
        "slide_11_technical.mp3",
        "slide_12_roi.mp3",
        "slide_13_thank_you.mp3"
    ]

    # Generate audio for each slide
    for i, (filename, narration) in enumerate(zip(slide_files, SLIDE_NARRATIONS), 1):
        output_path = slide_audio_dir / filename
        print(f"Generating audio for Slide {i}: {filename}")
        print(f"  Text length: {len(narration)} characters")

        success = generate_audio(narration, output_path)

        if not success:
            print("⚠️ Failed to generate audio, stopping")
            return

        # Get duration of generated file
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(output_path)],
            capture_output=True, text=True
        )

        try:
            data = json.loads(result.stdout)
            duration = float(data['format']['duration'])
            print(f"  Duration: {duration:.1f}s")
        except:
            print(f"  Duration: unknown")

        print()

    # Verify all files and calculate total duration
    print("=" * 60)
    print("VERIFICATION")
    print("=" * 60)

    total_duration = 0
    for filename in slide_files:
        file_path = slide_audio_dir / filename
        if file_path.exists():
            result = subprocess.run(
                ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(file_path)],
                capture_output=True, text=True
            )
            try:
                data = json.loads(result.stdout)
                duration = float(data['format']['duration'])
                total_duration += duration
                print(f"✓ {filename:<30} {duration:5.1f}s")
            except:
                print(f"✗ {filename:<30} Error reading duration")
        else:
            print(f"✗ {filename:<30} File not found")

    print("-" * 60)
    print(f"Total duration: {int(total_duration//60)}:{int(total_duration%60):02d}")

    if total_duration <= 300:
        print("✅ Presentation fits within 5 minutes!")
    else:
        print(f"⚠️ Presentation is {total_duration - 300:.0f} seconds over 5 minutes")

    print()
    print("To use these audio files:")
    print("1. Move them to the slide_audio directory:")
    print("   mv slide_audio_new/* slide_audio/")
    print("2. Run the presentation:")
    print("   python sync_present.py")

if __name__ == "__main__":
    main()