# 📡 API Specifications: EXW Clinical Data Integrations

---
**Author:** Coach Alan Pruitt | **Version:** 1.0
**Context:** Lovable App Development
---

## 🏗️ USDA FoodData Central (FDC) API
* **Base URL:** `https://api.nal.usda.gov/fdc/v1`
* **Purpose:** High-fidelity nutritional auditing for EXW150 (Fuel Box).
* **Endpoint:** `/foods/search`
* **Query Params:** `query`, `dataType`, `pageSize`, `api_key`.
* **Standard:** DGA 2025–2030 whole-food matrix auditing.

## 🏗️ National Weather Service (NWS) KNYL API
* **Base URL:** `https://api.weather.gov`
* **Station ID:** `KNYL` (Yuma MCAS)
* **Purpose:** Environmental redline auditing for EXW245/265 (Safety Box).
* **Endpoint:** `/stations/KNYL/observations/latest`
* **Standard:** MSSE Journal thermal-protection gates (Zone 10 Redlines).

&nbsp;

<div style="background-color: #FFFDD0; color: #000080; padding: 15px; border: 2px solid #000080; border-radius: 8px; font-family: 'Space Mono', monospace;">
    <h4>🛠️ API Integration Check</h4>
    * [ ] **Engine:** Gemini 1.5 Pro (Integration Pilot)<br>
    * [ ] **Audit:** Validate JSON response against SSoT mandates<br>
    * [ ] **Solve:** Hard-coded formula logic (DTK Kernel)
</div>

&nbsp;

---
**© 2026 Coach Alan Pruitt | CC BY-NC 4.0 | Accessibility: WCAG 2.1 AA**
