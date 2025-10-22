#!/usr/bin/env python3

import os
import re

# Configuration
IMG_DIR = "img"
README_FILE = "readme.md"
START_MARKER = "<!-- <animals> -->"
END_MARKER = "<!-- </animals> -->"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".avif"}

def find_images(directory):
    """Recursively find all image files in the directory."""
    images = []
    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in IMAGE_EXTENSIONS:
                images.append(os.path.join(root, file).replace("\\", "/"))  # use forward slashes
    images.sort()
    return images

def generate_markdown(images):
    """Generate Markdown image links."""
    return "\n\n".join(f"![]({image})" for image in images)

def update_readme(markdown_content):
    """Insert the markdown content into README.md between the markers."""
    with open(README_FILE, "r", encoding="utf8") as f:
        readme_text = f.read()

    pattern = re.compile(
        rf"({re.escape(START_MARKER)})(.*)({re.escape(END_MARKER)})",
        re.DOTALL
    )
    new_content = pattern.sub(rf"\1\n\n{markdown_content}\n\n\3", readme_text)

    with open(README_FILE, "w", encoding="utf8") as f:
        f.write(new_content)

def main():
    images = find_images(IMG_DIR)
    if not images:
        print("No images found in", IMG_DIR)
        return

    markdown_content = generate_markdown(images)
    update_readme(markdown_content)
    print(f"Updated {README_FILE} with {len(images)} images.")

if __name__ == "__main__":
    main()
