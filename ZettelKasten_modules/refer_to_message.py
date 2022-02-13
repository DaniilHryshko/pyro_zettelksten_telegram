async def implement_refer(message):
    try:
        title = message.forward_from_chat.title
        this_message_refer = f"https://t.me/{message.forward_from_chat.username}/{message.forward_from_message_id}"
        return f"__**Refer:**__ __[{title}]({this_message_refer})__\n"
    except AttributeError:
        pass
    try:
        title = message.forward_from.first_name
        this_message_refer = f"https://t.me/{message.message.forward_from.username}"
        return f"__*Refer:*__ [{title}]({this_message_refer})\n"
    except AttributeError:
        pass
    try:
        title = message.forward_from_chat.title
        this_message_refer = f"https://t.me/{message.forward_from_chat.username}"
        return f"__*Refer:*__ [{title}]({this_message_refer})\n"
    except AttributeError:
        pass

    return False
