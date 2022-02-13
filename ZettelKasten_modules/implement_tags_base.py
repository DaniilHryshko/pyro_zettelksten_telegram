from loader import channel_id, app


async def implement_tags(message):
    found_messages = app.search_messages(channel_id, query="#MOC")
    all_found_tags = set()
    all_my_tags = set()

    async for found_message in found_messages:
        if found_message.entities is not None:
            current_tags = await get_message_tag(found_message)
            all_my_tags.update(current_tags)
            found_message_links = await get_message_just_links(found_message)
        else:
            continue

        if message.entities:
            this_message_links = await get_message_just_links(message)
            if this_message_links.intersection(found_message_links):
                all_found_tags.update(current_tags)
        try:
            if message.forward_from.username:
                this_message_links = {f"@{message.forward_from.username}", f"https://t.me/{message.forward_from.username}"}
                if this_message_links.intersection(found_message_links):
                    all_found_tags.update(current_tags)
        except AttributeError:
            pass

        try:
            if message.forward_from_chat.username:
                this_message_links = {f"@{message.forward_from_chat.username}",
                                  f"https://t.me/{message.forward_from_chat.username}"}
                if this_message_links.intersection(found_message_links):
                    all_found_tags.update(current_tags)
        except AttributeError:
            pass

    if all_found_tags:
        tags_text = ''
        for tag in all_found_tags:
            tags_text += f"__{tag}__ "
        return ["__**Tags:**__ " + tags_text + '\n', all_my_tags]
    else:
        tags_text = "__**Tags:**__ __#inbox__\n"

    return [tags_text, all_my_tags]


async def get_message_just_links(message):
    text = message.text
    links = set()
    for entitie in message.entities:
        if entitie["type"] == "text_link":
            links.add(entitie.url)
        elif entitie["type"] != "hashtag":
            this_link = text[int(entitie["offset"]):int(entitie["offset"]) + int(entitie["length"])]
            links.add(this_link)
    return links


async def get_message_tag(message):
    text = message.text
    tags = set()
    for entitie in message.entities:
        if entitie["type"] == "hashtag":
            this_hashtag = text[int(entitie["offset"]):int(entitie["offset"]) + int(entitie["length"])]
            if this_hashtag != "#MOC":
                tags.add(this_hashtag)
    return tags
