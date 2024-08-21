# YouTubeNotifications Disnake|Discord
EN:  
  Discord bot that notifies your subscribers about new videos released on the YouTube platform.

  More details:
  Every 5 minutes the bot updates information about new publications, if a new video has been released, it publishes information in a special channel that you specify.
  
  Instructions:
  
  1. Go to the bot.py file and on line 28 change your bot token (you can find it on the Discord developer portal), also on line 9 you specify your server ID in test_guilds=[...].
  
  2. Go to the YouTubeNotifications.py file, which is located in the cogs folder, and on line 7 change the channel ID in Discord where the information will be published, then go to line 9 where you put the ID of the YouTube channel from which you want to receive       notifications.

RU: 
  Дискорд бот который оповещает ваших подписчиков о новых вышедших видео на платформе ютуб.
  
  Подробнее: 
  Каждые 5 минут бот обновляет информацию о новых публикациях если вышло новое видео то он опубликовывает информацию в специальный канал который вы указываете.
  
  Инструкция: 
  1. Заходите в файл bot.py и на 28 строчке меняем свой токен бота(его вы можете найти на дискорд девелопер портал), так же на 9 строчке вы указываете в test_guilds=[...] свой айди сервера.
  2. Заходите в файл YouTubeNotifications.py который находиться в папке cogs и на 7 строчке изменяете айди канала в дискорде где будет публиковаться информация, далее идете на 9 строчку где ставите айди ютуб канала с которого хотите получать уведомления.
