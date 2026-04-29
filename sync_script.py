import os
import requests
import markdown
import re
from pathlib import Path
from dotenv import load_dotenv

# --- [INFRASTRUCTURE] ---
# Loads credentials from your .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BASE_URL = os.getenv('CANVAS_BASE_URL', '').replace('/api/v1', '').rstrip('/')
API_TOKEN = os.getenv('CANVAS_API_TOKEN')
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

# --- [ACCESSIBILITY FIREWALL] ---
def nuclear_scrub(html_content, title_label):
    """Force-cleans HTML to resolve common Canvas Accessibility flags."""
    # 1. Header Hierarchy: Ensure no H1 tags (reserved for Canvas Title)
    html_content = re.sub(r'<h1>', '<h2>', html_content)
    html_content = re.sub(r'</h1>', '</h2>', html_content)
    
    # 2. Table Hardening: Inject semantic captions and scope headers
    if '<table>' in html_content:
        html_content = html_content.replace('<table>', f'<table style="border-collapse: collapse; width: 100%;" border="1"><caption style="font-style: italic; padding: 5px; color: #003366;">{title_label} Data Table</caption>')
        html_content = html_content.replace('<th>', '<th scope="col" style="background-color: #003366; color: #ffffff; padding: 10px;">')
    
    # 3. List Semantic Fix: Ensure padding and bullet visibility
    html_content = html_content.replace('<ul>', '<ul style="list-style-type: disc; margin-bottom: 1rem; margin-left: 1.5rem;">')
    return html_content

def wrap_in_kernel(html_body, label="Course Content"):
    """Wraps content in the Navy & Creme 'Sovereign' Container."""
    scrubbed_body = nuclear_scrub(html_body, label)
    return f"""
    <div role="main" aria-label="{label}" style="background-color: #FFF9F0; color: #003366; padding: 2rem; border: 3px solid #003366; border-radius: 12px; font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6;">
        <div class="awc-orchestrated-content">
            {scrubbed_body}
        </div>
    </div>"""

# --- [DEPLOYMENT ENGINES] ---

def deploy_front_page(course_id, folder_name):
    """Syncs the course-specific FRONT_PAGE.md with the Air-Gap spacing fix."""
    file_path = f"02_COURSES/{folder_name}/fall-2026/FRONT_PAGE.md"
    if not os.path.exists(file_path): 
        print(f"[ERROR] Could not find {file_path}")
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Render with 'sane_lists' to handle the list formatting errors
    html_body = markdown.markdown(md_content, extensions=['tables', 'sane_lists', 'fenced_code'])
    payload = wrap_in_kernel(html_body, f"{folder_name} Welcome")
    
    endpoint = f"{BASE_URL}/api/v1/courses/{course_id}/front_page"
    requests.put(endpoint, headers=headers, json={"wiki_page": {"body": payload}})
    print(f"[SUCCESS] {folder_name}: Front Page Orchestrated.")

def deploy_module_content(course_id, module_name, local_folder_path):
    """Prefix-Parser Engine: Routes content to Discussion, Assignment, or Page containers."""
    if not os.path.exists(local_folder_path): return

    # 1. Module Management
    mod_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules"
    module_res = requests.post(mod_url, headers=headers, json={"module": {"name": module_name}}).json()
    module_id = module_res.get('id')

    # 2. Atomic Purge (Prevents Duplicates in the Module view)
    items_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules/{module_id}/items"
    current_items = requests.get(items_url, headers=headers).json()
    if isinstance(current_items, list):
        for item in current_items:
            requests.delete(f"{items_url}/{item['id']}", headers=headers)

    # 3. File Processing & Routing
    files = sorted([f for f in os.listdir(local_folder_path) if f.endswith('.md')])
    for filename in files:
        with open(os.path.join(local_folder_path, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        raw_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'sane_lists'])
        title = filename.replace('.md', '').replace('_', ' ')
        html_payload = wrap_in_kernel(raw_html, title)

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
            # DEFAULT WIKI PAGE ROUTE
            slug = title.lower().replace(' ', '-')
            page_url = f"{BASE_URL}/api/v1/courses/{course_id}/pages/{slug}"
            requests.put(page_url, headers=headers, json={"wiki_page": {"title": title, "body": html_payload, "published": True}})
            requests.post(items_url, headers=headers, json={"module_item": {"type": "Page", "page_url": slug}})

        print(f"[ORCHESTRATED] Node {course_id} | {filename}")

# --- [MAIN EXECUTION] ---
if __name__ == "__main__":
    # Fleet Definitions: Course ID -> Folder Name
    fleet = {
        "38157": "EXW101",
        "38147": "EXW150",
        "38148": "EXW245",
        "38156": "EXW265"
    }

    print("🚀 EXECUTING SOVEREIGN ORCHESTRATOR v4.8")
    for course_id, folder in fleet.items():
        print(f"\n--- Processing {folder} (ID: {course_id}) ---")
        # 1. Refresh Home Pages
        deploy_front_page(course_id, folder)
        # 2. Deploy Module 0 (The Vaccination Pass)
        deploy_module_content(course_id, "Module 00: Orientation & Readiness", "01_ADMIN/01_SCAFFOLD/module-0")
        
    print("\n[!] MISSION COMPLETE: FLEET IS SYNCED AND VACCINATED.")