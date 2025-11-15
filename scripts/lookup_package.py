#!/usr/bin/env python3
"""
Lookup package repository information from config.json and patches.json.

Usage: lookup_package.py <config.json> <patches.json> <package-name>

Outputs bash-compatible environment variable assignments:
  original_repository_url="..."
  original_repository_branch="..."
  patched_repository_url="..."
  patched_repository_branch="..."
"""

import json
import re
import sys
from pathlib import Path


def lookup_package(config_path: Path, patches_path: Path, package_name: str) -> None:
    """Look up package information and return repository URLs and branches."""

    # Load config.json
    with config_path.open("r") as f:
        config = json.load(f)

    # Load patches.json
    with patches_path.open("r") as f:
        patches = json.load(f)

    # Find matching repository configuration
    original_url = None
    original_branch = ""

    for repo in config.get("repositories", []):
        base_url = repo.get("base_url", "")
        branch = repo.get("branch", "")
        package_regex = repo.get("package-regex", "")
        exclude_package_regex = repo.get("exclude-package-regex", "")

        # Check if package matches regex and is not excluded
        if package_regex and re.match(package_regex, package_name):
            # Check if package matches exclude regex
            if exclude_package_regex and re.match(exclude_package_regex, package_name):
                continue
            original_url = f"{base_url}/{package_name}"
            original_branch = branch
            break

    # Default to inveniosoftware if no match found
    if not original_url:
        raise ValueError(f"Package '{package_name}' not found in configuration.")

    # Look up patch information
    patched_url = ""
    patched_branch = ""

    if package_name in patches:
        patch_info = patches[package_name]
        patched_url = patch_info.get("url", "")
        patched_branch = patch_info.get("branch", "")

    # Output bash-compatible variable assignments
    print(f'original_repository_url="{original_url}"')
    print(f'original_repository_branch="{original_branch}"')
    print(f'patched_repository_url="{patched_url}"')
    print(f'patched_repository_branch="{patched_branch}"')


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: lookup_package.py <config.json> <patches.json> <package-name>",
            file=sys.stderr,
        )
        sys.exit(1)

    config_path = Path(sys.argv[1])
    patches_path = Path(sys.argv[2])
    package_name = sys.argv[3]

    try:
        lookup_package(config_path, patches_path, package_name)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
