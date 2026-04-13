# **Strategy: AI Quiz Master Architecture (v2.0)**

## **Retiring legacy LMS Quizzes for AI Readiness Gates**

To maintain high-fidelity workforce training, we are pivoting away from the Canvas "New Quiz" tool. All "Flight Manual Checks" are now handled via the **AI Toolkit** to ensure that the student can apply the SSoT Rules in a conversational, clinical context.

### **1\. The Readiness Gate (Assignment Structure)**

* **LMS Component:** Canvas Assignment (Text Entry Only).  
* **Assignment Group:** 🧠 Flight Manual Checks (20%).  
* **Grading:** Complete/Incomplete (10/0 SEAL Scale).  
* **The Mission:** The student must pass a 5-minute technical audit with the **Quiz Master** persona.

### **2\. The AI Quiz Master Persona (Gemini Environment)**

The Quiz Master is the **"Technical Gatekeeper."** Its logic is programmed to:

1. **Enforce Delimiters:** If the student fails to wrap their rule-check in \#\#\#, the Quiz Master immediately triggers a **"Gate Closed: Recalibrate"** response.  
2. **Verify SSoT Authority:** The student must upload the required PDF/Markdown (ACSM, PAGA, or YTSG) using the **Add File (+) button**.  
3. **Randomized Scenario Audit:** The Quiz Master provides one raw metric (e.g., "WBGT is 91°F") and asks the student: *"Identify the Safety Gate Rule for this pattern."*

### **3\. Submission Requirements (The Audit Trail)**

To receive credit for the Readiness Gate, the student must submit:

1. **The Readiness Statement:** A one-sentence declaration: *"I have verified the safety gates for Module \[X\] against the SSoT."*  
2. **The Quiz Transcript:** The full conversation showing the Quiz Master confirming: *"Pass: Technical Readiness Achieved."*

### 

### **4\. Why 20% Weighting?**

This weight is retained to emphasize that **Technical Safety** is a non-negotiable professional standard. If a student cannot pass the gate (Rule), they are not permitted to perform the Lab (Solve).

**Institutional Agility Note:** This move eliminates the friction of building/maintaining Canvas Quiz banks and forces students into the Gemini environment, where the actual professional work occurs.