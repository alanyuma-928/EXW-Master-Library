import os
import requests
import markdown
from datetime import datetime, timedelta
from dotenv import load_dotenv

# ===============================================================
# 1. LOAD SSoT CONFIGURATIONS (.env)
# ===============================================================
load_dotenv()

BASE_URL = os.getenv("CANVAS_BASE_URL")
TOKEN = os.getenv("CANVAS_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

COURSES = {
    "EXW101": os.getenv("ID_EXW101"),
    "EXW150": os.getenv("ID_EXW150"),
    "EXW245": os.getenv("ID_EXW245"),
    "EXW265": os.getenv("ID_EXW265")
}

AWC_HOLIDAYS = ["2026-09-07", "2026-11-11", "2026-11-26", "2026-11-27"]

# ===============================================================
# 2. CORE FUNCTIONS
# ===============================================================

def test_canvas_connection():
    print("\n### INITIALIZING CONNECTION TEST ###")
    endpoint = f"{BASE_URL}/users/self"
    try:
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()
        print(f"SUCCESS: Connected to AWC Instance as {response.json().get('name')}")
        return True
    except Exception as e:
        print(f"CONNECTION ERROR: {e}")
        return False

def purge_course_content(course_id, course_name):
    print(f"\n[!] PURGING {course_name} (ID: {course_id})")
    for endpoint in ["modules", "pages"]:
        url = f"{BASE_URL}/courses/{course_id}/{endpoint}"
        items = requests.get(f"{url}?per_page=100", headers=HEADERS).json()
        if isinstance(items, list):
            for item in items:
                key = 'id' if endpoint == 'modules' else 'url'
                requests.delete(f"{url}/{item.get(key)}", headers=HEADERS)
    print(f"DONE: {course_name} is cleared.")

def create_16_week_scaffold(course_id, course_name, start_date_str="2026-08-17"):
    print(f"\n[+] SCAFFOLDING {course_name}")
    base_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    for i in range(17):
        name = "Module 0: Orientation" if i == 0 else f"Module {i:02d}"
        if i == 16: name = "Module 16: Finals & Course Wrap"
        
        # Temporal Logic
        days_offset = 0 if i == 0 else (1 if i < 16 else 0)
        weeks_offset = 0 if i == 0 else (i - 1 if i < 16 else 15)
        unlock_date = base_date + timedelta(days=days_offset) + timedelta(weeks=weeks_offset)
        
        # Holiday Audit
        mod_date_str = unlock_date.strftime("%Y-%m-%d")
        holiday_alert = " [!] CAMPUS CLOSED" if mod_date_str in AWC_HOLIDAYS else ""

        payload = {
            "module": {
                "name": f"{name}{holiday_alert}",
                "position": i + 1,
                "unlock_at": unlock_date.isoformat(),
                "published": False
            }
        }
        requests.post(f"{BASE_URL}/courses/{course_id}/modules", headers=HEADERS, json=payload)
    print(f"  + 17-Module Scaffold Complete for {course_name}")

def inject_markdown_page(course_id, module_id, local_path):
    with open(local_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    body_html = markdown.markdown(md_content)
    wrapped_html = f"""
    <div style="background-color: #FDF5E6; color: #002D62; padding: 30px; font-family: sans-serif; border: 1px solid #002D62;">
        {body_html}
    </div>
    """
    # Clean title: 0.1_The_Master_Library.md -> 0.1 The Master Library
    title = os.path.basename(local_path).replace('.md', '').replace('_', ' ')
    
    page_res = requests.post(
        f"{BASE_URL}/courses/{course_id}/pages",
        headers=HEADERS,
        json={"wiki_page": {"title": title, "body": wrapped_html, "published": True}}
    )
    
    if page_res.status_code in [200, 201]:
        page_url = page_res.json().get('url')
        requests.post(
            f"{BASE_URL}/courses/{course_id}/modules/{module_id}/items",
            headers=HEADERS,
            json={"module_item": {"title": title, "type": "Page", "page_url": page_url}}
        )
        print(f"    - Injected: {title}")

def deploy_full_fleet():
    """
    Calibrated for: 02_COURSES/EXW245/fall-2026/module-0
    """
    for course_key, cid in COURSES.items():
        if not cid: continue
        
        print(f"\n>>> DEPLOYING CONTENT TO {course_key} (ID: {cid})")
        # Calibrated for hyphenated folder name
        course_root = f"02_COURSES/{course_key}/fall-2026"
        
        if not os.path.exists(course_root):
            print(f"  [!] Missing directory: {course_root}")
            continue

        canvas_modules = requests.get(f"{BASE_URL}/courses/{cid}/modules", headers=HEADERS).json()

        for folder in sorted(os.listdir(course_root)):
            # Calibrated for module-x naming
            if folder.startswith("module-"):
                local_mod_path = os.path.join(course_root, folder)
                mod_num = folder.split("-")[1] 
                
                # Match logic for Module 0 and Module 01+
                search_term = f"Module {mod_num}" if int(mod_num) > 0 else "Module 0:"
                canvas_mod = next((m for m in canvas_modules if search_term in m['name']), None)
                
                if canvas_mod:
                    print(f"  -- Syncing {folder} --")
                    for md_file in sorted(os.listdir(local_mod_path)):
                        if md_file.endswith(".md"):
                            inject_markdown_page(cid, canvas_mod['id'], os.path.join(local_mod_path, md_file))

# ===============================================================
# 3. MAIN EXECUTION GATE
# ===============================================================
if __name__ == "__main__":
    if test_canvas_connection():
        print("\n[P] Purge | [S] Scaffold | [D] Deploy Fleet | [Q] Quit")
        choice = input("Select Action: ").lower()
        if choice == 'p':
            for name, cid in COURSES.items(): purge_course_content(cid, name)
        elif choice == 's':
            for name, cid in COURSES.items(): create_16_week_scaffold(cid, name)
        elif choice == 'd':
            deploy_full_fleet()