import discord
from discord.ext.commands import Bot
import random
import re
from discord.ext import commands

description = '''Okay I guess'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Third Law')
    print(bot.user.name)
    print(bot.user.id)
    print('☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭')
    
    
@bot.command()
async def fully():
    await bot.say("automated luxury gay space ☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭")    
    
@bot.command()
async def testing():
    await bot.say("Test Acknowledged")

    
@bot.command()
async def roll(dice : str):
    ##initializing some attributes
    modifier = False
    mod = ''
    diceSum=0
    result = '('
        
    ##check to see if user specified a modifier for the roll
    if '+' in dice or '-' in dice:
        modifier = True
    
    ##split along whitespace and positive/negative signs
    SplitInput = re.split(r'[-+d\s]+',dice)
    print(SplitInput)
    ##assign number of rolls and the number of faces per die
    rolls = int(SplitInput[0])
    numberOfFaces = int(SplitInput[1])
    ##handling modifier if present
    if modifier:
        if '-' in dice:
            diceSum -= int(SplitInput[2])
        else:
            diceSum += int(SplitInput[2])
        mod = str(diceSum)

    ##calculating results & building output string
    for r in range(rolls):
        die = random.randint(1,int(numberOfFaces))
        diceSum += die
        result += str(die)
        if r != rolls-1:
            result += ' + '
    result += ') ' + mod + ' = ' + str(diceSum)
    await bot.say(result)

    
@bot.command()
async def checkid():
    id = discord.utils.get
    await bot.say(id)
    
with open('key.txt','r') as keyfile:
    key=keyfile.read()
bot.run(key)


