import math
import time as sleep
import calc_script_1_stat as calcStat
import calc_script_2_ev as calcEv


attnat = 1
defnat = 1
speatnat = 1
spdefnat = 1
spenat = 1 

test = int(input("Enter 1 for EV 2 for STAT: "))
if test == 1:
    stat = ["ss", "Hp", "Attack", "Defense", "Special Attack", "Special Defense" , "Speed"]
    base = [6]
    ivv = [6]
    evv = [0,0,0,0,0,0,0]
    evs = 0
    lvl = int(input("Input the level of your pokemon: "))
    if(lvl<0 or lvl>100):
        print("Level Can only reach max 100!")
        sleep(1)
        exit()

    print("Input Base Stats")
    for x in range(1, 7):
        base.append(int(input("Input "+stat[x]+": ")))

    print("Input Iv's on each Stats")
    for y in range(1, 7):
        ivv.append(int(input("Input "+stat[y]+" Iv: ")))
        if (ivv[y] < 0 or ivv[y] > 31):
                print("You can only set Ivs from 0 to 31!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()

    k = int(input("Input for [1]Single Ev Stat or [2]All the stats?\n"))
    if(k == 1):
        s = int(input("Which Stat would you like to input?\n[1]HP [2]Att [3]Def [4]SpeA [5]Spdef [6]Spe\n"))
        tray = int(input("Input how much Ev: "))
        if (s < 0 or s > 255):
            print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
            sleep(3)
            print("System is closing!")
            sleep(3)                
            exit()
        for p in range(1,7):
            if (p==s):
                evv.insert(p, tray)
    elif(k == 2):        
        print("Input Ev's on each Stats")
        for z in range(1, 7):
            evv.append(int(input("Input "+stat[z]+" Ev: ")))
            if (evv[z] < 0 or evv[z] > 255):
                print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()
        evs = evs + evv[z]
        if (evs > 510):
                print("You can only set Evs to a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()    
    else:
        print("Wrong Input!")
    print("\n[1]hardy [2]lonely [3]brave [4]adamant [5]naughty\n"
          "[6]bold [7]docile [8]relaxed [9]impish [10]lax\n "
          "[11]timid [12]hasty [13]serious [14]jolly [15]naive\n "
          "[16]modest [17]mild [18]quiet [19]bashful [20]rash\n "
          "[21]calm [22]gentle [23]sassy [24]careful [25]quirky")

    natpick = int(input("Pick Pokemon's Nature: "))
    if(natpick == 1 or natpick == 7 or natpick == 13 or natpick == 19 or natpick == 25):
        attnat = 1
        defnat = 1
        speatnat = 1
        spdefnat = 1
        spenat = 1
    if(natpick == 2 or natpick == 3 or natpick == 4 or natpick == 5): 
        attnat = 1.1
        if(natpick == 2):
            defnat = 0.9
        elif(natpick == 3):
            spenat = 0.9
        elif(natpick == 4):
            speatnat = 0.9
        else:
            spdefnat = 0.9
    if(natpick == 6 or natpick == 8 or natpick == 9 or natpick == 10):
        defnat = 1.1
        if(natpick == 6):
            attnat = 0.9
        elif(natpick == 8):
            spenat = 0.9
        elif(natpick == 9):
            speatnat = 0.9
        else:
            spdefnat = 0.9
    if(natpick == 11 or natpick == 12 or natpick == 14 or natpick == 15):
        spenat = 1.1
        if(natpick == 11):
            attnat = 0.9
        elif(natpick == 12):
            defnat = 0.9
        elif(natpick == 14):
            spenat = 0.9
        else:
            spdefnat = 0.9    
    if(natpick == 16 or natpick == 17 or natpick == 18 or natpick == 20):
        speatnat = 1.1
        if(natpick == 16):
            attnat = 0.9
        elif(natpick == 17):
            defnat = 0.9
        elif(natpick == 18):
            spenat = 0.9
        else:
            spdefnat = 0.9      
    if(natpick == 21 or natpick == 22 or natpick == 23 or natpick == 24):
        spdefnat = 1.1
        if(natpick == 16):
            attnat = 0.9
        elif(natpick == 17):
            defnat = 0.9
        elif(natpick == 18):
            spenat = 0.9
        else:
            speatnat = 0.9
   
    opt = int(input("Which stat do you want to check?\n[1] Attack [2] Defense [3] Special Attack \n [4] Special Defense [5] Speed \n"))
    mod = 0
    if opt == 1:
            mod = attnat
    elif opt == 2:
            mod = defnat
    elif opt == 3:
            mod = speatnat
    elif opt == 4:
            mod = spdefnat
    elif opt == 5:
            mod = spenat

    des = int(input("Enter desired increase: "))

    print("This is the amount of needed Ev for your pokemon: ", calcEv.ClassEv.desired(base,evv,ivv,opt,lvl,des,mod)) 
    exit()
elif test == 2:
    stat = ["ss", "Hp", "Attack", "Defense", "Special Attack", "Special Defense" , "Speed"]
    base = [6]
    ivv = [6]
    evv = [0,0,0,0,0,0,0]
    evs = 0
    pokemon = str(input("Enter Pokemon: "))
    lvl = int(input("Enter level: "))
    if(lvl<0 or lvl>100):
        print("Level Can only reach max 100!")
        sleep(1)
        exit()    
    print("[1]hardy [2]lonely [3]brave [4]adamant [5]naughty\n"
          "[6]bold [7]docile [8]relaxed [9]impish [10]lax\n "
          "[11]timid [12]hasty [13]serious [14]jolly [15]naive\n "
          "[16]modest [17]mild [18]quiet [19]bashful [20]rash\n "
          "[21]calm [22]gentle [23]sassy [24]careful [25]quirky")

    natpick = int(input("Pick Pokemon's Nature: "))
    if(natpick == 1 or natpick == 7 or natpick == 13 or natpick == 19 or natpick == 25):
        attnat = 1
        defnat = 1
        speatnat = 1
        spdefnat = 1
        spenat = 1
    if(natpick == 2 or natpick == 3 or natpick == 4 or natpick == 5): 
        attnat = 1.1
    if(natpick == 2):
        defnat = 0.9
    elif(natpick == 3):
        spenat = 0.9
    elif(natpick == 4):
        speatnat = 0.9
    else:
        spdefnat = 0.9
    if(natpick == 6 or natpick == 8 or natpick == 9 or natpick == 10):
        defnat = 1.1
    if(natpick == 6):
        attnat = 0.9
    elif(natpick == 8):
        spenat = 0.9
    elif(natpick == 9):
        speatnat = 0.9
    else:
        spdefnat = 0.9
    if(natpick == 11 or natpick == 12 or natpick == 14 or natpick == 15):
        spenat = 1.1
    if(natpick == 11):
        attnat = 0.9
    elif(natpick == 12):
        defnat = 0.9
    elif(natpick == 14):
        spenat = 0.9
    else:
        spdefnat = 0.9    
    if(natpick == 16 or natpick == 17 or natpick == 18 or natpick == 20):
        speatnat = 1.1
    if(natpick == 16):
        attnat = 0.9
    elif(natpick == 17):
        defnat = 0.9
    elif(natpick == 18):
        spenat = 0.9
    else:
        spdefnat = 0.9      
    if(natpick == 21 or natpick == 22 or natpick == 23 or natpick == 24):
        spdefnat = 1.1
    if(natpick == 16):
        attnat = 0.9
    elif(natpick == 17):
        defnat = 0.9
    elif(natpick == 18):
        spenat = 0.9
    else:
        speatnat = 0.9

print("Input Base Stats")
for x in range(1, 7):
        base.append(int(input("Input "+stat[x]+": ")))

print("Input Iv's on each Stats")
for y in range(1, 7):
        ivv.append(int(input("Input "+stat[y]+" Iv: ")))
        if (ivv[y] < 0 or ivv[y] > 31):
                print("You can only set Ivs from 0 to 31!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()

k = int(input("Input for [1]Single Ev Stat or [2]All the stats?\n"))
if(k == 1):
        s = int(input("Which Stat would you like to input?\n[1]HP [2]Att [3]Def [4]SpeA [5]Spdef [6]Spe\n"))
        tray = int(input("Input how much Ev: "))
        if (s < 0 or s > 255):
            print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
            sleep(3)
            print("System is closing!")
            sleep(3)                
            exit()
        for p in range(1,7):
            if (p==s):
                evv.insert(p, tray)
elif(k == 2):        
        print("Input Ev's on each Stats")
        for z in range(1, 7):
            evv.append(int(input("Input "+stat[z]+" Ev: ")))
            if (evv[z] < 0 or evv[z] > 255):
                print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()
        evs = evs + evv[z]
        if (evs > 510):
                print("You can only set Evs to a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()  
else:
    print("Invalid Input!")
    exit()
print("Here's the stats of your pokemon: ")
print("HP: ", calcStat.ClassStat.hpReturn(base,ivv,evv,lvl))
print("Attack: ", calcStat.ClassStat.attackReturn(base,ivv,evv,lvl,attnat))
print("Defense: ", calcStat.ClassStat.defenseReturn(base,ivv,evv,lvl,defnat))
print("Speocial Attack: ", calcStat.ClassStat.spattackReturn(base,ivv,evv,lvl,speatnat))
print("Special Defense: ", calcStat.ClassStat.spdefenseReturn(base,ivv,evv,lvl,spdefnat))
print("Speed: ", calcStat.ClassStat.speedReturn(base,ivv,evv,lvl,spenat))