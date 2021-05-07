import requests
import json
import random
from datetime import date
import datetime

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"]+ "\n\n-" + json_data[0]["a"]
  return quote

def get_covid():
  response = requests.get("https://api.covid19api.com/total/country/turkey")
  json_data = json.loads(response.text)
  totalConfirmed = 0
  totalDeaths = 0
  totalRecovered = 0
  dailyConfirmed = 0
  dailyDeaths = 0
  today = date.today()
  for country in json_data:
      dailyConfirmed = totalConfirmed
      dailyDeaths = totalDeaths
      totalConfirmed = country["Confirmed"]
      totalDeaths = country["Deaths"]
      totalRecovered = country["Recovered"]
  datas = [totalConfirmed, totalDeaths,totalRecovered,(totalConfirmed- dailyConfirmed),(totalDeaths - dailyDeaths),today]
  return datas
  
def get_Banana():
  lenght = random.randint(0,20)
  return ")" + lenght * "=" + ">"

def calc_Love(fname,sname):
  url = "https://love-calculator.p.rapidapi.com/getPercentage"
  querystring = {"fname":fname,"sname":sname}
  headers = {
    'x-rapidapi-key': "091e930bf4msh32d100b509d1337p191659jsne5e67a752866",
    'x-rapidapi-host': "love-calculator.p.rapidapi.com"
    }
  response = requests.request("GET", url, headers=headers, params=querystring)
  return json.loads(response.text)

def translate(message):
  url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"

  querystring = {"source":"en","target":"tr","input":message}

  headers = {
      'x-rapidapi-key': "091e930bf4msh32d100b509d1337p191659jsne5e67a752866",
      'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com"
      }
  response = requests.request("GET", url, headers=headers, params=querystring)

  return json.loads(response.text)

def slap(message):
  user0 =message.content.split(" ")
  user0 = user0[1]
  user1 = message.author.id
  user1 = "<@%s>"%(user1)
  gifs = ["https://media.giphy.com/media/3XlEk2RxPS1m8/giphy.gif",
    "https://media.giphy.com/media/s5zXKfeXaa6ZO/giphy.gif",
    "https://media.giphy.com/media/j3iGKfXRKlLqw/giphy.gif",
    "https://media.giphy.com/media/F0E72ofVJFEGc/giphy.gif",
    "https://media.giphy.com/media/wXgBk2fM696gM/giphy.gif",
    "https://media.giphy.com/media/RXGNsyRb1hDJm/giphy.gif",
    "https://media.giphy.com/media/26uf3m46sDFVPedig/giphy.gif",
    "https://media.giphy.com/media/IAAXyr5GU73xK/giphy.gif",
    "https://media.giphy.com/media/12LjisUEAp8bx6/giphy.gif",
    "https://media.giphy.com/media/Hj9ixvpSfqcQo/giphy.gif",
    "https://tenor.com/vX72.gif",
    "https://tenor.com/vEDn.gif",]
  gifs = random.choice(gifs)
  result = [user0,user1,gifs]
  return result

def valo():
  agents = ["https://media.giphy.com/media/ps6rntMhYWEyO3i4QI/giphy.gif",
  "https://media.giphy.com/media/LNCDNtqQkTBbDI2bGO/giphy.gif",
  "https://media.giphy.com/media/xfpEhOZAOSnMSSFFyt/giphy.gif",
  "https://media.giphy.com/media/wMa8tRg5iD0Vkaswqe/giphy.gif",
  "https://media.giphy.com/media/CiasqOHcXesqB8zKoI/giphy.gif",
  "https://media.giphy.com/media/ceUY9mubodXVYC0HlD/giphy.gif",
  "https://i.pinimg.com/564x/f5/6c/c2/f56cc2b685a2714c176d68a330cc42b6.jpg",
  "https://www.esporgazetesi.com/wp-content/uploads/2020/08/VALORANT_Jett-scaled.jpg",
  "https://gamerbase.org/wp-content/uploads/2021/01/VALORANT_Phoenix_Dark-2048x1152-1.jpg",
  "https://pbetr.com/wp-content/uploads/2020/03/sovavalorant.jpeg",
  "https://i.ytimg.com/vi/ZcJZsYMwwo0/maxresdefault.jpg",
  "https://esportimes.mncdn.com/wp-content/uploads/2021/01/valorant-brimstone-esportimes-1024x576.jpg",
  "https://i.ytimg.com/vi/Rux0HjzKQbw/maxresdefault.jpg",
  "https://gamergiller.com/wp-content/uploads/2020/04/omen-890x500.jpg",
  "https://www.kolsuzoyuncu.com/wp-content/uploads/sage.jpg"]
  txtagent = ["VIPER","ASTRA","YORU","SKYE","CYPHER","KILLJOY","RAZE",
  "JETT","PHOENIX","SOVA","REYNA","BRIMSTONE","BREACH","OMEN","SAGE"]
  index = random.randint(0,14)
  kill = random.randint(0,40)
  death = random.randint(5,30)
  assist = random.randint(0,10)
  agents = agents[index]
  txtagent = txtagent[index]
  swear = random.randint(0,15)
  result = [agents,kill,death,assist,swear,txtagent]
  return result

def which_game():
  games = ["Pokémon Go",
  "Borderlands 2",
  "Divinity: Original Sin 2",
  "Dishonored","Final Fantasy VII",
  "Assassin's Creed IV: Black Flag",
  "Monkey Island 2: LeChuck's Revenge",
  "Burnout 3: Takedown",
  "Fallout 2",
  "Undertale",
  "League of Legends",
  "Mega Man 3",
  "Soulcalibur",
  "Thief II: The Metal Age",
  "SimCity 2000",
  "Inside",
  "Contra",
  "Tony Hawk's Pro Skater 2",
  "Monster Hunter: World",
  "Resident Evil 2 (Remake)",
  "System Shock 2",
  "Grand Theft Auto: Vice City",
  "Persona 5",
  "Fortnite",
  "Fable 2",
  "GoldenEye 007",
  "Super Smash Bros. Ultimate",
  "The Elder Scrolls V: Skyrim",
  "X-COM: UFO Defense",
  "Suikoden II",
  "Battlefield 1942",
  "Dota 2",
  "Mario Kart 8 Deluxe",
  "Star Wars Jedi Knight II: Jedi Outcast",
  "Spelunky",
  "Donkey Kong",
  "The Sims",
  "Red Dead Redemption 2",
  "Splinter Cell: Chaos Theory",
  "Super Mario World 2: Yoshi's Island",
  "Silent Hill 2",
  "Grand Theft Auto: San Andreas",
  "Mass Effect",
  "Call of Duty 4: Modern Warfare",
  "Rise of the Tomb Raider",
  "Batman: Arkham City",
  "The Witness",
  "Journey",
  "Uncharted 2: Among Thieves",
  "Overwatch",
  "Deus Ex",
  "Baldur's Gate II: Shadows of Amn",
  "Ms. Pac-Man",
  "Counter-Strike 1.6",
  "Left 4 Dead 2",
  "EarthBound",
  "Resident Evil",
  "Diablo II",
  "StarCraft",
  "World of Warcraft",
  "Star Wars: Knights of the Old Republic",
  "Fallout: New Vegas",
  "Final Fantasy VI",
  "Mass Effect 2",
  "Pokémon Yellow",
  "Bloodborne",
  "Metroid Prime",
  "Resident Evil 4",
  "Shadow of the Colossus",
  "Metal Gear Solid",
  "God of War",
  "The Witcher 3: Wild Hunt",
  "BioShock",
  "Sid Meier's Civilization IV",
  "The Legend of Zelda: Ocarina of Time",
  "Minecraft",
  "Halo: Combat Evolved",
  "Half-Life",
  "Metal Gear Solid 3: Snake Eater",
  "The Last of Us",
  "Doom",
  "Chrono Trigger",
  "Portal",
  "Dark Souls",
  "Street Fighter II",
  "Super Mario Bros.",
  "Halo 2",
  "Castlevania: Symphony of the Night",
  "Grand Theft Auto V",
  "Super Mario 64",
  "Red Dead Redemption",
  "Half-Life 2",
  "Tetris",
  "Super Mario Bros. 3",
  "The Legend of Zelda: Breath of the Wild",
  "Super Metroid",
  "Portal 2",
  "Super Mario World",
  "The Legend of Zelda: A Link to the Past",
  "Valorant",
  "CS:Go"]


  gifs =["https://assets1.ignimgs.com/2018/03/19/pokemongo-1521495131603_640w.jpg",
  "https://assets2.ignimgs.com/2013/12/17/borderlands2jpg-e97334_640w.jpg",
  "https://assets1.ignimgs.com/2019/10/08/divinity2-1570559794060_640w.jpg",
  "https://assets2.ignimgs.com/2014/07/28/dishonored100812headerjpg-0d21a6_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/80finalfantasy7jpg-565a0a_1024w.jpg","https://assets1.ignimgs.com/2014/05/15/20994jpg-9582e2_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/62monkeyisland2jpg-565a14_640w.jpg","https://assets1.ignimgs.com/2016/11/30/65burnout3jpg-6c6148_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/83fallout2jpg-36b6cc_1024w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/undertale-1521495131607_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/74leagueoflegendsjpg-565a11_1024w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/mega-man-3-1521496758179_640w.png",
  "https://assets1.ignimgs.com/2018/03/19/soulcalibur-1521495131604_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/54thief2jpg-565a19_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/87simcity2000jpg-6c6142_1024w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/inside-1521495131595_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/84contrajpg-36b6cb_640w.jpg",
  "https://assets1.ignimgs.com/2019/10/16/83-thps2-1571246807014_640w.jpg",
  "https://assets1.ignimgs.com/thumbs/userUploaded/2018/8/31/hotkeysmhw11280-1535745227534_1024w.jpg",
  "https://assets1.ignimgs.com/2019/01/22/residentevil2-blogroll-1548123721286_640w.jpg","https://assets1.ignimgs.com/2016/11/30/90systemshock2jpg-565a07_640w.jpg","https://assets1.ignimgs.com/2016/11/30/88gtavicecityjpg-6c6141_640w.jpg","https://assets1.ignimgs.com/2018/03/19/persona5-1521495131601_1024w.jpg","https://assets1.ignimgs.com/2018/06/01/fortnite-switch-1527812947830_1024w.jpg",
  "https://assets1.ignimgs.com/2019/10/08/fable2-1570565712764_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/66goldeneye007jpg-6c6149_1024w.jpg",
  "https://assets1.ignimgs.com/2018/11/19/smashultimate-prev-blogroll-1542650383319_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/64skyrimjpg-36b6d5_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/85xcomufodefensejpg-565a0c_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/68suikoden2jpg-36b6d7_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/33battlefield1942jpg-565a20_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/50dota2jpg-565a1a_1024w.jpg",
  "https://assets1.ignimgs.com/2017/03/14/mariokart8deluxe-1280-1489529517460_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/55jedioutcastjpg-6c614a_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/72spelunkyjpg-36b6d1_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/60donkeykongjpg-6c6147_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/32rockbandjpg-6c6155_640w.jpg",
  "https://assets1.ignimgs.com/2018/12/21/rdr2-1545415551744_640w.jpg",
  "https://assets1.ignimgs.com/2019/10/08/splintercellct-1570570239007_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/92yoshisislandjpg-565a06_1024w.jpg",
  "https://assets2.ignimgs.com/2015/10/09/silenthill2-top100png-996828_640w.png",
  "https://assets1.ignimgs.com/2018/03/19/gtasanandreas-1521495131595_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/38masseffectjpg-6c6153_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/49modernwarfarejpg-36b6dd_1024w.jpg",
  "https://assets1.ignimgs.com/2019/10/08/riseofthetombraider-1570570697256_1024w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/batmanarkhamcity-1521495131593_640w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/thewitness-1521495131606_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/39journeyjpg-36b6de_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/47uncharted2jpg-6c614d_640w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/overwatch-1521495131600_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/19deusexjpg-565a27_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/18baldursgateiijpg-6c6159_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/53mspacmanjpg-36b6da_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/42counterstrike16jpg-6c6150_1024w.jpg",
  "https://assets2.ignimgs.com/2014/09/02/left-4-dead-2-20090923033652463-3001274jpg-ed62d9_640w.jpg",
  "https://assets1.ignimgs.com/2013/11/19/earthbound0724131600-copyjpg-885478_640w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/residentevil1-1521496667254_1024w.jpg",
  "https://assets1.ignimgs.com/2017/07/27/diablo-ii-1280-1501133847054_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/56starcraftjpg-36b6d9_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/35worldofwarcraftjpg-36b6df_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/31kotorjpg-565a21_640w.jpg",
  "https://assets1.ignimgs.com/2018/06/20/fnv-1529534456309_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/28ff6jpg-565a23_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/51masseffect2jpg-36b6db_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/52pokemonyellowjpg-6c614b_1024w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/bloodborne-1521495131594_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/46metroidprimejpg-6c614e_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/43residentevil4jpg-6c614f_1024w.jpg",
  "https://assets1.ignimgs.com/2018/01/30/shadowofthecolossus-1280-1517280966892_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/41metalgearsolidjpg-6c6151_1024w.jpg",
  "https://assets1.ignimgs.com/2016/06/21/untitled-3jpg-485315_640w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/thewitcher3-1521495131605_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/36bioshockjpg-6c6154_640w.jpg",
  "https://assets1.ignimgs.com/2016/05/12/civ631280jpg-653088_640w.jpg",
  "https://assets1.ignimgs.com/2014/08/27/zeldaoot1280jpg-dff35b_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/15minecraftjpg-36b6e4_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/22halocombatevolvedjpg-36b6e3_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/26half-lifejpg-36b6e1_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/25metalgearsolid3snakeeaterjpg-565a24_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/48thelastofusjpg-6c614c_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/03doomjpg-36b6c4_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/13chronotriggerjpg-565a29_640w.jpg",
  "https://assets1.ignimgs.com/2014/05/07/071portaljpg-a2a1b3_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/40darksoulsjpg-565a1d_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/20streetfighteriijpg-6c6158_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/04supermariobrosjpg-565a03_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/09halo2jpg-36b6e7_1024w.jpg",
  "https://assets1.ignimgs.com/2018/03/29/sotn1-1522363640372_1024w.png",
  "https://assets2.ignimgs.com/2016/11/30/16gtavjpg-565a28_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/11supermario64jpg-36b6e6_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/29reddeadredemptionjpg-36b6e0_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/06half-life2jpg-6c615c_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/10tetrisjpg-565a2b_1024w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/01supermariobros3jpg-36b6c5_640w.jpg",
  "https://assets1.ignimgs.com/2018/03/19/zeldabotw-1521495131608_640w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/07supermetroidjpg-36b6e8_640w.jpg",
  "https://assets2.ignimgs.com/2016/11/30/05portal2jpg-36b6e9_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/14supermarioworldjpg-36b6e5_1024w.jpg",
  "https://assets1.ignimgs.com/2016/11/30/02tlozalinktothepastjpg-36b6c3_640w.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Valorant_logo_-_pink_color_version.svg/1200px-Valorant_logo_-_pink_color_version.svg.png",
  "https://cdn.akamai.steamstatic.com/steam/apps/730/capsule_616x353.jpg?t=1612812939",]

  index = random.randint(0,101)
  games = games[index]
  gifs = gifs[index]
  result = [games,gifs]
  return result

def get_married():
  zaman = datetime.datetime.now()
  year = random.randint(0,15)
  year = int(zaman.year) + year
  result = [year , zaman.month, zaman.day]
  return result