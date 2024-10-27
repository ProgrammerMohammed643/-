from pyrogram import Client, idle

from pyromod import listen



bot = Client(
    "mo",
    api_id=29755247,
    api_hash="8dd9fb5fa2782d91b9847ace66eb885a",
    bot_token="7498694042:AAHfDRfVZq8p3zC0Bfc6pnyRi_-rF13-lgw",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "KOK0KK"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
