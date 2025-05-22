from telethon import TelegramClient, events
import asyncio

api_id = 1449955 
api_hash = 'd57bfe6bd0e6b76470655bf13232dc12'
bot_username = 'A2SVBouncerbot'

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
