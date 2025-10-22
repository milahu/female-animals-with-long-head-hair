#!/usr/bin/env python3

import sys
import os
import subprocess

def rename_file(file_path, new_path):
    try:
        # Try git mv first
        subprocess.run(
            ["git", "mv", file_path, new_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"Renamed (git) {file_path!r} -> {new_path!r}")
    except subprocess.CalledProcessError:
        # Fall back to os.rename if git mv fails
        try:
            os.rename(file_path, new_path)
            print(f"Renamed (filesystem) {file_path!r} -> {new_path!r}")
        except Exception as e:
            print(f"Error renaming {file_path!r}: {e}")

def rename_files(files):
    for file_path in files:
        if not os.path.isfile(file_path):
            print(f"Skipping {file_path!r} (not a valid file)")
            continue

        dir_name, file_name = os.path.split(file_path)
        new_file_name = file_name.replace(" ", "-")
        new_path = os.path.join(dir_name, new_file_name)

        if file_path == new_path:
            continue

        rename_file(file_path, new_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python move-to-dashes.py <file1> <file2> ...")
    else:
        rename_files(sys.argv[1:])
