from random import randint

# +------------------------
# | Text for various menus 
# +------------------------
main_text = ["New Game",\
             "Resume Game",\
             "View Leaderboard",\
             "Exit Game"]

town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game","Buy Items","View Inventory"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

world_map = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]


print("Welcome to Ratventure!")
print("----------------------")

# Code your main program here


#function to display the menu (town or open text)
def menu(txt):
    print('=======================')
    num=1
    for i in txt:
        print('{}) {}'.format(num,i))
        num+=1

#function to display player's statistics
def stats(holding):
    print('\n========================\nThe Hero\n')
    print('{:>8}: {}\n{:>8}: {}\n{:>8}: {}'.format('Damage',playerStats['dmg'],'Defence',playerStats['defence'],'HP',playerStats['HP']))
    print('\nYou have {} gold'.format(gold))#bonus feature
    if holding == True:
        print('You are holding the orb of power\n')
    print('========================')

#function to display map
def displayMap(world_map):                    
    first = (('+')+ ('---+'*8))
    for i in world_map:
        print(first)
        for j in i:
            if j == 'O': #make the orb invisible on map
                j = ' '
            elif j == 'H/O':#make the orb invisible on map
                j = 'H'
            print('{}{:^3}'.format(('|'),j), end = '')
        print('|')
    print(first)

#function to find hero   #index from index of list in the nested list, to the hero in the sub-list  eg. 5-3 (row-column)
def findHero(world_map):
    for i in range(len(world_map)):
        for j in range(len(world_map)):
            if world_map[i][j] == 'H':
                heroPos = ('{}-{}'.format(i,j))
                break
            else:
                if world_map[i][j][0] == 'H':
                    heroPos = ('{}-{}'.format(i,j))
                    break
    return(heroPos,world_map)
                    
                      

#function to find the positions of the town
def findTown():
    town = []
    for i in range(len(world_map)):
        for j in range(len(world_map[i])):
            if (world_map[i][j]) == 'T' or  (world_map[i][j])==('H/T'):
                po = ('{}-{}'.format(i,j))
                town.append(po)
    return town#returns the positions of the towns as a list

#function to check if hero is in town
def inTown(world_map):
    town = findTown()#find all the towns as a list
    pos,world_map = findHero(world_map)# find the hero position
    check = False
    for i in town:
        if pos == i: #if any of the town position is the same as hero position, then hero is in town
            check = True
            break
    return check #return true or false
                
            

#function to remove hero from map
def RemoveHero(world_map):
    heroPos,world_map= findHero(world_map)#find the hero first
    inde = heroPos.split('-')
    fst = int(inde[0])
    sec = int(inde[1])#get the rows and column
    p = world_map[fst][sec]
    if len(p)==1:#this means that there is nothing on the position and only the hero
        world_map[fst].pop(sec)
        world_map[fst].insert(sec,' ')
    else:#there are other things on it- 'H/T','H/O' etc
        popped = world_map[fst].pop(sec)
        popped = popped.split('/')
        world_map[fst].insert(sec,popped[1])      
    return world_map

#function to move the hero (actually does the moves)
def move(m,world_map):
    move = False
    heroPos,world_map= findHero(world_map)
    inde = heroPos.split('-')
    fst = int(inde[0])
    sec = int(inde[1])
    if m == 'w': #moves up
        if fst!=0:
            move = True
            RemoveHero(world_map)
            pos = world_map[fst-1][sec]
            if pos == ' ':
                world_map[fst-1].insert(sec,'H')
                world_map[fst-1].pop(sec+1)
            else:
                prev = world_map[fst-1].pop(sec)
                world_map[fst-1].insert(sec,'H/'+prev)

    elif m == 'a': #moves left
        if sec!=0:
            move = True
            RemoveHero(world_map)
            pos = world_map[fst][sec-1]
            if pos == ' ':
                world_map[fst].pop(sec-1)
                world_map[fst].insert((sec-1),'H')
 
            else:
                prev = world_map[fst].pop(sec-1)
                world_map[fst].insert((sec-1),'H/'+prev)

    elif m == 's': #moves down
        if fst!= 7:
            move = True
            RemoveHero(world_map)
            pos = world_map[fst+1][sec]
            if pos == ' ':
                world_map[fst+1].pop(sec) #remove previous item in the position
                world_map[fst+1].insert(sec,'H') #add Hero the the position
                
            else:
                prev = world_map[fst+1].pop(sec) #asign the previous item to a variable and remove it from the previous position
                world_map[fst+1].insert(sec,'H/'+prev) #add the hero and the previous item to the position again
    elif m == 'd': #moves right
        if sec!= 7:
            move = True
            RemoveHero(world_map)
            pos = world_map[fst][sec+1]
            if pos == ' ':
                world_map[fst].pop(sec+1)
                world_map[fst].insert((sec+1),'H')

            else:
                prev = world_map[fst].pop(sec+1)
                world_map[fst].insert((sec+1),'H/'+prev)
    return (move,world_map)       


#function to prompt and also validate the move       
def moveFunction(world_map):
    while True:
        displayMap(world_map)
        print('W = up; A = left; S = down; D = right')
        m = (input('Your move: '))
        m = m.lower()#to allow the function to work regardless of caps or no cap
        moved,world_map = move(m,world_map)
        if moved == True:#the move function returns if player has actually moved
            displayMap(world_map)#if hero has actually moved, display the new map and break
            break
        else:#loop again until users enter a valid option
            print('\nInvalid move!')
    return(world_map)

#function to combat rat minions
def combat(day,holding,gold):
    ratStats = {'Damage':'1-3','Defence':1,'HP':10}
    print('Day {}: You are out in the open'.format(day))
    start_game = True #declare for the game to loop first, which ends later when hero dies
    while True:
        print('\nEncounter! - Rat')
        for i in ratStats:
            print('{} : {}'.format(i,ratStats[i]))
        menu(fight_text) #display to run or attack
        aOrR = input('Enter choice: ') #attack Or Run
        if aOrR == '1':#attack
            ran = False#declare plyaer has not ran
            hdamage = randint(2,4)
            hdefence = 1
            rdamage = randint(1,3)
            rdefence = 1
            if holding == True:
                hdamage +=5
                hdefence +=5
            if ('Sword')in owned:
                hdamage+=3
                if ('Poison')in owned:
                    hdamage+=5
            if ('Armor')in owned:
                hdefence+=3
            takenD = rdamage - hdefence
            dealtD = hdamage - rdefence
            if takenD <0:#taken damage cannot be lower than 0
                takenD = 0
            playerStats['HP']-=takenD
            ratStats['HP']-=dealtD
            print('\nYou deal {} damage to the Rat'.format(dealtD))
            print('Ouch! The Rat hit you for {} damage!'.format(takenD))
            if ratStats['HP'] <=0 and playerStats['HP'] <=0:#tie between the rat minion and the rat king
                print('Both you and the rat minion are dead!')
                print('You have not defeated the rat king')
                print('Game over! You lose')
                start_game = False#declare game over
                break       
            if (ratStats['HP'] > 0) and (playerStats['HP']>0):
                print('You have {} HP left.'.format(playerStats['HP']))
                continue
            elif ratStats['HP'] <= 0:#rat dead
                print('The rat is dead! You are victorious!\n')
                print('You have gained 50 gold!')#additional feature
                gold+=50
                print('You now have {} gold'.format(gold))
                break
            else:
                print('Game over! You lose')
                start_game = False
                break
        elif aOrR == '2':#run
            print('You run and hide\n')
            ran = True#declare player has ran
            break
        else:#programe validation
            print('Invalid option\n')
    return (ran,start_game,gold)
                

        
#function to determine if player is on orb or the direction of orb
def sense():
    #see if player found the orb
    for i in range(len(world_map)):
        for j in range(len(world_map[i])):
            if world_map[i][j] == 'H/O':
                found = True
                direction = 'Found'
            elif world_map[i][j] == 'O':
                found = False
                hPos,w = findHero(world_map)
                hPos = hPos.split('-')
                if int(hPos[0]) == i: #same horizontal line (west or east)
                    if int(hPos[1])>j:
                        direction = 'west'
                    else:
                        direction = 'east'
                elif int(hPos[1]) == j: #same vertical line (north or south)
                    if int(hPos[0])> i:
                        direction = 'north'
                    else:
                        direction = 'south'
                elif int(hPos[0]) > i: #northwest or northeast
                    if int(hPos[1])>j: #northwest
                        direction = 'northwest'
                    else:
                        direction = 'northeast'
                elif int(hPos[0])<i: #southwest or southeast
                    if int(hPos[1])<j: #southeast
                        direction = 'southeast'
                    else:
                        direction = 'southwest'
    return (found,direction)


#function to check if hero has met the king
def checking(world_map):
    met = False
    pos,world_map = findHero(world_map)#find the hero position
    if pos == '7-7': #since rat king is always at that position
        met = True

    return (met)

#function to display king stats
def kingStats(ratKstats):
    for i in ratKstats:
        print('{}: {}'.format(i,ratKstats[i]))

#function to combat rat king when hero meets the rat king
def seeKing(day,holding):
    ratKstats = {'Damage':'6-10','Defence':5,'HP':25} #when player runs and comes back, king restores all hp 
    start_game = True #allow user to loop, will make it False when game is over
    print('Day {}: You see the Rat King!\nEncounter! - Rat King!'.format(day))
    while True:
        tie = False#to declare it is not a tie first
        kingStats(ratKstats)
        menu(fight_text)#display run/attack
        ar = input('Enter choice: ')
        print()
        if ar == '1': #attack
            ran = True
            kdmg = randint(6,10)
            if holding == False:
                hdmg = 0
                hdef = 1
                print('You do not have the Orb of Power - the Rat King is immune!')
            else:
                hdmg = randint(7,9)
                hdef = 6
                if ('Sword')in owned:#additional
                    hdmg+=3
                    if 'Poison' in owned:#poision only works if there is a sword
                        hdmg+=5
                if ('Armor')in owned:#additional
                    hdef+=3
            taken = kdmg - hdef
            dealt = hdmg - 5 #hero damage minus king defence
            if dealt <0:
                dealt = 0
            playerStats['HP']-=taken
            if playerStats['HP']<0:
                playerStats['HP'] = 0
            ratKstats['HP']-=dealt
            print('You deal {} damge to the Rat King'.format(dealt))
            print('Ouch! the Rat King hit you for {} damage!'.format(taken))
            print('You have {} HP left'.format(playerStats['HP']))   
            if ratKstats['HP'] <= 0 and playerStats['HP'] <=0:#king and hero die together (tie)
                print('Both you and the rat king have 0 HP left\nIts a tie!')
                print('The world is saved!')
                tie = True
            if ratKstats['HP']<=0 or playerStats['HP']<=0:
                if ratKstats['HP']<=0:#king hp <0
                    if tie == False:
                        print('The Rat King is dead! You are victorious!')
                        print('Congratulations, you have defeated the Rat King!\nThe world is saved! You win!\n')
                    p = 0#to confirm about not saving the game . if it is the second time prompted, p =1 and 
                    while True:
                        if p == 0:#if it is the first time user is asked
                            print('Do you want to save your score for this game?')
                        else:
                            print('You have chosen not to save the game, are you sure?')#second time asked
                        print('1) Save\n2) Do not save')
                        yesno = input('Enter choice: ')
                        if yesno == '1':
                            name = input('Enter your player name: ')
                            print('Days taken: {}'.format(day))
                            file = open('BonusScores.txt','a')#different file from the basic and adv
                            file.write('{}:{}\n'.format(name,day))
                            file.close()
                            print('Score is saved!')
                            break
                        elif yesno == '2' and p == 0:#if it is the first time user is asked . user has chosen not to save the game for the first time
                            p+=1
                        elif yesno == '2' and p!=0:#second time asked
                            print('You have chosen not to save the game')
                            break       #confirm and break the loop    
                        else:
                            print('Invalid opition\n')
                    
                else:#hero hp <0
                    print('Game over! You lose!')
                start_game = False
                break
                    
        elif ar == '2':
            print('You run and hide')
            ran = True
            break
        else:
            print('Invalid option')
    return (ran,start_game)

#function to display location of the hero (in town or open)   
def location():
    check = inTown(world_map)
    if check == True:
        loca = 'You are in a town'
    else:
        loca = 'You are out in the open' #no need to check if hero is at ratking as the function checking() alr does it
    return loca

#function to randomise orb           
def randomise(world_map):#FOR ORB
    while True:
        grp = randint(1,3) #split the possible locations to 3 boxes (the whole map is a square, so i split it to 3 boxes top right, bottom left&right)
        i = randint(0,3)#row
        j = randint(0,3)#column
        if grp == 1:#top right
            j+=4 #adds 4 to the columns
        elif grp == 2: #bottom left
            i+=4 #adds 4 to the row
        else:#bottom right (adds 4 to column and rows)
            i+=4
            j+=4
        if world_map[i][j] == ' ':#if its blank
            world_map[i].pop(j)
            world_map[i].insert(j,'O')
            break
        #if it there is already something there, loop again until it is a blank space
    return(world_map)


#function to determine the positions of the towns
def choosePositions(): #FOR TOWNS
    world_map[0].pop(0)#put town in the first place
    world_map[0].insert(0,'T')
    num = 0 #the number of towns other than the one already existing
    while num <4:#this loops until it finds suitable positions for the towns
        row = randint(0,7)
        column = randint(0,7)
        #the pop&insert code below is for the first town of the map(top left corner)
        world_map[0].pop(1)
        world_map[0].insert(1,'-')
        world_map[0].pop(2)
        world_map[0].insert(2,'-')
        world_map[1].pop(0)
        world_map[1].insert(0,'-')
        world_map[1].pop(1)
        world_map[1].insert(1,'-')
        world_map[2].pop(0)
        world_map[2].insert(0,'-')
        if world_map[row][column] == ' ':
            num +=1
            world_map[row].pop(column)
            world_map[row].insert(column,'T')
            for i in range(len(world_map)):
                for j in range(len(world_map)):
                    if world_map[i][j] == 'T':
                        if j <=6: #right Ns
                            if world_map[i][j+1] == ' ' or  world_map[i][j+1] == '-':#all these check if the position is already taken up like the rat king
                                world_map[i].pop(j+1)
                                world_map[i].insert(j+1,'-')
                            if j < 6:
                                if world_map[i][j+2] == ' ' or  world_map[i][j+2] == '-':#all these check if the position is already taken up like the rat king
                                    world_map[i].pop(j+2)
                                    world_map[i].insert(j+2,'-')
                        if j >= 1:#left Ns
                            if world_map[i][j-1] == ' ' or  world_map[i][j-1] == '-':
                                world_map[i].pop(j-1)
                                world_map[i].insert(j-1,'-')
                            if j >1:
                                if world_map[i][j-2] == ' ' or  world_map[i][j-2] == '-':
                                    world_map[i].pop(j-2)
                                    world_map[i].insert(j-2,'-')
                        if i >=1:#top Ns
                            if world_map[i-1][j] == ' ' or  world_map[i-1][j] == '-':
                                world_map[i-1].pop(j)
                                world_map[i-1].insert(j,'-')
                            if i >1:
                                if world_map[i-2][j] == ' ' or  world_map[i-2][j] == '-':
                                    world_map[i-2].pop(j)
                                    world_map[i-2].insert(j,'-')
                        if i <=6:#btm Ns
                            if world_map[i+1][j] == ' ' or  world_map[i+1][j] == '-':
                                world_map[i+1].pop(j)
                                world_map[i+1].insert(j,'-')
                            if i <6:
                                if world_map[i+2][j] == ' ' or  world_map[i+2][j] == '-':
                                    world_map[i+2].pop(j)
                                    world_map[i+2].insert(j,'-')
                        if i>0 and j > 0:#top left
                            if world_map[i-1][j-1] == ' ' or  world_map[i-1][j-1] == '-':
                                world_map[i-1].pop(j-1)
                                world_map[i-1].insert(j-1,'-')
                        if i >0 and j<7: #top right
                            if world_map[i-1][j+1] == ' ' or  world_map[i-1][j+1] == '-':
                                world_map[i-1].pop(j+1)
                                world_map[i-1].insert(j+1,'-')
                        if i<7 and j>0: #bottom left
                            if world_map[i+1][j-1] == ' ' or  world_map[i+1][j-1] == '-':
                                world_map[i+1].pop(j-1)
                                world_map[i+1].insert(j-1,'-')
                        if i<7 and j<7: #bottom right
                            if world_map[i+1][j+1] == ' ' or  world_map[i+1][j+1] == '-':
                                world_map[i+1].pop(j+1)
                                world_map[i+1].insert(j+1,'-')
##how the previous function works
##we add the '-' surrounding the towns and that marks as next town cannot be on the place(below shows a sample of it)
##+---+---+---+---+---+---+---+---+
##| T | - | - |   |   |   |   |   |
##+---+---+---+---+---+---+---+---+
##| - | - |   |   |   |   |   |   |
##+---+---+---+---+---+---+---+---+
##| - |   |   | - |   |   |   |   |
##+---+---+---+---+---+---+---+---+
##|   |   | - | - | - |   |   |   |
##+---+---+---+---+---+---+---+---+
##|   | - | - | T | - | - |   |   |
##+---+---+---+---+---+---+---+---+
##|   |   | - | - | - |   |   |   |
##+---+---+---+---+---+---+---+---+
##|   |   |   | - |   |   |   |   |
##+---+---+---+---+---+---+---+---+
##|   |   |   |   |   |   |   | K |
##+---+---+---+---+---+---+---+---+                                
##i have a if statement to ensure that the programe does not replace other characters like the rat king
##after all of that, the function randTown() will remove all the extra stuff in the world_map



#funcion to remove all the extra stuff from randomising the towns and return the world map
def randTown(world_map):
    choosePositions()
    for i in range(len(world_map)):
        for j in range(len(world_map)):
            if world_map[i][j] == '-':
                world_map[i].pop(j)
                world_map[i].insert(j,' ')
    return(world_map)

#function to print a statement with spaces above and below
def prints(text):
    print(f'\n{text}\n')

#function to display the leaderboard
def viewLeaderboard():
    leaderboard = {}
    try:
        file = open('BonusScores.txt','r')
        for i in file:
            i = i.strip()
            i = i.split(':')
            leaderboard[(i[0])] = (i[1])#put data from the file to a dictionary, with  key and value as name and days taken
        file.close()
        if leaderboard == {}:#no one in th eleaderboard
            print('There are currently no players in the leaderboard!\n')
        else:#there is someone who have saved their score
            top = []
            top5 = {}
            for i in leaderboard:
                top.append(int(leaderboard[i]))
            top.sort()
            print()
            if len(leaderboard)<5:#less than 5 people have saved their scores
                print('There are currently less than 5 players')
                for i in range(len(leaderboard)):
                    for j in leaderboard:
                        if top[i] == int(leaderboard[j]):
                            top5[j]= top[i]
                        
            else:#else there is suffient people to display the full top 5 places
                for i in range(0,5):
                    for j in leaderboard:
                        if top[i] == int(leaderboard[j]):
                            top5[j] = top[i]
            print('{}'.format('-'*45))
            print('{:10} {:<20}{:<10}'.format('Rank',"Player's name",'Days taken'))
            print('{}'.format('-'*45))
            rank = 1
            for i in top5:
                print('{:10} {:<20}{:<10}'.format(str(rank),i,top5[i]))
                rank +=1
            print('{}'.format('-'*45))
    except:
        prints("There is no one in the leaderboard yet!")
                 
def exitt():#to provide validation if users are sure about exiting the game
    print('Exit the game? Your current progress will not be saved\n1) Exit\n2) Do not exit')
    while True:
        n = input('Enter choice: ')
        if n == '1':
            print('Exit Game!')
            e = True #assign true to 'e'
            break
        elif n =='2':
            print('You have chosen not to exit the game')
            e = False
            break
        else:
            print('Invalid option\n')
    return e #e stands for exit, if e ==True, exit==True




################################            Bonus feature
items = [['Sword','Damage+3',300],['Armor','Defence+3',300],['Poison','adds 5 damage on top of sword',1000]]
owned=[]
gold = 0 
################################  THIS IS THE MAIN PROGRAME
while True:
    menu(main_text)
    choice = (input('Enter choice: '))
    #used str as input to validate str inputs from user
    
    if choice == '1': #New game
        playerStats = {'dmg':'2-4','defence':1,'HP':20}
        day =1
        start_game = True
        holding = False #this is to declare that user is not holding orb
        world_map=randTown(world_map) #randomise the towns
        world_map = randomise(world_map) #randomly place the orb
        world_map[0].pop(0)# to put in the hero to the map
        world_map[0].insert(0,'H/T')
        break
    elif choice == '2':#resume game saved previously
        try:
            f = open('savedGameBonus.txt','r')
            f.readline()
            f.readline()
            f.readline()
            k = f.readline()#fourth line is the day number, must be an integer, if cannot convert means no saved game
            f.close()
            int(k)
            
        except:
            prints('You do not have any saved game, please save a game before resuming it')
            continue#skips all fowllowing lines
        file = open('savedGameBonus.txt','r')#open the file again
        owned = file.readline()#first line == items
        gold = int(file.readline())#second line
        if owned == '[]\n':
            owned = []
        else:
            owned = owned.strip()
            owned = owned.replace('[','')
            owned = owned.replace(']','')
            owned = owned.replace("'","")
            owned = owned.split(',')
            on = []#declare another list
            for i in owned:
                i=i.strip()
                on.append(i)
            owned = on#items that are owned previously
        
        world_map = []
        w = (file.readline()) #second line is the world_map but with separators 'n' and 'f'
        w=w.split('n')
        w.remove(w[0])#remove the first nested list(empty lis)
        for i in w:
            i = i.split('f')
            i.remove(i[8]) #remove the last value of the list (created as caused by the separator)
            world_map.append(i)  
        day = int(file.readline()) #third line is the day
        hold = file.readline() #read fourth line True or False
        if hold == 'True\n':
            holding = True
        else:
            holding = False
    
        plis = []
        for i in file:
            i = i.strip()
            plis.append(i)#append data into the file first
        file.close()
        playerStats={}
        playerStats['dmg'] = (plis[0])
        playerStats['defence'] = int(plis[1])
        playerStats['HP'] = int(plis[2])
        start_game = True
        break
    elif choice == '3':#viewleaderboard
        viewLeaderboard()
    elif choice == '4':#exit the game
        print('Exit Game') #do not need to validate to confirm if player really wants to exit as game have not started
        start_game = False
        break
    else:#program validation
        print('Invalid option')
while start_game == True:
    loca = location()
    prints('Day {}: {}'.format(day,loca))#format the location where the hero is currently at
    menu(town_text)
    c = input('Enter choice: ')#did not convert input to integer as an error will occur when the user inputs str
    if c == '1': #shows stats
        stats(holding)
    elif c == '2': #show the map
        displayMap(world_map)
    elif c == '3': #move
        moveFunction(world_map) #move the hero and check if the hero has moved
        day+=1
        check = inTown(world_map) #check if user in town
        while check == False: #check if the user is in a town and if player met the rat king
            met = checking(world_map) #check if user met the rat king first in every loop
            if met == False:
                ran,start_game,gold = combat(day,holding,gold) #combat and check if player have ran
            else:
                ran,start_game = seeKing(day,holding)
            if start_game == False:#if hero dies to rat minion, and #if king or hero dies, break the loop
                break
            while True:
                menu(open_text)
                ch = input('Enter choice: ')
                if ch == '3': #move player
                    moveFunction(world_map)
                    day+=1
                    check = inTown(world_map) #check if in town
                    break
                elif ch == '5':#exit game
                    e = exitt()
                    if e == False:#chose not to exit
                        continue #does not run the next codes
                    #when going to exit
                    start_game = False #break the whole loop
                    check = True #it is required to break the second while loop (while check == False)
                    break #breaks the last loop
                if ran == True:
                    if ch == '1' or ch =='2' or ch =='4': #leads to combat
                        break
                    else:
                        print('Option is invalid!')
                elif ch == '1': #show stats
                    stats(holding)
                elif ch == '2': #display the map
                    displayMap(world_map)
                elif ch == '4': #sense orb
                    if holding == True:#if the user already has the orb of power
                        print('\nYou have already found the orb of power!')
                        print('Your hero stats cannot be increased further!\n')
                    else:
                        f,direction = sense()
                        day+=1
                        if f == True: #if player is on orb
                            print('You found the Orb of Power!\nYour attack increases by 5!\nYour defence increases by 5!')
                            playerStats['defence']+=5
                            playerStats['dmg']= '7-9'
                            if 'Sword'in owned:
                                playerStats['dmg']='10-12'
                                if 'Poison' in owned:
                                    playerStats['dmg']='15-17'
                            
                            holding = True
                        else:#print the direction
                            print('You sense that the Orb of Power is to the {}'.format(direction))
                        loca = location()
                        print('Day {}: {}'.format(day,loca))
                else:
                    print('Option is invalid!')
                      
    elif c == '4': #rest
        playerStats['HP'] = 20
        print('\nYour health has been fully restored to 20HP\n')
        day+=1
    elif c == '5': #save the game
        save = True #let it be true first, late can change

        f = open('savedGameBonus.txt','w+') #see if there is anything first VALIDATION
        f.readline()#remove 1st line
        f.readline()#remove second line
        f.readline()
        k = f.readline()#assign fourthline (the day number)
        f.close()
        try:
            int(k)#try to convert it to int, if it is not and integer, except statement will exceute
            no_game = False
        except:
            no_game = True
        if no_game == False: #if there are no game saved previously, program skips this statement
            print('You already have a game saved previously, once you decide to save a new game,\nall previous data will be lost,do you want save the new game?')
            while True:
                yn =input('1) Save\n2) Do not save\nEnter choice: ')
                if yn == '2':
                    print('You have chosen not to save the game')
                    save = False#assign it to be false
                    break
                elif yn == '1':
                    print('Save the new game')
                    break
                else:
                    print('Option is invalid')
        if save == True:#Actual saving of the game
            file = open('savedGameBonus.txt','w')#remove any other data previously in the file so the program can work properly
            file.write(str(owned)+'\n')#write all owened items inside the first line
            file.write(str(gold)+'\n')#write the gold inside (second line)
            for i in world_map:#the 'n'and 'f' serves as a separator from string indentified to a nested list
                file.write('n')
                for j in i:
                    file.write(j + 'f')
            file.write('\n'+str(day)+'\n')
            file.write(str(holding)+'\n')
            for i in playerStats:
                file.write('{}\n'.format(playerStats[i]))
            file.close()
            print('Game Saved')
            while True:
                print('Do you want to conitnue with your current game?\n1) Continue\n2) Exit Game')
                c = input('Enter choice: ')
                if c == '1':#conitnue game
                    break #inner loop
                elif c == '2':
                    print('Exit game')
                    break #inner loop
                else:
                    print('\nEnter a valid option\n')
            if c == '2':#outer loop when user have chosen to exit game after exiting
                break
            
    elif c == '6':#exit game
        e = exitt()
        if e == True:
            break
    elif c == '7':#buy items in the town BONUS
        if len(owned)==len(items):
            print('\nYou already have all the items\nYou cannot buy them again\n')
            continue
        print('{:<10}{:<10}{:<35}{:<5}'.format('Number','Item','Description','Cost(gold)'))
        print('{}'.format('-'*75))
        m=1
        for i in items:
            print('{:^10}{:<10}{:<35}{:<5}'.format(m,i[0],i[1],i[2]))
            m+=1
        while True:
            print('\nYou have {} gold\n'.format(gold))
            b = input("Enter the number of the item you want to buy or enter 'e' to exit: ")
            if b == 'e' or b == 'E':#exit the shop
                print('\nExit shop\n')
                break
            try:
                b=int(b)#if user entered str, exception will run
                if b>len(items) or b<0:
                    excpt = 'str'+1#cause the except statement to execute because of error
                s = items[b-1][0]
                if s in owned:#if already owned the item
                    print('\nYou cannot buy an item more than once\n')
                    break
                if (items[b-1][2])>gold:#not enough gold
                    print('You do not have enough gold')
                else:
                    owned.append(items[b-1][0])#enough gold and proceed with buying 
                    print('You have brought {}, {}\n'.format(items[b-1][0],items[b-1][1]))#show item brought and show the stats
                    if items[b-1][0] == 'Sword':
                        if holding == False:
                            playerStats['dmg']=('5-7')#brought sowrd but no orb
                            if 'Poison' in owned:
                                playerStats['dmg']=('10-12')#if player has brought poison before
                            
                        else:
                            playerStats['dmg']=('10-12')#brought sword and has orb
                            if 'Poison' in owned:
                                playerStats['dmg']=('15-17')#if player has brought poison before
                    if items[b-1][0] == 'Armor':
                            playerStats['defence']+=3#brought armor, defence+3
                    if items[b-1][0] == 'Poison':
                        if 'Sword' in owned:
                            if holding == False:#has sword and no orb
                                playerStats['dmg']=('10-12')
                            else:#have sowrd and has orb
                                playerStats['dmg']=('15-17')
                        else:#poison will onlytake effect if sword is present
                            print('You do not have the sword, the poison will not have any effect\n')
                            
                    gold-=items[b-1][2]
                    print('\nYou now have {} gold left'.format(gold))
                    break
            except:
                print('Enter a valid option')
        
    elif c == '8':#view inventory BONUS
        if owned == []:#if player's inventory is empty
            print('\nYou do not have any items in your inventory\n')
        else:#display what is inside
            print('\nInventory')
            print('{}'.format('-'*20))
            for i in range(len(owned)):
                print('{}) {}'.format(i+1,owned[i]))
            print()

        
    else:
        print('Invalid option\n')


    
    

