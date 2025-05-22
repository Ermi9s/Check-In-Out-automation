import asyncio
from automation_server.settings import TG_HASH,TG_ID,BOT
from telethon import TelegramClient, events


api_id = int(TG_ID)
api_hash = TG_HASH
bot_username = BOT

client = TelegramClient('checkout_session', api_id, api_hash)

async def main():
    await client.start()
    print("sending /checkout...")
    await client.send_message(bot_username, '/checkout')

    @client.on(events.NewMessage(from_users=bot_username))
    async def handler(event):
        if event.buttons:
            print(f"button: {event.buttons[0][0].text}")
            await event.click(0)
            print("clicked the button.")
            await asyncio.sleep(2)
            await client.disconnect()

    await asyncio.sleep(10)

with client:
    client.loop.run_until_complete(main())
