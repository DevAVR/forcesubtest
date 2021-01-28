@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*http.*"))
async def echo(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are B A N N E D 🤣🤣🤣🤣")
        return
    TRChatBase(update.from_user.id, update.text, "/echo")
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Join My Updates Channel to use ME 😎 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
