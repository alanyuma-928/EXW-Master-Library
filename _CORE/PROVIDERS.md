### PAGA_API_GATEWAY_PROTOCOL
**Source Authority:** U.S. Office of Disease Prevention and Health Promotion (ODPHP)
**Base Endpoint:** https://health.gov/myhealthfinder/api/v3/
**Course Target:** Physical Activity Guidelines for Americans (PAGA) 2018 (2nd Ed)

---

### I. API Retrieval Rules (The Middleware Fetch)
1. **Endpoint Target:** Utilize the `topicId` or `keyword` parameters to fetch specific activity guidelines (e.g., Topic ID 536 for "Physical Activity").
2. **Data Sanitization:** * Strip all non-essential HTML tags from the API return.
    * Extract specific dosage integers (MET-minutes, frequency, and duration).
3. **Temporal Stamp:** Every fetch must be logged in `_SCRIPTS/SNAPSHOTS/` with the format `YYYY-MM-DD_PAGA_DATA.json`.

---

### II. The Clinical Filter (The Mission Loop Mapping)
Raw API data must be "passed through" these logic gates before being baked into a module:

* **Pattern Mapping:** If the API returns data for a specific age or condition, map it to the `### CLIENT_PROFILE ###` requirements.
* **Rule Extraction:** The API text must be summarized into a concise **FITT-VP** format (Frequency, Intensity, Time, Type).
* **Solve Logic:** The Assistant must check the API data against the **ACSM 12th Ed** safety contraindications held in `EXW245_SSOT.md`.

---

### III. Formatting & Safety Gates
* **Unit Conversion:** Convert raw clinical data into student-facing descriptions (e.g., "Moderate Intensity" = "Brisk Walking/Talk Test").
* **Accessibility Audit:** Ensure the API-derived text does not contain "hidden" characters or formatting that breaks the **WCAG 2.1 AA** contrast ratio in the `navy_creme_shell.html`.
* **The "Zero-Failure" Fallback:** If the API returns a 404 or Timeout, the Assistant MUST revert to the static text stored in the local `EXW245_SSOT.md` and append a warning to the `BUILD_STATUS.md` log.

---

### IV. Middleware Signature
*All output derived from this provider must include the following hidden comment at the bottom of the HTML code:*
``