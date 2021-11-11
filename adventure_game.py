import random
import sys

class Adventurer:
    def __init__ (self, name):
        self.name = name
        self.health = 100
        self.gold = 0
        
    def getHealth(self):
        return self.health
        
    def getName(self):
        return self.name
    
    def doAttack(self):
        return random.randint(1, 35)
    
    def damageAdventurer(self, damage):
        self.health = self.health - damage
        
    def getGold(self, goldAmt):
        self.gold = self.gold + goldAmt
        
    def totalGold(self):
        return self.gold
        
    
class Weapon:
    def __init__ (self):
        self.weapon = ""
        self.stat = 0
        
    def assignWeapon(self):
        num = random.randint(0, 2)
         
        if num == 0:
            self.weapon = 'sword'
        elif num == 1:
            self.weapon = 'çrossbow'
        else:
            self.weapon = 'axe'
          
    def getWeapon(self):
        return self.weapon
        
        
class Enemy:
    def __init__ (self):
        self.enemy = ""
        self.intro = ""
        self.health = 0
        self.attack = 0
        
    def assignEnemy(self):
        num = random.randint(0, 2)
         
        if num == 0:
            self.enemy = 'a goblin'
            self.intro = 'What vile, nasty creatures!'
            self.health = random.randint(15, 36)
        elif num == 1:
            self.enemy = 'a witch'
            self.intro = 'Clever and dangerous; witches are the ones who laid the curse upon the land.'
            self.health = random.randint(15, 36)
        else:
            self.enemy = 'a fae'
            self.intro = 'Quick witted and cunning; the fae are not to be trifled with.'
            self.health = random.randint(15, 36)
          
    def getEnemy(self):
        return self.enemy
    
    def getIntro(self):
        return self.intro
    
    def getEnemyHealth(self):
        return self.health
    
    
    def damageEnemy(self, damage):
        self.health = self.health - damage
        
    def doEnemyAttack(self):
        return random.randint(1, 15)
        
    
class Moves:
    def __init__ (self):
        self.move = ""
        
    def assignMove(self, adventurer):
        num = random.randint(0, 2)
         
        if num == 0:
            print('\nNothing happened!')
        elif num == 1:
            goldAmt = random.randint(1, 50)
            adventurer.getGold(goldAmt)
            print('\nYou gained {0} gold! You have {1} gold.'.format( goldAmt, adventurer.totalGold()))
        elif num == 2:
            enemy = Enemy()
            enemy.assignEnemy()
            print('\nYou have encountered {0}. {1} Its health is {2}.\n'.format(enemy.getEnemy(), enemy.getIntro(), enemy.getEnemyHealth()))
            #loop here for attack
            while enemy.getEnemyHealth() > 0:
                hitAdventurer = enemy.doEnemyAttack()
                adventurer.damageAdventurer(hitAdventurer)
                if adventurer.getHealth() > 0:
                    print('The {0} is attacking!'.format(enemy.getEnemy()))
                    print('You have taken damage! Currently at {0} health.\n'.format(adventurer.getHealth()))
                else:
                    print('Alas, you have been vanquished! GAME OVER.')
                    sys.exit()
                hitEnemy = adventurer.doAttack()
                enemy.damageEnemy(hitEnemy)
                if enemy.getEnemyHealth() > 0:
                    print('Attacking {0}!'.format(enemy.getEnemy()))
                    print('Attacker is hit for {0} damage! {1} is at {2} health.\n'.format(hitEnemy, enemy.getEnemy(), enemy.getEnemyHealth() ))
                else:
                    print('***Enemy has been vanquised!***')
                



                
        else:
            print('There was an error')
        
        
def main():
    print('Welcome to Ardavan, dear traveler.')
    print('Our fair land has been cursed and our prince kidnapped.')
    print('With your assistance, we hope to restore our land and rescue our prince.')
    beginadv = input('Do you wish to aid us in this quest? Y/N? ')
    print('--------------')
    
    if beginadv.upper() == 'Y':
        name = input('\nHuzzah! What name shall we call you along our journey? ')
    elif beginadv.upper() == 'N':
        print('\nWe wish you well on your journey dear traveler.')
        #This should now print out your stats.
        sys.exit()
    else:
        print('There has been an error.')
        sys.exit()
    
        
    p1 = Adventurer(name)
    w1 = Weapon()
    w1.assignWeapon()

    #print('Title: {}, Health {}.'.format(e1.getEnemy(), e1.getEnemyHealth()))

    print('\nFor joining our quest, {0}, we bestow upon you this weapon. A {1}'.format(p1.getName(), w1.getWeapon()))
    print('Our guide wishes to take us into the forest, the last place that the prince was seen.')
    step2 = input('Do we follow him? Y/N? ')
    print('--------------')
    
    move = Moves()
    move.assignMove(p1)
    
    if step2.upper() == 'Y':
        print('\nWe have come to a fork in the path.')
        print('Toward the right, we will be heading toward the old castle ruins.')
        step3 = input('If we take the left, we will be heading for the swamp. R/L? ')
        print('--------------')
        move.assignMove(p1)
        
        if step3.upper() == 'R':
            print('\nSmoke drifts from a small cottage ahead on our path, the last stop before the ruins.')
            print('Though it is shabby, it could lead to some clue about the whereabouts of the prince. ')
            step4 = input('Do we examine the cottage? Y/N? ')
            print('--------------')
            move.assignMove(p1)

            if step4.upper() == 'Y':
                print('\nThe cottage appears to be empty though a small cooking fire burns in the ')
                print('Hearth and the smell of food wafts out. ')
                step5 = input('Do you want to grab food and leave payment for the owner? Y/N ')
                print('--------------')
                move.assignMove(p1)

                if step5.upper() == 'Y':
                    print('\nYou grab the food and leave 10 gold')
                    print('The food is poisoned! You have died.')
                    print('You Lose.')
                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                    sys.exit()

                else: #You don't eat the food
                    print('\nDecide to leave the cottage as it is and head back onto our path. ')
                    print('The castle ruins are close! ')
                    print('You decide to seek shelter there for the evening')
                    print('\nUpon moving into the castle ruins, the ground rumbles beneath our party’s feet before collapsing.')
                    step6 = input('All are plunged into darkness. Do you light a match? Y/N? ')
                    print('--------------')
                    move.assignMove(p1)

                    if step6.upper() == 'Y':
                        print('\nAs the match flickers to light, your party realizes they are in the old crypt of the castle. ')
                        step7 = input('Should we seek the prince here? Y/N? ')
                        print('--------------')
                        move.assignMove(p1)

                        if step7.upper() == 'Y':
                            print('\nA voice calls from behind, begging for assistance.')
                            step8 = input('Do you assist? Y/N? ')
                            print('--------------')
                            move.assignMove(p1)

                            if step8.upper() == 'Y':
                                print('\nThe prince! But certainly not the voice calling for assistance.')
                                print('The prince had been attempting to break the curse and was not kidnapped.')
                                print('The prince asks for a piece of your gold')
                                step9 = input('Do you give it to him? Y/N? ')
                                print('--------------')
                                move.assignMove(p1)

                                if step9.upper() == 'Y':
                                    print('\nOf Course! Whatever the prince needs must be helpful, right? ')
                                    print('The prince places the gold piece against the cover of the book in his hands.')
                                    print('It sizzles for a moment before binding itself to the book')
                                    print('The book drops to the ground and a woman materializes, ')
                                    print('hair as gold as the piece you handed the prince. ')
                                    step10 = input('She wishes to bestow a token upon your party. Do you take it? Y/N? ')
                                    print('--------------')
                                    move.assignMove(p1)

                                    if step10.upper() == 'Y':
                                        print('\nWith her gift, the curse is lifted and you have recovered the prince! YOU WIN!')
                                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                        sys.exit()
                                    else: #do not take the gift
                                        print('\nBy turning aside her gift, you leave the land cursed as it was when you arrived.  But you at least found the prince! ')
                                        print('You Win, but the land remains cursed.')
                                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                        sys.exit()

                                else: #do not give prince the gold
                                    print('\nI’ve earned this gold fair and square!')
                                    print('Leave with your goods and say good riddance to the land and its strange curse.')
                                    print('You Lose.')
                                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                    sys.exit()

                            else: #Do Not Assist
                                print('\nEnough of this adventure!')
                                print('Leave with your goods and say good riddance to the land and its strange curse.')
                                print('You Lose.')
                                print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                sys.exit()

                        else: #Do not seek the prince
                            print('\nEnough of this adventure!')
                            print('Leave with your goods and say good riddance to the land and its strange curse.')
                            print('You Lose.')
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                            sys.exit()

                    else: #Do not light the match
                        print('\nIn the darkness, things take on an eerie feel.')
                        print('Your flesh crawls at the very feel of things and ')
                        print('at the first sight of light you leave, abandoning your mission.')
                        print('You Lose.')
                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                        sys.exit()


            else: #Don't Exmine the Cottage
                print('\nUpon skirting the cottage, you spot the ruins of the castle')
                print('and decide to seek shelter there for the evening.')
                print('\nUpon moving into the castle ruins, the ground rumbled beneath the partys feet before collapsing')
                step11 = input('All are plunged into darkness. Do you light a match? Y/N? ')
                print('--------------')
                move.assignMove(p1)

                if step11.upper() == 'Y':
                    print('\nAs the match flickers to light, your party realizes they are in the old crypt of the castle. ')
                    step12 = input('Should we seek the prince here? Y/N? ')
                    print('--------------')
                    move.assignMove(p1)

                    if step12.upper() == 'Y':
                        print('\nA voice calls from behind, begging for assistance.')
                        step13 = input('Do you assist? Y/N? ')
                        print('--------------')
                        move.assignMove(p1)

                        if step13.upper() == 'Y':
                            print('\nThe prince! But certainly not the voice calling for assistance.')
                            print('The prince had been attempting to break the curse and was not kidnapped.')
                            print('The prince asks for a piece of your gold')
                            step14 = input('Do you give it to him? Y/N? ')
                            print('--------------')
                            move.assignMove(p1)

                            if step14.upper() == 'Y':
                                print('\nOf Course! Whatever the prince needs must be helpful, right? ')
                                print('\nThe prince places the gold piece against the cover of the book in his hands.')
                                print('It sizzles for a moment before binding itself to the book')
                                print('The book drops to the ground and a woman materializes, ')
                                print('hair as gold as the piece you handed the prince. ')
                                step15 = input('She wishes to bestow a token upon your party. Do you take it? Y/N? ')
                                print('--------------')
                                move.assignMove(p1)

                                if step15.upper() == 'Y':
                                    print('\nWith her gift, the curse is lifted and you have recovered the prince! YOU WIN!')    
                                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                    sys.exit()
                                else: #do not take the gift
                                    print('\nBy turning aside her gift, you leave the land cursed as it was when you arrived.  But you at least found the prince! ')
                                    print('You Win, but the land remains cursed.')
                                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                    sys.exit()

                            else: #do not give prince the gold
                                print('\nI’ve earned this gold fair and square!')
                                print('Leave with your goods and say good riddance to the land and its strange curse.')
                                print('You Lose.')
                                print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                sys.exit()

                        else: #Do Not Assist
                            print('\nEnough of this adventure!')
                            print('Leave with your goods and say good riddance to the land and its strange curse.')
                            print('You Lose.')
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                            sys.exit()

                    else: #Do not seek the prince
                        print('\nEnough of this adventure!')
                        print('Leave with your goods and say good riddance to the land and its strange curse.')
                        print('You Lose.')
                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                        sys.exit()

                else: #Do not light the match
                    print('\nIn the darkness, things take on an eerie feel.')
                    print('Your flesh crawls at the very feel of things and ')
                    print('at the first sight of light you leave, abandoning your mission.')
                    print('You Lose.')
                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                    sys.exit()


        elif step3.upper() == 'L': #L Choice
            print('\nA light flickers to life several paces ahead.')
            print('Do we wish to examine the light?')
            step16 = input('It might lead us toward the sorcery that has befalled the kingdom. Y/N? ')
            print('--------------')
            move.assignMove(p1)

            if step16.upper() == 'Y':
                print('\nIt appears to be a will o’ the wisp. We should turn back before we become lost in the swamp.')
                print('From here, we can see a trail of smoke.')
                print('It might be someone with more information. ')
                print('\nSmoke drifts from a small cottage ahead on our path, the last stop before the ruins. ')
                print('Though it is shabby, it could lead to some clue about the whereabouts of the prince. ')
                step17 = input('Do we examine the cottage? Y/N? ')
                print('--------------')
                move.assignMove(p1)

                if step17.upper() == 'Y':
                    print('\nThe cottage appears to be empty though a small cooking fire burns in the ')
                    print('Hearth and the smell of food wafts out. ')
                    step18 = input('Do you want to grab food and leave payment for the owner? Y/N ')
                    print('--------------')
                    move.assignMove(p1)

                    if step18.upper() == 'Y':
                        print('\nYou grab the food and leave 10 gold')
                        print('The food is poisoned! You have died.')
                        print('You Lose.')
                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                        sys.exit()

                    else: #You don't eat the food
                        print('\nDecide to leave the cottage as it is and head back onto our path. ')
                        print('The castle ruins are close! ')
                        print('You decide to seek shelter there for the evening')
                        print('\nUpon moving into the castle ruins, the ground rumbles beneath our party’s feet before collapsing.')
                        step19 = input('All are plunged into darkness. Do you light a match? Y/N? ')
                        print('--------------')
                        move.assignMove(p1)

                        if step19.upper() == 'Y':
                            print('\nAs the match flickers to light, your party realizes they are in the old crypt of the castle. ')
                            step20 = input('Should we seek the prince here? Y/N? ')
                            print('--------------')
                            move.assignMove(p1)

                            if step20.upper() == 'Y':
                                print('\nA voice calls from behind, begging for assistance.')
                                step21 = input('Do you assist? Y/N? ')
                                print('--------------')
                                move.assignMove(p1)

                                if step21.upper() == 'Y':
                                    print('\nThe prince! But certainly not the voice calling for assistance.')
                                    print('The prince had been attempting to break the curse and was not kidnapped.')
                                    print('The prince asks for a piece of your gold')
                                    step22 = input('Do you give it to him? Y/N? ')
                                    print('--------------')
                                    move.assignMove(p1)

                                    if step22.upper() == 'Y':
                                        print('\nOf Course! Whatever the prince needs must be helpful, right? ')
                                        print('The prince places the gold piece against the cover of the book in his hands.')
                                        print('It sizzles for a moment before binding itself to the book')
                                        print('The book drops to the ground and a woman materializes, ')
                                        print('hair as gold as the piece you handed the prince. ')
                                        step23 = input('She wishes to bestow a token upon your party. Do you take it? Y/N? ')
                                        print('--------------')
                                        move.assignMove(p1)

                                        if step23.upper() == 'Y':
                                            print('\nWith her gift, the curse is lifted and you have recovered the prince! YOU WIN!')    
                                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                            sys.exit()
                                        else: #do not take the gift
                                            print('\nBy turning aside her gift, you leave the land cursed as it was when you arrived.  But you at least found the prince! ')
                                            print('You Win, but the land remains cursed.')
                                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                            sys.exit()

                                    else: #do not give prince the gold
                                        print('\nI’ve earned this gold fair and square!')
                                        print('Leave with your goods and say good riddance to the land and its strange curse.')
                                        print('You Lose.')
                                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                        sys.exit()

                                else: #Do Not Assist
                                    print('\nEnough of this adventure!')
                                    print('Leave with your goods and say good riddance to the land and its strange curse.')
                                    print('You Lose.')
                                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                    sys.exit()

                            else: #Do not seek the prince
                                print('\nEnough of this adventure!')
                                print('Leave with your goods and say good riddance to the land and its strange curse.')
                                print('You Lose.')
                                print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                sys.exit()

                        else: #Do not light the match
                            print('\nIn the darkness, things take on an eerie feel.')
                            print('Your flesh crawls at the very feel of things and ')
                            print('at the first sight of light you leave, abandoning your mission.')
                            print('You Lose.')
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                            sys.exit()
                else: #do not examine the cottage ((added these in later, hence the out of order numbers)
                    print('\nUpon skirting the cottage, you spot the ruins of the castle')
                    print('and decide to seek shelter there for the evening.')
                    print('\nUpon moving into the castle ruins, the ground rumbled beneath the partys feet before collapsing')
                    step40 = input('All are plunged into darkness. Do you light a match? Y/N? ')
                    print('--------------')
                    move.assignMove(p1)

                    if step40.upper() == 'Y':
                        print('\nAs the match flickers to light, your party realizes they are in the old crypt of the castle. ')
                        step41 = input('Should we seek the prince here? Y/N? ')
                        print('--------------')
                        move.assignMove(p1)

                        if step41.upper() == 'Y':
                            print('\nA voice calls from behind, begging for assistance.')
                            step42 = input('Do you assist? Y/N? ')
                            print('--------------')
                            move.assignMove(p1)

                            if step42.upper() == 'Y':
                                print('\nThe prince! But certainly not the voice calling for assistance.')
                                print('The prince had been attempting to break the curse and was not kidnapped.')
                                print('The prince asks for a piece of your gold')
                                step43 = input('Do you give it to him? Y/N? ')
                                print('--------------')
                                move.assignMove(p1)

                                if step43.upper() == 'Y':
                                    print('\nOf Course! Whatever the prince needs must be helpful, right? ')
                                    print('\nThe prince places the gold piece against the cover of the book in his hands.')
                                    print('It sizzles for a moment before binding itself to the book')
                                    print('The book drops to the ground and a woman materializes, ')
                                    print('hair as gold as the piece you handed the prince. ')
                                    step44 = input('She wishes to bestow a token upon your party. Do you take it? Y/N? ')
                                    print('--------------')
                                    move.assignMove(p1)

                                    if step44.upper() == 'Y':
                                        print('\nWith her gift, the curse is lifted and you have recovered the prince! YOU WIN!')    
                                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                        sys.exit()
                                    else: #do not take the gift
                                        print('\nBy turning aside her gift, you leave the land cursed as it was when you arrived.  But you at least found the prince! ')
                                        print('You Win, but the land remains cursed.')
                                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                        sys.exit()

                                else: #do not give prince the gold
                                    print('\nI’ve earned this gold fair and square!')
                                    print('Leave with your goods and say good riddance to the land and its strange curse.')
                                    print('You Lose.')
                                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                    sys.exit()

                            else: #Do Not Assist
                                print('\nEnough of this adventure!')
                                print('Leave with your goods and say good riddance to the land and its strange curse.')
                                print('You Lose.')
                                print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                sys.exit()

                        else: #Do not seek the prince
                            print('\nEnough of this adventure!')
                            print('Leave with your goods and say good riddance to the land and its strange curse.')
                            print('You Lose.')
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                            sys.exit()

                    else: #Do not light the match
                        print('\nIn the darkness, things take on an eerie feel.')
                        print('Your flesh crawls at the very feel of things and ')
                        print('at the first sight of light you leave, abandoning your mission.')
                        print('You Lose.')
                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                        sys.exit()
                    
            else: #Don't Examine the light
                    print('\nWith the light failing us for the day, we should seek shelter.')
                    print('The castle ruins, though dangerous, would provide perfect shelter.')
                    step24 = input('Should we head into the ruins? Y/N? ')
                    print('--------------')
                    move.assignMove(p1)

                    if step24.upper() == 'Y':
                        print('\nUpon moving into the castle ruins, the ground rumbles beneath our party’s feet before collapsing.')
                        step25 = input('All are plunged into darkness. Do you light a match? Y/N? ')
                        print('--------------')
                        move.assignMove(p1)

                        if step25.upper() == 'Y':
                            print('\nAs the match flickers to light, your party realizes they are in the old crypt of the castle. ')
                            step26 = input('Should we seek the prince here? Y/N? ')
                            print('--------------')
                            move.assignMove(p1)

                            if step26.upper() == 'Y':
                                print('\nA voice calls from behind, begging for assistance.')
                                step27 = input('Do you assist? Y/N? ')
                                print('--------------')
                                move.assignMove(p1)

                                if step27.upper() == 'Y':
                                    print('\nThe prince! But certainly not the voice calling for assistance.')
                                    print('The prince had been attempting to break the curse and was not kidnapped.')
                                    print('The prince asks for a piece of your gold')
                                    step28 = input('Do you give it to him? Y/N? ')
                                    print('--------------')
                                    move.assignMove(p1)

                                    if step28.upper() == 'Y':
                                        print('\nOf Course! Whatever the prince needs must be helpful, right? ')
                                        print('The prince places the gold piece against the cover of the book in his hands.')
                                        print('It sizzles for a moment before binding itself to the book')
                                        print('The book drops to the ground and a woman materializes, ')
                                        print('hair as gold as the piece you handed the prince. ')
                                        step29 = input('She wishes to bestow a token upon your party. Do you take it? Y/N? ')
                                        print('--------------')
                                        move.assignMove(p1)

                                        if step29.upper() == 'Y':
                                            print('\nWith her gift, the curse is lifted and you have recovered the prince! YOU WIN!')    
                                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                            sys.exit()
                                        else: #do not take the gift
                                            print('\nBy turning aside her gift, you leave the land cursed as it was when you arrived.  But you at least found the prince! ')
                                            print('You Win, but the land remains cursed.')
                                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                            sys.exit()

                                    else: #do not give prince the gold
                                        print('\nI’ve earned this gold fair and square!')
                                        print('Leave with your goods and say good riddance to the land and its strange curse.')
                                        print('You Lose.')
                                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                        sys.exit()

                                else: #Do Not Assist
                                    print('\nEnough of this adventure!')
                                    print('Leave with your goods and say good riddance to the land and its strange curse.')
                                    print('You Lose.')
                                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                    sys.exit()

                            else: #Do not seek the prince
                                print('\nEnough of this adventure!')
                                print('Leave with your goods and say good riddance to the land and its strange curse.')
                                print('You Lose.')
                                print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                sys.exit()

                        else: #Do not light the match
                            print('\nIn the darkness, things take on an eerie feel.')
                            print('Your flesh crawls at the very feel of things and ')
                            print('at the first sight of light you leave, abandoning your mission.')
                            print('You Lose.')
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                            sys.exit()

                    else: #do not head into the ruins
                        print('The grounds of the castle ruins are in shambles.')
                        print('On our way around, the party steps upon an old trap door.')
                        print('The fall down the shaft is long, but everyone reaches the bottom in one piece.')
                        step30 = input('In the darkness, your party cannot see. Do you light a match? Y/N? ')
                        print('--------------')
                        move.assignMove(p1)

                        if step30.upper() == 'Y':
                            print('\nAs the match flickers to light, your party realizes they are in the old crypt of the castle. ')
                            step31 = input('Should we seek the prince here? Y/N? ')
                            print('--------------')
                            move.assignMove(p1)

                            if step31.upper() == 'Y':
                                print('\nA voice calls from behind, begging for assistance.')
                                step32 = input('Do you assist? Y/N? ')
                                print('--------------')
                                move.assignMove(p1)

                                if step32.upper() == 'Y':
                                    print('\nThe prince! But certainly not the voice calling for assistance.')
                                    print('The prince had been attempting to break the curse and was not kidnapped.')
                                    print('The prince asks for a piece of your gold')
                                    step33 = input('Do you give it to him? Y/N? ')
                                    print('--------------')
                                    move.assignMove(p1)

                                    if step33.upper() == 'Y':
                                        print('\nOf Course! Whatever the prince needs must be helpful, right? ')
                                        print('The prince places the gold piece against the cover of the book in his hands.')
                                        print('It sizzles for a moment before binding itself to the book')
                                        print('The book drops to the ground and a woman materializes, ')
                                        print('hair as gold as the piece you handed the prince. ')
                                        step34 = input('She wishes to bestow a token upon your party. Do you take it? Y/N? ')
                                        print('--------------')
                                        move.assignMove(p1)

                                        if step34.upper() == 'Y':
                                            print('\nWith her gift, the curse is lifted and you have recovered the prince! YOU WIN!')    
                                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                            sys.exit()
                                        else: #do not take the gift
                                            print('\nBy turning aside her gift, you leave the land cursed as it was when you arrived.  But you at least found the prince! ')
                                            print('You Win, but the land remains cursed.')
                                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                            sys.exit()

                                    else: #do not give prince the gold
                                        print('\nI’ve earned this gold fair and square!')
                                        print('Leave with your goods and say good riddance to the land and its strange curse.')
                                        print('You Lose.')
                                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                        sys.exit()

                                else: #Do Not Assist
                                    print('\nEnough of this adventure!')
                                    print('Leave with your goods and say good riddance to the land and its strange curse.')
                                    print('You Lose.')
                                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                    sys.exit()

                            else: #Do not seek the prince
                                print('\nEnough of this adventure!')
                                print('Leave with your goods and say good riddance to the land and its strange curse.')
                                print('You Lose.')
                                print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                                sys.exit()

                        else: #Do not light the match
                            print('\nIn the darkness, things take on an eerie feel.')
                            print('Your flesh crawls at the very feel of things and ')
                            print('at the first sight of light you leave, abandoning your mission.')
                            print('You Lose.')
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                            sys.exit()

        else: #enter an incorrect key on R/L
            print('Invalid key selection')
            sys.exit()

    else: #decide to skirt the forest
        print('\nIf we continue on this path, we’ll be able to get around the forest and to the castle from the far side.')
        print('Perhaps the old ruins are where the prince is located.')
        #Castle Ruin path should go here.
        print('\nThe ruins are just ahead. Watch your step! ')
        print('The ground has not been sturdy for a long time. ')
        print('The ground rumbles and sinks beneath our party’s feet. ')
        print('\nAll are plunged into darkness. ')
        step35 = input('Should we light a match? Y/N')
        print('--------------')
        move.assignMove(p1)

        if step35.upper() == 'Y':
            print('\nAs the match flickers to light, your party realizes they are in the old crypt of the castle. ')
            step36 = input('Should we seek the prince here? Y/N? ')
            print('--------------')
            move.assignMove(p1)

            if step36.upper() == 'Y':
                print('\nA voice calls from behind, begging for assistance.')
                step37 = input('Do you assist? Y/N? ')
                print('--------------')
                move.assignMove(p1)

                if step37.upper() == 'Y':
                    print('\nThe prince! But certainly not the voice calling for assistance.')
                    print('The prince had been attempting to break the curse and was not kidnapped.')
                    print('The prince asks for a piece of your gold')
                    step38 = input('Do you give it to him? Y/N? ')
                    print('--------------')
                    move.assignMove(p1)

                    if step38.upper() == 'Y':
                        print('\nOf Course! Whatever the prince needs must be helpful, right? ')
                        print('The prince places the gold piece against the cover of the book in his hands.')
                        print('It sizzles for a moment before binding itself to the book')
                        print('The book drops to the ground and a woman materializes, ')
                        print('hair as gold as the piece you handed the prince. ')
                        step39 = input('She wishes to bestow a token upon your party. Do you take it? Y/N? ')
                        print('--------------')
                        move.assignMove(p1)

                        if step39.upper() == 'Y':
                            print('\nWith her gift, the curse is lifted and you have recovered the prince! YOU WIN!')    
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                            sys.exit()
                        else: #do not take the gift
                            print('\nBy turning aside her gift, you leave the land cursed as it was when you arrived.  But you at least found the prince! ')
                            print('You Win, but the land remains cursed.')
                            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(p1), p1.getHealth(p1) ))
                            sys.exit()

                    else: #do not give prince the gold
                        print('\nI’ve earned this gold fair and square!')
                        print('Leave with your goods and say good riddance to the land and its strange curse.')
                        print('You Lose.')
                        print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                        sys.exit()

                else: #Do Not Assist
                    print('\nEnough of this adventure!')
                    print('Leave with your goods and say good riddance to the land and its strange curse.')
                    print('You Lose.')
                    print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                    sys.exit()

            else: #Do not seek the prince
                print('\nEnough of this adventure!')
                print('Leave with your goods and say good riddance to the land and its strange curse.')
                print('You Lose.')
                print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
                sys.exit()

        else: #Do not light the match
            print('\nIn the darkness, things take on an eerie feel.')
            print('Your flesh crawls at the very feel of things and ')
            print('at the first sight of light you leave, abandoning your mission.')
            print('You Lose.')
            print('End Gold: {0} End Health: {1} '.format(p1.totalGold(), p1.getHealth() ))
            sys.exit()



main()