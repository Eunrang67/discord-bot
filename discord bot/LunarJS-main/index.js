const Discord = require('discord.js');
const client = new Discord.Client();
const token = 'NzQzMDM5MDkyMzYyNTc1OTAy.XzO3FA.Y7WEQtsaQmcq0lN7f3_LhO3vXrQ';
const moment = require("moment");
const ADMINID = 692324859224522753;

require("moment-duration-format");

client.on('ready', () => {
  console.log('봇이 실행되었습니다');
});

client.on('message', (message) => {
  if(message.author.bot) return;

  if(message.channel.type == 'dm') {
    return
  }

  else if(message.content.startsWith('&출력 ')) {
    let contents = message.content.slice('&출력 '.length);
    let embed = new Discord.RichEmbed()
      .setAuthor("💬 메시지 출력 💬")
      .setColor('#FFFF00')
      .setFooter(`루나 [Lunar]`)
      .setTimestamp()
    embed.addField('출력내용: ', contents);
    embed.addField('명령어 실행 유저 :', `<@${message.author.id}>`);
    message.channel.send(embed);
  }

  else if(message.content.startsWith('&봇초대링크 ')) {
    let botid = message.content.slice('&봇초대링크 '.length);
    let embed = new Discord.RichEmbed()
      .setAuthor("💌 봇 초대링크 생성 💌")
      .setColor('#FFFF00')
      .setFooter(`루나 [Lunar]`)
      .setTimestamp()
    embed.addField('출력내용: ', 'https://discord.com/oauth2/authorize?client_id=743039092362575902&scope=bot' + botid + '&scope=bot');
    embed.addField('명령어 실행 유저 :', `<@${message.author.id}>`);
    message.channel.send(embed);
  } 
  
  if(message.content == '&초대링크') {
    message.author.send('https://bit.ly/366KI6k');
    message.channel.send('초대 링크를 DM으로 보냈습니다!');
  }


  if(message.content == '&공식서버') {
    message.author.send('https://discord.gg/gQMjyWk');
    message.channel.send('공식 디스코드 서버 링크를 DM으로 보냈습니다!');
  }

  if(message.content == '&명령어') {
    let embed = new Discord.RichEmbed()
    let img = 'https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png';
    embed.setColor('#FFFF00')
    embed.setAuthor('루나봇 명령어', img)
    embed.setFooter(`루나 [Lunar]`)
    embed.addField('명령어 사용 가이드', '서버 관리 명령어는 서버 안에서 각각 알맞은 권한이 있어야 실행가능 합니다.\n( ) 괄호 안 메시지는 선택 입력이며 [ ] 대괄호 메시지는 필수 입력입니다');
    embed.addField('서버 관리 명령어', '&추방 @user (추방사유) - 멘션한 사용자를 서버에서 추방합니다\n&차단 @user (차단사유) - 멘션한 사용자를 서버에서 차단합니다\n&차단해제 [계정ID] - 입력한 계정 ID 차단을 해제합니다\n&삭제 [N] - N개의 메시지를 삭제합니다\n&DM공지 [내용] - 공지를 DM으로 전송합니다\n&찬반투표 [투표내용] - [투표내용]에 대한 찬반투표를 진행합니다\n&채널정보 #channel - 멘션한 채널의 정보를 보여줍니다');
    embed.addField('일반 명령어', '&봇상태 - 루나봇 상태를 출력합니다\n&공식서버 - 루나봇 커뮤니티 링크를 출력합니다\n&초대링크 - 루나봇 초대링크를 DM으로 보냅니다\n&개발 - 루나봇 개발 정보를 출력합니다\n&핑 - 루나봇 네트워크 지연 시간을 보여줍니다\n&봇초대링크 [봇ID] - [봇ID]의 봇 초대링크를 생성합니다\n&출력 [INPUT] - [INPUT]을 출력합니다\n&프사 @user - 멘션한 사용자의 프사를 출력합니다');
    embed.addField('루나봇 관리자 명령어', '&봇공지 - 루나봇 공지를 서버에 전송합니다\n&서버 - 봇이 들어가있는 서버를 출력합니다');
    embed.setTimestamp()
    message.author.send(embed);
    message.channel.send('명령어 도움말을 DM으로 보냈습니다!');
  }

  if(message.content == '&서버') {
    if(message.author.id == ADMINID) {
      let embed = new Discord.RichEmbed()
      let img = 'https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png'
      embed.setColor('#FFFF00')
      embed.setFooter('루나 [Lunar]')
      let arr = client.guilds.array();
      let list = '';
      list = `\`\`\`css\n`;
      
      for(let i=0;i<arr.length;i++) {
        // list += `${arr[i].name} - ${arr[i].id}\n`
        list += `${arr[i].name}\n`
      }
      list += `\`\`\`\n`
      embed.addField('서버 리스트:',        `${list}`);
      embed.setTimestamp()
      message.author.send(embed);
      message.channel.send('DM으로 서버 목록을 전송했습니다!')
    }
    else {
      message.channel.send(`<@${message.author.id}>` + '님은 이 명령어를 사용할 수 없습니다! (봇 관리자 명령어)');
    }
  }

  if(message.content == '&봇상태') {
    let embed = new Discord.RichEmbed()
    let img = 'https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png';
    var duration = moment.duration(client.uptime).format(" D [일], H [시간], m [분], s [초]");
    embed.setColor('#FFFF00')
    embed.setAuthor('루나봇의 상태입니다!', img)
    embed.setFooter('루나 [Lunar]')
    embed.addField('사용중인 램',    `${(process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2)} MB`, true);
    embed.addField('봇 작동시킨지..', `${duration}`, true);
    embed.addField('서버 개수',       `${client.guilds.size.toLocaleString()}`, true);
    embed.addField('Discord.js 버전',   `v${Discord.version}`, true);
    embed.addField('Node.js 버전',         `${process.version}`, true);
    embed.addField('Discord.py 버전', 'v1.5.0', true);
    embed.addField('Python 버전', 'v3.8.5', true);
    embed.setTimestamp()
    message.channel.send(embed);
  }

  if(message.content == '&개발') {
    let embed = new Discord.RichEmbed()
    let img = 'https://cdn.discordapp.com/attachments/744186060182913138/769473852626567188/Lunaricon.png';
    embed.setColor('#FFFF00')
    embed.setAuthor('루나봇 개발 정보입니다!', img)
    embed.setFooter('루나 [Lunar]')
    embed.addField('개발자 :', '<@692324859224522753> & <@556300258716418050>');
    embed.addField('봇 버전 :', 'v2.5');
    embed.addField('최근 업데이트 날짜 :', '2020/10/15');
    embed.addField('Discord.js 버전',   `v${Discord.version}`);
    embed.addField('Node.js 버전',         `${process.version}`);
    embed.addField('Discord.py 버전', 'v1.5.0');
    embed.addField('Python 버전', 'v3.8.5');
    embed.setTimestamp()
    message.channel.send(embed);
  }
      
      else if(message.content.startsWith('&삭제')) {
        if(Permission_MESSAGES(message)) return
    
        var clearLine = message.content.slice('&삭제 '.length);
        var isNum = !isNaN(clearLine)
    
        if(isNum && (clearLine <= 0 || 100 < clearLine)) {
          let embed2 = new Discord.RichEmbed()
              embed2.setColor('#FFFF00')
              embed2.setFooter(`루나 [Lunar]`)
              embed2.addField('<a:no:761038850046033980> 오류 <a:no:761038850046033980>', '1부터 99까지의 숫자만 입력해주세요!')
              embed2.addField('명령어 실행 유저 :', `<@${message.author.id}>`);
              embed2.setTimestamp()
              message.channel.send(embed2)
          return;
        } else if(!isNum) { // c @나긋해 3
          if(message.content.split('<@').length == 2) {
            if(isNaN(message.content.split(' ')[2])) return;
    
            var user = message.content.split(' ')[1].split('<@!')[1].split('>')[0];
            var count = parseInt(message.content.split(' ')[2])+1;
            const _limit = 10;
            let _cnt = 0;
    
            message.channel.fetchMessages({limit: _limit}).then(collected => {
              collected.every(msg => {
                if(msg.author.id == user) {
                  msg.delete();
                  ++_cnt;
                }
                return !(_cnt == count);
              });
            });
          }
        } else {
          message.channel.bulkDelete(parseInt(clearLine)+1)
            .then(() => {
              let embed = new Discord.RichEmbed()
              embed.setColor('#FFFF00')
              embed.setFooter(`루나 [Lunar]`)
              embed.addField('<a:yes:761038848947126323> 삭제 성공! <a:yes:761038848947126323>', + clearLine + '개의 메시지를 삭제했습니다!')
              embed.addField('명령어 실행 유저 :', `<@${message.author.id}>`);
              embed.setTimestamp()
              message.channel.send(embed)
            })
            .catch(console.error)
        }
      }
    });

    
    
    function Permission_MESSAGES(message) {
      if(!message.member.hasPermission("MANAGE_MESSAGES")) {
        let embed = new Discord.RichEmbed()
            embed.setColor('#FFFF00')
            embed.setFooter(`루나 [Lunar]`)
            embed.addField('<a:no:761038850046033980> 권한 부족! <a:no:761038850046033980>', `<@${message.author.id}>` + '님은 명령어를 실행할 권한이 없습니다!')
            embed.addField('명령어 실행 유저 :', `<@${message.author.id}>`);
            embed.setTimestamp()
        message.channel.send(embed)
        return true;
      } else {
        return false;
      }
    }

    function Permission_ADMIN(message) {
      if(!message.member.hasPermission("ADMINISTRATOR")) {
        let embed = new Discord.RichEmbed()
            embed.setColor('#FFFF00')
            embed.setFooter(`루나 [Lunar]`)
            embed.addField('<a:no:761038850046033980> 권한 부족! <a:no:761038850046033980>', `<@${message.author.id}>` + '님은 명령어를 실행할 권한이 없습니다!')
            embed.addField('명령어 실행 유저 :', `<@${message.author.id}>`);
            embed.setTimestamp()
        message.channel.send(embed)
        return true;
      } else {
        return false;
      }
    }
    
    function changeCommandStringLength(str, limitLen = 8) {
      let tmp = str;
      limitLen -= tmp.length;
    
      for(let i=0;i<limitLen;i++) {
          tmp += ' ';
      }
    
      return tmp;
    }
    
    async function AutoMsgDelete(message, str, delay = 3000) {
      let msg = await message.channel.send(str);
    
      setTimeout(() => {
        msg.delete();
      }, delay);
    }
    
    
    client.login(token);
