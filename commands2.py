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
  else:
    Sonuc = Sonuc[1]
    gif = gif[1]
    user1_health = 0
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
  
  
  