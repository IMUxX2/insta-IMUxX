#© ^ AhMaD BaRoN ^ °
#  To @hhmhhh 

"""For check: Send Your Country name then reply .check
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="che ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Subscribe @CQCQQ```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Subscribe @CQCQQ```")
       return
    chat = '@s5xbot'
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Subscribe @CQCQQ ```")
       return
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1066309224))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@S5XBOT) u Nigga```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
