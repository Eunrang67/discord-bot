import discord
import datetime
import random
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def 핑(ctx):
    await ctx.send(f'-> {round(client.latency * 1000)}ms')

@client.command()
async def 테스트(ctx, *, content):
    await ctx.send(f'{content}')

@client.command()
async def 도움말(ctx):
    embed = discord.Embed(title=f"명령어 도움말", color=0xFFFF00, timestamp=message.created_at)
    embed.add_field(name=">추방 <@user>", value=f"멘션한 유저를 서버에서 추방합니다", inline=False)
    embed.add_field(name=">차단 <@user>", value=f"멘션한 유저를 서버에서 차단합니다", inline=False)
    embed.add_field(name=">프로필 <@user>", value=f"멘션한 유저의 프로필 사진을 볼 수 있습니다(?)", inline=False)
    embed.add_field(name=">embed <제목>/<내용>", value=f"입력한 제목과 내용으로 embed를 생성합니다", inline=False)
    embed.add_field(name=">DM <@user> <내용>", value=f"멘션한 유저에게 DM을 전송합니다", inline=False)
    embed.add_field(name=">삭제 <숫자>", value=f"입력한 숫자만큼 메시지를 삭제합니다", inline=False)
    embed.add_field(name=">초대링크", value=f"그냥 말 그대로 봇 초대링크(?)", inline=False)
    embed.add_field(name=">정보 <@user>", value=f"멘션한 사용자의 정보를 출력합니다", inline=False)
    embed.add_field(name=">채널정보 <#ch>", value=f"멘션한 채널의 정보를 출력합니다", inline=False)
    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
    await ctx.send(embed=embed)

client.run('Nzg3MjY3OTY2OTg2MDkyNTY0.X9Sebg.yVmnUbsqOcOrVEZ9gojo5Ta9pOI')
    