
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "فيجا"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6154101472d61616307fe.jpg",
        caption=f"""╭═★⊷⌯⧼[𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀](https://t.me/SOURCEVEGA)⧽⌯⊶★═╮\n★‹ [𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀](https://t.me/SOURCEVEGA)\n★‹ [𝐀𝐒𝗞 𝗧𝐎 𝐌𝗘](https://t.me/SOURCEVEGA)\n★‹ [𝐊𝐈𝐌𝐌𝐘](https://t.me/TOPVEGA)\n★‹ [𝐓𝐎.𝐌𝐄](https://t.me/VE_GA_CH)\n╰═★⊷⌯⧼[𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀](https://t.me/SOURCEVEGA)⧽⌯⊶★═╯\n ⍟ 𝚆𝙴𝙻𝙲𝙾𝙼 𝚃𝙾 𝚂𝙾𝚄𝚁𝙲𝙴 𝚅𝙴𝙶𝙰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⎖᳒𝐊𝐈𝐌𝐌𝐘⌯⤹𝐊𝐈𝐍𝐆.𝐕𝐄𝐆𝐀⤸‹♱༄►", url=f"https://t.me/TOPVEGA"), 
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐑 𝐕𝐄𝐆𝐀⚡️", url=f"https://t.me/SOURCEVEGA"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/KiMY_X_bot?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



