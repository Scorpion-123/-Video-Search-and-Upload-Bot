import os
import hashlib
import asyncio
import aiohttp
import aiofiles
from tqdm import tqdm
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
BASE_API_URL = "https://api.socialverseapp.com"
UPLOAD_DIR = "./videos"
FLIC_TOKEN = "<YOUR_TOKEN>"
HEADERS = {
    "Flic-Token": FLIC_TOKEN,
    "Content-Type": "application/json"
}

# Async Functions
async def get_upload_url(session, video_title):
    """Fetches the pre-signed upload URL and hash from the API."""
    async with session.post(f"{BASE_API_URL}/posts/generate-upload-url", headers=HEADERS) as response:
        if response.status != 200:
            raise Exception(f"Failed to get upload URL: {response.status}")
        data = await response.json()
        return data["upload_url"], data["hash"]

async def upload_video(session, upload_url, file_path):
    """Uploads the video to the server using the pre-signed URL."""
    async with aiofiles.open(file_path, 'rb') as f:
        file_data = await f.read()
    async with session.put(upload_url, data=file_data) as response:
        if response.status not in (200, 201):
            raise Exception(f"Failed to upload video: {response.status}")
    return True

async def create_post(session, title, video_hash, category_id):
    """Creates a post using the uploaded video hash."""
    payload = {
        "title": title,
        "hash": video_hash,
        "is_available_in_public_feed": False,
        "category_id": category_id
    }
    async with session.post(f"{BASE_API_URL}/posts", headers=HEADERS, json=payload) as response:
        if response.status != 200:
            raise Exception(f"Failed to create post: {response.status}")
        return await response.json()

async def process_video(file_path, title, category_id):
    """Complete process of uploading a video."""
    async with aiohttp.ClientSession() as session:
        try:
            print(f"Processing: {file_path}")
            upload_url, video_hash = await get_upload_url(session, title)
            await upload_video(session, upload_url, file_path)
            await create_post(session, title, video_hash, category_id)
            print(f"Uploaded and post created for: {title}")
            os.remove(file_path)
            print(f"Deleted local file: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# Directory Monitoring
class VideoFileHandler(FileSystemEventHandler):
    def __init__(self, category_id):
        self.category_id = category_id

    def on_created(self, event):
        if event.src_path.endswith(".mp4"):
            file_path = event.src_path
            title = os.path.basename(file_path).rsplit('.', 1)[0]
            asyncio.run(process_video(file_path, title, self.category_id))

def monitor_directory(category_id):
    """Monitors the videos directory for new files."""
    event_handler = VideoFileHandler(category_id)
    observer = Observer()
    observer.schedule(event_handler, UPLOAD_DIR, recursive=False)
    observer.start()
    print("Monitoring directory for new videos...")
    try:
        while True:
            asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Main Script
if __name__ == "__main__":
    category_id = 1  # Replace with your desired category ID
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    monitor_directory(category_id)
