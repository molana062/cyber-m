# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

from userbot import LOGS, bot, BOTLOG_CHATID
from userbot.modules import ALL_MODULES

INVALID_PH = (
    "\nERROR: The Phone No. entered is INVALID"
    "\n Tip: Use Country Code along with number."
    "\n or check your phone number and try again !"
)

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


if not BOTLOG_CHATID:
    LOGS.warning(
        "Yout BOTLOG_CHATID isn't set yet."
        "this variable is highly recomended to fill to make sure"
        "all errors go to your log chat not current chat and considered as a spammer.")



LOGS.info("You are running 404 Userbot")

bot.run_until_disconnected()
