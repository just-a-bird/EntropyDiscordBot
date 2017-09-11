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
    ##Start out assuming modifier is zero
    subtract = False
    addative = 0
    sign = ' + '
    try:
        ##try to map rolls to ints by splitting along d -- only works if no modifier is specified
        try:
            rolls, limit = map(int, dice.split('d'))
            addative=0
        ##handle the modifier
        except Exception:
            split=re.split('d',dice)
            rolls=int(split[0])
            modsplit = re.split("([+-])", split[1])
            limit = modsplit[0]
            if modsplit[1] == '-':
                subtract = True
            modifier = modsplit[2]
            try:
                addative=int(modifier)
            except Exception:
                await bot.say('modifier must be an integer')
  
    except Exception:
        await bot.say('The correct format is #d# + or - # (no spaces)')
        return
    if subtract:
        sign = ' - '
        diceSum = 0-addative
    else:
        diceSum=addative
        
    result = '('
    for r in range(rolls):
        die = random.randint(1,int(limit))
        diceSum += die
        result += str(die)
        if r != rolls-1:
            result += ' + '
    
    result += ') ' + sign + str(addative) + ' = ' + str(diceSum)
    await bot.say(result)

    
@bot.command()
async def checkid():
    id = discord.utils.get
    await bot.say(id)
    
with open('key.txt','r') as keyfile:
    key=keyfile.read()
bot.run(key)


