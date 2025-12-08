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




from gpytranslate import Translator
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command(["tr", "trt", "translate"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def _(client: Client, message: Message):
    trans = Translator()
    if message.reply_to_message:
        dest = "id" if len(message.command) < 2 else message.text.split(None, 2)[1]
        to_translate = message.reply_to_message.text or message.reply_to_message.caption
    else:
        if len(message.command) < 3:
            return
        dest = message.text.split(None, 2)[1]
        to_translate = message.text.split(None, 2)[2]
    source = await trans.detect(to_translate)
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = f"<b>Language {source} Go to Language {dest}</b>:\n<code>{translation.text}</code>"
    reply_me_or_user = message.reply_to_message or message
    await client.send_message(
        message.chat.id, reply, reply_to_message_id=reply_me_or_user.id
)


add_command_help(
    "translate",
    [
        [
            "tr <ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ> <ᴛᴇxᴛ/ʀᴇᴘʟʏ>",
            "Tʀᴀɴꜱʟᴀᴛᴇꜱ ᴛᴇxᴛ ᴛᴏ ᴛʜᴇ ꜱᴇᴛ ʟᴀɴɢᴜᴀɢᴇ. (Dᴇғᴀᴜʟᴛ Eɴɢʟɪꜱʜ ᴄᴏᴅᴇ)",
        ],
    ],
      ) 
