'''
Open a local file and read its content
Each line is an RSS feed to be scanned
If the feed is a YouTube channel, add to channels 
If the feed is a YouTube playlist, add to playlists
If the feed is a YouTube video, add to videos

'''
import feedparser
import yt_dlp


# Path to the file containing the list of RSS feeds
RSS_FEEDS_FILE = 'channels.txt'

# Read the file containing the list of RSS feeds
with open(RSS_FEEDS_FILE, 'r') as file:
    feeds = file.readlines()

# Initialize lists to store the channels, playlists, and videos to be scanned
channels = []
playlists = []
videos = []

# Loop through the feeds
for feed in feeds:
    feed = feed.strip()
    if 'channel' in feed:
        channels.append(feed)
    elif 'playlist' in feed:
        playlists.append(feed)
    elif 'watch' in feed:
        videos.append(feed)

for channel in channels:
    print(channel)
    # Parse the RSS feed
    feed = feedparser.parse(channel)

    # Check if the feed is fetched successfully
    if feed.bozo == 0:
        print(f"Channel: {feed.feed.title}")
        for entry in feed.entries:
            title = entry.title
            link = entry.link
            author = entry.author
            published = entry.published
            print(f"Author: {author}\nTitle: {title}\nLink: {link}\nPublished at: {published}\n")

            download_flag = "n"
            download_flag = input("Do you want to download this video? (y/n): ")
            if download_flag == "y":
                ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'outtmpl': f'{title}.mp4',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
            else:
                print("Video not downloaded.")
    else:
        print("Error fetching the RSS feed.")