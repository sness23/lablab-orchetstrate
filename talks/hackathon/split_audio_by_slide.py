#!/usr/bin/env python3
"""
Split audio files to create one audio file per slide.
This ensures perfect synchronization between audio and slides.
"""

import subprocess
import json
from pathlib import Path
import os

def get_audio_duration(file_path):
    """Get duration of an audio file in seconds."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(file_path)],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        return float(data['format']['duration'])
    except:
        return 0

def split_audio(input_file, output_file, start_time, duration):
    """Split audio file using ffmpeg."""
    cmd = [
        "ffmpeg", "-i", str(input_file),
        "-ss", str(start_time),  # Start time
        "-t", str(duration),     # Duration
        "-acodec", "copy",        # Copy codec (no re-encoding)
        "-y",                     # Overwrite output
        str(output_file)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ Created: {output_file.name}")
        return True
    else:
        print(f"✗ Failed to create: {output_file.name}")
        print(f"  Error: {result.stderr}")
        return False

def main():
    audio_dir = Path("audio")
    slide_audio_dir = Path("slide_audio")

    # Create output directory
    slide_audio_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("CREATING ONE AUDIO FILE PER SLIDE")
    print("=" * 60)
    print()

    # Define the mapping from current audio to individual slides
    # Based on the current audio files at 1.30x speed

    audio_splits = [
        # Source file -> list of (output_name, start_ratio, end_ratio)
        ("01_intro.mp3", [
            ("slide_01_title.mp3", 0.0, 1.0),  # Full file for title slide
        ]),

        ("02_solution.mp3", [
            ("slide_02_problem.mp3", 0.0, 0.5),   # First half for problem
            ("slide_03_solution.mp3", 0.5, 1.0),  # Second half for solution
        ]),

        ("03_lead_discovery.mp3", [
            ("slide_04_alex_rives.mp3", 0.0, 0.5),      # First half for Alex intro
            ("slide_05_lead_discovery.mp3", 0.5, 1.0),  # Second half for discovery
        ]),

        ("04_profile_builder.mp3", [
            ("slide_06_profile_builder.mp3", 0.0, 1.0),  # Full file
        ]),

        ("05_product_match.mp3", [
            ("slide_07_product_match.mp3", 0.0, 1.0),  # Full file
        ]),

        ("06_smykm_outreach.mp3", [
            ("slide_08_smykm_outreach.mp3", 0.0, 0.55),       # First 55% for SMYKM
            ("slide_09_personalization.mp3", 0.55, 1.0),  # Last 45% for personalization
        ]),

        ("07_bonus_features.mp3", [
            ("slide_10_bonus_features.mp3", 0.0, 1.0),  # Full file
        ]),

        ("08_technical_roi.mp3", [
            ("slide_11_technical.mp3", 0.0, 0.5),  # First half for technical
            ("slide_12_roi.mp3", 0.5, 1.0),        # Second half for ROI
        ]),

        ("09_closing.mp3", [
            ("slide_13_thank_you.mp3", 0.0, 1.0),  # Full file
        ]),
    ]

    # Process each audio file
    for source_file, splits in audio_splits:
        source_path = audio_dir / source_file

        if not source_path.exists():
            print(f"⚠️ Source file not found: {source_file}")
            continue

        # Get duration of source file
        duration = get_audio_duration(source_path)
        if duration == 0:
            print(f"⚠️ Could not get duration for: {source_file}")
            continue

        print(f"\nProcessing: {source_file} (duration: {duration:.1f}s)")
        print("-" * 40)

        for output_name, start_ratio, end_ratio in splits:
            output_path = slide_audio_dir / output_name

            # Calculate actual times
            start_time = duration * start_ratio
            split_duration = duration * (end_ratio - start_ratio)

            print(f"  Splitting {start_time:.1f}s - {start_time + split_duration:.1f}s")

            # If it's the full file, just copy it
            if start_ratio == 0.0 and end_ratio == 1.0:
                subprocess.run(["cp", str(source_path), str(output_path)])
                print(f"  ✓ Copied full file to: {output_name}")
            else:
                # Split the file
                split_audio(source_path, output_path, start_time, split_duration)

    print()
    print("=" * 60)
    print("VERIFICATION")
    print("=" * 60)

    # Verify all files were created and show durations
    total_duration = 0
    slide_files = sorted(slide_audio_dir.glob("slide_*.mp3"))

    if len(slide_files) == 13:
        print("✅ All 13 slide audio files created!")
        print()
        print("Slide audio durations:")
        print("-" * 40)

        for audio_file in slide_files:
            duration = get_audio_duration(audio_file)
            total_duration += duration
            print(f"  {audio_file.name:<30} {duration:5.1f}s")

        print("-" * 40)
        print(f"Total duration: {int(total_duration//60)}:{int(total_duration%60):02d}")

        if total_duration <= 300:
            print("✅ Presentation fits within 5 minutes!")
        else:
            print(f"⚠️ Presentation is {total_duration - 300:.0f} seconds over 5 minutes")
    else:
        print(f"❌ Only {len(slide_files)} of 13 files created")
        print("Missing files:")
        expected = set([f"slide_{i:02d}_{name}.mp3" for i, name in enumerate([
            "title", "problem", "solution", "alex_rives", "lead_discovery",
            "profile_builder", "product_match", "smykm_outreach", "personalization",
            "bonus_features", "technical", "roi", "thank_you"
        ], 1)])

        actual = set([f.name for f in slide_files])
        for missing in expected - actual:
            print(f"  - {missing}")

if __name__ == "__main__":
    main()