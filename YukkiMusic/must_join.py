from functools import wraps
from config.config import MUST_JOIN
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


def must_join_channel(func):
    @wraps(func)
    async def sz_message(_, message):
        try:
            await message._client.get_chat_member(MUST_JOIN, message.from_user.id)
            if MUST_JOIN.isalpha():          
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await message._client.get_chat(MUST_JOIN)
                link = chat_info.invite_link
        except UserNotParticipant:
            return await message.reply(
                    f"🗽يجب ان تشترك في قنـاة البــوت⬇️\n\n[⚙¦ قنــاة ســورس️ الاغــانـي](https://t.me/UUU_C_1)\n⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺\n**🤖قنـاة الـبـوت ⬅️** @{MUST_JOIN} »\n⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀━⊶★━⩺\n🖥¦حتي تتمكن من استخدامي\n◍ اشترك ثم اضغط « شغل والاغنيه » مره اخري√\n\n🌐¦ By ||[⌁ 𝙲𝙾𝚄𝙳𝚁𝙰 [𝙰𝙻𝙺𝙰𝙱𝙴𝚁] 𝙰𝚈𝙺𝚂𝙼𝙺](https://t.me/SOURCE VEGA )||",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("اضـغط هنا للأشتـراك بقـناة البـوت✅", url=f"https://t.me/{MUST_JOIN}"),
                            ],
                            [
                                InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀", url=f"https://t.me/SOURCE VEGA "),
                            ] 
                         ] 
                      ) 
                   ) 
        return await func(_, message)    
    return sz_message
