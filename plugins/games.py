from pyrogram import Client, filters

@Client.on_message(filters.command("Hyy"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await message.reply_text(
        text=stick_snd(query),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )
def stick_snd(country_name):
    try:
stick_snd = f"""Hey how are you"""

return stick_snd
    except Exception as error:
        return error
