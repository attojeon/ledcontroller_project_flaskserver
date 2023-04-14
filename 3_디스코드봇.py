'''
- 봇커맨드 사용하기 
- 접두어로 봇명령 구분하기 
### 메시지 보내기 차이점 ###
- message.channel.send() VS ctx.send()
'''
import discord
from discord.ext import commands
from datetime import datetime

#####################################
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
LED_P = 25
GPIO.setup(LED_P, GPIO.OUT)

def led_on():
    print(">>> led light on!")
    GPIO.output(LED_P, True)

def led_off():
    print("   <<< led light off!")
    GPIO.output(LED_P, False)
####################################

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents) 

@bot.event
async def on_ready():
    print('#'*80)
    print(f"{bot.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {bot.user.name}(id:{bot.user.id})")
    print(f"서비스 시작시간:{ datetime.now()}")
    print('#'*80)

# 사용법 : /hello
# 간단한 인사와 인사한 작자의 이름을 보여줌 
@bot.command()
async def hello(ctx):
    username = ctx.author.name
    await ctx.send(f"안녕하세요. {username}님")

@bot.command(aliases=['on','켜기'])
async def ledon(ctx):
    led_on()
    msg = "LED 켜짐"
    await ctx.send(msg)

@bot.command(aliases=['off','끄기'])
async def ledon(ctx):
    led_off()
    msg = "LED 꺼짐"
    await ctx.send(msg)


TOKEN = 'MTA4NDAzMDQzODQxMjEyODI1Ng.G5kXqS.WBg_P1WXAYa2zysF28sPscu7MJ-WSd6AzzIW7I'  
bot.run( TOKEN)