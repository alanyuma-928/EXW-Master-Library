# EXW-Master-Library: Curriculum-as-Code

## TL;DR
This repository is the central authority for Exercise Science and Wellness (EXW) curriculum. It leverages the **Mission Loop** framework and enforces the **PAGA 2018 (2nd Ed.)** and **ACSM 12th Ed.** as the exclusive Single Sources of Truth (SSoT) for all instructional design.

---

## <h2>Core Architecture & SSoT</h2>
All instructional materials, assessments, and AI-driven tools within this library must adhere to the following standards. Any information conflicting with these sources is to be discarded to ensure clinical and academic integrity.

* **PAGA 2018 (2nd Ed.):** The primary authority for physical activity guidelines.
* **ACSM 12th Ed.:** The authority for clinical exercise testing and prescription (specifically for EXW245).
* **OER Standards:** All content is designed as Open Educational Resources to ensure zero-cost barriers for community college students.

## <h2>The Mission Loop Framework</h2>
All course workflows utilize the **Pattern / Rule / Solve** framework to prioritize problem framing and clinical auditing:

1.  **Identify Patterns:** Analyze client data, physical inactivity trends, or physiological profiles.
2.  **Apply Rules:** Audit findings against PAGA or ACSM federal and clinical guidelines.
3.  **Solve:** Generate evidence-based interventions, prescriptions, or community health solutions.

---

## <h2>Course Portfolio</h2>

| Course | Title | SSoT | Framework focus |
| :--- | :--- | :--- | :--- |
| **EXW101** | Concepts of Kinesiology | PAGA 2018 | Foundations & Community Intervention |
| **EXW150** | Nutrition for Sports | PAGA / USDA | Nutritional Literacy & Sustainability |
| **EXW245** | Exercise Testing & Rx | ACSM 12th Ed | Clinical Auditing & Lab Scaffolding |
| **EXW265** | Special Populations | PAGA 2018 | Chronic Condition Safety & Adaptation |

---

## <h2>Technical Specifications</h2>

### <h3>Accessibility & Semantic Hierarchy</h3>
* **Heading Logic:** Per institutional standards, all Markdown starts at the `<h2>` level (reserving `H1` for Canvas Page Titles).
* **Strict Hierarchy:** Subsequent headings must follow a logical flow (`<h3>`, `<h4>`) without skipping levels.
* **WCAG 2.1 AA:** All integrated CSS or HTML must maintain a minimum **4.5:1** contrast ratio and utilize ARIA-compliant semantic structures.

### <h3>AI Delimiter Protocol</h3>
To maintain structural integrity for AI-driven "Tool Box" or "Quiz Master" prompts, all clinical case data, client profiles, or medical inputs must be wrapped in triple-hash (`###`) delimiters.

**Example Implementation:**
```markdown
###
[Insert Client Physiological Profile Here]
###
[Apply Mission Loop Logic: Rule/Solve]
###
