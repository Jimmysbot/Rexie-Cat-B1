from pyrogram import Client, filters
@Client.on_message(filters.command(["football"]))
async def football(bot, message):
         await bot.send_dice(emoji="⚽️")
