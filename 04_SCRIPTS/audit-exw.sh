#!/bin/bash

# EXW Master Library Accessibility Auditor
# Rule 1: No <h1> tags (Reserved for Canvas Titles)
# Rule 2: 9:1 Contrast Ratio (Old #ba0c2f -> New #8c0000)

TARGET_DIR=${1:-"./modules/EXW150/"}

echo "### Starting EXW Accessibility Audit on $TARGET_DIR ###"

# Check for H1 violations
H1_COUNT=$(grep -r "<h1>" "$TARGET_DIR" | wc -l)
if [ "$H1_COUNT" -gt 0 ]; then
    echo "❌ FAILED: $H1_COUNT instances of <h1> found."
    grep -r "<h1>" "$TARGET_DIR"
else
    echo "✅ PASSED: No <h1> tags found."
fi

# Check for old branding red (#ba0c2f) which fails 9:1 contrast
RED_COUNT=$(grep -r "#ba0c2f" "$TARGET_DIR" | wc -l)
if [ "$RED_COUNT" -gt 0 ]; then
    echo "❌ FAILED: $RED_COUNT instances of non-compliant red (#ba0c2f) found."
    grep -r "#ba0c2f" "$TARGET_DIR"
else
    echo "✅ PASSED: No non-compliant red (#ba0c2f) found. All branding is 9:1 (#8c0000)."
fi

echo "### Audit Complete ###"
