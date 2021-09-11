from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben {bn}.Sesli sohbetlerde kesintsiz müzik çalabilirim.Aşağıdaki yönergeleri takip ediniz***,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Kullanım Kılavuzu 📜", url="https://t.me/MissMusicSupport")
                  ],[
                    InlineKeyboardButton(
                        "🥳 Asistan 🥳", url="https://t.me/MissMuzikAsistan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grubumuz 🎙️", url="https://t.me/intikamailesi"
                    )],
                [
                    InlineKeyboardButton(text= "😇Sahibim😇", url = "https://t.me/MissKraL")
                ]
            ]
        ),
     disable_web_page_preview=True      
    )
