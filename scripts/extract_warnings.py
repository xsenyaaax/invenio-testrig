#!/usr/bin/env python3
"""
Extract warnings from test logs and add them to result-summary.json.

Usage: extract_warnings.py <log_path> <log_type> <result_summary_path>

Extracts warnings matching the pattern '^\\s+Warning: (.*)$' from test logs,
deduplicates them with counts, and adds them to result-summary.json.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def extract_warnings(log_path: Path) -> dict[str, int]:
    """Extract and count warnings from a log file."""
    warnings: dict[str, int] = defaultdict(int)
    warning_pattern = re.compile(r"^\s+Warning: (.*)$")

    if not log_path.exists():
        return {}

    with log_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = warning_pattern.match(line)
            if match:
                warning_text = match.group(1).strip()
                warnings[warning_text] += 1

    return dict(warnings)


def update_result_summary(
    result_summary_path: Path, log_type: str, warnings: dict[str, int]
) -> None:
    """Update result-summary.json with warning information."""

    # Load existing result summary
    if result_summary_path.exists():
        with result_summary_path.open("r") as f:
            result_summary = json.load(f)
    else:
        result_summary = {}

    # Initialize warnings structure if it doesn't exist
    if "warnings" not in result_summary:
        result_summary["warnings"] = {}

    if "warnings_count" not in result_summary:
        result_summary["warnings_count"] = {}

    # Add warnings for this log type
    result_summary["warnings"][log_type] = warnings

    # Calculate and add cumulative warning count
    total_count = sum(warnings.values())
    result_summary["warnings_count"][log_type] = total_count

    # Write updated result summary
    with result_summary_path.open("w") as f:
        json.dump(result_summary, f, indent=2)


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 4:
        print(
            "Usage: extract_warnings.py <log_path> <log_type> <result_summary_path>",
            file=sys.stderr,
        )
        sys.exit(1)

    log_path = Path(sys.argv[1])
    log_type = sys.argv[2]
    result_summary_path = Path(sys.argv[3])

    try:
        # Extract warnings from log
        warnings = extract_warnings(log_path)

        if warnings:
            print(f"Found {len(warnings)} unique warning(s) in {log_type} log:")
            for warning_text, count in warnings.items():
                print(f"  [{count}x] {warning_text}")
        else:
            print(f"No warnings found in {log_type} log")

        # Update result summary
        update_result_summary(result_summary_path, log_type, warnings)
        print(f"✓ Updated {result_summary_path}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
