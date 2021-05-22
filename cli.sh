#!/bin/bash
MY_DIR="${0%/*}"
source "$MY_DIR/venv/bin/activate"
exec python3 "$MY_DIR/cliMain.py" "$@"
