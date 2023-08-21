#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text=" Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"),
        ],
        ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=" Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text=" Oᴡɴᴇʀ ", user_id=OWNER),
        ],
    ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=" Cʟᴏsᴇ ", callback_data="close"
                    )
                ]
            ]
        )
