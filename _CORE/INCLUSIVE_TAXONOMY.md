# INCLUSIVE_TAXONOMY.md
**Status:** Core Constraint (Tier 1)
**Purpose:** Standardize inclusive clinical terminology across all EXW modules.

---

### I. Terminology Mapping
When the API or student input uses "Legacy Terms," the Assistant must silently translate them to "Standardized Selectors":

| Legacy Term | Standardized Selector (AWC) | Clinical Focus |
| :--- | :--- | :--- |
| Pregnancy | **Prenatal & Postpartum** | Maternal health & fetal development cycles. |
| Wheelchair | **Adaptive / Limited Mobility** | Spinal cord injury, CP, or temporary restrictions. |
| Senior Citizen | **Older Adults** | Alignment with PAGA Chapter 5. |
| Handicapped | **Accessible / Adaptive** | Adherence to WCAG 2.1 AA. |

---

### II. Caloric & Nutritional Logic
* **Adaptive Mobility:** When this selector is active, the Assistant must prompt the student to recalibrate caloric requirements due to specific mobility challenges.
* **Prenatal:** All exercise prescriptions must be audited against the PAGA "Pregnancy and Postpartum" safety rules (SSoT).