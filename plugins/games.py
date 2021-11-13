from pyrogram import Client, filters
@Client.on_message(filters.command(["football"]))
async def football(bot, message):
         chat_id=message.chat_id
         await bot.send_dice(emoji="⚽️")
