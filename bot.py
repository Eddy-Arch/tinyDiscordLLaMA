#!/usr/bin/env python3
from websockets import client
import discord
import asyncio
import config
from discord.ext import commands
from colorama import Fore, Back, Style
from discord.ext.commands import has_permissions, CheckFailure
from config import *
if config.model =="falcon":
    from models.falcon import *
    print("Loaded Falcon Model")
elif config.model =="vicuna":
    from models.vicuna import *
    print("Loaded Vicuna Model")
elif config.model =="llama":
    from models.vicuna import *
    print("Loaded LLaMA Model")
else:
    print("improper model name passed, loading default model (Falcon)")
    from falcon import *

client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())
client.remove_command("help")

continue_generation = asyncio.Event()  # Event to control generation
generation_task = None  # Task representing the generation process

@client.command()
async def generate(ctx, *args):
    global continue_generation, generation_task

    if generation_task and not generation_task.done():
        await ctx.send("Generation is already in progress.")
        return

    words = ' '.join(args)
    print(words)
    prompt = words
    continue_generation.set()  # Set the event to continue generation

    async def generate_sentences():
        sentences_generator = generate_from_model(prompt)
        for sentence in sentences_generator:
            if not continue_generation.is_set():  # Check the event
                break
            if sentence == '\n' or sentence == "":
                print("")
            else:
                await ctx.send(sentence)

    generation_task = asyncio.create_task(generate_sentences())

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
    await ctx.send("currently using: " + str(config.model))

client.run(token)
