import asyncio

from vkbottle.user import Message, UserLabeler

from config import prefix_bot, edit_message
from custom_rules.permission import Permission

bl = UserLabeler()


@bl.message(
        Permission(),
        text=[prefix_bot + " игра"],
)
async def game(message: Message):
    loader = (
        '⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜',
        """
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        """,
        """
        
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜

        """,
        """
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛✊✊⬛⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛⬛⬛⬜
        ⬜⬜⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛✊✊⬛
        ⬜⬛⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛✊✊⬛
        """,
        """
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛✊✊⬛⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛⬛⬛⬜
        ⬜⬜⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛✊✊⬛
        ⬜⬛⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛✊✊⬛
        ⬛✊⬛⬜⬛✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬛✊✊⬛⬛✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬛✊✊✊✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬜⬛✊✊✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬜⬜⬛✊✊✊✊✊✊✊✊✊✊✊✊⬛
        """,
        """
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛✊✊⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛✊✊⬛⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛⬛⬛⬜
        ⬜⬜⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛✊✊⬛
        ⬜⬛⬜⬜⬛✊✊⬛✊✊⬛✊✊⬛✊✊⬛
        ⬛✊⬛⬜⬛✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬛✊✊⬛⬛✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬛✊✊✊✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬜⬛✊✊✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬜⬜⬛✊✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬜⬜⬜⬛✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬜⬜⬜⬛✊✊✊✊✊✊✊✊✊✊✊⬛
        ⬜⬜⬜⬜⬜⬛✊✊✊✊✊✊✊✊✊⬛⬜
        ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
        """,
    )

    for new_text in loader:
        await edit_message(message, new_text)
        await asyncio.sleep(1)
