import discord
import asyncio
import requests
import datetime
import random
import json
from captcha.image import ImageCaptcha
ADMINID = [692324859224522753]
intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Login account : ")
    print('{0.user}'.format(client))
    print("connection was successful")
    print("=========================")
    #await client.get_channel(int(796735989065318421)).send('( 대충 봇이 실행되었다는 메시지 )')


@client.event
async def my_background_task():
    await client.wait_until_ready()
    ping = round(client.latency * 1000)
    while not client.is_closed():
        game = discord.Game(f">도움말")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f'서버:{len(client.guilds)}개')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f'>초대링크')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f"핑:{ping}ms")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
client.loop.create_task(my_background_task())

@client.event
async def on_guild_join(guild):
    guildname = {guild.name}
    embed = discord.Embed(title=f"봇 초대됨", color=0xFFFF00)
    embed.add_field(name="서버 : ", value=f'{guild.name}', inline = False)
    embed.add_field(name="서버 주인 : ", value=f'{guild.owner}', inline = False)
    embed.add_field(name="서버 개수 : ", value=f'{len(client.guilds)}개', inline = False)
    await client.get_channel(int(791822438001672203)).send(embed=embed)

@client.event
async def on_guild_remove(guild):
    guildname = {guild.name}
    embed = discord.Embed(title=f"봇 추방됨", color=0xFFFF00)
    embed.add_field(name="서버 : ", value=f'{guild.name}', inline = False)
    embed.add_field(name="서버 주인 : ", value=f'{guild.owner}', inline = False)
    embed.add_field(name="서버 개수 : ", value=f'{len(client.guilds)}개', inline = False)
    await client.get_channel(int(791822438001672203)).send(embed=embed)

@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        await client.get_channel(syschannel).send(f"{member}님이{member.guild} 서버에 입장하셨습니다!\n현재 인원수 : {str(len(member.guild.members))}")
    except:
        return None

@client.event
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id 
    try:
        await client.get_channel(syschannel).send(f"{member}님이{member.guild} 서버에 입장하셨습니다!\n현재 인원수 : {str(len(member.guild.members))}")
    except:
        return None

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content  == ">도움말" or message.content  == ">명령어" or message.content  == ">도움":
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
        await message.author.send(embed=embed)
        okembed = discord.Embed(title=f"명령어 도움말", color=0xFFFF00, timestamp=message.created_at)
        okembed.add_field(name="Direct Message", value=f"DM으로 도움말을 전송하였습니다", inline=False)
        okembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=okembed)
        return

    if message.content.startswith(">추방 "):
        if(message.author.guild_permissions.kick_members):
            try:
                user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[27:]
                if(len(message.content.split(" ")) == 2):
                    reason = "추방 사유가 입력되지 않았습니다!"
                await user.kick(reason=reason)
                userembed = discord.Embed(title=f"추방 알림", color=0xFFFF00, timestamp=message.created_at)
                userembed.add_field(name="서버", value=f"{message.guild.name}", inline=False)
                userembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                userembed.add_field(name="추방 사유", value=f"```{reason}```", inline=False)
                userembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await user.send(embed=userembed)
                kickembed = discord.Embed(title=f"추방 성공", color=0x00FF00, timestamp=message.created_at)
                kickembed.add_field(name="유저", value=f"{user}", inline=False)
                kickembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                kickembed.add_field(name="추방 사유", value=f"```{reason}```", inline=False)
                kickembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=kickembed)
            except Exception as e:
                if str(e) == '403 Forbidden (error code: 50007): Cannot send messages to this user':
                    kickembed = discord.Embed(title=f"추방 성공", color=0x00FF00, timestamp=message.created_at)
                    kickembed.add_field(name="유저", value=f"{user}", inline=False)
                    kickembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                    kickembed.add_field(name="추방 사유", value=f"```{reason}```", inline=False)
                    kickembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=kickembed)
                elif str(e) == '400 Bad Request (error code: 50007): Cannot send messages to this user':
                    kickembed = discord.Embed(title=f"추방 성공", color=0x00FF00, timestamp=message.created_at)
                    kickembed.add_field(name="유저", value=f"{user}", inline=False)
                    kickembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                    kickembed.add_field(name="추방 사유", value=f"```{reason}```", inline=False)
                    kickembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=kickembed)
                else:
                    errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
                    errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
                    errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                    errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=errorembed)
                return
        else:
            pererrorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            pererrorembed.add_field(name="오류 내용", value=f"명령어를 실행시킬 권한이 없습니다", inline=False)
            pererrorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            pererrorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=pererrorembed)
            return

    if message.content.startswith(">차단 "):
        if(message.author.guild_permissions.ban_members):
            try:
                user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[27:]
                if(len(message.content.split(" ")) == 2): 
                    reason = "차단 사유가 입력되지 않았습니다!"
                await user.ban(reason=reason)
                userembed = discord.Embed(title=f"차단 알림", color=0xFFFF00, timestamp=message.created_at)
                userembed.add_field(name="서버", value=f"{message.guild.name}", inline=False)
                userembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                userembed.add_field(name="차단 사유", value=f"```{reason}```", inline=False)
                userembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await user.send(embed=userembed)
                banembed = discord.Embed(title=f"차단 성공", color=0x00FF00, timestamp=message.created_at)
                banembed.add_field(name="유저", value=f"{user}", inline=False)
                banembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                banembed.add_field(name="차단 사유", value=f"```{reason}```", inline=False)
                banembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=banembed)
            except Exception as e:
                if str(e) == '403 Forbidden (error code: 50007): Cannot send messages to this user':
                    banembed = discord.Embed(title=f"차단 성공", color=0x00FF00, timestamp=message.created_at)
                    banembed.add_field(name="유저", value=f"{user}", inline=False)
                    banembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                    banembed.add_field(name="차단 사유", value=f"```{reason}```", inline=False)
                    banembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=banembed)
                elif str(e) == '400 Bad Request (error code: 50007): Cannot send messages to this user':
                    banembed = discord.Embed(title=f"차단 성공", color=0x00FF00, timestamp=message.created_at)
                    banembed.add_field(name="유저", value=f"{user}", inline=False)
                    banembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                    banembed.add_field(name="차단 사유", value=f"```{reason}```", inline=False)
                    banembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=banembed)
                else:
                    errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
                    errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
                    errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                    errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=errorembed)
                return
        else:
            pererrorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            pererrorembed.add_field(name="오류 내용", value=f"명령어를 실행시킬 권한이 없습니다", inline=False)
            pererrorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            pererrorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=pererrorembed)
            return

    if message.content.startswith(">차단해제 "):
        if(message.author.guild_permissions.ban_members):
            try:
                user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                await user.unban()
                userembed = discord.Embed(title=f"차단해제 알림", color=0xFFFF00, timestamp=message.created_at)
                userembed.add_field(name="서버", value=f"{message.guild.name}", inline=False)
                userembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                userembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await user.send(embed=userembed)
                unbanembed = discord.Embed(title=f"차단해제 성공", color=0x00FF00, timestamp=message.created_at)
                unbanembed.add_field(name="유저", value=f"{user}", inline=False)
                unbanembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                unbanembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=unbanembed)
            except Exception as e:
                errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
                errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
                errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=errorembed)
                return
        else:
            pererrorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            pererrorembed.add_field(name="오류 내용", value=f"명령어를 실행시킬 권한이 없습니다", inline=False)
            pererrorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            pererrorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=pererrorembed)
            return

    elif message.content.startswith('>프로필'):
                if str(message.content[5:]) == '':
                    user = message.author
                    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                    if not len(message.author.roles) == 1:
                        roles = [role for role in user.roles]
                        embed=discord.Embed(colour=0x0080FF, timestamp=message.created_at, title=f"유저 프로필 사진")
                    else:
                        embed=discord.Embed(colour=0x0080FF, timestamp=message.created_at)
                    embed.add_field(name="유저 :", value= f'{user}', inline=True)
                    embed.set_image(url=user.avatar_url)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                else:
                    try:
                        user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x0080FF, timestamp=message.created_at, title=f"유저 프로필 사진")
                            else:
                                embed=discord.Embed(colour=0x0080FF, timestamp=message.created_at)
                            embed.add_field(name="유저 :", value= f'{user}', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x0080FF, timestamp=message.created_at, title=f"봇 프로필 사진")
                            else:
                                embed=discord.Embed(colour=0x0080FF, timestamp=message.created_at)
                            embed.add_field(name="봇 :", value= f'{user}', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                    except Exception as e:
                        errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
                        errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
                        errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                        errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                        await message.channel.send(embed=errorembed)

    elif message.content.startswith(">DM"):
        try:
            user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
            contents = message.content[27:]
            DMembed = discord.Embed(title=f"Direct Message", color=0x0080FF, timestamp=message.created_at)
            DMembed.add_field(name="내용", value=f"```{contents}```", inline=False)
            DMembed.add_field(name="보낸 사람", value=f"{message.author.mention}", inline=False)
            DMembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await user.send(embed=DMembed)
            chembed = discord.Embed(title=f"DM 전송 완료", color=0x00FF00, timestamp=message.created_at)
            chembed.add_field(name="내용", value=f"```{contents}```", inline=False)
            chembed.add_field(name="보낸 사람", value=f"{message.author.mention}", inline=False)
            chembed.add_field(name="받는 사람", value=f"{user}", inline=False)
            chembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=chembed)
        except Exception as e:
            errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
            errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=errorembed)
            return
        return

    elif message.content.startswith(">embed"):
        if(message.author.guild_permissions.administrator):
            try:
                title = message.content.split("/")[0][6:]
                content = message.content.split("/")[1]
                embed=discord.Embed(title=f"{title}", description = f"{content}", colour = 0x0080FF, timestamp=message.created_at)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            except Exception as e:
                errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
                errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
                errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=errorembed)
                return
        else:
            errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
            errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=errorembed)
            return

    elif message.content  == '>핑':
        ping= round(client.latency * 1000)
        if ping >= 0 and ping <= 100:
            pings = "🔵 아주 좋음"
            embed = discord.Embed(title=f"네트워크 지연 시간",color=0x0080FF, timestamp=message.created_at)
            embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
            await message.channel.send(embed=embed)
        elif ping >= 101 and ping <= 200:
            pings = "🟢 좋음" 
            embed = discord.Embed(title=f"네트워크 지연 시간",color=0x0080FF, timestamp=message.created_at)
            embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
            await message.channel.send(embed=embed)
        elif ping >= 201 and ping <= 500:
            pings = "🟡 보통"
            embed = discord.Embed(title=f"네트워크 지연 시간",color=0x0080FF, timestamp=message.created_at)
            embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
            await message.channel.send(embed=embed)
        elif ping >= 501 and ping <= 1000:
            pings = "🟠 나쁨"
            embed = discord.Embed(title=f"네트워크 지연 시간",color=0x0080FF, timestamp=message.created_at)
            embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
            await message.channel.send(embed=embed)
        elif ping >= 1000:
            pings = "🔴 매우나쁨"
            embed = discord.Embed(title=f"📡 네트워크 상태 📡",color=0x0080FF, timestamp=message.created_at)
            embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
            await message.channel.send(embed=embed)

    elif message.content == '>초대링크':
        embed = discord.Embed(title=f"초대링크", color=0x0080FF, timestamp=message.created_at)
        embed.add_field(name="초대링크 안내", value=f"봇을 초대하려면 [여기](https://discord.com/oauth2/authorize?client_id=787267966986092564&permissions=8&scope=bot)를 클릭하세요")
        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        return

    elif message.content.startswith('>삭제'):
        try:   
            if message.author.guild_permissions.manage_messages:
                n = message.content.split(' ')
                await message.channel.purge(limit=int(n[1])+1)
                embed = discord.Embed(title=f"삭제 완료", color=0x00FF00, timestamp=message.created_at)
                embed.add_field(name="메시지 삭제 개수", value=f"{str(int(n[1]))}개", inline=False)
                embed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                return
            else:    
                pererrorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
                pererrorembed.add_field(name="오류 내용", value=f"명령어를 실행시킬 권한이 없습니다", inline=False)
                pererrorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                pererrorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=pererrorembed)
                return
        except Exception as e:
            errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
            errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=errorembed)
            return

    elif message.content.startswith('>정보'):
        try:
            if str(message.content[4:]) == '':
                user = message.author
                date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                embed = discord.Embed(title=f"사용자 정보", color=0x0080FF, timestamp=message.created_at)
                embed.add_field(name="사용자명", value=user, inline = False)
                embed.add_field(name="ID", value=user.id, inline = False)
                embed.add_field(name="별명", value=user.display_name,  inline = False)
                embed.add_field(name="계정 생성 날짜", value=f"{date.year}-{date.month}-{date.day}", inline = False)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                embed.add_field(name = '상태메시지&하는 중', value = user.activity, inline = False)
                await message.channel.send(embed=embed)
                return

            else:
                user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                embed = discord.Embed(title=f"사용자 정보", color=0x0080FF, timestamp=message.created_at)
                embed.add_field(name="사용자명", value=user, inline = False)
                embed.add_field(name="ID", value=user.id, inline = False)
                embed.add_field(name="별명", value=user.display_name,  inline = False)
                embed.add_field(name="계정 생성 날짜", value=f"{date.year}-{date.month}-{date.day}", inline = False)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                embed.add_field(name = '상태메시지&하는 중', value = user.activity, inline = False)
                await message.channel.send(embed=embed)
                return
        except Exception as e:
            errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
            errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=errorembed)
            return
        return

    elif message.content.startswith(">채널정보"):
        if len(message.channel_mentions) == 0:
            channel = message.channel
        else:
                channel = message.channel_mentions[0]
        name = channel.name
        cid = channel.id
        topic = channel.topic 
        if topic == "" or topic == None:
            topic = "없음"
        pos = str(channel.position+1) + "번"
        ctype = str(channel.type)
        created = str(channel.created_at)
        embed = discord.Embed(title=f"{name} 채널정보", color=0x0080FF, timestamp=message.created_at)
        embed.add_field(name="채널 이름", value=name, inline = False)
        embed.add_field(name="채널 ID", value=cid, inline = False)
        embed.add_field(name="채널 주제", value=topic, inline = False)
        embed.add_field(name="채널 순서", value=pos, inline = False)
        embed.add_field(name="채널 종류", value=ctype, inline = False)
        embed.add_field(name="채널 생성일", value=created, inline = False)
        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed = embed)
        return
         
    elif message.content.startswith(">인증역할"):
        if str(message.content[6:]) == '':
            errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            errorembed.add_field(name="오류 내용", value=f"역할 이름이 입력되지 않았습니다", inline=False)
            errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=errorembed)
            return
        global captcharole
        captcharole = message.content[6:]
        successembed = discord.Embed(title=f"역할 설정 완료", color=0x00FF00, timestamp=message.created_at)
        successembed.add_field(name="설정된 역할:", value=captcharole, inline=False)
        successembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
        successembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=successembed)

    elif message.content  == '>인증':
        try:
            author = message.author
            role = discord.utils.get(message.guild.roles, name=captcharole)
            lmage_captcha = ImageCaptcha()
            a = ""
            for i in range(6):
                a += str(random.randint(0, 9))
            name = str(message.author.id) + ".png"
            lmage_captcha.write(a, name)
            await message.channel.send(file=discord.File(name))
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel
            try:
                msg = await client.wait_for("message", timeout=10, check=check)
            except:
                timeerrorembed = discord.Embed(title=f"시간 초과", color=0xFF0000, timestamp=message.created_at)
                timeerrorembed.add_field(name="입력 시간이 초과되었습니다", value=f"다시 시도해주세요", inline=False)
                timeerrorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                timeerrorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=timeerrorembed)
                return
            if msg.content == a:
                successembed = discord.Embed(title=f"인증 성공", color=0x00FF00, timestamp=message.created_at)
                successembed.add_field(name="인증에 성공하였습니다!", value=f"역할이 부여되었습니다", inline=False)
                successembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                successembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=successembed)
                try:
                    role = discord.utils.get(message.guild.roles, name=captcharole)
                    await author.add_roles(role)
                except:
                    return
            else:
                errorembed = discord.Embed(title=f"인증 실패", color=0xFF0000, timestamp=message.created_at)
                errorembed.add_field(name="입력한 문자가 다릅니다", value=f"다시 시도해주세요", inline=False)
                errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=errorembed)
        except Exception as e:
            if str(e) == "name 'captcharole' is not defined":
                errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
                errorembed.add_field(name="오류 내용", value=f"역할이 설정되지 않았습니다\n`>인증역할`명령어를 이용하여\n역할을 설정해주세요", inline=False)
                errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
                errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=errorembed)
                return
            errorembed = discord.Embed(title=f"오류 발생", color=0xFF0000, timestamp=message.created_at)
            errorembed.add_field(name="오류 내용", value=f"```{str(e)}```", inline=False)
            errorembed.add_field(name="실행자", value=f"{message.author.mention}", inline=False)
            errorembed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=errorembed)
            return
        return

    elif message.content.startswith(">테스트"):
        contents = message.content[5:]
        with open('C:/Users/root0/Desktop/test.json', 'w', encoding='UTF8') as f:
            json.dump(contents, f, ensure_ascii=False)

client.run('Nzg3MjY3OTY2OTg2MDkyNTY0.X9Sebg.yVmnUbsqOcOrVEZ9gojo5Ta9pOI')
