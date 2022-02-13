from loader import app


async def replace_title(message):
    text = message.text
    new_title_dict = dict()

    for entitie in message.entities:
        if entitie["type"] == "url":
            this_link = text[int(entitie["offset"]):int(entitie["offset"]) + int(entitie["length"])]
            try:
                web_title = message.web_page["title"]
                type_of_message = classification_type_of_links(web_title)
                new_title_dict[f'{this_link}'] = web_title + await type_of_message
            except TypeError:
                try:
                    chat = await app.get_chat(this_link[13:])
                    type_of_message = classification_type_of_links(chat)
                    new_title_dict[f'{this_link}'] = chat.title + await type_of_message
                except:
                    new_title_dict[f'{this_link}'] = this_link

        elif entitie["type"] == "mention":
            mention = text[int(entitie["offset"]):int(entitie["offset"]) + int(entitie["length"])]
            chat = await app.get_chat(mention)
            type_of_message = classification_type_of_links(chat)
            new_title_dict[mention] = f'{chat.first_name} {chat.last_name if chat.last_name is not None else ""}' + await type_of_message

        elif entitie["type"] == "text_link":
            this_text = text[int(entitie["offset"]):int(entitie["offset"]) + int(entitie["length"])]
            new_title_dict[f'+12332fc{entitie.url}'] = this_text.strip()

    for title in new_title_dict:
        if title[0] == "@":
            new_links = f"https://t.me/{title[1:]}"
            text = text.replace(title, f"[{new_title_dict[title]}]({new_links})")
        elif "+12332fc" in title:
            new_links = f"{title[8:]}"
            text = text.replace(new_title_dict[title], f"[{new_title_dict[title]}]({new_links})")

        else:
            text = text.replace(title, f"[{new_title_dict[title]}]({title})")

    return text


async def classification_type_of_links(chat):
    if chat["type"] == "private":
        private_type = " !P"
        return private_type
    elif chat["type"] == "telegram_megagroup":
        telegram_megagroup_type = " !MG"
        return telegram_megagroup_type
    elif chat["type"] == "supergroup":
        supergroup_type = " !SG"
        return supergroup_type
    elif chat["type"] == "channel":
        channel_type = " !С"
        return channel_type
    elif chat["type"] == "article":
        web_type = " !W"
        return web_type
    elif chat["type"] == "bot":
        bot_type = " !B"
        return bot_type
    else:
        undefined_type = " U! "
        return undefined_type
