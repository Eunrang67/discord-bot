import discord
import asyncio
import requests
import datetime
import random
from captcha.image import ImageCaptcha
ADMINID = [692324859224522753]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def my_background_task():
    await client.wait_until_ready()
    ping = round(client.latency * 1000)
    while not client.is_closed():
        game = discord.Game(f"&명령어")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f'서버:{len(client.guilds)}개')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f'&초대링크')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f"핑:{ping}ms")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
client.loop.create_task(my_background_task())

@client.event
async def on_guild_join(guild):
    guildname = {guild.name}
    embed = discord.Embed(title=f"<a:yes:761038848947126323> 봇 초대됨 <a:yes:761038848947126323>", color=0xFFFF00)
    embed.add_field(name="서버 : ", value=f'{guild.name}({guild.id})', inline = False)
    embed.add_field(name="서버 주인 : ", value=f'{guild.owner}', inline = False)
    embed.add_field(name="서버 개수 : ", value=f'{len(client.guilds)}개', inline = False)
    await client.get_channel(int(771020771576905738)).send(embed=embed)

@client.event
async def on_guild_remove(guild):
    embed = discord.Embed(title=f"<a:no:761038850046033980> 봇 추방됨 <a:no:761038850046033980>", color=0xFFFF00)
    embed.add_field(name="서버 : ", value=f'{guild.name}({guild.id})', inline = False)
    embed.add_field(name="서버 주인 : ", value=f'{guild.owner}', inline = False)
    embed.add_field(name="서버 개수 : ", value=f'{len(client.guilds)}개', inline = False)
    await client.get_channel(int(771020771576905738)).send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("&채널정보"):
        if(message.author.guild_permissions.manage_channels):
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
            embed = discord.Embed(title=f"{name} 채널정보", color=0xFFFF00, timestamp=message.created_at)
            embed.add_field(name="채널 이름", value=name, inline = False)
            embed.add_field(name="채널 ID", value=cid, inline = False)
            embed.add_field(name="채널 주제", value=topic, inline = False)
            embed.add_field(name="채널 순서", value=pos, inline = False)
            embed.add_field(name="채널 종류", value=ctype, inline = False)
            embed.add_field(name="채널 생성일", value=created, inline = False)
            embed.add_field(name="명령어 실행유저", value = message.author.mention)
            embed.set_footer(text=f"루나[LUNAR]", icon_url='https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png')
            await message.channel.send(embed = embed)
        else:
            await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 권한 부족 <a:no:761038850046033980>", description = message.author.mention + "님은 이 명령어를 사용할 수 없습니다", color = 0xFFFF00))

    if message.content.startswith("&추방 "):
        if(message.author.guild_permissions.kick_members):
            try:
                user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[25:]
                if(len(message.content.split(" ")) == 2):
                    reason = "추방 사유가 입력되지 않았습니다!"
                await user.kick(reason=reason)
                await user.send(embed=discord.Embed(title="추방", description = f'{message.guild.name} 서버에서\n{message.author.mention}님에 의해 추방되었습니다! \n 추방사유 : ```{reason}```', color = 0xFFFF00))
                await message.channel.send(embed=discord.Embed(title="<a:yes:761038848947126323> 추방 성공 <a:yes:761038848947126323>", description = f"{user} 님은 {message.author.mention}님의 의해\n해당 서버에서 추방되었습니다! \n 추방사유 :```{reason}```", color = 0xFFFF00))
            except Exception as e:
                if str(e) == '400 Bad Request (error code: 50007): Cannot send messages to this user':
                    await message.channel.send(embed=discord.Embed(title="<a:yes:761038848947126323> 추방 성공 <a:yes:761038848947126323>", description = f"{user} 님은 {message.author.mention}님의 의해\n해당 서버에서 추방되었습니다! \n 추방사유 :```{reason}```", color = 0xFFFF00))
                elif str(e) == '403 Forbidden (error code: 50013): Missing Permissions':
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 오류 발생 <a:no:761038850046033980>", description = f'봇이 해당 유저를 추방할 수 있는 권한이 없습니다.', color = 0xFFFF00))
                elif str(e) == '404 Not Found (error code: 10007): Unknown Member':
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 오류 발생 <a:no:761038850046033980>", description = f'해당 유저를 찾을 수 없습니다.', color = 0xFFFF00))
                else:
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 오류 발생 <a:no:761038850046033980>", description = str(e), color = 0xFFFF00))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 권한 부족 <a:no:761038850046033980>", description = message.author.mention + "님은 유저를 추방할 수 있는 권한이 없습니다!", color = 0xFFFF00))
            return

    if message.content.startswith("&차단 "):
        if(message.author.guild_permissions.ban_members):
            try:
                user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[25:]
                if(len(message.content.split(" ")) == 2): 
                    reason = "차단 사유가 입력되지 않았습니다!"
                await user.ban(reason=reason)
                await user.send(embed=discord.Embed(title="차단", description = f'{message.guild.name} 서버에서\n{message.author.mention}님에 의해 차단되었습니다! \n 차단사유 : ```{reason}```', color = 0xFFFF00))
                await message.channel.send(embed=discord.Embed(title="<a:yes:761038848947126323> 차단 성공 <a:yes:761038848947126323>", description = f"{user} 님은 {message.author.mention}님의 의해\n해당 서버에서 차단되었습니다. \n 차단사유 :```{reason}```", color = 0xFFFF00))
            except Exception as e:
                if str(e) == '400 Bad Request (error code: 50007): Cannot send messages to this user':
                    await message.channel.send(embed=discord.Embed(title="<a:yes:761038848947126323> 차단 성공 <a:yes:761038848947126323>", description = f"{user} 님은 {message.author.mention}님의 의해\n해당 서버에서 차단되었습니다! \n 차단사유 :```{reason}```", color = 0xFFFF00))
                elif str(e) == '403 Forbidden (error code: 50013): Missing Permissions':
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 오류 발생 <a:no:761038850046033980>", description = f'봇이 해당 유저를 차단할 수 있는 권한이 없습니다.', color = 0xFFFF00))
                elif str(e) == '404 Not Found (error code: 10007): Unknown Member':
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 오류 발생 <a:no:761038850046033980>", description = f'해당 유저를 찾을 수 없습니다.', color = 0xFFFF00))
                else:
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 오류 발생 <a:no:761038850046033980>", description = str(e), color = 0xFFFF00))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 권한 부족 <a:no:761038850046033980>", description = message.author.mention + "님은 유저를 차단할 수 있는 권한이 없습니다!", color = 0xFFFF00))
            return
    
    elif message.content.startswith(f"&찬반투표"):
        if(message.author.guild_permissions.administrator):
            contents = message.content[6:]
            vote = await message.channel.send(embed=discord.Embed(title="<a:yes:761038848947126323> 찬반투표 <a:no:761038850046033980>", description = contents, color = 0xFFFF00))
            await vote.add_reaction('<a:yes:761038848947126323>')
            await vote.add_reaction('<a:no:761038850046033980>')
        else:
            await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 권한 부족 <a:no:761038850046033980>", description = message.author.mention + "님은 투표 기능을 사용할 수 있는 권한이 없습니다!", color = 0xFFFF00))
            return
    
    elif message.content.startswith(f"&봇공지"):
        if message.author.id in ADMINID:
            if str(message.content[4:]) == '' or str(message.content[7:]) == ' ':
                embed = discord.Embed(color=discord.Colour.red(),
                                      title='<a:no:761038850046033980> 공지 <a:no:761038850046033980> ',
                                      description='공지 메시지를 입력해주세요.', timestamp=message.created_at)
                embed.set_footer(text=f"{message.author}", icon_url="https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png")
                await message.channel.send(embed=embed)
                return
            try:
                msg = message.content[4:]
                oksv = 0
                embed = discord.Embed(
                    title=msg.split('///')[0],
                    description=msg.split('///')[
                                    1] + f"\n\n이 채널에 공지가 오기 싫다면 `봇-공지` 채널을 만들어주세요!\n[루나봇 초대하기](https://discord.com/oauth2/authorize?client_id=743039092362575902&scope=bot)\n[루나봇 커뮤니티](https://discord.gg/qjYAcJ8)",
                    colour=0xFFFF00,
                    timestamp=message.created_at
                ).set_footer(icon_url="https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png", text=f'루나 [Lunar]').set_thumbnail(
                    url=client.user.avatar_url_as(format=None, static_format="png", size=1024))
                embed.set_thumbnail(url=client.user.avatar_url)
                await message.channel.send(f"@everyone")
            except IndexError:
                await message.channel.send(f"형식이 틀렸습니다. ``&공지 <제목>///<내용>``으로 다시 시도해보세요!")
                return
            m = await message.channel.send("아래와 같이 공지가 발신됩니다!", embed=embed)
            await m.add_reaction('<a:yes:761038848947126323>')
            await m.add_reaction('<a:no:761038850046033980>')
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=20,
                                                       check=lambda reaction, user: user == message.author and str(
                                                           reaction.emoji) in ['<a:yes:761038848947126323>',
                                                                               '<a:no:761038850046033980>'])
            except asyncio.TimeoutError:
                embed = discord.Embed(color=discord.Colour.red(),
                                      title=f'<a:no:761038850046033980> 공지 <a:no:761038850046033980> ',
                                      description='시간이 초과되었습니다.', timestamp=message.created_at)
                embed.set_footer(text=f"루나 [Lunar]", icon_url="https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png")
                await message.channel.send(embed=embed)
            else:
                if str(reaction.emoji) == "<a:no:761038850046033980>":
                    embed = discord.Embed(color=discord.Colour.red(),
                                          title=f'<a:no:761038850046033980> 공지 <a:no:761038850046033980> ',
                                          description='발신 취소완료', timestamp=message.created_at)
                    embed.set_footer(text=f"루나 [Lunar]", icon_url="https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png")
                    await message.channel.send(embed=embed)
                    await asyncio.sleep(2.5)
                    await m.delete()
                elif str(reaction.emoji) == "<a:yes:761038848947126323>":
                    n = await message.channel.send("공지 발신중입니다....\n잠시만 기다려주세요")
                    for i in client.guilds:
                        arr = [0]
                        alla = False
                        flag = True
                        z = 0
                        for j in i.channels:
                            arr.append(j.id)
                            z += 1
                            if "일반" in j.name or "공지" in j.name or "채팅" in j.name or "chat" in j.name or "자유채팅" in j.name or "봇-공지" in j.name:
                                if str(j.type) == 'text':
                                    try:
                                        oksv += 1
                                        await j.send(embed=embed)
                                        alla = True
                                    except:
                                        pass
                                    break
                        if alla == False:
                            try:
                                chan = i.channels[1]
                            except:
                                pass
                            if str(chan.type) == 'text':
                                try:
                                    oksv += 1
                                    await chan.send(embed=embed)
                                except:
                                    pass
                    await message.channel.send(
                        f'<a:yes:761038848947126323> 공지 발신 완료 <a:yes:761038848947126323>\n\n{len(client.guilds)}개의 서버 중 {oksv}개의 서버에 발신 완료 <a:yes:761038848947126323>, {len(client.guilds) - oksv}개의 서버에 발신 실패 <a:no:761038850046033980>')
                    await asyncio.sleep(2.5)
                    await m.delete()
                    await n.delete()
        else:
            embed = discord.Embed(color=0xFFFF00,
                                  title=f'<a:no:761038850046033980> 사용불가 <a:no:761038850046033980>',
                                  description='사용불가 명령어 입니다\n(봇 관리자 명령어)', timestamp=message.created_at)
            embed.set_footer(text=f"루나 [Lunar]", icon_url="https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png")
            await message.channel.send(embed=embed)

    elif message.content  == '&핑':
                ping= round(client.latency * 1000)
                if ping >= 0 and ping <= 100:
                    pings = "🔵 아주 좋음"
                    embed = discord.Embed(title=f"네트워크 상태",color=0xFFFF00, timestamp=message.created_at)
                    embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
                    await message.channel.send(embed=embed)
                elif ping >= 101 and ping <= 200:
                    pings = "🟢 좋음" 
                    embed = discord.Embed(title=f"📡 네트워크 상태 📡",color=0xFFFF00, timestamp=message.created_at)
                    embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
                    await message.channel.send(embed=embed)
                elif ping >= 201 and ping <= 500:
                    pings = "🟡 보통"
                    embed = discord.Embed(title=f"📡 네트워크 상태 📡",color=0xFFFF00, timestamp=message.created_at)
                    embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
                    await message.channel.send(embed=embed)
                elif ping >= 501 and ping <= 1000:
                    pings = "🟠 나쁨"
                    embed = discord.Embed(title=f"📡 네트워크 상태 📡",color=0xFFFF00, timestamp=message.created_at)
                    embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
                    await message.channel.send(embed=embed)
                elif ping >= 1000:
                    pings = "🔴 매우나쁨"
                    embed = discord.Embed(title=f"📡 네트워크 상태 📡",color=0xFFFF00, timestamp=message.created_at)
                    embed.add_field(name="PING", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762172038236078121/766939527151091752/mug_obj_155903397022937788.png")
                    await message.channel.send(embed=embed)

    elif message.content.startswith('&프사'):
                if str(message.content[4:]) == '':
                    user = message.author
                    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                    if not len(message.author.roles) == 1:
                        roles = [role for role in user.roles]
                        embed=discord.Embed(colour=user.color, timestamp=message.created_at)
                    else:
                        embed=discord.Embed(colour=0xFFFF00, timestamp=message.created_at)
                    embed.add_field(name="사용자정보", value= f'{user}님의 프로필 사진', inline=True)
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
                                embed=discord.Embed(colour=0xFFFF00, timestamp=message.created_at, title=f"사용자정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0xFFFF00, timestamp=message.created_at)
                            embed.add_field(name="사용자정보", value= f'{user} 님의 프로필 사진', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"봇정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0xFFFF00, timestamp=message.created_at)
                            embed.add_field(name="사용자정보", value= f'{user} 님의 프로필 사진', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                    except:
                        user = await message.guild.fetch_member(int(message.content.split(' ')[1][3:21]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0xFFFF00, timestamp=message.created_at, title=f"사용자정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0xFFFF00, timestamp=message.created_at)
                            embed.add_field(name="사용자정보", value= f'{user} 님의 프로필 사진', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"봇정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0xFFFF00, timestamp=message.created_at)
                            embed.add_field(name="사용자정보", value= f'{user} 님의 프로필 사진', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)

    elif message.content.startswith(f"&캡챠"):
                author = message.author
                role = discord.utils.get(message.guild.roles, name="유저")
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
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 인증 실패 <a:no:761038850046033980>", description = f"시간이 초과되었습니다! \n 다시 시도해 보세요", color = 0xFFFF00))
                    return

                if msg.content == a:
                    await message.channel.send(embed=discord.Embed(title="<a:yes:761038848947126323> 인증 성공 <a:yes:761038848947126323>", description = f"캡챠인증에 성공하였습니다!", color = 0xFFFF00))
                    try:
                        role = discord.utils.get(message.guild.roles, name="유저")
                        await author.add_roles(role)
                    except:
                        return
                else:
                    await message.channel.send(embed=discord.Embed(title="<a:no:761038850046033980> 인증 실패 <a:no:761038850046033980>", description = f"입력된 문자가 틀렸습니다!", color = 0xFFFF00))


client.run('NzQzMDM5MDkyMzYyNTc1OTAy.XzO3FA.Y7WEQtsaQmcq0lN7f3_LhO3vXrQ')
