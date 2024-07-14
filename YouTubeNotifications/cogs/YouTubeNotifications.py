import disnake
from disnake.ext import commands
import asyncio
import feedparser

# Replace 'YOUR_CHANNEL_ID' with the ID of the channel the bot will send messages to
CHANNEL_ID = 'YOUR_CHANNEL_ID'
# Replace 'YOUR_YOUTUBE_CHANNEL_URL' with the URL of the YouTube channel the bot will follow
YOUTUBE_CHANNEL_URL = 'YOUR_YOUTUBE_CHANNEL_URL'

class YouTubeNotifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_video_id = None

    async def check_for_new_videos(self):
        while True:
            try:
                feed = feedparser.parse(YOUTUBE_CHANNEL_URL)
                # If there are new videos in the feed
                if self.last_video_id != feed.entries[0].id:
                    self.last_video_id = feed.entries[0].id
                    # Get new video details
                    title = feed.entries[0].title
                    link = feed.entries[0].link
                    # Send a message to the channel
                    channel = self.bot.get_channel(CHANNEL_ID)
                    await channel.send(f"Новое видео на YouTube: {title}\n{link}")
            except Exception as e:
                print(f"Error checking new videos: {e}")
            # Check out new videos every 5 minutes
            await asyncio.sleep(300)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"YouTube-бот запущен как {self.bot.user}")
        # Run the task to check for new videos
        self.bot.loop.create_task(self.check_for_new_videos())

def setup(bot: commands.Bot):
    bot.add_cog(YouTubeNotifier(bot))