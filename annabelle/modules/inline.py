from config import MY_ID, HANDLER
from annabelle import Annabelle 
from pyrogram import Client
from pyrogram import filters as vrn
from pyrogram.types.messages_and_media import Message


@Annabelle.on_message(vrn.command("inline", HANDLER))
async def inline(bot:Annabelle, msg:Message) :
    chat_id = msg.chat.id
    peer_id = "Annabellev1_bot"
    try :
        try :
            chat_id = 5292470029
            await bot.send_message(chat_id, text="/start")
        except :
            user_id = 5292470029
            await bot.unblock_user(user_id)
            await bot.send_message(chat_id=user_id, text="/start")
    except :
        await bot.resolve_peer(peer_id)

    result = await bot.get_inline_bot_results(bot=peer_id, query="inline")
    query_id = result.query_id
    result_id = result.results[0].id
    await bot.send_inline_bot_result(chat_id, query_id, result_id)
