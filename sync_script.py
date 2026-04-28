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

# --- [THE NUCLEAR SCRUB] ---
def nuclear_scrub(html_content, title_label):
    html_content = re.sub(r'<h1>', '<h2>', html_content)
    html_content = re.sub(r'</h1>', '</h2>', html_content)
    if '<table>' in html_content:
        html_content = html_content.replace('<table>', f'<table style="border-collapse: collapse; width: 100%;" border="1"><caption style="font-style: italic; padding: 5px; color: #003366;">{title_label} Data Table</caption>')
        html_content = html_content.replace('<th>', '<th scope="col" style="background-color: #003366; color: #ffffff; padding: 10px;">')
    html_content = html_content.replace('<ul>', '<ul style="list-style-type: disc; margin-bottom: 1rem; margin-left: 1.5rem;">')
    return html_content

def wrap_in_kernel(html_body, label="Course Content"):
    scrubbed_body = nuclear_scrub(html_body, label)
    return f"""<div role="main" aria-label="{label}" style="background-color: #FFF9F0 !important; color: #003366 !important; padding: 2rem; border: 3px solid #003366; border-radius: 12px; font-family: sans-serif; line-height: 1.6;"><div class="awc-fix">{scrubbed_body}</div></div>"""

# --- [THE ORCHESTRATION ENGINE] ---

def deploy_front_page(course_id, file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    raw_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'sane_lists'])
    html_payload = wrap_in_kernel(raw_html, "Course Dashboard")
    
    url = f"{BASE_URL}/api/v1/courses/{course_id}/pages/front-page"
    requests.put(url, headers=headers, json={"wiki_page": {"title": "Course Home", "body": html_payload, "published": True, "front_page": True}})
    
    course_url = f"{BASE_URL}/api/v1/courses/{course_id}"
    requests.put(course_url, headers=headers, json={"course": {"default_view": "wiki"}})
    print(f"[SUCCESS] Front Page Locked for {course_id}")

def deploy_module_content(course_id, module_name, local_folder_path):
    if not os.path.exists(local_folder_path): return

    # 1. Get/Create Module
    mod_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules"
    module_id = requests.post(mod_url, headers=headers, json={"module": {"name": module_name}}).json().get('id')

    # 2. ATOMIC PURGE (Clears items to prevent duplicates)
    items_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules/{module_id}/items"
    for item in requests.get(items_url, headers=headers).json():
        requests.delete(f"{items_url}/{item['id']}", headers=headers)

    # 3. PREFIX PARSER & INJECTION
    files = sorted([f for f in os.listdir(local_folder_path) if f.endswith('.md')])
    for filename in files:
        with open(os.path.join(local_folder_path, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        raw_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'sane_lists'])
        title = filename.replace('.md', '').replace('_', ' ')
        html_payload = wrap_in_kernel(raw_html, title)

        # --- ROUTING LOGIC ---
        if filename.startswith("DISC_"):
            # DISCUSSION ROUTE
            clean_title = title.replace("DISC ", "")
            disc_url = f"{BASE_URL}/api/v1/courses/{course_id}/discussion_topics"
            res = requests.post(disc_url, headers=headers, json={"title": clean_title, "message": html_payload, "published": True}).json()
            requests.post(items_url, headers=headers, json={"module_item": {"type": "Discussion", "content_id": res['id']}})
            
        elif filename.startswith("ASGN_"):
            # ASSIGNMENT ROUTE
            clean_title = title.replace("ASGN ", "")
            asgn_url = f"{BASE_URL}/api/v1/courses/{course_id}/assignments"
            res = requests.post(asgn_url, headers=headers, json={"assignment": {"name": clean_title, "description": html_payload, "points_possible": 100, "submission_types": ["online_upload"], "published": True}}).json()
            requests.post(items_url, headers=headers, json={"module_item": {"type": "Assignment", "content_id": res['id']}})
            
        else:
            # DEFAULT PAGE ROUTE
            slug = title.lower().replace(' ', '-')
            page_url = f"{BASE_URL}/api/v1/courses/{course_id}/pages/{slug}"
            requests.put(page_url, headers=headers, json={"wiki_page": {"title": title, "body": html_payload, "published": True}})
            requests.post(items_url, headers=headers, json={"module_item": {"type": "Page", "page_url": slug}})

        print(f"[ORCHESTRATED] {filename} -> Correct Container")

# ==========================================
# 4. EXECUTION
# ==========================================
if __name__ == "__main__":
    fleet = {"38157": "EXW101", "38147": "EXW150", "38148": "EXW245", "38156": "EXW265"}

    for course_id, folder in fleet.items():
        print(f"\n🚀 ORCHESTRATING MODULES FOR {folder}...")
        deploy_front_page(course_id, f"02_COURSES/{folder}/fall-2026/FRONT_PAGE.md")
        deploy_module_content(course_id, "Module 00: Orientation & Readiness", "01_ADMIN/01_SCAFFOLD/module-0")

    print("\n[!] Orchestration Complete.")