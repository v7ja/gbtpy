from OpsAi import Ai
from pyrogram import Client,filters

API_ID = 13066983
API_HASH = "154e45eb588378308ad53f9bb8ed4bed"
TOKEN = "6007683095:AAHcWSFplVtaqQJYnWaBAYH9htFdWP9ZWBI"
app = Client("ChatGpt", api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN) 


@app.on_message(filters.command("start"))
async def StartMsg(_,msg):
 await msg.reply("Hello: I am ChatGpt")
 
@app.on_message(filters.command("بوت",""))
async def YesSir(_,msg):
 await msg.reply("ᥕ𝖾𝗅ᥴ᥆𝗆𝖾 : 𝗆𝗒 ᥒα𝗆𝖾 Ꭵ𝗌 {𝗒α𝖻h}")
 

@app.on_message(filters.private & ~filters.reply)
async def echo(bot, msg):
    a = msg.text
    s = Ai(query = a)
    await bot.send_message(chat_id=msg.chat.id, text=s.chat()) 
    

@app.on_message(filters.text)
async def reply(bot, msg):
  try:
    if  msg.reply_to_message.from_user.is_bot:
    	a = msg.text
    	s = Ai(query = a)
    	await msg.reply_text(text=s.chat(),quote=True)
  except:pass
    
@app.on_message(filters.regex(r"^يابه (.+)"),group=-1)
async def reply_with_text(bot, msg):
    a = msg.text.split(None,1)[1]
    s = Ai(query = a)
    await msg.reply_text(text=s.chat(),quote=True)
    
    
 
print("Run..")   
app.run()
