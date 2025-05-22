from telethon import TelegramClient, events, Button
import asyncio

api_id = 1449955
api_hash = 'd57bfe6bd0e6b76470655bf13232dc12'
bot_username = 'A2SVBouncerbot'

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
