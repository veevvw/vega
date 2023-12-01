####  source vega
####  لو معرفتش تشغله ابعتلي تلي هفيدك اليوزر@TOPVEGA


import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from YukkiMusic import app

@app.on_message(filters.voice_chat_started)
async def zohary(client: Client, message: Message): 
      Startt = "عـندي بـرد مش هغني🥲🎧✨"
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def zoharyy(client: Client, message: Message): 
      Enddd = "قفله فدماغك🥲💤🎧"
      await message.reply_text(Enddd)

async def send_invite(message):
   for x in message.voice_chat_members_invited.users:
       try:
        link = await app.export_chat_invite_link(message.chat.id)
       except:
        link = "البوت ليس ادمن لم استطع انشاء رابط"
       await app.send_message(x.id, f"قام هذا الشخص {message.from_user.mention} \n بدعوتك الي المحادثة الصوتية \nرابط المجموعة : {link}")
@app.on_message(filters.voice_chat_members_invited)
async def fuckoff(client: Client, message: Message):
           text = f"• قام {message.from_user.mention}\n • بدعوة : "
           x = 0
           for user in message.voice_chat_members_invited.users:
               try:
                text += f"{user.first_name} "
                x += 1
               except Exception:
                pass
           try:
             await message.reply_text(f"{text} .")
             await send_invite(message)
           except:
             pass