import asyncio
from telethon import TelegramClient, events
from automation_server.settings import TG_HASH,TG_ID,BOT


api_id = int(TG_ID)
api_hash = TG_HASH
bot_username = BOT

client = TelegramClient('checkin_session', api_id, api_hash)

async def main():
    await client.start()

    msg = await client.send_message(bot_username, '/checkin')
    print("Sent /checkin")


    @client.on(events.NewMessage(from_users=bot_username))
    async def handler(event):
        if event.buttons:
            button = event.buttons[0][1] 
            print(f"Clicking button: {button.text}")
            
            await event.click(0, 1)      
            await asyncio.sleep(3)
            await client.disconnect()

    
    await asyncio.sleep(10)

with client:
    client.loop.run_until_complete(main())
