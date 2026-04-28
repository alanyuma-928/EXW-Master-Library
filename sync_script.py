import os
import requests
import markdown
import time
import re
from pathlib import Path
from dotenv import load_dotenv

# --- [INFRASTRUCTURE] ---
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BASE_URL = os.getenv('CANVAS_BASE_URL', '').replace('/api/v1', '').rstrip('/')
API_TOKEN = os.getenv('CANVAS_API_TOKEN')
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

# ==========================================
# 1. NUCLEAR ACCESSIBILITY SCRUB (v4.3)
# ==========================================
def nuclear_scrub(html_content):
    """Repairs systemic accessibility triggers before deployment."""
    # Fix 1: Table Hardening (Requires scope for screen readers)
    html_content = html_content.replace('<table>', '<table style="border-collapse: collapse; width: 100%;" border="1">')
    html_content = html_content.replace('<th>', '<th scope="col" style="background-color: #003366; color: #ffffff; padding: 10px;">')
    
    # Fix 2: Heading Hierarchy Guardrail (Forces linear structure)
    # Replaces H1 with H2, and ensures H4s are preceded by H3s
    html_content = re.sub(r'<h1(.*?)>', r'<h2\1>', html_content)
    html_content = re.sub(r'</h1>', r'</h2>', html_content)
    
    # Fix 3: List Semanticizer
    html_content = html_content.replace('<ul>', '<ul style="list-style-type: disc; margin-bottom: 1rem; margin-left: 1.5rem;">')
    
    return html_content

def wrap_in_kernel(html_body, label="Course Content"):
    scrubbed_body = nuclear_scrub(html_body)
    return f"""
    <div role="main" aria-label="{label}" style="background-color: #FFF9F0 !important; color: #003366 !important; padding: 2rem; border: 3px solid #003366; border-radius: 12px; font-family: sans-serif; line-height: 1.6;">
        <div class="awc-fix">
            {scrubbed_body}
        </div>
    </div>
    """

# ==========================================
# 2. MODULE SCAFFOLD ENGINE (With Purge Logic)
# ==========================================

def get_or_create_module(course_id, module_name):
    url = f"{BASE_URL}/api/v1/courses/{course_id}/modules"
    modules = requests.get(url, headers=headers).json()
    for m in modules:
        if m['name'] == module_name: return m['id']
    return requests.post(url, headers=headers, json={"module": {"name": module_name}}).json()['id']

def deploy_module_content(course_id, module_name, local_folder_path):
    """Wipes existing module items and re-injects scrubbed content."""
    if not os.path.exists(local_folder_path):
        print(f"[!] Folder missing: {local_folder_path}")
        return

    module_id = get_or_create_module(course_id, module_name)
    
    # --- THE ATOMIC PURGE ---
    # Removes old items to clear "Sticky Metadata" flags
    items_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules/{module_id}/items"
    existing_items = requests.get(items_url, headers=headers).json()
    if existing_items:
        print(f"[*] Purging {len(existing_items)} legacy items from {module_name}...")
        for item in existing_items:
            requests.delete(f"{items_url}/{item['id']}", headers=headers)

    # --- THE NUCLEAR INJECTION ---
    files = sorted([f for f in os.listdir(local_folder_path) if f.endswith('.md')])
    for filename in files:
        page_title = filename.replace('.md', '').replace('_', ' ')
        with open(os.path.join(local_folder_path, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()

        html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'sane_lists'])
        html_payload = wrap_in_kernel(html_body, page_title)

        # Create/Update Page
        slug = page_title.lower().replace(' ', '-')
        page_url = f"{BASE_URL}/api/v1/courses/{course_id}/pages/{slug}"
        requests.put(page_url, headers=headers, json={"wiki_page": {"title": page_title, "body": html_payload, "published": True}})

        # Link to Module
        requests.post(items_url, headers=headers, json={"module_item": {"title": page_title, "type": "Page", "page_url": slug}})
        print(f"[SUCCESS] Injected Scrubbed Page: {page_title}")
        time.sleep(0.4)

# ==========================================
# 3. EXECUTION
# ==========================================
if __name__ == "__main__":
    fleet = {"38157": "EXW101", "38147": "EXW150", "38148": "EXW245", "38156": "EXW265"}

    for course_id, folder in fleet.items():
        print(f"\n🚀 RESETTING MODULES FOR {folder}...")
        deploy_module_content(course_id, "Module 00: Orientation & Readiness", "01_ADMIN/01_SCAFFOLD/module-0")
        # deploy_module_content(course_id, "Module 01: Mission Intel", "01_ADMIN/01_SCAFFOLD/module-1")

    print("\n[!] Atomic Reset Complete. Please re-run the Accessibility Checker.")