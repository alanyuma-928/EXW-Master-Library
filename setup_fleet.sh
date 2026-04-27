#!/bin/bash

# Define the Course Fleet
COURSES=("EXW101" "EXW150" "EXW245" "EXW265")

echo "### INITIALIZING FALL 2026 DIRECTORY AUDIT ###"

# Loop through each course to build the hierarchy
for COURSE in "${COURSES[@]}"; do
    TARGET_DIR="02_COURSES/$COURSE/fall-2026/module-0"
    
    echo "[+] Creating structure for $COURSE..."
    
    # Create the directory path (-p ensures parent directories are created)
    mkdir -p "$TARGET_DIR"
    
    # Create an empty Syllabus file if it doesn't exist
    if [ ! -f "$TARGET_DIR/Syllabus.md" ]; then
        touch "$TARGET_DIR/Syllabus.md"
        echo "    - Created: $TARGET_DIR/Syllabus.md"
    else
        echo "    - Found existing: $TARGET_DIR/Syllabus.md (Skipping overwrite)"
    fi
done

echo "### AUDIT COMPLETE: DIRECTORIES CALIBRATED FOR SYNC_SCRIPT.PY ###"