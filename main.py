import random as r
import time as t
import os

pk_list = ["Venusaur", "Charizard", "Blastoise", "Pikachu", "Arcanine", "Machamp", 
           "Gengar", "Rhydon", "Gyarados", "Lapras", "Dragonite", "Mewtwo"]
pk_healthstat = [364, 360, 362, 274, 384, 384, 324, 414, 394, 464, 386, 416]
pk_attackstat = [289, 293, 291, 229, 350, 394, 251, 394, 383, 295, 403, 350]
pk_defencestat = [291, 280, 328, 174, 284, 284, 240, 372, 282, 284, 317, 306]
pk_move1list = ["Razor Leaf", "Flamethrower", "Hydro Pump", "Thunderbolt", "Flare Blitz", "Dynamic Punch", 
                "Dark Pulse", "Giga Impact", "Hurricane", "Ice Beam", "Dragon Rush", "Psystrike"]
pk_move2list = ["Take Down", "Air Slash", "Bite", "Slam", "Rock Slide", "Strength", 
                "Shadow Ball", "Earthquake", "Hyrdro Pump", "Hyrdro Pump", "Hurricane", "Psychic"]
pk_movedamagelist =   [55, 90, 90, 75, 110, 60, 90, 80, 120, 75, 100, 80, 80, 80, 150, 100, 110, 110, 90, 110, 100, 110, 100, 90]
in_items = ["pokeball", "potion", "revive"]

current_option = 0
sub_menu = "Null"
sub_sub_menu = 0

selectedpk = 0
pl_InMenu = True
pl_InBattle = False

pl_HasSelectedPokemon = True

in_pokeball = 3
in_potion = 3
in_revive = 2

en_pk1_health = 0
en_pk2_health = 0
en_pk3_health = 0

en_pk1_maxhealth = 1
en_pk2_maxhealth = 1
en_pk3_maxhealth = 1

en_pk1_ID = 0
en_pk2_ID = 0
en_pk3_ID = 0

pl_CurrentPokemon = 1
en_CurrentPokemon = 1

pk1_health = 0
pk2_health = 0
pk3_health = 0

pk1_maxhealth = 416
pk2_maxhealth = 324
pk3_maxhealth = 360

pk1_ID = 11
pk2_ID = 6
pk3_ID = 1

Pokemon1 = "Mewtwo"
Pokemon2 = "Gengar"
Pokemon3 = "Charizard"

EN_PK1 = ""
EN_PK2 = ""
EN_PK3 = ""

def start_attack(AttackNo, EorP):
    
    global en_pk1_health, en_pk2_health, en_pk3_health, pk1_health, pk2_health, pk3_health, current_option, sub_menu, sub_sub_menu, selectedpk, pl_InMenu, pl_InBattle
    
    if EorP == "P":
        movelist = globals()["pk_move" + str(AttackNo) + "list"]
        move = (movelist[globals()["pk" + str(pl_CurrentPokemon) + "_ID"]])
        if AttackNo == 1:
            power = pk_movedamagelist[globals()["pk" + str(pl_CurrentPokemon) + "_ID"] * 2]
        elif AttackNo == 2:
            power = pk_movedamagelist[globals()["pk" + str(pl_CurrentPokemon) + "_ID"] * 2 + 1]
        at = pk_attackstat[globals()["pk" + str(pl_CurrentPokemon) + "_ID"]]
        df = pk_defencestat[globals()["en_pk" + str(en_CurrentPokemon) + "_ID"]]
        
        pk_DamageDealt = round((((2*100/5+2)*power*(at/df))/50+2) * (r.randint(85, 100)/100))
        print((str(globals()["Pokemon" + str(pl_CurrentPokemon)])) + " used " + str(move) + "!")
        print("It dealt " + str(pk_DamageDealt) + " Damage!")
        
        en_tempPK = globals()["en_pk" + str(en_CurrentPokemon) + "_health"]
        en_tempPK = en_tempPK - pk_DamageDealt
        
        if en_tempPK <= 0:
            print("Enemy's " + str(globals()["EN_PK" + str(en_CurrentPokemon)]) + "has fainted!")
            globals()["en_pk" + str(en_CurrentPokemon) + "_health"] = en_tempPK
            en_newPK()

        globals()["en_pk" + str(en_CurrentPokemon) + "_health"] = en_tempPK
        start_attack(0, "E")
    elif EorP == "E":
        AttackNo = r.randint(1, 2)
        if AttackNo == 1:
            power = pk_movedamagelist[globals()["en_pk" + str(en_CurrentPokemon) + "_ID"] * 2]
        elif AttackNo == 2:
            power = pk_movedamagelist[globals()["en_pk" + str(en_CurrentPokemon) + "_ID"] * 2 + 1]
        movelist = globals()["pk_move" + str(AttackNo) + "list"]
        move = (movelist[globals()["en_pk" + str(en_CurrentPokemon) + "_ID"]])
        at = pk_attackstat[globals()["en_pk" + str(en_CurrentPokemon) + "_ID"]]
        df = pk_defencestat[globals()["pk" + str(pl_CurrentPokemon) + "_ID"]]
        pk_EnemyDamage = round((((2*100/5+2)*power*(at/df))/50+2) * (r.randint(85, 100)/100))
        
        print("Enemy's " + globals()["EN_PK" + str(en_CurrentPokemon)] + " used " + (move) + "!")
        print("It dealt " + str(pk_EnemyDamage) + " damage!")
        
        globals()["pk" + str(pl_CurrentPokemon) + "_health"] = globals()["pk" + str(pl_CurrentPokemon) + "_health"] - pk_EnemyDamage
        
        if globals()["pk" + str(pl_CurrentPokemon) + "_health"] <= 0:
            print("Your Pokemon " + str(globals()["Pokemon" + str(pl_CurrentPokemon)]) + " has fainted!")
            if pk1_health <= 0 and pk2_health <= 0 and pk3_health <= 0:
                print("You have been deafeated and have lost the Pokemon Battle.")
                pl_InMenu = True
                pl_InBattle = False
                current_option = 0
            else:
                selectedpk = 0
                while not selectedpk == -1:
                    pl_input = "Null"
                    while not pl_input in [1, 2, 3]:
                      pl_input = (input("Please select a Pokemon to Switch to:\n1 = " + str(Pokemon1) + "\n2 = " + str(Pokemon2) + "\n3 = " + str(Pokemon3)))
                      try:
                        pl_input = int(pl_input)
                      except ValueError:
                        os.system('cls||clear')
                        print("That Option is Invalid.")
                    selectedpk = pl_input
                    os.system('cls||clear')
                    SwitchPokemon(selectedpk, "E")

        t.sleep(1)
        os.system('cls||clear')
        current_option = 0
        sub_menu = "Null"
        sub_sub_menu = 0
        
def en_newPK():
    
    global en_CurrentPokemon, pl_InBattle, pl_InMenu, current_option
    
    if en_pk1_health <= 0 and en_pk2_health <= 0 and en_pk3_health <= 0:
        print("You have won the Pokemon Battle!")
        pl_InMenu = True
        pl_InBattle = False
        current_option = 0
    else:
        decisionmade = (r.choice([1, 2, 3]))
        while globals()["en_pk" + str(decisionmade) + "_health"] <= 0 or decisionmade == en_CurrentPokemon:
            decisionmade = (r.choice([1, 2, 3]))
            
        en_CurrentPokemon = decisionmade
        print("Enemy sent out " + str(globals()["EN_PK" + str(en_CurrentPokemon)]) + "!")

def use_item(item):
    global in_pokeball, in_potion, in_revive, pk1_health, pk2_health, pk3_health

    pl_input = "Null"
    in_selectedPK = 0
    
    if item == "Pokeball":
        print("You can't catch another trainer's Pokemon!")
            
    elif item == "Potion" or item == "Revive":
        pl_HasItem = False
        if item == "Potion":
            if in_potion > 0:
                pl_HasItem = True
    
        elif item == "Revive":
            if in_revive > 0:
                pl_HasItem = True
            
        if pl_HasItem == True:
            if item == "Potion":
                print("Please select a Pokemon to heal!")
            elif item == "Revive":
                print("Please select a Pokemon to revive!")

            pl_input = "Null"
            while not pl_input in [1, 2, 3]:
              pl_input = (input("1 = " + str(Pokemon1) + "\n2 = " + str(Pokemon2) + "\n3 = " + str(Pokemon3) + "\n--> "))
              try:
                pl_input = int(pl_input)
              except ValueError:
                os.system('cls||clear')
                print("That Option is Invalid.")
                if item == "Potion":
                  print("Please select a Pokemon to heal!")
                elif item == "Revive":
                  print("Please select a Pokemon to revive!")
            os.system('cls||clear')
            in_selectedPK = pl_input
                        
            pl_tempHealth = globals()["pk" + str(in_selectedPK) + "_health"]
            pl_tempMaxHealth = globals()["pk" + str(in_selectedPK) + "_maxhealth"]
            startattack = False
                
            if item == "Potion":
                if pl_tempHealth + 35 >= pl_tempMaxHealth:
                    pl_tempHealth = pl_tempMaxHealth
                else:
                    pl_tempHealth = pl_tempHealth + 35
                in_potion = in_potion - 1
                startattack = True
                in_strPK = in_selectedPK
                in_selectedPK = "Null"
                            

            elif item == "Revive":
                if pl_tempHealth > 0:
                    print("This Pokemon has not fainted!")
                else:
                    pl_tempHealth = round(pl_tempMaxHealth / 2)
                    in_revive = in_revive - 1
                    startattack = True
                    in_strPK = in_selectedPK
                    in_selectedPK = "Null"
                                    
                            
                    globals()["pk" + str(in_selectedPK) + "_health"] = pl_tempHealth
            if startattack == True:
                print("Used " + str(item) + " on " + str(globals()["Pokemon" + str(in_strPK)]) + "!")
                start_attack(0, "E")
        else:
            print("You don't have any " + str(item) + "s left!")
        
def SwitchPokemon(PKno, EorP):
    
    global pl_CurrentPokemon, selectedpk
    
    if pl_CurrentPokemon == PKno:
        print("Please Select a Different Pokemon!")
    else:
        pl_CanSendPK = False
        temp_pkhealth = globals()["pk" + str(PKno) + "_health"]
            
        if temp_pkhealth > 0:
            pl_CanSendPK = True
        else:
            print("That Pokemon has fainted!")
            
        if pl_CanSendPK == True:
            print(str(globals()["Pokemon" + str(pl_CurrentPokemon)]) + " come back!")
            
            pl_CurrentPokemon = PKno
            
            print("Go " + str(globals()["Pokemon" + str(PKno)]) + "!")
            
            if EorP == "P":
                start_attack(0, "E")
            elif EorP == "E":
                selectedpk = -1
            
while True:
    while pl_InMenu == True:
      
      pl_input = "Null"
      while not pl_input in [1, 2, 3]:
        pl_input = (input("Please select an Option:\n1 = Start Battle\n2 = Select Pokemon\n3 = Select Items\n--> "))
        try:
          pl_input = int(pl_input)
        except ValueError:
          os.system('cls||clear')
          print("That Option is Invalid.")

      os.system('cls||clear')
      current_option = pl_input
      if current_option == 1:
          if pl_HasSelectedPokemon == True:
              pl_InBattle = True
              pl_InMenu = False
              CurrentENPK = 1
              current_option = 0
              while not CurrentENPK == 0:
                  CurrentSelectedENPK = r.randint(0, 11)
                  globals()["en_pk" + str(CurrentENPK) + "_ID"] = CurrentSelectedENPK
                  globals()["en_pk" + str(CurrentENPK) + "_maxhealth"] = (pk_healthstat[CurrentSelectedENPK])
                  globals()["EN_PK" + str(CurrentENPK)] = (pk_list[CurrentSelectedENPK])
                  if CurrentENPK == 3:
                      CurrentENPK = 0
                  else:
                      CurrentENPK = CurrentENPK + 1
              pk1_health = pk1_maxhealth
              pk2_health = pk2_maxhealth
              pk3_health = pk3_maxhealth
              en_pk1_health = en_pk1_maxhealth
              en_pk2_health = en_pk2_maxhealth
              en_pk3_health = en_pk3_maxhealth
              pl_CurrentPokemon = 1
              en_CurrentPokemon = 1
              print("Enemy trainer challenged you to a Pokemon Battle")
              print("Enemy sent out " + str(EN_PK1) + "!")
              t.sleep(0.2)
              print("Go " + str(Pokemon1) + "!")
          else:
              print("Please Select Your Pokemon first!")
      elif current_option == 2:
          SelectingPokemon = True
          CurrentPK = 1
          CurrentSelectedPK = 0
          print("Please select your first Pokemon")
          while SelectingPokemon == True:
              pl_input = "Null"
              while not pl_input in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                pl_input = (input("Please select an Option:\n1 = Venusaur\n2 = Charizard\n3 = Blastoise\n4 = Pikachu\n5 = Arcanine\n6 = Machamp\n7 = Gengar\n8 = Rhydon\n9 = Gyarados\n10 = Lapras\n11 = Dragonite\n12 = Mewtwo\n--> "))
                try:
                  pl_input = int(pl_input)
                except ValueError:
                  print("That Option is Invalid.")
                  os.system('cls||clear')
              CurrentSelectedPK = pl_input - 1
              os.system('cls||clear')
              print("Selected " + str(pk_list[CurrentSelectedPK]))
              t.sleep(0.5)
              os.system('cls||clear')
                
              globals()["pk" + str(CurrentPK) + "_ID"] = CurrentSelectedPK
              globals()["pk" + str(CurrentPK) + "_maxhealth"] = (pk_healthstat[CurrentSelectedPK])
              globals()["Pokemon" + str(CurrentPK)] = (pk_list[CurrentSelectedPK])
              CurrentSelectedPK = 0
              if CurrentPK == 3:
                  SelectingPokemon = False
                  pl_HasSelectedPokemon = True
                  print("Pokemon selection complete")
              else:
                  CurrentPK = CurrentPK + 1
                  print("Please select Pokemon Number " + str(CurrentPK) + ".")
              
      elif current_option == 3:
          SelectingItems = True
          CurrentItem = 0
          print("Please select the amount of pokeballs you want.")
          itemcount = 0
          while SelectingItems == True:
              pl_input = "Null"
              while not isinstance(pl_input, int) == True:
                pl_input = (input("--> "))
                try:
                  pl_input = int(pl_input)
                except ValueError:
                  os.system('cls||clear')
                  print("That Option is Invalid.\nPlease select the amount of " + str(in_items[CurrentItem]) + "s you want")
                
              itemcount = pl_input
              globals()["in_" + str(in_items[CurrentItem])] = itemcount
              if CurrentItem == 2:
                  SelectingItems = False
                  os.system('cls||clear')
                  print("Item selection complete")
                  t.sleep(1)
                  os.system('cls||clear')
              else:
                  CurrentItem = CurrentItem + 1
                  os.system('cls||clear')
                  print("Please select the amount of " + str(in_items[CurrentItem]) + "s you want")
                  pl_input = "Null"
              itemcount = 0
                            
    while pl_InBattle == True:
        
      pl_input = "Null"
      while not pl_input in [1, 2, 3, 4]:
        pl_input = (input("Please select an Option:\n1 = Fight\n2 = Pokemon\n3 = Item\n4 = Run\n--> "))
        try:
          pl_input = int(pl_input)
        except ValueError:
          os.system('cls||clear')
          print("That Option is Invalid.")
      current_option = pl_input
      
      if current_option == 1:
          os.system('cls||clear')
          sub_menu = "Fight"
          sub_sub_menu = 0
          while sub_menu == "Fight":
              pl_input = "Null"
              while not pl_input in [1, 2, 3]:
                pl_input = (input("Please select an Move to Use:\n1 = " + str(pk_move1list[globals()["pk" + str(pl_CurrentPokemon) + "_ID"]]) + "\n2 = " + str(pk_move2list[globals()["pk" + str(pl_CurrentPokemon) + "_ID"]]) + "\n3 = Back To Menu\n--> "))
                try:
                  pl_input = int(pl_input)
                except ValueError:
                  os.system('cls||clear')
                  print("That Option is Invalid.")
              sub_sub_menu = pl_input
                      
              if not sub_sub_menu == 3:
                  os.system('cls||clear')
                  start_attack(sub_sub_menu, "P")
              else:
                  os.system('cls||clear')
                  sub_menu = "Null"
                  sub_sub_menu = 0
                
      elif current_option == 2:
          os.system('cls||clear')
          sub_menu = "Pokemon"
          sub_sub_menu = 0
          while sub_menu == "Pokemon":
              pl_input = "Null"
              while not pl_input in [1, 2, 3, 4]:
                pl_input = (input("Please select a Pokemon to Switch to:\n1 = " + str(Pokemon1) + "\n2 = " + str(Pokemon2) + "\n3 = " + str(Pokemon3) + "\n4 = Back to Menu\n--> "))
                try:
                  pl_input = int(pl_input)
                except ValueError:
                  os.system('cls||clear')
                  print("That Option is Invalid.")
              sub_sub_menu = pl_input
              
              if not sub_sub_menu == 4:
                  os.system('cls||clear')
                  SwitchPokemon(sub_sub_menu, "P")
              else:
                os.system('cls||clear')
                sub_menu = "Null"
                sub_sub_menu = 0
                
      elif current_option == 3:
          os.system('cls||clear')
          sub_menu = "Item"
          sub_sub_menu = 0
          while sub_menu == "Item":
              pl_input = "Null"
              while not pl_input in [1, 2, 3, 4]:
                pl_input = (input("Please select an Item to Use:\n1 = Pokeball\n2 = Potion\n3 = Revive\n4 = Back to Menu\n--> "))
                try:
                  pl_input = int(pl_input)
                except ValueError:
                  os.system('cls||clear')
                  print("That Option is Invalid.")
              sub_sub_menu = pl_input                 
              if not sub_sub_menu == 4:
                os.system('cls||clear')
                if sub_sub_menu == 1:
                  use_item("Pokeball")
                elif sub_sub_menu == 2:
                  use_item("Potion")
                elif sub_sub_menu == 3:
                  use_item("Revive")
                
              else:
                os.system('cls||clear')
                sub_menu = "Null"
                sub_sub_menu = 0            
                
      elif current_option == 4:
          os.system('cls||clear')
          print("You cannot run from this battle!")
