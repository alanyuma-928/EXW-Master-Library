# Canvas CSS & Component Library (v3.0)

[cite_start]Use these snippets to maintain WCAG 2.1 AA compliance and professional branding in the Canvas RCE[cite: 226].

---

## 1. Professional Header (The Flight Manual)
*Standardized Cardinal Red (#ba0c2f) with Teal (#2CCCD3) accent.*

```html
<header style="background-color: #ba0c2f; padding: 2rem 1.5rem; border-bottom: 6px solid #2CCCD3; text-align: center;">
    <h2 style="color: #ffffff; margin: 0; font-size: 2rem;">[MODULE TITLE]</h2>
    <p style="margin: 10px 0 0 0; color: #eafffd; font-style: italic;">"The Centaur Protocol: AI-Enhanced Clinical Care"</p>
</header>
---

## 2. The Coach's Huddle (Callout Box)
*Use this for P-T-C-F instructions and the 150-word Clinical Audit requirement.*

```html
<section style="background-color: #eafffd; border-left: 6px solid #2CCCD3; padding: 1.5rem; border: 1px solid #2CCCD3; border-radius: 4px;">
    <h3 style="margin-top: 0; color: #00878d;">🤝 The Coach's Huddle: Documentation Protocol</h3>
    <p><strong>Part 1:</strong> Your P-T-C-F Engine Prompt.<br>
    <strong>Part 2:</strong> Your 150-word Clinical Audit against the SSOT.</p>
</section>
---

## 3. The 10/7/0 Mastery Table
*Use this component to explain the grading logic for specific Labs and Practical Applications. It reinforces the SEAL Philosophy and the Clinical Audit requirement.*

```html
<div style="margin-top: 25px; margin-bottom: 25px; border: 1px solid #e1e1e1; border-radius: 8px; overflow: hidden;">
    <div style="background-color: #f5f5f5; padding: 15px 20px; border-bottom: 1px solid #ddd;">
        <h3 style="margin: 0; color: #ba0c2f; font-size: 1.4rem;">📊 Evaluation: The Clinical Mastery Scale</h3>
    </div>
    <div style="padding: 20px;">
        <p>In this residency, we grade on <strong>Competency</strong>. You must demonstrate that you can safely pilot the AI Engine and audit its output against the Source of Truth.</p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 1rem;">
            <thead>
                <tr style="background-color: #ba0c2f; color: white; text-align: left;">
                    <th style="padding: 12px; border: 1px solid #ddd; width: 30%;" scope="col">Mastery Level</th>
                    <th style="padding: 12px; border: 1px solid #ddd;" scope="col">Clinical Criteria</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background-color: #fff;">
                    <td style="padding: 12px; border: 1px solid #ddd;"><strong>🌟 Exemplary (10 pts)</strong></td>
                    <td style="padding: 12px; border: 1px solid #ddd;">
                        <strong>Field-Ready.</strong> Two-part submission is complete. The Clinical Audit successfully identifies a specific "Safety Gate" trap or PAGA/Dietary Guideline nuance.
                    </td>
                </tr>
                <tr style="background-color: #f9f9f9;">
                    <td style="padding: 12px; border: 1px solid #ddd;"><strong>✅ Competent (7 pts)</strong></td>
                    <td style="padding: 12px; border: 1px solid #ddd;">
                        <strong>Safe to Practice.</strong> Submission is safe and functional, but the Audit is descriptive rather than analytical. No safety gates were identified.
                    </td>
                </tr>
                <tr style="background-color: #fff0f3;">
                    <td style="padding: 12px; border: 1px solid #ddd; border-left: 5px solid #ba0c2f;"><strong>🔧 Recalibrate (0 pts)</strong></td>
                    <td style="padding: 12px; border: 1px solid #ddd;">
                        <strong>Structural Failure.</strong> Critical safety error, PII leak, or "Lazy Prompt" (missing Audit). <em>Immediate strategy adjustment and resubmission required.</em>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
