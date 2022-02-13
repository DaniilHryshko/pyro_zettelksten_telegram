from pyrogram import filters

from loader import channel_id, app
from .change_message_links import replace_title


@app.on_message(filters.chat(channel_id) & filters.edited)
async def edited_handler(client, message):
    new_text = await replace_title(message)
    if "Tags:" in new_text:
        new_text = new_text.replace("Tags:", "__**Tags:**__")
    elif "Refer:" in new_text:
        new_text = new_text.replace("Tags:", "__**Refer:**__")
    await app.edit_message_text(channel_id, message.message_id, new_text)
