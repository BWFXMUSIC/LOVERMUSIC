from NihalX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = ["🦋🦋🦋🦋🦋"]

TAGMES = [ " **❅ बेबी कहा हो। 🤗** ",
           " **❅ ओए सो गए क्या, ऑनलाइन आओ ।😊** ",
           " **❅ ओए वीसी आओ बात करते हैं । 😃** ",
           " **❅ खाना खाया कि नही। 🥲** ",
           " **❅ घर में सब कैसे हैं। 🥺** ",
           " **❅ पता है बहुत याद आ रही आपकी। 🤭** ",
           " **❅ और बताओ कैसे हो।..?? 🤨** ",
           " **❅ मेरी भी सैटिंग करवा दो प्लीज..?? 🙂** ",
           " **❅ आपका नाम क्या है।..?? 🥲** ",
           " **❅ नाश्ता हो गया..?? 😋** ",
           " **❅ मुझे अपने ग्रूप में ऐड कर लो। 😍** ",
           " **❅ आपका दोस्त आपको बुला रहा है। 😅** ",
           " **❅ मुझसे शादी करोगे ..?? 🤔** ",
           " **❅ सोने चले गए क्या 🙄** ",
           " **❅ अरे यार कोई AC चला दो 😕** ",
           " **❅ आप कहा से हो..?? 🙃** ",
           " **❅ हेलो जी नमस्ते 😛** ",
           " **❅ BABY क्या कर रही हो..? 🤔** ",
           " **❅ क्या आप मुझे जानते हो .? ☺️** ",
           " **❅ आओ baby Ludo खेलते है .🤗** ",
           " **❅ चलती है क्या 9 से 12... 😇** ",
           " **❅ आपके पापा क्या करते है 🤭** ",
           " **❅ आओ baby बाजार चलते है गोलगप्पे खाने। 🥺** ",
           " **❅ अकेली ना बाजार जाया करो, नज़र लग जायेगी। 😶** ",
           " **❅ और बताओ BF कैसा है ..?? 🤔** ",
           " **❅ गुड मॉर्निंग 😜** ",
           " **❅ मेरा एक काम करोगे। 🙂** ",
           " **❅ DJ वाले बाबू मेरा गाना चला दो। 😪** ",
           " **❅ आप से मिलकर अच्छा लगा।☺** ",
           " **❅ मेरे बाबू ने थाना थाया।..? 🙊** ",
           " **❅ पढ़ाई कैसी चल रही हैं ? 😺** ",
           " **❅ हम को प्यार हुआ। 🥲** ",
           " **❅ Nykaa कौन है...? 😅** ",
           " **❅ तू खींच मेरी फ़ोटो ..? 😅** ",
           " **❅ Phone काट मम्मी आ गई क्या। 😆** ",
           " **❅ और भाबी से कब मिल वा रहे हो । 😉** ",
           " **❅ क्या आप मुझसे प्यार करते हो 💚** ",
           " **❅ मैं तुम से बहुत प्यार करती हूं..? 👀** ",
           " **❅ बेबी एक kiss दो ना..?? 🙉** ",
           " **❅ एक जॉक सुनाऊं..? 😹** ",
           " **❅ vc पर आओ कुछ दिखाती हूं  😻** ",
           " **❅ क्या तुम instagram चलते हो..?? 🙃** ",
           " **❅ whatsapp नंबर दो ना अपना..? 😕** ",
           " **❅ आप की दोस्त से मेरी सेटिंग करा दो ..? 🙃** ",
           " **❅ सारा काम हो गया हो तो ऑनलाइन आ जाओ।..? 🙃** ",
           " **❅ कहा से हो आप 😊** ",
           " **❅ जा तुझे आज़ाद कर दिया मैंने मेरे दिल से। 🥺** ",
           " **❅ मेरा एक काम करोगे, ग्रूप मे कुछ मेंबर ऐड कर दो ..? ♥️** ",
           " **❅ मैं तुमसे नाराज़ हूं 😠** ",
           " **❅ आपकी फैमिली कैसी है..? ❤** ",
           " **❅ क्या हुआ..? 🤔** ",
           " **❅ बहुत याद आ रही है आपकी 😒** ",
           " **❅ भूल गए मुझे 😏** ",
           " **❅ झूठ क्यों बोला आपने मुझसे 🤐** ",
           " **❅ इतना भाव मत खाया करो, रोटी खाया करो कम से कम मोटी तो हो जाओगी 😒** ",
           " **❅ ये attitude किसे दिखा रहे हो 😮** ",
           " **❅ हेमलो कहा busy ho 👀** ",
           " **❅ आपके जैसा दोस्त पाकर मे बहुत खुश हूं। 🙈** ",
           " **❅ आज मन बहुत उदास है ☹️** ",
           " **❅ मुझसे भी बात कर लो ना 🥺** ",
           " **❅ आज खाने में क्या बनाया है 👀** ",
           " **❅ क्या चल रहा है 🙂** ",
           " **❅ message क्यों नहीं करती हो..🥺** ",
           " **❅ मैं मासूम हूं ना 🥺** ",
           " **❅ कल मज़ा आया था ना 😅** ",
           " **❅ कल कहा busy थे 😕** ",
           " **❅ आप relationship में हो क्या..? 👀** ",
           " **❅ कितने शांत रहते हो यार आप 😼** ",
           " **❅ आपको गाना, गाना आता है..? 😸** ",
           " **❅ घूमने चलोगे मेरे साथ..?? 🙈** ",
           " **❅ हमेशा हैप्पी रहा करो यार 🤞** ",
           " **❅ क्या हम दोस्त बन सकते है...? 🥰** ",
           " **❅ आप का विवाह हो गया क्या.. 🥺** ",
           " **❅ कहा busy the इतने दिनों से 🥲** ",
           " **❅ single हो या mingle 😉** ",
           " **❅ आओ पार्टी करते है 🥳** ",
           " **❅ Bio में link हैं join कर लो 🧐** ",
           " **❅ मैं तुमसे प्यार नहीं करती, 🥺** ",
           " **❅ यहां आ जाओ ना @BWF_MUSIC1 मस्ती करेंगे 🤭** ",
           " **❅ भूल जाओ मुझे,..? 😊** ",
           " **❅ अपना बना ले पिया, अपना बना ले 🥺** ",
           " **❅ मेरा ग्रुप भी join कर लो ना 🤗** ",
           " **❅ मैने तेरा नाम Dil rakh diya 😗** ",
           " **❅ तुमारे सारे दोस्त कहा गए 🥺** ",
           " **❅ my cute owner @L2R_KING0 🥰** ",
           " **❅ किसकी याद मे खोए हो जान 😜** ",
           " **❅ गुड नाईट जी बहुत रात हो गई 🥰** ",
           ]
 

@app.on_message(filters.command(["hitag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("Only admin can use this command!")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall hello 👈 Try this next time for tagging..")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall hii 👈 Try this or reply any message...")
    else:
        return await message.reply("/tagall hii 👈 Try this or reply any message...")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("No active mention process is started by me.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("This command is only for admins. You can't use this command.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ Mention process stopped ♦")
