📝 API Integration
1. Get Upload URL
Endpoint: https://api.socialverseapp.com/posts/generate-upload-url
Headers:
json
Copy code
{
    "Flic-Token": "<YOUR_TOKEN>",
    "Content-Type": "application/json"
}
Response: Contains the upload_url and hash for the video.
2. Upload Video
Use the pre-signed URL obtained in Step 1 with a PUT request to upload the video file.
3. Create Post
Endpoint: https://api.socialverseapp.com/posts
Headers:
json
Copy code
{
    "Flic-Token": "<YOUR_TOKEN>",
    "Content-Type": "application/json"
}
Body:
json
Copy code
{
    "title": "<video title>",
    "hash": "<hash from Step 1>",
    "is_available_in_public_feed": false,
    "category_id": <category_id>
}
📂 Project Structure
plaintext
Copy code
.
├── bot.py                # Main script for the bot
├── videos/               # Directory for monitoring .mp4 files
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
🔄 How It Works
The bot monitors the /videos directory for new .mp4 files.
When a new file is detected:
It fetches an upload URL and hash using the Get Upload URL API.
Uploads the video file to the server using the pre-signed URL.
Creates a post entry in the database using the Create Post API.
Deletes the local file after a successful upload.
Operations like API calls and uploads are handled asynchronously for optimal performance.
▶️ Running the Bot
Replace <YOUR_TOKEN> in the script with your API token.

Run the bot:

bash
Copy code
python bot.py
Add .mp4 files to the /videos directory, and the bot will process them automatically.

⚠️ Error Handling
Handles API request failures gracefully with retries and logs.
Skips files that fail during upload and logs the errors for review.
🌟 Future Enhancements
Platform Integration: Add direct support for downloading videos from Instagram, TikTok, and Reddit using their APIs.
Customizable Categories: Allow dynamic selection of category_id for uploads.
Detailed Logs: Implement a logging system to track progress and errors.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

💡 Contact
For any questions or support, please contact:

Email: support@socialverseapp.com
Website: SocialVerseApp
markdown
Copy code

### Instructions for Usage:
1. Copy the above content into a `README.md` file in your project directory.
2. Adjust the contact and licensing information as needed.
3. Provide the `requirements.txt` file for dependencies:

```plaintext
aiohttp
watchdog
tqdm
aiofiles
