from pyrogram import Client as Peaky
from pyrogram import filters as Peaky
from pyrogram.types import Message
from plugins.cust_p_filters import admin_fliter

@Peaky.on_message(
    Peaky.command(["pin"]) &
    admin_fliter
)
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Peaky.on_message(
    Peaky.command(["unpin"]) &
    admin_fliter
)
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
