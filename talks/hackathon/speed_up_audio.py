#!/usr/bin/env python3
"""Speed up audio files to fit within 5-minute presentation limit."""

import os
import subprocess
from pathlib import Path

def speed_up_audio(input_file, output_file, tempo="121"):
    """Speed up audio file using sox or ffmpeg."""

    # First try with sox (better quality for speed changes)
    try:
        cmd = [
            "sox", input_file, output_file,
            "tempo", tempo.replace("%", ""),
            "rate", "44100"  # Ensure consistent sample rate
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Processed with sox: {os.path.basename(input_file)}")
            return True
    except FileNotFoundError:
        pass

    # Fallback to ffmpeg with atempo filter
    try:
        # FFmpeg's atempo is limited to 0.5-2.0, so we need to calculate the factor
        factor = float(tempo.replace("%", "")) / 100

        # Build the atempo filter (may need to chain for factors > 2)
        atempo_filter = f"atempo={factor}"
        if factor > 2.0:
            # Chain multiple atempo filters for factors > 2
            atempo_filter = "atempo=2.0,atempo=" + str(factor / 2.0)

        cmd = [
            "ffmpeg", "-i", input_file,
            "-filter:a", atempo_filter,
            "-y",  # Overwrite output
            output_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Processed with ffmpeg: {os.path.basename(input_file)}")
            return True
        else:
            print(f"✗ Error processing {input_file}: {result.stderr}")
            return False
    except FileNotFoundError:
        print("✗ Neither sox nor ffmpeg found. Please install one of them.")
        return False

def main():
    audio_dir = Path("audio")
    backup_dir = Path("audio_backup")

    # Create backup directory
    backup_dir.mkdir(exist_ok=True)

    # Speed factor (121% = 1.21x speed)
    tempo = "121"

    print(f"Speeding up audio files by {tempo}% to fit within 5 minutes...")
    print("-" * 50)

    # Process each MP3 file
    audio_files = list(audio_dir.glob("*.mp3"))

    if not audio_files:
        print("No MP3 files found in audio directory")
        return

    for audio_file in sorted(audio_files):
        # Backup original file
        backup_file = backup_dir / audio_file.name
        if not backup_file.exists():
            subprocess.run(["cp", str(audio_file), str(backup_file)])
            print(f"  Backed up: {audio_file.name}")

        # Create temp file for processing
        temp_file = audio_dir / f"temp_{audio_file.name}"

        # Speed up the audio
        if speed_up_audio(str(backup_file), str(temp_file), tempo):
            # Replace original with sped-up version
            subprocess.run(["mv", str(temp_file), str(audio_file)])
        else:
            # Clean up temp file if it exists
            if temp_file.exists():
                temp_file.unlink()

    print("-" * 50)
    print("Checking new durations...")

    # Check new durations
    total_duration = 0
    for audio_file in sorted(audio_dir.glob("*.mp3")):
        try:
            result = subprocess.run(
                ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(audio_file)],
                capture_output=True, text=True
            )
            import json
            data = json.loads(result.stdout)
            duration = float(data['format']['duration'])
            total_duration += duration
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            print(f"  {audio_file.name:<25} {minutes:2d}:{seconds:02d}")
        except:
            print(f"  {audio_file.name:<25} Unable to read")

    print("-" * 50)
    print(f"Total duration: {int(total_duration//60)}:{int(total_duration%60):02d}")

    if total_duration <= 300:
        print("✅ Success! Presentation now fits within 5 minutes.")
    else:
        print(f"⚠️  Still over 5 minutes. Consider speeding up to {int((total_duration/290)*100)}%")

if __name__ == "__main__":
    main()