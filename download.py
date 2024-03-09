import requests
import os

# Set the URL of the file to download
url = "https://d.apkpure.com/b/APK/com.blacklotus.app?versionCode=3"

# Set the name of the file to save the downloaded content to
filename = "com.blacklotus.app.apk"

# Set the user-agent to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Download the file from the URL with the specified user-agent
response = requests.get(url, headers=headers)

# Save the downloaded content to a local file
with open(filename, 'wb') as f:
    f.write(response.content)

# Print a message indicating that the download was successful
print(f"Downloaded {url} to {filename}")

# Delete the file
os.remove(filename)

# Print a message indicating that the file was deleted
print(f"Deleted {filename}")