import os
import discord
import commands
import commands2

client = discord.Client()

@client.event
async def on_ready():
  print("Successfully logged on {0.user}".format(client))
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!alıntı"):
    await message.channel.send(commands.get_quote())

  if message.content.startswith("!yardim"):
    await message.channel.send("Komutlar : \n!sa  -*Müslüman bot selam alır*\n!alıntı  -*Rastgele özlü söz yazar*\n!covid  -*Türkiye Covid-19 istatistiklerini gösterir*\n!muz  -*Gerçek hesaplamalar sonucu temsili malafat döndürür*\n!ver  -*Bot versiyon*\n!love  -*2 isim yazarak aralarındaki aşkı ölçer (!love isim1 isim2)*\n!cevir  -*İngilizce metinleri Türkçeye çevirir*\n!tokat  -*Bir arkadaşınızı etiketleyerek tokatlarsınız (!tokat @isim)*\n!valo  -*Valorant performansınızı görüntüler*\n!csgo  -*Cs go hakkında bilinmeyen gerçekleri söyler*\n!oyun  -*Hangi oyun olduğunuzu söyler*\n!vs  -*1V1 atarak kimin daha iyi olduğunu öğrenin (!vs @nick)*\n!evlen  -*Ne zaman evleneceğinizi söyler*\n!maas  -*Maaşınızı yazar*\n!kopek  -*Hangi köpek olduğunuzu gösterir*\n!Daha fazla komut için çalışıyoruz...")

  if message.content.startswith("!sa"):
    await message.channel.send("as")

  if message.content.startswith("!covid"):
    datas = commands.get_covid()
    await message.channel.send("\U0001F4CA Covid-19 Verileri Türkiye \U0001F1F9\U0001F1F7\n\n\U0001F6A9 Toplam Vaka : %d\n\U00002755 Toplam Ölüm : %d\n\U00002705 Toplam İyileşen : %d\n\n\U0001F7E5 Bugünkü Vaka : %d\n\U000026A0 Bugünkü Ölüm : %d\n\n\U0001F4C5 Tarih : %s"%(datas[0],datas[1],datas[2],datas[3],datas[4],datas[5])) 

  if message.content.startswith("!ver"):
    await message.channel.send("Versiyon : 0.1 Beta")

  if message.content.startswith("!muz"):
    user = message.author.id
    user = "<@%s>"%(user)
    await message.channel.send("%s' in Muzu\n%s"%(user,commands.get_Banana()))
    
    
  if message.content.startswith("!love"):
    mesaj = message.content.split(" ")
    result =commands.calc_Love(mesaj[1],mesaj[2])
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

  if message.content.startswith("!cevir"):
    mesaj =message.content.split(" ")
    mesaj.remove("!cevir")
    messaj = ""
    for msg in mesaj:
      messaj = messaj + " " + msg
    result = commands.translate(messaj)["outputs"][0]
    result = result["output"]
    user = message.author.id
    user = "<@%s>"%(user)
    await message.channel.send("\U0001F4CB %s\n\n%s"%(user,result))

  if message.content.startswith("!tokat"):
    result = commands.slap(message)
    await message.channel.send("%s  %s **'i Tokat Manyağı Yapıyor**\n\n"%(result[1],result[0]))
    await message.channel.send("\n"+result[2])

  if message.content.startswith("!csgo"):
    await message.channel.send("||CS:GO çöp bir oyundur.||")

  if message.content.startswith("!valo"):
    result = commands.valo()
    user = message.author.id
    user = "<@%s>"%(user)
    await message.channel.send("\U0001F4C8 %s **'in Maç Performansı**\n\n\n\U0001F464Seçilen Ajan : **%s** \n\n\U0001F1F0 Kill : **%s**\n\n\U0001F1E9 Ölüm : **%s**\n\n\U0001F1E6 Asist : **%s**\n\n\U0001F92C Edilen küfür sayısı : **%s**\n"%(user,result[5],result[1],result[2],result[3],result[4]))
    await message.channel.send(result[0])

  if message.content.startswith("!oyun"):
    result = commands.which_game()
    user = message.author.id
    user = "<@%s>"%(user)
    await message.channel.send("%s **Sen bir oyun olsaydın** \U0001F3AE \n ```fix\n%s\n```\n\n"%(user,result[0]))
    await message.channel.send(result[1])

  if message.content.startswith("!evlen"):
    user = message.author.id
    user = "<@%s>"%(user)
    result = commands.get_married()
    await message.channel.send("\n\n%s ***'in Evleneceği Tarih	:*** ```fix\n%s.%s.%s\n```\U0001F935\U0001F470"%(user,result[2],result[1],result[0]))

  if message.content.startswith("!maas"):
    user = message.author.id
    user = "<@%s>"%(user)
    result = commands.get_salary()
    await message.channel.send("%s**'in Maaşı :**\n ```css\n%s TL\n```"%(user,result))

  if message.content.startswith("!kopek"):
    user = message.author.id
    user = "<@%s>"%(user)
    result = commands.which_dog()
    await message.channel.send("\n%s ***Bir köpek olsaydı \U0001F436	:***\n"%(user))
    await message.channel.send("%s"%(result))
    
  if message.content.startswith("!vs"):
    result = commands2.do_vs(message)
    await message.channel.send("\n\n%s \t\t\t\t\t **VS** \t\t\t\t\t %s\n\nSeçilen Silah : **%s**\t\t\t\t\tSeçilen Silah : **%s**\n\nArmor : **%s**\t\t\t\t\tArmor : **%s**\n\nKalan Can : **%d**\t\t\t\t\t\t\t\tKalan Can : **%d**\n"%(result[7],result[8],result[0],result[3],result[1],result[4],result[2],result[5]))

    await message.channel.send("%s"%(result[9]))
client.run(os.getenv("TOKEN"))
