from pyrogram import filters

from loader import channel_id, app
from ZettelKasten_modules import implement_tags, get_message_tag, implement_refer, replace_title


@app.on_message(filters.chat(channel_id) & ~filters.edited)
async def base_handler(client, message):
    tags_list = await implement_tags(message)
    refer = await implement_refer(message)
    await app.delete_messages(channel_id, message.message_id)
    if message.entities is not None:
        new_title = await replace_title(message)
        tags = await get_message_tag(message)
        if tags & tags_list[1]:
            await app.send_message(channel_id, f"{tags_list[0]}{refer if refer else ''}\n{new_title}")
        else:
            await app.send_message(channel_id, f"{tags_list[0]}{refer if refer else ''}\n{new_title}")
    else:
        await app.send_message(channel_id, f"{tags_list[0]}{refer if refer else ''}\n{message.text}")