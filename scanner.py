'''
Open a local file and read its content
Each line is an RSS feed to be scanned
If the feed is a YouTube channel, add it to the list of channels to be scanned
If the feed is a YouTube playlist, add it to the list of playlists to be scanned
If the feed is a YouTube video, add it to the list of videos to be scanned

'''
import os
import feedparser


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
    else:
        print("Error fetching the RSS feed.")