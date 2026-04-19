# SOP: Input Isolation Protocol (Secure Data Containers)

## 1. Overview
The Input Isolation Protocol establishes a technical "Firewall" within Markdown assets to separate sensitive clinical data from instructional narrative. This enables zero-latency local AI auditing while maintaining strict data privacy standards.

## 2. Secure Data Containers (Triple-Hash ###)
All raw clinical metrics, patient profiles, and medical data must be wrapped in `###` delimiters. 
*   **Active Data**: Text within delimiters. This is the only data target for AI clinical audits and metabolic math.
*   **Static Narrative**: Text outside delimiters. This is instructional context and should not be used as clinical variables.

## 3. Mandatory Container Tags
The following tags are required for all Lab and Assessment templates:
*   `### Client Profile ###`: For demographics, biometric baselines, and activity history.
*   `### Medical History ###`: For diagnoses, contraindications, and current medications.
*   `### Lab Data ###`: For raw test results (VO2 max, SBP/DBP, glucose, etc.).

## 4. Operational Integrity
Any clinical "Solve" (X.4) that references data NOT contained within these secure isolation blocks will be flagged as **"Logic Leak: Unverified Source"**.
