import requests
import os

### SETTINGS & AUTHENTICATION ###
# API_TOKEN and BASE_URL are pulled from your .env file
# Ensure FRONT_PAGE_FILE = "FRONT_PAGE.md" exists in your course root

def deploy_front_page(course_id, file_path, headers):
    """
    Targets the Canvas Wiki Pages endpoint to set the Course Home Page.
    """
    if not os.path.exists(file_path):
        print(f"[!] No Front Page file found at {file_path}. Skipping.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    # Convert Markdown to your Navy/Creme HTML Kernel
    html_payload = f"""
    <div style="background-color: #FFF9F0; color: #003366; padding: 25px; border: 2px solid #003366; border-radius: 8px;">
        {content}
    </div>
    """

    # Step 1: Create or Update the Wiki Page
    url = f"{os.getenv('BASE_URL')}/api/v1/courses/{course_id}/pages/front-page"
    data = {
        "wiki_page": {
            "title": "Course Home",
            "body": html_payload,
            "published": True,
            "front_page": True # The "Toggle"
        }
    }

    response = requests.put(url, headers=headers, json=data)

    # Step 2: Force Canvas to use the Wiki Front Page as the Course Home
    if response.status_code == 200:
        course_url = f"{os.getenv('BASE_URL')}/api/v1/courses/{course_id}"
        course_data = {"course": {"default_view": "wiki"}}
        requests.put(course_url, headers=headers, json=course_data)
        print(f"[SUCCESS] Front Page deployed and locked for Course ID: {course_id}")
    else:
        print(f"[ERROR] Failed to deploy Front Page: {response.status_code}")

### MAIN EXECUTION LOOP ###
# Add 'deploy_front_page' call to your existing [D]eploy Fleet logic