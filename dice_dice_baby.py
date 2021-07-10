# GNU Terry Pratchett
# Created by Tholmne
# Initial Creation Date: 31/05/2021
# Version: 0.1.3

import discord, os
from random import randint
from dotenv import load_dotenv

rolls = []
roll_list = []

#Define the dice function
def roll_many (n , x ):
    for i in range( n ):
        roll = randint( 1 , x )
        rolls.append( roll )

load_dotenv()
token = os.getenv( 'Discord_Token' )

client = discord.Client()

@client.event
async def on_ready():
    print ( 'Logged in as {0.user}'.format(client) )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# Help text
    if message.content.startswith( '/help' ):
        await message.channel.send( "Current commands:" )
        await message.channel.send( "/roll - roll dice in the form of XdY i.e /roll 1d6 or /roll 10d12." )
        await message.channel.send( "/bw(b,g,w) X - roll a dicepool for Burning Wheel. X is the given dice pool size and b,g,w indicated the shade. i.e /bwb 5, /bww 10")

# Roll dice of any ammount or number of sides
    if message.content.startswith( '/roll' ):
        dice = message.content.strip( "/roll" )
        dice_pool = int( dice.split ( 'd' ) [ 0 ] )
        sides = int( dice.split ( 'd' ) [ 1 ] )
        roll_many( dice_pool , sides )
        await message.channel.send( rolls )

# Burning Wheel Black shade
    if message.content.startswith( '/bwb' ):
        rolls = int( message.content.strip( '/bwb' ) )
        success = failure = 0
        while rolls != 0:
            roll = randint(1,6)
            roll_list.append(roll)
            if roll <= 3:
                failure = failure+1
                rolls = rolls-1
            elif roll >= 4:
                success = success+1
                rolls = rolls-1
        await message.channel.send( str( success ) + " successes and " + str( failure ) + " traitors rolled" )
        await message.channel.send( roll_list )

# Burning Wheel Grey shade
    if message.content.startswith( '/bwg' ):
        rolls = int( message.content.strip( '/bwg' ) )
        success = failure = 0
        while rolls != 0:
            roll = randint(1,6)
            roll_list.append(roll)
            if roll <= 2:
                failure = failure+1
                rolls = rolls-1
            elif roll >= 3:
                success = success+1
                rolls = rolls-1
        await message.channel.send( str( success ) + " successes and " + str( failure ) + " traitors rolled" )
        await message.channel.send( roll_list )

# Burning Wheel White shade
    if message.content.startswith( '/bww' ):
        rolls = int( message.content.strip( '/bww' ) )
        success = failure = 0
        while rolls != 0:
            roll = randint(1,6)
            roll_list.append(roll)
            if roll <= 1:
                failure = failure+1
                rolls = rolls-1
            elif roll >= 2:
                success = success+1
                rolls = rolls-1
        await message.channel.send( str( success ) + " successes and " + str( failure ) + " traitors rolled" )
        await message.channel.send( roll_list )

# Red Markets good/bad roll
    if message.content.startswith( '/rgb' ):
        mod = int( message.content.strip( '/rgb' ) )
        good = int( roll_many( 1 , 10 ) )+int( mod )
        bad = roll_many( 1 , 10 )
        result = good-bad
    await message.channel.send( result + " successes" )


client.run(token)
