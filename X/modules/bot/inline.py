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



import time
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
import asyncio

from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from X.helpers.data import Data
from X.helpers.inline import inline_wrapper, paginate_help
from config import BOT_VER, BRANCH as branch
from X import CMD_HELP, StartTime, app

modules = CMD_HELP

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Day"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


async def alive_function(message: Message, answers):
    uptime = await get_readable_time((time.time() - StartTime))
    msg = f"""
<b> — ʜɪ, ɪ'ᴍ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ.</b>

<b> • ᴍʏ ᴍᴀsᴛᴇʀ:</b> {message.from_user.mention}
<b> • ᴍᴏᴅᴜʟᴇs:</b> <code>{len(CMD_HELP)} Modules</code>
<b> • ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:</b> <code>{pyver.split()[0]}</code>
<b> • ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ:</b> <code>{pyrover}</code>
<b> • ʙᴏᴛ ᴛɪᴍᴇ:</b> <code>{uptime}</code>

<b> — 𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : 1.0</b>
"""
    answers.append(
        InlineQueryResultArticle(
            title="alipp",
            description="ᴄʜᴇᴄᴋ ʙᴏᴛ's sᴛᴀᴛs",
            thumb_url="https://files.catbox.moe/djqewp.jpg",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("──「 ʜᴇʟᴘ 」──", callback_data="helper")]]
            ),
        )
    )
    return answers


async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"❏ **ᴘɪɴɢ ᴘᴏɴɢ 🏓**\n"
        f"├• **📡 ᴘɪɴɢ:** `%sms`\n"
        f"├• **⌚ ᴜᴘᴛɪᴍᴇ** `{uptime}` \n"
        f"└• **💻 ᴍᴀsᴛᴇʀ:** {client.me.mention}" % (duration)
    )

async def peler_function(message: Message, answers):
    msg = (
        f"Deleted Account \n"
        "ㅤㅤStatus : Userbot Active \n"
        f"ㅤㅤㅤㅤModules:</b> <code>{len(modules)} Modules</code> \n"
        f"ㅤㅤㅤㅤBot Version: {BOT_VER} \n"
        f"ㅤㅤㅤㅤBranch: {branch} \n\n"
    )
    answers.append(
        InlineQueryResultArticle(
            title="alive",
            description="ᴄʜᴇᴄᴋ ʙᴏᴛ's sᴛᴀᴛs",
            thumb_url="https://files.catbox.moe/djqewp.jpg",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/nexameetup"), InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url="https://github.com/karmaxexclusive")], [InlineKeyboardButton(text="ᴍᴇɴᴜ", callback_data="reopen")]]
            ),
        )
    )
    return answers


async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            description="Check Command List & Help",
            thumb_url="https://files.catbox.moe/djqewp.jpg",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers


@app.on_inline_query()
@inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alipp":
            answerss = await alive_function(query, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
        elif string_given.startswith("alive"):
            answers = await peler_function(query, answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=5)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
