import os
import discord
from discord.ext import commands 
from PIL import Image
from io import BytesIO
import comms
import comms2

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Game(name="V0.2   !yardim"))
  print("Successfully logged on {0.user}".format(client))

@client.command()
async def wanted(ctx, user : discord.Member = None):
  if user == None :
    user = ctx.author
  Wanted = Image.open("stuffs//wanted.jpg")
  asset = ctx.author.avatar_url_as(size = 128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((255,255))
  Wanted.paste(pfp, (98,201))
  Wanted.save("stuffs//wanted.jpg")
  await ctx.send(file = discord.File("stuffs//wanted.jpg"))

@client.command()
async def alinti(ctx):
  await ctx.send(comms.get_quote())

@client.command()
async def hello(ctx):
  await ctx.send("Hello")

@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
    return

  if message.content.startswith("!yardim"):
    await message.channel.send("Komutlar : \n!sa  -*Müslüman bot selam alır*\n!alıntı  -*Rastgele özlü söz yazar*\n!covid  -*Türkiye Covid-19 istatistiklerini gösterir*\n!muz  -*Gerçek hesaplamalar sonucu temsili malafat döndürür*\n!ver  -*Bot versiyon*\n!love  -*2 isim yazarak aralarındaki aşkı ölçer (!love isim1 isim2)*\n!cevir  -*İngilizce metinleri Türkçeye çevirir*\n!tokat  -*Bir arkadaşınızı etiketleyerek tokatlarsınız (!tokat @isim)*\n!valo  -*Valorant performansınızı görüntüler*\n!csgo  -*Cs go hakkında bilinmeyen gerçekleri söyler*\n!oyun  -*Hangi oyun olduğunuzu söyler*\n!vs  -*1V1 atarak kimin daha iyi olduğunu öğrenin (!vs @nick)*\n!evlen  -*Ne zaman evleneceğinizi söyler*\n!maas  -*Maaşınızı yazar*\n!kopek  -*Hangi köpek olduğunuzu gösterir*\n!warders  -*Warders nedir?*\n!ulke  -*Tekrar Doğsaydınız hangi ülkeli olurdunuz?*\nDaha fazla komut için çalışıyoruz...")

  if message.content.startswith("!sa"):
    await message.channel.send("as")

  if message.content.startswith("!covid"):
    datas = comms.get_covid()
    await message.channel.send("\U0001F4CA Covid-19 Verileri Türkiye \U0001F1F9\U0001F1F7\n\n\U0001F6A9 Toplam Vaka : %d\n\U00002755 Toplam Ölüm : %d\n\U00002705 Toplam İyileşen : %d\n\n\U0001F7E5 Bugünkü Vaka : %d\n\U000026A0 Bugünkü Ölüm : %d\n\n\U0001F4C5 Tarih : %s"%(datas[0],datas[1],datas[2],datas[3],datas[4],datas[5])) 

  if message.content.startswith("!ver"):
    await message.channel.send("Versiyon : 0.2 Beta")

  if message.content.startswith("!muz"):
    user = message.author.id
    user = "<@%s>"%(user)
    await message.channel.send("%s' in Muzu\n%s"%(user,comms.get_Banana()))
    
    
  if message.content.startswith("!love"):
    mesaj = message.content.split(" ")
    result =comms.calc_Love(mesaj[1],mesaj[2])
    yorum = ""
    yuzde = ""
    if(int(result["percentage"]) < 20):
      yorum = "Olmaz kanka bu ilişki yürümez "
      yuzde = result["percentage"] + "\U00002665\U00002665"
      gif = "https://media.giphy.com/media/ftdjO4qK3toNIsIynN/giphy.gif"

    elif(int(result["percentage"]) < 40):
      yorum = "Daha iyisi olur boşver bundan yâr olmaz..."
      yuzde = result["percentage"] + "\U00002665\U00002665\U00002665"
      gif = "https://media.giphy.com/media/3oriNM8HF8oijarwre/giphy.gif"

    elif(int(result["percentage"]) < 50):
      yorum = "Şansını dene olur mu olur ama söz veremem!"
      yuzde = result["percentage"] + "\U00002665\U00002665\U00002665\U00002665"
      gif = "https://media.giphy.com/media/3ov9k7CZy0ZsGITGNO/giphy.gif"

    elif(int(result["percentage"]) < 60):
      yorum = "Zorlu bir ilişki olabilir ama başaracaksınız!"
      yuzde = result["percentage"] + "\U00002665\U00002665\U00002665\U00002665\U00002665"
      gif = "https://media.giphy.com/media/Xp94ClLDMd9kc/giphy.gif"

    elif(int(result["percentage"]) < 70):
      yorum = "Sanki ruh eşini buldun gibi, yürü burdan aslanım!"
      yuzde = result["percentage"] + "\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665"
      gif = "https://media.giphy.com/media/WUrKpJUmNAsxTzHhao/giphy.gif"

    elif(int(result["percentage"]) < 80):
      yorum = "Millet kıskanır bu ilişkiyi yeminle helal olsun"
      yuzde = result["percentage"] + "\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665"
      gif = "https://media.giphy.com/media/wahoqHUmK0lFu/giphy.gif"

    elif(int(result["percentage"]) < 90):
      yorum = "Dünyaya bir daha gelseniz yine birbirinizi bulursunuz"
      yuzde = result["percentage"] + "\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665"
      gif = "https://media.giphy.com/media/3o6ZthkAMShWZvK7NC/giphy.gif"

    elif(int(result["percentage"]) <= 100):
      yorum = "Evlenseniz mi artık ?"
      yuzde = result["percentage"]+ "\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665\U00002665"
      gif = "https://media.giphy.com/media/fTmRLmuQ2BIzXlujyY/giphy.gif"
    await message.channel.send(" **%s** \U0001F970 **%s** \n\n\U0001F4C8 Aşk oranı : **%s**\U00002665\n\n\U0001F4DD Yorumum : **%s**\n\n"%(result["fname"],result["sname"],yuzde,yorum))
    await message.channel.send(gif)

  if message.content.startswith("!___cevir"):
    await message.channel.send(file = discord.File("stuffs//pp.jpg"))
    

  if message.content.startswith("!tokat"):
    result = comms.slap(message)
    await message.channel.send("%s  %s **'i Tokat Manyağı Yapıyor**\n\n"%(result[1],result[0]))
    await message.channel.send("\n"+result[2])

  if message.content.startswith("!csgo"):
    await message.channel.send("||CS:GO çöp bir oyundur.||")

  if message.content.startswith("!valo"):
    result = comms.valo()
    user = message.author.id
    user = "<@%s>"%(user)
    await message.channel.send("\U0001F4C8 %s **'in Maç Performansı**\n\n\n\U0001F464Seçilen Ajan : **%s** \n\n\U0001F1F0 Kill : **%s**\n\n\U0001F1E9 Ölüm : **%s**\n\n\U0001F1E6 Asist : **%s**\n\n\U0001F92C Edilen küfür sayısı : **%s**\n"%(user,result[5],result[1],result[2],result[3],result[4]))
    await message.channel.send(result[0])

  if message.content.startswith("!oyun"):
    result = comms.which_game()
    user = message.author.id
    user = "<@%s>"%(user)
    await message.channel.send("%s **Sen bir oyun olsaydın** \U0001F3AE \n ```fix\n%s\n```\n\n"%(user,result[0]))
    await message.channel.send(result[1])

  if message.content.startswith("!evlen"):
    user = message.author.id
    user = "<@%s>"%(user)
    result = comms.get_married()
    await message.channel.send("\n\n%s ***'in Evleneceği Tarih	:*** ```fix\n%s.%s.%s\n```\U0001F935\U0001F470"%(user,result[2],result[1],result[0]))

  if message.content.startswith("!maas"):
    user = message.author.id
    user = "<@%s>"%(user)
    result = comms.get_salary()
    await message.channel.send("%s**'in Maaşı :**\n ```css\n%s TL\n```"%(user,result))

  if message.content.startswith("!kopek"):
    user = message.author.id
    user = "<@%s>"%(user)
    result = comms.which_dog()
    await message.channel.send("\n%s ***Bir köpek olsaydı \U0001F436	:***\n"%(user))
    await message.channel.send("%s"%(result))
    
  if message.content.startswith("!vs"):
    result = comms2.do_vs(message)
    liste = ["Seçilen Silah", "Armor","Kalan Can"]
    await message.channel.send("\n\n%s \t\t\t\t\t **VS** \t\t\t\t\t %s\n\n%-15s : **%-15s**\t\t\t\t\t%-15s : **%-15s**\n\n%-17s : **%-15s**\t\t\t\t%-17s : **%-15s**\n\n%-13s : **%-10d**\t\t\t\t\t\t\t\t%-13s : **%-10d**\n"%(result[8],result[7],liste[0],result[0],liste[0],result[3],liste[1],result[1],liste[1],result[4],liste[2],result[2],liste[2],result[5]))

    await message.channel.send("%s"%(result[9]))
  
  if message.content.startswith("!warders"):
    await message.channel.send("\n```fix\nHayatımın Anlamı \U0001F49B \U0001F5A4\n```")

  if message.content.startswith("!ulke"):
    user = message.author.id
    user = "<@%s>"%(user)
    result = comms2.Get_Countries()
    await message.channel.send("\n%s\n```fix\n\U0001F3D9 Yeniden Dünyaya Gelsen Doğacağın Ülke : %s\n```"%(user,result[1]))
    await message.channel.send("%s"%(result[0]))

client.run(os.getenv("TOKEN"))
