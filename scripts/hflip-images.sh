#!/usr/bin/env bash

# Usage: ./scripts/hflip-images.sh /path/to/input /path/to/output

# Exit immediately if a command exits with a non-zero status
set -e

# Check that exactly two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_dir> <output_dir>"
    exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="$2"

# Check that input directory exists
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Input directory '$INPUT_DIR' does not exist."
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all PNG images in the input directory
for img in "$INPUT_DIR"/*.png; do
    # Skip if no PNG files found
    [ -e "$img" ] || { echo "No PNG images found in $INPUT_DIR"; exit 1; }

    # Extract filename
    filename=$(basename "$img")

    dst="$OUTPUT_DIR/$filename"
    if [ -e "$dst" ]; then
      echo "keeping $dst"
      continue
    fi

    # Flip image horizontally using ImageMagick
    magick "$img" -flop "$dst"

    echo "writing $dst"
done
