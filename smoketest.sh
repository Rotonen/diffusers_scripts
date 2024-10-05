#!/usr/bin/env bash
set -euo pipefail

time (
    for script in *.py
    do
        echo ""
        echo "${script}"
        echo ""
        time uv run --locked "${script}" --no-open-outputs &> /dev/null
    done
)

open outputs/
