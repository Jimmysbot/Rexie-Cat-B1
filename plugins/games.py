from pyrogram import Client, filters
@Clinet.on_message(filters.private & filter.command("football"))
async def football(bot, message):
         await bot.send_sticker("CAACAgUAAxkBAAIFKmDd2r4NMyGSyWgVu2v-fQxvJxBxAAL1AgACufE4VgHHxPJeyWOKHgQ")
