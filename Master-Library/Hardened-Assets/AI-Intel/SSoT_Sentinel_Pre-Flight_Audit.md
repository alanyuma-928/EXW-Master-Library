# SOP: SSoT Sentinel (Pre-Flight Audit)

## 1. Purpose
The SSoT Sentinel is a mandatory verification gate that ensures every curriculum asset is grounded in its clinical and federal "Source of Truth" before deployment.

## 2. Audit Requirements (The anchors)
Every Module must explicitly cite one or more of the following anchors in the **Rule** section of the Mission Loop:
*   **PAGA 2018 (2nd Ed.)**: Mandated for all general activity and population guidelines.
*   **ACSM 12th Ed.**: Mandated for all clinical math, metabolic testing, and lab protocols.
*   **DGA 2025-2030**: Mandated for all nutritional "Solve" logic (EXW150).

## 3. The Non-Compliance Flag
If an asset is processed by the AI Engine and found to be missing these specific citations:
1.  The file status must be set to **"Non-Compliant System File"**.
2.  The generation process must halt.
3.  The Pilot must inject the missing SSoT data before the audit can be rerun.

## 4. Verification Workflow
1. **Scan Header**: Verify course-specific SSoT metadata.
2. **Audit Rule Section**: Search for string-match of the Mandatory Anchors.
3. **Lock Status**: Only files passing the SSoT Sentinel audit can be moved to the `/Hardened-Assets/` directory.
