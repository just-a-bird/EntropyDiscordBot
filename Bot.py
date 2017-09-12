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
    ##check for valid user syntax
    try:
        ##try to map rolls to ints by splitting along d -- only works if no modifier is specified
        try:
            ##rolls = number of dice, limit == number of faces on the dice
            rolls, limit = map(int, dice.split('d'))
            addative=0
        ##handle the modifier
        except Exception:
            ##split using the 'd' character
            ##[0] will be number of dice, [1] 'd', [2] everything else
            split=re.split('d',dice)
            rolls=int(split[0])
            ##split everything after the d using + or -
            modsplit = re.split("([+-])", split[1])
            ##limit == number of face on the dice, comes before the + or -
            limit = modsplit[0]
            ##check if modifier is meant to subtract
            if modsplit[1] == '-':
                subtract = True
            ##get the actual modifier value
            modifier = modsplit[2]
            try:
                ##try to convert modifier string to an int
                addative=int(modifier)
            except Exception:
                ##user-specified modifier wasn't an int
                await bot.say('modifier must be an integer')
    ##invalid user syntax
    except Exception:
        await bot.say('The correct format is #d# + or - # (no spaces)')
        return
        
    ##handle a negative modifier
    if subtract:
        sign = ' - '
        diceSum = 0-addative
    else:
        diceSum=addative
        
    ##formatting the result string and adding rolls to the total
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


