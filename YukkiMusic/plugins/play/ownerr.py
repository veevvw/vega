import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv
#

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

KIMMY = getenv("KIMMY")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(
    command(["كمي","كيمي","مبرمج","مطور السورس","المبرمج","المطورين"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("TOPVEGA")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺\n\n⭐ ¦𝚅𝙴𝙶𝙰 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n🎃 ¦𝙸𝙳 :`{usr.id}`\n💌 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺**",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )





@app.on_message(
    command(["مطور", "المطور"])
    & filters.group
    & ~filters.edited
)
async def KIMMY(client: Client, message: Message):
    usr = await client.get_users(OWNER)
    name = usr.first_name
    async for photo in client.iter_profile_photos(OWNER, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺**
                    
🔥 ¦𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
📀 ¦𝚄𝚂𝙴𝚁 :@{OWNER} 
🆔 ¦𝙸𝙳 :`{usr.id}`
 
**⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺** """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{OWNER}")
            ],                   
          ]              
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")


@app.on_message(command("تحويل لصوره"))
async def elkatifh(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



