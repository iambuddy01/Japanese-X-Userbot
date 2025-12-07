#MIT License

#Copyright (c) 2024 deleted-account

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.





import random
from X import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀssɪsᴛᴀɴᴛ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

logoX = [
    "https://files.catbox.moe/djqewp.jpg"
]

alive_logo = random.choice(logoX)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "ʜᴇʟʟᴏ, ᴍʏ ᴍᴀsᴛᴇʀ!!\nɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ🤗 !!\nɪ ɢᴜᴇss, ᴛʜᴀᴛ ʏᴏᴜ ᴋɴᴏᴡ ᴍᴇ , ᴜʜʜ ɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ..\nᴡᴇʟʟ.\n\nᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀssɪᴛᴀɴᴛ \n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ #deleted_account\n\nʏᴏᴜ ᴄᴀɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍʏ ᴍᴀsᴛᴇʀ ᴛʜʀᴏᴜɢʜ ᴛʜɪs ʙᴏᴛ.\nɪғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ᴀssɪᴛᴀɴᴛ ʏᴏᴜ ᴄᴀɴ ᴅᴇᴘʟᴏʏ ғʀᴏᴍ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/nexameetup"),
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/nexameetup"),
            InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/karmaxexclusive"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
