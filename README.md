Ratventure
Python text based game


--Main Menu
the program will first start with an option to start new game etc, (town_text). if start game, everything will be default towns and orb will be randomised, if resume, program will read the last game saved to the file and
there cannot be more than one game saved at a time. if there are no game saved, user will be prompted.Players can view the leaderboard, if no on saved their scores yet, programe will display that to users, if less than 5 players,
programe will display that there are less than 5 players and show the players in ranking, if there are 5 or more, programe will show top 5 players. Last option is to exit game


--in the game TOWN
once in the game and everytime player is at the town, users can display their stats, which shows Hero damage, defence, HP and if player has the orb of power, the program shows that as well
users can display map, that function is just to show the map, another function is to allow players to move within the map (takes 1 day), when hero is in the open, he will encounter a rat minion(unless he is at the position of the King)
hero cannot move out of the map .if user try to move it out, it will not be moved and user will be asked to enter another option unitl the option is valid. The rest function can only be in
town and it restores the hero's HP to 20, and it takes 1 day. Save game option - allows users to save all data needed for the game,(orb,HP,damage,defence,days, town positions etc)
Last option is to exit the game
BONUS - players can buy sowrd(adds 3 damage),armor(adds 3 defence), and poison which only works with a sword and adds 5 damage, they can only buy each of the items once. In the shop, if players want to exit the shop, they can press'e'
 if they do not have enough gold for any items they want, they will be prompted saying that they do noy have enough gold.
 when they brought all of their items, they are unable to buy any more, these items can be brought with gold, that is earned b defeating rat minions in combat
BONUS - the last option in the town menu is to view thei inventory, that shows what items they currently have.
BONUS - when players choose to display their stats,how much gold they have will be shown as well.

--in the game IN THE OPEN (program is such that everytime user is in the open, will encounter a rat minion except for when met with rat King)
when player is out in the open,player can display stats, view map and move normally like mentioned previously. Users can also sense orb (adds 1 day) to either sense the direction of the orb or to collect the orb if user is standing on it
last option is to exit the game, players will be prompted if they are sure and if confirm exit, game will not be saved , if not the game continues. Only the function 'Move' and 'Exit game' works normally if
 user ran away from the battle, if user did not run, all functions work normally

--in the game Combatting rat minions (everytime player runs, rat regains all health)
players have two option to either attack or run, after every attack, player's HP, Rats'HP ,its defence and its damage range will be shown, dealt damage = opponent damage minus your defence,
if player has HP less than or equal to 0, player loses the battle and exits the game
if rat has HP less than or equal to 0, player win the round and gets to continue the game. If player chooses to run, some of the open text function will not be working as mentioned before.
Both the rat and hero cannot deal negative damage to each other, if negative damage is detected, the damage will be 0
BONUS- each time player defeats a rat minion, they drop 50 gold.

--in the game Combatting the rat king (everytime player runs, king regains all health)
similarly, player can attack or run, when player HP drop to 0 and below,player loses and exit the game.If king's HP drop to 0 or below, player wins the game, player will be prompted if they want to save the score
if they want to save, they will enter their player name and program will save their name and score(days taken to complete). If they chose not to save, they will be prompted again if they are sure about not saving, if they are sure
 about not saving, game will end without saving.

--in the game Combat (rat and rat King)(RESULT IS TIE)
if the result is tie, for combat with minions, rat minion dies but hero loses and exits. For the combat with the king, both king and hero dies, but when kingis dead, world is saved and player can still
save their score as per normal like defeating the rat king.