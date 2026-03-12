#!/usr/bin/env python3
"""Rename files in the current directory by replacing spaces with underscores."""

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="Replace spaces with underscores in filenames.")
    parser.add_argument("-force", action="store_true", help="Rename all files without asking for approval")
    args = parser.parse_args()

    cwd = os.getcwd()
    files_with_spaces = sorted(f for f in os.listdir(cwd) if " " in f)

    if not files_with_spaces:
        print("No files with spaces found in the current directory.")
        return

    renamed = 0
    for old_name in files_with_spaces:
        new_name = old_name.replace(" ", "_")
        if os.path.exists(os.path.join(cwd, new_name)):
            print(f"SKIP: '{new_name}' already exists, skipping '{old_name}'")
            continue

        if args.force:
            os.rename(os.path.join(cwd, old_name), os.path.join(cwd, new_name))
            print(f"Renamed: '{old_name}' -> '{new_name}'")
            renamed += 1
        else:
            answer = input(f"Rename '{old_name}' -> '{new_name}'? [y/n] ").strip().lower()
            if answer == "y":
                os.rename(os.path.join(cwd, old_name), os.path.join(cwd, new_name))
                print(f"  Renamed.")
                renamed += 1
            else:
                print(f"  Skipped.")

    print(f"\nDone. {renamed}/{len(files_with_spaces)} file(s) renamed.")


if __name__ == "__main__":
    main()
