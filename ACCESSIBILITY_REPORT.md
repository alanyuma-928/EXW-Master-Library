# EXW Master Library Accessibility Audit Report
**Project:** EXW 245: Exercise Testing & Prescription  
**Standards:** WCAG 2.1 AA (Title II ADA)  
**Proprietary Metric:** Double-Contrast Guard (Hard Rule: 9:1 Contrast Ratio)

---

## 📊 Summary of Findings

| Module | Files Audited | Critical Violations | Heading Issues | Contrast Issues |
| :--- | :--- | :--- | :--- | :--- |
| **Module 0** | 8 | 0 | 0 | 16 |
| **Module 1** | 2 | 2 | 2 | 8 |
| **Fall 2026** | 16 | 16 | 16 | 64 |

---

## 🚩 Module 0: Introductory Pages
**Files:** `01-welcome.html` to `08-readiness-check.html`

### 1. Contrast Ratio (Hard Rule: 9:1)
- **Violation**: The branding header and footer use Matador Red (`#ba0c2f`) with White (`#ffffff`) text.
- **Contrast Ratio**: **6.64:1** (Fails 9:1 mandate).
- **Locations**: All files in Module 0.
- **Recommended Fix**:
```diff
- background-color: #ba0c2f; color: #ffffff;
+ background-color: #8c0000; color: #ffffff; /* Darkened red to meet 9:1 */
```

### 2. Heading Hierarchy (The Matador Protocol)
- **Status**: **PASS**. All files correctly begin with an `<h2>` and avoid `<h1>`.

---

## 🚩 Module 1: Pre-Screening & Risk Stratification
**Files:** `home.html`

### 1. Contrast Ratio (Hard Rule: 9:1)
- **Violation**: SSoT Shield `span` uses `#ba0c2f` on `#eafffd`.
- **Contrast Ratio**: **6.38:1** (Fails 9:1 mandate).
- **Recommended Fix**: Use a darker accent color for shield labels.

### 2. Heading Hierarchy (The Matador Protocol)
- **Violation**: `header h1` tag detected. `<h1>` is reserved for Canvas Page Titles.
- **Location**: `modules/EXW245/module-1/home.html:161`
- **Recommended Fix**:
```diff
- <h1>Module 1: Pre-Screening & Risk Stratification</h1>
+ <h2>Module 1: Pre-Screening & Risk Stratification</h2>
```

---

## 🚩 Fall 2026: Assignment Templates
**Files:** `modules/EXW245/fall-2026/module-*/assignment.html`

### 1. Contrast Ratio (Hard Rule: 9:1)
- **Violation**: Standard assignment template branding fails the 9:1 contrast mandate in headers and footers.
- **Violation**: `exemplar-box h3` uses `#2e7d32` on `#f0fdf4`.
- **Contrast Ratio**: **5:1** (Fails 9:1 mandate).
- **Recommended Fix**: Darken the green accent to `#1b5e20`.

### 2. Heading Hierarchy (The Matador Protocol)
- **Violation**: Systematic use of `<h1>` in the header section across all 16 assignment templates.
- **Location**: Line 136 in all `assignment.html` files.
- **Recommended Fix**: Convert `<h1>` to `<h2>` to comply with Canvas RCE standards.

---

## 🧱 Clinical Delimiters (###)
- **Status**: **PASS**. The SSoT documentation (`03-ssot.html`) correctly instructs residents on the delimiter protocol. 
- **Observation**: Ensure that future lab data implementations utilize `<pre>` tags for clinical data blocks as seen in the Module 11 reference.

---
**Auditor Signature:** Clinical AI Auditor (Gemini)  
**Date:** March 12, 2026  
**Status:** 🔴 RECALIBRATE REQUIRED
