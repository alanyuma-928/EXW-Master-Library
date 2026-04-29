# EXW245_SSOT.md
**Course:** Guidelines for Exercise Testing and Prescription  
**Semester:** Fall 2026 (8/17/26 – 12/4/26)  
**Authority Level:** Tier 2 (Course-Specific SSoT)

---

### I. The Single Source of Truth (SSoT)
* **Primary:** Physical Activity Guidelines for Americans (PAGA) 2018 (2nd Ed).
* **Secondary:** ACSM’s Guidelines for Exercise Testing and Prescription (12th Ed).
* **Conflict Protocol:** If ACSM or external "fad" data contradicts PAGA 2018, the PAGA 2018 standard is the final authority.

---

### II. Course Logic & Lab Scaffolding
* **Location:** AWC Yuma Campus GY 116.
* **Hybrid Model:** * **Part A (AI Guided):** Simulation and math verification via the Antigravity Middleware.
    * **Part B (Practical):** Lode Corival application using hyperbolic braking and research-grade accuracy.

---

### III. Clinical Parameters (API Integration Points)
When the Middleware fetches data via `_CORE/PROVIDERS.md`, it must audit for these specific variables:
* **Pre-Participation Screening:** ACSM algorithm for medical clearance.
* **Biometrics:** Blood Pressure (BP) and Heart Rate (HR) baseline standards.
* **Metabolic Equations:** Ensure all $VO_{2}$ and MET calculations utilize LaTeX formatting.
    * *Formula Example:* $$Relative~VO_{2} = \frac{Absolute~VO_{2} \times 1000}{Body~Weight~(kg)}$$

---

### IV. Population Specifics
The following populations require specific "Rule" mapping from the PAGA API:
1. **Healthy Adults:** 150–300 min/week moderate-intensity aerobic activity.
2. **Older Adults:** Focus on multicomponent physical activity (balance + aerobic + muscle-strengthening).
3. **Chronic Conditions:** Tailored prescriptions for Hypertension, Type 2 Diabetes, and Obesity.

---

### V. Operational Rules
* **BurnTimeCard Integration:** Outdoor lab activities must be audited against real-time NWS/EPA data.
* **Delimiters:** All student clinical profiles must be wrapped in `### CLIENT_PROFILE ###` to ensure the AI doesn't confuse case data with instructional rules.