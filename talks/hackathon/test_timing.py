#!/usr/bin/env python3
"""Test script to verify slide timing matches audio content."""

import subprocess
import json
from pathlib import Path

# The slide transitions from run_now.py
SLIDE_TRANSITIONS = [
    (0, "Slide 1: TechBio Lead Gen and SMYKM - Title"),
    (23, "Slide 2: The Problem - 80% Research Time"),
    (33, "Slide 3: Our Solution - 4 AI Agents"),
    (43, "Slide 4: Demo - Alex Rives Target Lead"),
    (51, "Slide 5: Step 1 - Lead Discovery"),
    (60, "Slide 6: Step 2 - Profile Builder"),
    (74, "Slide 7: Step 3 - Product Match"),
    (87, "Slide 8: Step 4 - SMYKM Outreach"),
    (102, "Slide 9: Key Personalization Hooks"),
    (112, "Slide 10: Bonus Features - Sales Toolkit"),
    (130, "Slide 11: Technical Implementation"),
    (137, "Slide 12: ROI Impact - The Numbers"),
    (144, "Slide 13: Thank You"),
]

# Audio content mapping
audio_content = [
    ("01_intro.mp3", "Title/Intro content"),
    ("02_solution.mp3", "Problem + Solution slides"),
    ("03_lead_discovery.mp3", "Alex Rives demo + Lead Discovery"),
    ("04_profile_builder.mp3", "Profile Builder slide"),
    ("05_product_match.mp3", "Product Match slide"),
    ("06_smykm_outreach.mp3", "SMYKM Outreach + Personalization"),
    ("07_bonus_features.mp3", "Bonus Features slide"),
    ("08_technical_roi.mp3", "Technical + ROI slides"),
    ("09_closing.mp3", "Thank You slide"),
]

print("=" * 70)
print("PRESENTATION TIMING VERIFICATION")
print("=" * 70)
print()

# Get actual audio durations
audio_dir = Path("audio")
audio_durations = []
cumulative = 0

for audio_file, content in audio_content:
    audio_path = audio_dir / audio_file
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(audio_path)],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    duration = float(data['format']['duration'])
    audio_durations.append((audio_file, duration, cumulative, cumulative + duration, content))
    cumulative += duration

# Print timeline
print("AUDIO TIMELINE:")
print("-" * 70)
for audio_file, duration, start, end, content in audio_durations:
    print(f"{start:5.1f}s - {end:5.1f}s : {audio_file:<25} ({content})")
print()

print("SLIDE TRANSITIONS:")
print("-" * 70)
for i, (time, slide) in enumerate(SLIDE_TRANSITIONS):
    # Find which audio is playing at this time
    audio_playing = "None"
    for audio_file, duration, start, end, content in audio_durations:
        if start <= time < end:
            audio_playing = audio_file
            break

    marker = "→" if i > 0 else "START"
    print(f"{time:5d}s {marker:5} {slide:<45} [{audio_playing}]")

print()
print("VERIFICATION:")
print("-" * 70)

# Check key alignments
checks = [
    ("Problem slide (2)", 23, "Should be after intro ends (~22.5s)"),
    ("Solution slide (3)", 33, "Should be midway through 02_solution.mp3"),
    ("Alex Rives slide (4)", 43, "Should be after 02_solution.mp3 ends"),
    ("Lead Discovery (5)", 51, "Should be midway through 03_lead_discovery.mp3"),
    ("Profile Builder (6)", 60, "Should be after 03_lead_discovery.mp3 ends"),
    ("SMYKM Outreach (8)", 87, "Should be after 05_product_match.mp3 ends"),
    ("Personalization (9)", 102, "Should be during 06_smykm_outreach.mp3"),
    ("Thank You (13)", 144, "Should be after 08_technical_roi.mp3 ends"),
]

for slide_name, expected_time, description in checks:
    # Find actual audio playing at that time
    for audio_file, duration, start, end, content in audio_durations:
        if start <= expected_time < end:
            status = "✓"
            audio_info = f"Playing: {audio_file} ({content})"
            break
    else:
        status = "✗"
        audio_info = "No audio playing!"

    print(f"{status} {slide_name:<20} at {expected_time:3d}s : {description}")
    print(f"  {audio_info}")

print()
print(f"Total presentation duration: {int(cumulative//60)}:{int(cumulative%60):02d}")
print("=" * 70)