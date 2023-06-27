#!/usr/bin/env python3
from websockets import client
import discord
import asyncio
import config
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from config import *

if config.model == "falcon":
    from models.falcon import *
    print("Loaded Falcon Model")
elif config.model == "vicuna":
    from models.vicuna import *
    print("Loaded Vicuna Model")
elif config.model == "llama":
    from models.vicuna import *
    print("Loaded LLaMA Model")
elif config.model == "guanaco":
    from models.guanaco import *
    print("Loaded Guanaco Model")
else:
    print("Improper model name passed, loading default model (Falcon)")
    from falcon import *

client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())
client.remove_command("help")

continue_generation = asyncio.Event()  # Event to control generation
generation_task = None  # Task representing the generation process

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_message(message):
    global generation_task

    if client.user in message.mentions:
        words = ' '.join(message.content.split()[1:])  # Extract the words after the mention
        prompt = words
        print(words)
        continue_generation.set()  # Set the event to continue generation

        if generation_task and not generation_task.done():
            await message.channel.send("Generation is already in progress.")
        else:
            async def generate_sentences():
                sentences_generator = generate_from_model(prompt)
                for sentence in sentences_generator:
                    async with message.channel.typing():
                        if not continue_generation.is_set():  # Check the event
                            break
                        if sentence == '\n' or sentence == "":
                            print("")
                        else:
                            await message.channel.send(sentence)

            generation_task = asyncio.create_task(generate_sentences())
    else:
        await client.process_commands(message)

@client.command()
async def stop(ctx, *args):
    global continue_generation, generation_task

    if generation_task and not generation_task.done():
        continue_generation.clear()  # Clear the event to stop generation
        await generation_task
        await ctx.send("Generation stopped.")
    else:
        await ctx.send("No generation is currently in progress.")

@client.command()
async def model(ctx):
    await ctx.send("Currently using: " + str(config.model))

client.run(token)

