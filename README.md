# YouTubeNotifications
Discord bot that notifies your subscribers about new videos released on the YouTube platform.

More details:
Every 5 minutes the bot updates information about new publications, if a new video has been released, it publishes information in a special channel that you specify.

Instructions:

1. Go to the bot.py file and on line 28 change your bot token (you can find it on the Discord developer portal), also on line 9 you specify your server ID in test_guilds=[...].

2. Go to the YouTubeNotifications.py file, which is located in the cogs folder, and on line 7 change the channel ID in Discord where the information will be published, then go to line 9 where you put the ID of the YouTube channel from which you want to receive notifications.
