from vkbottle.user import UserLabeler, Message, User

TOKEN = "test"
bl = UserLabeler()
user = User(token=TOKEN)


prefix_bot = "хуй"
prefix_dd = "дд"


async def edit_message(
        message: Message,
        text: str = '',
        **kwargs
) -> int:
    kwargs.setdefault('message_id', message.id)
    kwargs.setdefault('message', text)
    kwargs.setdefault('peer_id', message.peer_id)
    kwargs.setdefault('keep_forward_messages', True)
    kwargs.setdefault('keep_snippets', True)
    kwargs.setdefault('dont_parse_links', False)

    return await user.api.messages.edit(
        **kwargs
    )
