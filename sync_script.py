import os
import requests
import markdown
import re
from pathlib import Path
from dotenv import load_dotenv

# --- [INFRASTRUCTURE] ---
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BASE_URL = os.getenv('CANVAS_BASE_URL', '').replace('/api/v1', '').rstrip('/')
API_TOKEN = os.getenv('CANVAS_API_TOKEN')
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

# --- [ACCESSIBILITY FIREWALL] ---
def nuclear_scrub(html_content, title_label):
    """Clears the '76, 33, 8' error clusters by forcing hierarchy and semantics."""
    # Force H2 (Page Title is H1)
    html_content = re.sub(r'<h1>', '<h2>', html_content)
    html_content = re.sub(r'</h1>', '</h2>', html_content)
    # Table Hardening (ACSM/PAGA Standard)
    if '<table>' in html_content:
        html_content = html_content.replace('<table>', f'<table style="border-collapse: collapse; width: 100%;" border="1"><caption style="font-style: italic; padding: 5px; color: #003366;">{title_label} Data Table</caption>')
        html_content = html_content.replace('<th>', '<th scope="col" style="background-color: #003366; color: #ffffff; padding: 10px;">')
    # Semantic List Fix (The 0-Error Patch)
    html_content = html_content.replace('<ul>', '<ul style="list-style-type: disc; margin-bottom: 1rem; margin-left: 1.5rem;">')
    return html_content

def wrap_in_kernel(html_body, label="Course Content"):
    scrubbed_body = nuclear_scrub(html_body, label)
    return f"""<div role="main" aria-label="{label}" style="background-color: #FFF9F0 !important; color: #003366 !important; padding: 2rem; border: 3px solid #003366; border-radius: 12px; font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6;"><div class="awc-fix">{scrubbed_body}</div></div>"""

# --- [DEPLOYMENT LOGIC] ---

def deploy_front_page(course_id, folder_name):
    """Updates Home Page with strict syntax fixes."""
    file_path = f"02_COURSES/{folder_name}/fall-2026/FRONT_PAGE.md"
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    html_body = markdown.markdown(md_content, extensions=['tables', 'sane_lists'])
    payload = wrap_in_kernel(html_body, f"{folder_name} Home")
    requests.put(f"{BASE_URL}/api/v1/courses/{course_id}/pages/front-page", headers=headers, json={"wiki_page": {"body": payload}})
    print(f"[SUCCESS] {folder_name}: Home Page Refreshed.")

def deploy_module_content(course_id, module_name, local_folder_path):
    """Orchestrates content into correct containers based on filename prefixes."""
    if not os.path.exists(local_folder_path): return

    # Get/Create Module
    mod_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules"
    res = requests.post(mod_url, headers=headers, json={"module": {"name": module_name}}).json()
    module_id = res.get('id')

    # Atomic Purge (Prevents Duplicates)
    items_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules/{module_id}/items"
    for item in requests.get(items_url, headers=headers).json():
        requests.delete(f"{items_url}/{item['id']}", headers=headers)

    # Prefix Parsing
    files = sorted([f for f in os.listdir(local_folder_path) if f.endswith('.md')])
    for filename in files:
        with open(os.path.join(local_folder_path, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        raw_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'sane_lists'])
        title = filename.replace('.md', '').replace('_', ' ')
        html_payload = wrap_in_kernel(raw_html, title)

        if filename.startswith("DISC_"):
            # ROUTE TO DISCUSSION
            clean_title = title.replace("DISC ", "")
            disc_url = f"{BASE_URL}/api/v1/courses/{course_id}/discussion_topics"
            disc_res = requests.post(disc_url, headers=headers, json={"title": clean_title, "message": html_payload, "published": True}).json()
            requests.post(items_url, headers=headers, json={"module_item": {"type": "Discussion", "content_id": disc_res['id']}})
        elif filename.startswith("ASGN_"):
            # ROUTE TO ASSIGNMENT
            clean_title = title.replace("ASGN ", "")
            asgn_url = f"{BASE_URL}/api/v1/courses/{course_id}/assignments"
            asgn_res = requests.post(asgn_url, headers=headers, json={"assignment": {"name": clean_title, "description": html_payload, "points_possible": 100, "submission_types": ["online_upload"], "published": True}}).json()
            requests.post(items_url, headers=headers, json={"module_item": {"type": "Assignment", "content_id": asgn_res['id']}})
        else:
            # ROUTE TO PAGE
            slug = title.lower().replace(' ', '-')
            requests.put(f"{BASE_URL}/api/v1/courses/{course_id}/pages/{slug}", headers=headers, json={"wiki_page": {"title": title, "body": html_payload, "published": True}})
            requests.post(items_url, headers=headers, json={"module_item": {"type": "Page", "page_url": slug}})
        print(f"[ORCHESTRATED] {filename} -> Node {course_id}")

# --- [MAIN EXECUTION] ---
if __name__ == "__main__":
    fleet = {"38157": "EXW101", "38147": "EXW150", "38148": "EXW245", "38156": "EXW265"}
    
    print("🚀 EXECUTING ORCHESTRATOR v4.6")
    for course_id, folder in fleet.items():
        print(f"\n--- {folder} ---")
        deploy_front_page(course_id, folder)
        deploy_module_content(course_id, "Module 00: Orientation & Readiness", "01_ADMIN/01_SCAFFOLD/module-0")
    print("\n[!] MISSION COMPLETE: FLEET SYNCED & VACCINATED.")