import discord
import asyncio
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_ready():
    print('존아봇 준비완료')

async def send_good_morning():
    await client.wait_until_ready()
    while not client.is_closed():
        now = datetime.now()
        target_time = now.replace(hour=8, minute=30, second=0, microsecond=0)
        if now >= target_time:
            target_time += timedelta(days=1)
        delta = target_time - now
        await asyncio.sleep(delta.total_seconds())
        channel = client.get_channel(channel_id)
        await channel.send('쫀아')

client.loop.create_task(send_good_morning())
client.run('TOKEN')
