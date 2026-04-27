import time

def deploy_front_page(course_id, file_path, headers):
    if not os.path.exists(file_path): return

    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Kernel wrap with ARS block and Coach Alan signature
    html_content = markdown.markdown(md_content, extensions=['tables'])
    html_payload = f"""
    <div style="background-color: #FFF9F0; color: #003366; padding: 30px; border: 3px solid #003366; border-radius: 10px;">
        {html_content}
    </div>
    """

    base_url = os.getenv('BASE_URL')
    page_url = f"{base_url}/api/v1/courses/{course_id}/pages/front-page"
    
    # Step 1: Push Content & Publish
    print(f"[*] Sending payload to {course_id}...")
    requests.put(page_url, headers=headers, json={{
        "wiki_page": {{"title": "Course Home", "body": html_payload, "published": True}}
    }})
    time.sleep(1) # Breath for the API

    # Step 2: Force Toggle to Front Page
    print("[*] Toggling Front Page status...")
    requests.put(page_url, headers=headers, json={{"wiki_page": {{"front_page": True}}}})
    time.sleep(1)

    # Step 3: Force Course View to Wiki
    print("[*] Locking Home View...")
    course_url = f"{base_url}/api/v1/courses/{course_id}"
    requests.put(course_url, headers=headers, json={{"course": {{"default_view": "wiki"}}}})
    
    print(f"[SUCCESS] Course {course_id} is now fully updated.")