from pyrogram import Client, filters
@Client.on_message(filters.private & (filters.command(["football"]))
async def football(bot, message):
         await bot.send_sticker("CAACAgUAAxkBAAIFKmDd2r4NMyGSyWgVu2v-fQxvJxBxAAL1AgACufE4VgHHxPJeyWOKHgQ")
