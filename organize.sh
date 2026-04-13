#!/bin/bash
# EXW MASTER LIBRARY ENFORCER SCRIPT
# This script enforces the structural integrity of the repository.

echo "[*] Checking structural integrity..."

# Create necessary directories
mkdir -p 01_ADMIN/STANDARDS 02_COURSES 04_ASSETS config data exports ssot templates

# Move stray templates
find . -maxdepth 1 -name "*.html" -exec mv {} templates/ 2>/dev/null \;
find 01_ADMIN -name "*.html" ! -path "01_ADMIN/HOME_PAGES/*" -exec mv {} templates/ 2>/dev/null \;

echo "[+] Integrity check complete."
