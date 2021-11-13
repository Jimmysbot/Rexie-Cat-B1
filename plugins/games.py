from pyrogram import Client, filters

# Sticke
@Client.on_message(filters.command(["sticke"]))
async def sticke(bot, message):   
    if message.reply_to_message.["sticke"]:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")
