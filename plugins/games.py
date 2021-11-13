from pyrogram import Client, filters
@Client.on_message(filters.command(["football"]))
async def football(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚽️')

@Client.on_message(filters.command(["spin"]))
async def spin(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎰')

@Client.on_message(filters.command(["dice"]))
async def dice(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎲')

@Client.on_message(filters.command(["dart"]))
async def dart(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='🎯')
