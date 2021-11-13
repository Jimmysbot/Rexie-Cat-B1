from pyrogram import Client, filters
@Client.on_message(filters.command(["football"]))
async def football(bot, message):
         await message.reply_sticker("CAACAgUAAxkBAAIFKmDd2r4NMyGSyWgVu2v-fQxvJxBxAAL1AgACufE4VgHHxPJeyWOKHgQ")
