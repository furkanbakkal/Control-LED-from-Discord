import discord
from discord.ext import commands
import RPi.GPIO as GPIO          #adding modules

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)      
GPIO.setup(11, GPIO.OUT)       #We set the GPIO17 pin on the 11th as OUTPUT

TOKEN = "Your Bot's Token"

description = '''Python Discord Bot'''
bot = commands.Bot(command_prefix='!', description=description)  
#our distinctive symbol "!" We set it to (exclamation). So when entering the command,we will enter it like !command

@bot.event
async def on_ready():         #If our Bot is ready ...
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def led1(ctx):               #if the incoming data is "led1" ...
    await ctx.send("led açıldı :bulb:")   #Let our bot return to us and ...
    GPIO.output(11,1)             # GPIO17 -> 3.3V

@bot.command()
async def led0(ctx):                #if the incoming data is "led0" ...
    await ctx.send("led kapatıldı :bulb:")  #Let our bot return to us and ...
    GPIO.output(11,0)           # GPIO17 -> 0V 
    
@bot.command() 
async def sıcaklık(ctx):      #if incoming data is "sıcaklık"...
    temp=open("/sys/class/thermal/thermal_zone0/temp", "r")   #We opened file which stores RPI's temperature data
    temp= str(round((float(temp.readline())/1000),1))    #reading temperature data
    
    await ctx.send("İşlemci sıcaklığı: "+ temp + " °C") #writing temperature
    
@bot.command() 
async def yardım(ctx):   #it is help command
    await ctx.send(":card_box: Komut Listesi:\n:arrow_right: **led1** : ledi yakar \n:arrow_right:** led0** : ledi kapatır \n:arrow_right: **sıcaklık** : Raspberry Pi işlemci sıcaklığını gösterir")
    
bot.run(TOKEN)
