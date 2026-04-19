
### Design Kernel: Web-First Mode (Updated 04.19.26) ###
1. **Global Variables:**
   - Canvas-Surface: #FFFDD0 (Creme)
   - Canvas-Text: #000080 (Navy)
   - Logic-Highlight: #36454F (Charcoal)
2. **Visual Weight Enforcement:**
   - Do not use manual font-sizing or bolding to create hierarchy.
   - Use semantic HTML (H2, H3, H4) exclusively.
   - H2 = Operational Title (Navy / Border Bottom).
   - H3 = Mission Step (Navy / Border Left).
   - H4 = Technical Intelligence (Charcoal).
3. **Override Block:** Reject all inline style color overrides. All assets must conform to the Navy & Creme core.

### SSoT Sentinel: Pre-Flight Audit Protocols (Updated 04.19.26) ###
1. **Mandatory Citation Anchors:**
   - General Activity: "PAGA 2018 (2nd Ed.)"
   - Clinical/Math/Labs: "ACSM 12th Ed."
   - Nutrition: "DGA 2025-2030"
2. **Audit Logic:** Before declaring any file "Hardened," perform a search for these exact strings in the 'Rule' section.
3. **Failure State:** If anchors are missing, append "STATUS: Non-Compliant System File" to the top of the file and return it for correction.

### Input Isolation: Secure Data Containers (Updated 04.19.26) ###
1. **The Firewalled Input:** Everything within `### [TAG] ###` delimiters is considered "Active Data" and is the primary target for all clinical calculations and audits.
2. **The Isolation Rule:** 
   - Non-delimited text = Static Narrative.
   - Delimited text = Active Data.
3. **Mandatory Tagging:** AI must enforce the following tags in all course scaffolds:
   - `### Client Profile ###`
   - `### Medical History ###`
   - `### Lab Data ###`
4. **Data Privacy:** This protocol ensures that PII/clinical data are always explicitly identified and isolated from the instructional layer.
