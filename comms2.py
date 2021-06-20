import requests
import json
import random

def do_vs(message):
  #0 = legs , #1=chest , #2=head
  guns = ["Classic","Shorty","Frenzy","Ghost","Sheriff",
          "Stinger","Spectre","Bucky","Judge","Bulldog",
          "Guardian","Phantom","Vandal","Marshal","Operator",
          "Ares","Odin"]
  ArmorType=["Armor yok","Hafif Armor","Ağır Armor"]
  health = ["100","125","150"]
  Lenght = ["0-30m",">50m"]
  shoot_type = ["legs","chest","head"]
  user0 = []
  user1 = []
  index_0 = random.randint(0,2)
  index_1 = random.randint(0,2)
  user0_armor = ArmorType[index_0]
  user0_health = health[index_0]

  user1_armor = ArmorType[index_1]
  user1_health = health[index_1]

  totalDamage0 = 0
  totalDamage1 = 0
  user0_health = int(user0_health)
  user1_health = int(user1_health)
  user1_status = 1
  user0_status = 1
  counter = 0
  while(user0_health >= 0 or user1_health >= 0):
    damage0 = random.randint(0,50)
    damage1 = random.randint(0,50)
    totalDamage0 +=damage0
    totalDamage1 +=damage1
    user0_health -=damage1
    user1_health -=damage0
    if(user1_health <= 0 or user0_health <= 0):
      if(user0_health > 0 and user1_health <= 0):
        user1_status = 0
        user1_health = 0
        break
      elif(user0_health <= 0 and user1_health > 0):
        user0_health = 0
        user0_status = 0
        break
      elif (user0_health <= 0 and user1_health <= 0):
        totalDamage0 = 0
        totalDamage1 = 0
        user0_health = int(user0_health)
        user1_health = int(user1_health)
        continue
  gif = ["https://i.ytimg.com/vi/3xT4XydSFAI/sddefault.jpg",
    "https://i.ytimg.com/vi/Ub6Yfb_zpCI/maxresdefault.jpg"]

  Sonuc = ["LOSE","WIN"]
  if(user0_status == 0):
    Sonuc = Sonuc[0]
    gif = gif[0]
    user0_health = 0
  else:
    Sonuc = Sonuc[1]
    gif = gif[1]
    user1_health = 0
  if(Sonuc == "WIN" and user0_health < 0):
    user0_health = user0_health*-1
  user0_gun = random.choice(guns)
  user1_gun = random.choice(guns)
  fight_len = random.choice(Lenght)

  
  user0_message =message.content.split(" ")
  user0_message = user0_message[1]
  user1_mention = message.author.id
  user1_mention = "<@%s>"%(user1_mention)
  result = [
  user0_gun,
  user0_armor,
  user0_health,
  user1_gun,
  user1_armor,
  user1_health,
  Sonuc,
  user0_message,
  user1_mention,
  gif]

  return result
  

def Get_Countries():
  gif_list = [
  "https://www.worldometers.info/img/flags/af-flag.gif",
  "https://www.worldometers.info/img/flags/al-flag.gif",
  "https://www.worldometers.info/img/flags/ag-flag.gif",
  "https://www.worldometers.info/img/flags/an-flag.gif",
  "https://www.worldometers.info/img/flags/ao-flag.gif",
  "https://www.worldometers.info/img/flags/ac-flag.gif",
  "https://www.worldometers.info/img/flags/ar-flag.gif",
  "https://www.worldometers.info/img/flags/am-flag.gif",
  "https://www.worldometers.info/img/flags/as-flag.gif",
  "https://www.worldometers.info/img/flags/au-flag.gif",
  "https://www.worldometers.info/img/flags/aj-flag.gif",
  "https://www.worldometers.info/img/flags/bf-flag.gif",
  "https://www.worldometers.info/img/flags/ba-flag.gif",
  "https://www.worldometers.info/img/flags/bg-flag.gif",
  "https://www.worldometers.info/img/flags/bb-flag.gif",
  "https://www.worldometers.info/img/flags/bo-flag.gif",
  "https://www.worldometers.info/img/flags/be-flag.gif",
  "https://www.worldometers.info/img/flags/bh-flag.gif",
  "https://www.worldometers.info/img/flags/bn-flag.gif",
  "https://www.worldometers.info/img/flags/bt-flag.gif",
  "https://www.worldometers.info/img/flags/bl-flag.gif",
  "https://www.worldometers.info/img/flags/bk-flag.gif",
  "https://www.worldometers.info/img/flags/bc-flag.gif",
  "https://www.worldometers.info/img/flags/br-flag.gif",
  "https://www.worldometers.info/img/flags/bx-flag.gif",
  "https://www.worldometers.info/img/flags/bu-flag.gif",
  "https://www.worldometers.info/img/flags/uv-flag.gif",
  "https://www.worldometers.info/img/flags/by-flag.gif",
  "https://www.worldometers.info/img/flags/iv-flag.gif",
  "https://www.worldometers.info/img/flags/cv-flag.gif",
  "https://www.worldometers.info/img/flags/cb-flag.gif",
  "https://www.worldometers.info/img/flags/cm-flag.gif",
  "https://www.worldometers.info/img/flags/ca-flag.gif",
  "https://www.worldometers.info/img/flags/ct-flag.gif",
  "https://www.worldometers.info/img/flags/cd-flag.gif",
  "https://www.worldometers.info/img/flags/ci-flag.gif",
  "https://www.worldometers.info/img/flags/ch-flag.gif",
  "https://www.worldometers.info/img/flags/co-flag.gif",
  "https://www.worldometers.info/img/flags/cn-flag.gif",
  "https://www.worldometers.info/img/flags/cg-flag.gif",
  "https://www.worldometers.info/img/flags/cs-flag.gif",
  "https://www.worldometers.info/img/flags/hr-flag.gif",
  "https://www.worldometers.info/img/flags/cu-flag.gif",
  "https://www.worldometers.info/img/flags/cy-flag.gif",
  "https://www.worldometers.info/img/flags/ez-flag.gif",
  "https://www.worldometers.info/img/flags/da-flag.gif",
  "https://www.worldometers.info/img/flags/dj-flag.gif",
  "https://www.worldometers.info/img/flags/do-flag.gif",
  "https://www.worldometers.info/img/flags/dr-flag.gif",
  "https://www.worldometers.info/img/flags/kn-flag.gif",
  "https://www.worldometers.info/img/flags/congo-flag.gif",
  "https://www.worldometers.info/img/flags/ec-flag.gif",
  "https://www.worldometers.info/img/flags/eg-flag.gif",
  "https://www.worldometers.info/img/flags/es-flag.gif",
  "https://www.worldometers.info/img/flags/ek-flag.gif",
  "https://www.worldometers.info/img/flags/er-flag.gif",
  "https://www.worldometers.info/img/flags/en-flag.gif",
  "https://www.worldometers.info/img/flags/wz-flag.gif",
  "https://www.worldometers.info/img/flags/et-flag.gif",
  "https://www.worldometers.info/img/flags/fj-flag.gif",
  "https://www.worldometers.info/img/flags/fi-flag.gif",
  "https://www.worldometers.info/img/flags/fr-flag.gif",
  "https://www.worldometers.info/img/flags/gb-flag.gif",
  "https://www.worldometers.info/img/flags/ga-flag.gif",
  "https://www.worldometers.info/img/flags/gg-flag.gif",
  "https://www.worldometers.info/img/flags/gm-flag.gif",
  "https://www.worldometers.info/img/flags/gh-flag.gif",
  "https://www.worldometers.info/img/flags/gr-flag.gif",
  "https://www.worldometers.info/img/flags/gj-flag.gif",
  "https://www.worldometers.info/img/flags/gt-flag.gif",
  "https://www.worldometers.info/img/flags/gv-flag.gif",
  "https://www.worldometers.info/img/flags/pu-flag.gif",
  "https://www.worldometers.info/img/flags/gy-flag.gif",
  "https://www.worldometers.info/img/flags/ha-flag.gif",
  "https://www.worldometers.info/img/flags/vt-flag.gif",
  "https://www.worldometers.info/img/flags/ho-flag.gif",
  "https://www.worldometers.info/img/flags/hu-flag.gif",
  "https://www.worldometers.info/img/flags/ic-flag.gif",
  "https://www.worldometers.info/img/flags/in-flag.gif",
  "https://www.worldometers.info/img/flags/id-flag.gif",
  "https://www.worldometers.info/img/flags/ir-flag.gif",
  "https://www.worldometers.info/img/flags/iz-flag.gif",
  "https://www.worldometers.info/img/flags/ei-flag.gif",
  "https://www.worldometers.info/img/flags/is-flag.gif",
  "https://www.worldometers.info/img/flags/it-flag.gif",
  "https://www.worldometers.info/img/flags/jm-flag.gif",
  "https://www.worldometers.info/img/flags/ja-flag.gif",
  "https://www.worldometers.info/img/flags/jo-flag.gif",
  "https://www.worldometers.info/img/flags/kz-flag.gif",
  "https://www.worldometers.info/img/flags/ke-flag.gif",
  "https://www.worldometers.info/img/flags/kr-flag.gif",
  "https://www.worldometers.info/img/flags/ku-flag.gif",
  "https://www.worldometers.info/img/flags/kg-flag.gif",
  "https://www.worldometers.info/img/flags/la-flag.gif",
  "https://www.worldometers.info/img/flags/lg-flag.gif",
  "https://www.worldometers.info/img/flags/le-flag.gif",
  "https://www.worldometers.info/img/flags/lt-flag.gif",
  "https://www.worldometers.info/img/flags/li-flag.gif",
  "https://www.worldometers.info/img/flags/ly-flag.gif",
  "https://www.worldometers.info/img/flags/ls-flag.gif",
  "https://www.worldometers.info/img/flags/lh-flag.gif",
  "https://www.worldometers.info/img/flags/lu-flag.gif",
  "https://www.worldometers.info/img/flags/ma-flag.gif",
  "https://www.worldometers.info/img/flags/mi-flag.gif",
  "https://www.worldometers.info/img/flags/my-flag.gif",
  "https://www.worldometers.info/img/flags/mv-flag.gif",
  "https://www.worldometers.info/img/flags/ml-flag.gif",
  "https://www.worldometers.info/img/flags/mt-flag.gif",
  "https://www.worldometers.info/img/flags/rm-flag.gif",
  "https://www.worldometers.info/img/flags/mr-flag.gif",
  "https://www.worldometers.info/img/flags/mp-flag.gif",
  "https://www.worldometers.info/img/flags/mx-flag.gif",
  "https://www.worldometers.info/img/flags/fm-flag.gif",
  "https://www.worldometers.info/img/flags/md-flag.gif",
  "https://www.worldometers.info/img/flags/mn-flag.gif",
  "https://www.worldometers.info/img/flags/mg-flag.gif",
  "https://www.worldometers.info/img/flags/mj-flag.gif",
  "https://www.worldometers.info/img/flags/mo-flag.gif",
  "https://www.worldometers.info/img/flags/mz-flag.gif",
  "https://www.worldometers.info/img/flags/bm-flag.gif",
  "https://www.worldometers.info/img/flags/wa-flag.gif",
  "https://www.worldometers.info/img/flags/nr-flag.gif",
  "https://www.worldometers.info/img/flags/np-flag.gif",
  "https://www.worldometers.info/img/flags/nl-flag.gif",
  "https://www.worldometers.info/img/flags/nz-flag.gif",
  "https://www.worldometers.info/img/flags/nu-flag.gif",
  "https://www.worldometers.info/img/flags/ng-flag.gif",
  "https://www.worldometers.info/img/flags/ni-flag.gif",
  "https://www.worldometers.info/img/flags/mk-flag.gif",
  "https://www.worldometers.info/img/flags/no-flag.gif",
  "https://www.worldometers.info/img/flags/mu-flag.gif",
  "https://www.worldometers.info/img/flags/pk-flag.gif",
  "https://www.worldometers.info/img/flags/ps-flag.gif",
  "https://www.worldometers.info/img/flags/pm-flag.gif",
  "https://www.worldometers.info/img/flags/pp-flag.gif",
  "https://www.worldometers.info/img/flags/pa-flag.gif",
  "https://www.worldometers.info/img/flags/pe-flag.gif",
  "https://www.worldometers.info/img/flags/rp-flag.gif",
  "https://www.worldometers.info/img/flags/pl-flag.gif",
  "https://www.worldometers.info/img/flags/po-flag.gif",
  "https://www.worldometers.info/img/flags/qa-flag.gif",
  "https://www.worldometers.info/img/flags/ro-flag.gif",
  "https://www.worldometers.info/img/flags/rs-flag.gif",
  "https://www.worldometers.info/img/flags/rw-flag.gif",
  "https://www.worldometers.info/img/flags/sc-flag.gif",
  "https://www.worldometers.info/img/flags/st-flag.gif",
  "https://www.worldometers.info/img/flags/ws-flag.gif",
  "https://www.worldometers.info/img/flags/sm-flag.gif",
  "https://www.worldometers.info/img/flags/tp-flag.gif",
  "https://www.worldometers.info/img/flags/sa-flag.gif",
  "https://www.worldometers.info/img/flags/sg-flag.gif",
  "https://www.worldometers.info/img/flags/ri-flag.gif",
  "https://www.worldometers.info/img/flags/se-flag.gif",
  "https://www.worldometers.info/img/flags/sl-flag.gif",
  "https://www.worldometers.info/img/flags/sn-flag.gif",
  "https://www.worldometers.info/img/flags/lo-flag.gif",
  "https://www.worldometers.info/img/flags/si-flag.gif",
  "https://www.worldometers.info/img/flags/bp-flag.gif",
  "https://www.worldometers.info/img/flags/so-flag.gif",
  "https://www.worldometers.info/img/flags/sf-flag.gif",
  "https://www.worldometers.info/img/flags/ks-flag.gif",
  "https://www.worldometers.info/img/flags/od-flag.gif",
  "https://www.worldometers.info/img/flags/sp-flag.gif",
  "https://www.worldometers.info/img/flags/ce-flag.gif",
  "https://www.worldometers.info/img/flags/vc-flag.gif",
  "https://www.worldometers.info/img/flags/palestine-flag.gif",
  "https://www.worldometers.info/img/flags/su-flag.gif",
  "https://www.worldometers.info/img/flags/ns-flag.gif",
  "https://www.worldometers.info/img/flags/sw-flag.gif",
  "https://www.worldometers.info/img/flags/sz-flag.gif",
  "https://www.worldometers.info/img/flags/sy-flag.gif",
  "https://www.worldometers.info/img/flags/ti-flag.gif",
  "https://www.worldometers.info/img/flags/tz-flag.gif",
  "https://www.worldometers.info/img/flags/th-flag.gif",
  "https://www.worldometers.info/img/flags/tt-flag.gif",
  "https://www.worldometers.info/img/flags/to-flag.gif",
  "https://www.worldometers.info/img/flags/tn-flag.gif",
  "https://www.worldometers.info/img/flags/td-flag.gif",
  "https://www.worldometers.info/img/flags/ts-flag.gif",
  "https://www.worldometers.info/img/flags/tu-flag.gif",
  "https://www.worldometers.info/img/flags/tx-flag.gif",
  "https://www.worldometers.info/img/flags/tv-flag.gif",
  "https://www.worldometers.info/img/flags/ae-flag.gif",
  "https://www.worldometers.info/img/flags/uk-flag.gif",
  "https://www.worldometers.info/img/flags/us-flag.gif",
  "https://www.worldometers.info/img/flags/ug-flag.gif",
  "https://www.worldometers.info/img/flags/up-flag.gif",
  "https://www.worldometers.info/img/flags/uy-flag.gif",
  "https://www.worldometers.info/img/flags/uz-flag.gif",
  "https://www.worldometers.info/img/flags/nh-flag.gif",
  "https://www.worldometers.info/img/flags/ve-flag.gif",
  "https://www.worldometers.info/img/flags/vm-flag.gif",
  "https://www.worldometers.info/img/flags/ym-flag.gif",
  "https://www.worldometers.info/img/flags/za-flag.gif",
  "https://www.worldometers.info/img/flags/zi-flag.gif",
  ]
  
  Country_Names = [
  "Afganistan",
  "Arnavutluk",
  "Cezayir",
  "Andora",
  "Angola",
  "Antigua ve Barbuda",
  "Arjantin",
  "Ermenistan",
  "Avustralya",
  "Avusturya",
  "Azerbaycan",
  "Bahamalar",
  "Bahreyn",
  "Bangladeş",
  "Barbados",
  "Belarus",
  "Belçika",
  "Belize",
  "Benin",
  "Butan",
  "Bolivya",
  "Bosna Hersek",
  "Bostvana",
  "Brezilya",
  "Brunei",
  "Bulgaristan",
  "Burkina Faso",
  "Burundi",
  "Fildişi Sahilleri",
  "Cabo Verde",
  "Kamboçya",
  "Kamerun",
  "Kanada",
  "Orta Afrika Cumhuriyeti",
  "Çad",
  "Şili",
  "Çin",
  "Kolombiya",
  "Komorlar",
  "Kongo",
  "Kostarika",
  "Hırvatistan",
  "Küba",
  "Kıbrıs",
  "Çekya",
  "Danimarka",
  "Cibuti",
  "Dominika",
  "Dominik Cumhuriyeti",
  "Kuzey Kore",
  "Demokratik Kongo Cumhuriyeti",
  "Ekvator",
  "Mısır",
  "El Salvador",
  "Ekvator Ginesi",
  "Eritre",
  "Estonya",
  "Esvatini",
  "Etiyopya",
  "Fiji",
  "Finlandiya",
  "Fransa",
  "Gabon",
  "Gambiya",
  "Gürcistan",
  "Almanya",
  "Gana",
  "Yunanistan",
  "Grenada",
  "Guetamala",
  "Gine",
  "Gine-Bissau",
  "Guyana",
  "Haiti",
  "Vatikan",
  "Honduras",
  "Macarsitan",
  "İzlanda",
  "Hindistan",
  "Endonezya",
  "İran",
  "Irak",
  "İrlanda",
  "İsrail",
  "İtalya",
  "Jamaika",
  "Japonya",
  "Ürdün",
  "Kazakistan",
  "Kenya",
  "Kiribati",
  "Küveyt",
  "Kırgızistan",
  "Laos",
  "Letonya",
  "Lübnan",
  "Lesoto",
  "Liberya",
  "Libya",
  "Lihtenştayn",
  "Litvanya",
  "Lüksemburg",
  "Madagaskar",
  "Malawi",
  "Malezya",
  "Maldivler",
  "Mali",
  "Malta",
  "Marşal Adaları",
  "Moritanya",
  "Mauritius",
  "Meksika",
  "Mikronezya",
  "Moldova",
  "Monako",
  "Moğolistan",
  "Karadağ",
  "Fas",
  "Mozambik",
  "Myanmar",
  "Namibya",
  "Nauru",
  "Nepal",
  "Hollanda",
  "Yeni Zelanda",
  "Nikaragua",
  "Nijer",
  "Nijerya",
  "Kuzey Makedonya",
  "Norveç",
  "Umman",
  "Pakistan",
  "Palau",
  "Panama",
  "Papua Yeni Gine",
  "Paraguay",
  "Peru",
  "Filipinler",
  "Polonya",
  "Portekiz",
  "Katar",
  "Romanya",
  "Rusya",
  "Ruanda",
  "Saint Kitts ve Nevis",
  "Saint Lucia",
  "Samoa",
  "San Marino",
  "Sao Tome ve Principe",
  "Suudi Arabistan",
  "Senegal",
  "Sırbistan",
  "Seyşeller",
  "Sierra Leone",
  "Singapur",
  "Slovakya",
  "Slovenya",
  "Solomon Adaları",
  "Somali",
  "Güney Afrika",
  "Güney Korea",
  "Güney Sudan",
  "İspanya",
  "Sri Lanka",
  "Saint Vincent Grenadinler",
  "Filistin Devleti",
  "Sudan",
  "Surinam",
  "İsveç",
  "İsviçre",
  "Suriye",
  "Tacikistan",
  "Tanzanya",
  "Tayland",
  "Doğu Timor",
  "Togo",
  "Tonga",
  "Trinidad and Tobago",
  "Tunus",
  "Türkiye",
  "Türkmenistan",
  "Tuvalu",
  "Birleşik Arap Emirlikleri",
  "İngiltere",
  "Amerika Birleşik Devletleri",
  "Uganda",
  "Ukrayna",
  "Uruguay",
  "Özbekistan",
  "Vanuatu",
  "Venezuela",
  "Vietnam",
  "Yemen",
  "Zambiya",
  "Zimbabve",
  ]
  index = random.randint(0,191)
  result = [gif_list[index],Country_Names[index]]
  
  return result