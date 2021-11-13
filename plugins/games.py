from pyrogram import Client, filters
@Client.on_message(filters.command(["football"]))
async def football(bot, message):
         chat_id=message.chat.id
         await bot.send_dice(chat_id=chat_id, emoji='⚽️')
