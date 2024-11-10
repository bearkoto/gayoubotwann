from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴄᴇᴄᴀɴ"
__HELP__ = """
📚 <b>--Folder Untuk Cecan--</b>

<blockquote><b>🚦 Perintah : <code>{0}cecan [query]</code>
🦠 Penjelasan : Mengirim Foto Random Sesuai Query.</b></blockquote>
<blockquote><b>📖 Penggunaan : 
 Query: 
    Indonesia,
    china,
    thailand,
    vietnam,
    waifu,
    neko,
    shinobu,
    hubble,
    malaysia,
    japan,
    korea</b></blockquote>
"""

URLS = {
    "indonesia": "https://aemt.uk.to/indonesia",
    "china": "https://aemt.uk.to/china",
    "thailand": "https://aemt.uk.to/thailand",
    "vietnam": "https://aemt.uk.to/vietnam",
    "waifu": "https://aemt.uk.to/waifu",
    "neko": "https://aemt.uk.to/neko",
    "shinobu": "https://aemt.uk.to/shinobu",
    "hubble": "https://aemt.uk.to/hubbleimg",
    "malaysia": "https://aemt.uk.to/malaysia",
    "japan": "https://aemt.uk.to/japan",
    "korea": "https://aemt.uk.to/korea"
}

@WANN.UBOT("cecan")
@WANN.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Processing...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal mengambil gambar cecan Error: {e}")
