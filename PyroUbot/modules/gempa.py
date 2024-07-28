import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "gempa"
__HELP__ = """
<blockquote><b>『 gempa 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gempa</code> 
   <i>penjelasan:</b> untuk stalking instagram menggunakan username</i></blockquote>
"""

@PY.UBOT("gempa")
async def stalkig(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    chat_id = message.chat.id
    url = f"https://widipe.com/gempa"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            tanggal = hasil['tanggal']
            jam = hasil['jam']
            photoUrl = f"https://cdn.vectorstock.com/i/1000v/71/92/music-lyrics-logo-mark-for-concert-vector-35117192.jpg"
            caption = f"""
<b><emoji id=5841235769728962577>⭐</emoji>TANGGAL: <code>{tanggal}</code></b>
<b><emoji id=5843952899184398024>⭐</emoji>JAM: <code>{jam}</code></b>
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No 'result' key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")