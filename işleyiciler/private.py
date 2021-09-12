from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben {bn}
Sesli sohbetlerde müzik dinlemenize olanak sağlarım.
📜Kullanma Kılavuzu📜
💠 /oynat - Şarkıyı oynatır.
💠 /durdur - Şarkıyı durdurur.
💠 /devam - Şarkıyı devam ettirir.
💠 /atla - Diğer şarkıya geçer.
💠 /son - Botu kapatır.
💠 /bul - Şarkı aratır.
    
   Güncelleme ve diğer botlar için kanalımıza göz atın : [FLACK WAR](https://t.me/flackwardev)
   Kurucular : [BURAK](https://t.me/burakizm) [BAY KAOS](https://t.me/Baykaoss)
        """,
       
    )
