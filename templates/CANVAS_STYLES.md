# Canvas CSS & Component Library (v3.2)

Use these snippets to maintain WCAG 2.1 AA compliance and professional branding in the Canvas RCE. All text colors are optimized for a 4.5:1 contrast ratio (#1a1a1a), and tables include semantic captions and header scopes.

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
*Use this component for P-T-C-F instructions and the mandatory 150-word Clinical Audit requirement. The background is a light Teal for high visibility against standard content.*

```html
<section style="background-color: #eafffd; border-left: 6px solid #2CCCD3; padding: 1.5rem; border: 1px solid #2CCCD3; border-radius: 4px; color: #1a1a1a;">
    <h3 style="margin-top: 0; color: #00878d;">🤝 The Coach's Huddle: Documentation Protocol</h3>
    <p><strong>The Professional Standard:</strong> Professionalism in clinical settings starts with documentation. In this residency, we mirror clinical record-keeping.</p>
    <p style="margin-bottom: 0;"><strong>Submission Standard:</strong> All Labs are <strong>Text Entry Only</strong>. You must submit your <strong>P-T-C-F Engine Prompt</strong> and your <strong>150-word Clinical Audit</strong> directly into the Canvas entry box.</p>
</section>

---

## 3. The Exemplary/Competent/Recalibrate Mastery Table
*Use this component to explain the grading logic for Labs and Practical Applications.*

```html
<div style="margin-top: 25px; margin-bottom: 25px; border: 1px solid #e1e1e1; border-radius: 8px; overflow: hidden; color: #1a1a1a;">
    <div style="background-color: #f5f5f5; padding: 15px 20px; border-bottom: 1px solid #ddd;">
        <h3 style="margin: 0; color: #ba0c2f; font-size: 1.4rem;">📊 Evaluation: The Clinical Mastery Scale</h3>
    </div>
    <div style="padding: 20px;">
        <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 1rem;">
            <caption style="text-align: left; padding: 10px; font-style: italic; color: #1a1a1a;">Table: Clinical Mastery Scale and Grading Criteria</caption>
            <thead>
                <tr style="background-color: #ba0c2f; color: white; text-align: left;">
                    <th style="padding: 12px; border: 1px solid #ddd; width: 30%;" scope="col">Mastery Level</th>
                    <th style="padding: 12px; border: 1px solid #ddd;" scope="col">Clinical Criteria</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background-color: #fff;">
                    <td style="padding: 12px; border: 1px solid #ddd;"><strong>🌟 Exemplary (10 pts)</strong></td>
                    <td style="padding: 12px; border: 1px solid #ddd;">Field-Ready. Audit identifies a specific safety gate trap.</td>
                </tr>
                <tr style="background-color: #f9f9f9;">
                    <td style="padding: 12px; border: 1px solid #ddd;"><strong>✅ Competent (7 pts)</strong></td>
                    <td style="padding: 12px; border: 1px solid #ddd;">Safe to Practice. Audit is descriptive rather than analytical.</td>
                </tr>
                <tr style="background-color: #fff0f3;">
                    <td style="padding: 12px; border: 1px solid #ddd; border-left: 5px solid #ba0c2f;"><strong>🔧 Recalibrate (0 pts)</strong></td>
                    <td style="padding: 12px; border: 1px solid #ddd;">Critical safety error or PII leak. Resubmission required.</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
