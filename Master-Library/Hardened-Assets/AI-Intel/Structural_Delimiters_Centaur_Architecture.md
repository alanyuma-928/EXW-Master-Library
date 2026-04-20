## The "Centaur" Architecture: Mastering Structural Delimiters

Another great student question about delimiters:

> *Hi Coach,* > *What does a Structural Delimiter (###) look like on a prompt? Could you please give me an example?*

**Here you go!**

In our **EXW265 Clinical AI Residency**, a **Structural Delimiter** (like `###` or `---`) acts as a "firewall" between different parts of your instructions. Think of it as the clear markings on a runway—it tells the AI "Engine" exactly where one section ends and the next begins, so the data doesn't get "tangled" in flight.

Without delimiters, the AI might confuse your **Context** with your **Task**, leading to a "hallucination" where it follows instructions it was only supposed to reference.

### The "Centaur" Prompt Example
Here is how an **Architect** (Prompt Engineer) structures a clinical query using delimiters to organize the **Persona-Task-Context-Format** framework:

---

### The Centaur Architecture: Persona-Task-Context-Format

**Persona:** Act as a Clinical Exercise Physiologist at the Matador Wellness Center. You are a specialist in PAGA 2nd Edition guidelines for clinical populations.

###

**Task:** Create a 4-week progressive walking plan for a patient recovering from a mild myocardial infarction.

###

**Context:** The client is a 62-year-old male. He has completed Phase II Cardiac Rehab and is cleared for independent exercise.
* **Safety Constraint:** Keep intensity between RPE 3–4 (Light to Moderate).
* **Onvida Rule:** No PII included. Client is a retired "Agricultural Worker" in Yuma.

###

**Format:** Provide the plan in a clear table format. Include a "Red Flag" section at the bottom listing symptoms that require immediate cessation of exercise (Angina, dizziness, etc.).

###


---

### Why the ### Matters for the Pilot
* **Visual Check:** When you look at your prompt, you can instantly see if you missed a section (e.g., "Did I forget the Context?").
* **The "Engine" Logic:** Large Language Models (the Engine) are trained to recognize `###` as a **Header Delimiter**. It prevents "Instruction Bleed," where the AI might mistakenly treat the "Red Flag" symptoms in the Format section as part of the patient's current **Context**.
* **Audit Trail:** If the AI hallucinates, you can look back at your "blocks" and see if your instructions were too crowded.

### Why do we use them in Yuma?
1. **Precision:** It forces the AI to "Slow is Smooth" by categorizing the data before it starts generating.
2. **The Auditor's Edge:** It makes it easier for you, the **Pilot**, to audit the output later because you can see exactly which "block" of instructions the AI might have missed.
3. **Safety:** It prevents the AI from mixing up the "Small Town" context with the clinical task, keeping our neighbors' data structured and secure.

Best,  
**Coach Alan Pruitt**

---
**Author:** Coach Alan Pruitt  
**Version:** 1.0 (Fall 2026 Prep)  
**License:** CC BY-NC 4.0

**SSoT:** PAGA 2018 (2nd Ed)