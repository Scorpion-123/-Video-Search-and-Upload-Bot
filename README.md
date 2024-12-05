# 🎥 SocialVerse Video Bot

A Python-based bot for downloading videos from **Instagram**, **TikTok**, and **Reddit** and uploading them to a server using REST APIs. The bot supports asynchronous operations, directory monitoring, and auto-deletion of local files after a successful upload.

---

## 📋 **Features**

### Core Features
1. **Search and Download Videos:** Download videos from specified platforms (Instagram, TikTok, and Reddit).
2. **Upload Videos to Server:** Upload videos using provided API endpoints with pre-signed URLs.
3. **Auto-Delete Local Files:** Automatically delete local `.mp4` files after successful uploads.
4. **Directory Monitoring:** Monitors the `/videos` directory for new `.mp4` files and processes them automatically.
5. **Async Operations:** Utilizes `asyncio` for concurrent downloads, uploads, and API calls.

---

## 🛠️ **Technical Requirements**

- **Programming Language:** Python
- **Libraries:**
  - `aiohttp` for asynchronous API requests.
  - `watchdog` for directory monitoring.
  - `tqdm` for progress bars.
  - `asyncio` for concurrency.
  - `aiofiles` for non-blocking file operations.
- **Error Handling:** Gracefully handles API errors, file I/O issues, and network interruptions.

---

## 🚀 **Setup and Installation**

### Prerequisites
1. Python 3.8+ installed on your system.
2. Install required dependencies:

   ```bash
   pip install aiohttp watchdog tqdm aiofiles
3. Replace <YOUR_TOKEN> in the script with your SocialVerse API token.

---

## 🛠️ **How It Works**
1. The bot monitors the `/videos` directory for `.mp4` files.
2. For each new video file:
   - It fetches an upload URL and hash using the **Get Upload URL** API.
   - The video is uploaded using the pre-signed URL.
   - A post is created on the SocialVerse platform using the **Create Post** API.
3. After successful upload and post creation, the local video file is deleted.
4. All operations are performed asynchronously to ensure optimal performance.

--- 

## 📁 Basic Project Structure
```
video-bot/
├── main.py                # Main script
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```
