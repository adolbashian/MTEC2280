import random
import time

GlobalJump = 7
GlobalTruth = True

def RNG():
	rng = random.randint(0,5)
	return rng

def isDead(inputB):
	if(inputB == 1):
		print("Continue")
		reduceJumps(inputB)
		return False
	if(inputB == 0):
		#SoundEffect - DEATH
		print("You Died")
		return True

def resetJumps(inputA):
	inputA = 5

def reduceJumps(inputC):
	inputC -= 1
	#SoundEffect - JUMPDOWN
	return inputC

def Rewards(Jumper, RandomEvent):
	rwn = RNG()
	if(rwn == 0):
		#SoundEffect - REST
		print(RandomEvent['Rest'])
		Jumper = GlobalJump
		return Jumper
	if(rwn == 1):
		#SoundEffect - Full Restore
		print(RandomEvent['RestoreA'])
		Jumper = Jumper + 1
		return Jumper
	if(rwn == 2):
		#SoundEffect - Bad Luck
		print(RandomEvent['BadLuck'])
		Jumper = Jumper - 1
		return Jumper
	else:
		#SoundEffect - DEATH
		print("No Rewards, Just a case of Bad Luck")
		return Jumper

def ClockBoost(value, clock):
	value = value + 2;
	print("Boost Value: %s" % value)
	clock = clock + value
	return clock 


def nextLevel(lvl):
	if(lvl == 0):
		LevelOne
	elif(lvl == 1):


	elif(lvl == 2):


def RabbitHole(jp, SLegs):
	RH = {'Diamonds' : "You are hit repeatedly with Arrows!", 'Hearts' : "You continue falling. . . . . . . . . .", 'Spades' : "You hit the floor", 'Clubs' : "You hit the ground, realizing your legs are stone!"}
	rwn = RNG() % 4
	
	if(rwn == 0):
		print("You fall. . .")
		time.sleep(2.5)
		print("You hear slithering, an ominous voice speaks")
		time.sleep(1.5)
		print("I will weigh your actions, justice or punishment")
		time.sleep(1.5)
		rt = RNG() % 2
		if(rt == 1 or rt == 0):
			print("Justice")
			time.sleep(1.0)
			jp = jp + 1
		if(rt == 2):
			print("Punishment")
			time.sleep(2.5)
			jp = jp - 1
		print("You realize you are in place, never having moved at all")
		time.sleep(2.5)

	if(rwn == 1):
		print(RH['Diamonds'])
		jp = jp - 3

	if(rwn == 2):
		print(RH['Hearts'])
		SLegs = True
		nextLevel()

	if(rwn == 3):
		print(RH['Spades'])

	if(rwn == 4):
		print(RH['Clubs'])
		print("You then trampolene, back to your original position")
		print("Your legs ache from hitting the ground")
		jp = jp - 1

def fightWyvern(jumps):
	PlayerStates = {'Rest' : 0, 'Attack' : 1}
	WyvernStates = {'Rest' : 0, 'Attack' : 1}

	cPlayerState = PlayerStates['Attack']
	cWyvernState = WyvernStates['Rest']

	WyvernHP = 7
	Jumps = jumps

	aPlayer = True
	aWyvern = True

	while(aPlayer == True or aWyvern == True):
		if (WyvernHP <= 0):
			aWyvern = False
			return True

		if(Jumps <= 0):
			#SoundEffect - DEATH
			print("Game Over")
			aPlayer = False
			GlobalTruth = False
			return False

		if(cPlayerState == PlayerStates['Attack']):
				#SoundEffect - DEATH
				print("It's your Turn! Attack?")
				userInputB = input("(1/0)")
				
				if(userInputB == 1):
					rdmroll = RNG()

					if(rdmroll == 0):
						#SoundEffect - DEATH
						print("Missed Wyvern !")
						print("Jumps: %s remaining" % Jumps)
						print("\n")
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']
						time.sleep(2.5)

					if(rdmroll == 1):
						WyvernHP -= 1
						Jumps -= 1
						#SoundEffect - DEATH
						print("Hit Wyvern !")
						print("Jumps: %s remaining" % Jumps)
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 2):
						WyvernHP -= 3
						#SoundEffect - DEATH
						print("Critical Hit on Wyvern !")
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 3):
						WyvernHP -= 1
						Jumps -= 1
						#SoundEffect - DEATH
						print("Hit Wyvern !")
						print("Jumps: %s remaining" % Jumps)
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 4):
						WyvernHP -= 3
						#SoundEffect - DEATH
						print("Critical Hit on Wyvern !")
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 5):
						#SoundEffect - DEATH
						print("Missed Wyvern !")
						print("Jumps: %s remaining" % Jumps)
						print("\n")

						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']
						time.sleep(2.5)


				elif(userInputB == 0):

					time.sleep(2.5)
					cPlayerState = PlayerStates['Rest']
					cWyvernState = WyvernStates['Attack']

		if(cWyvernState == WyvernStates['Attack']):
			rdmroll = RNG()

			if(rdmroll == 0):
				#SoundEffect - DEATH
				print("Wyvern missed!")
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 1):
				#SoundEffect - DEATH
				print("Wyvern hit!")
				Jumps -= 1
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 2):
				#SoundEffect - DEATH
				print("Wyvern missed!")
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 3):
				#SoundEffect - DEATH
				print("Wyvern missed!")
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

			if(rdmroll == 4):
				#SoundEffect - DEATH
				print("Critical hit!")
				Jumps -= 4
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 5):
				#SoundEffect - DEATH
				print("Wyvern Grazed!")
				Jumps -= 1
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']


def secondLevel():
	LevelTwo = {'ChallengeA' : "Stalagmite! Jump out of the way!", 'ChallengeB' : "A Doomba appears, do you jump on it", 'ChallengeC' : "Pitfall!", 'ChallengeD' : "A Wild Wyvern Appears!"}
	RandomEvents = {'Rest': "Your legs feel rested", 'RestoreA': "You can jump one more time",'Power': "Hit a Power Block! Temporary infinite jumps", 'BadLuck' : "You lost one jump"}
	
	on = True
	terminus = 0
	goal = 25
	SJumps = 15
	GlobalJump = SJumps

	print("Something wicked this way comes")
	print("As you grow stronger, the winds shall turn against you")
	print("\n")
	print("\n")
	time.sleep(2.5)

	while(on == True):
		if(terminus >= 25):
			print("You Win!")
			on = False

		rdn = RNG()

		if(rdn == 0):
			#SoundEffect - DEATH
			print(LevelTwo['ChallengeA'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)
			if(Dead == False):
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 1):
			#SoundEffect - DEATH
			print(LevelTwo['ChallengeB'])
			print("Jumps: %s remaining" % SJumps)
			

			if(SJumps < 1):
				print("You Died")
				on = False
			
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				terminus = terminus + 1
				print("Jumps: %s remaining" % SJumps)
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("\n")
				time.sleep(2.5)
				continue

			else:
				print("You Died")
				on = False

		if(rdn == 2):
			#SoundEffect - DEATH
			print("You're walking")
			time.sleep(2.5)

		if(rdn == 3):
			#SoundEffect - DEATH
			print(LevelTwo['ChallengeC'])
			
			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				#SoundEffect - DEATH
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Jumps: %s remaining" % SJumps)
				print("\n")
				SJumps = reduceJumps(SJumps)
				terminus = terminus + 1
				time.sleep(2.5)

		if(rdn == 4):
			#SoundEffect - DEATH
			SJumps = Rewards(int(SJumps), RandomEvents)
			time.sleep(2.5)

		if(rdn == 5):
			#SoundEffect - DEATH
			print(LevelTwo['ChallengeD'])
			terminus = terminus + 1
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("Jumps: %s remaining" % SJumps)
			print("\n")
			time.sleep(2.5)
			fightWyvern(SJumps)
			on = GlobalTruth

			
		else:
			print("You're Walking, yet still going backwards")
			time.sleep(2.5)

def levelThree():
	LevelTwo = {'ChallengeA' : "Stalagtite! Jump out of the way!", 'ChallengeB' : "A Doomba appears, do you jump on it", 'ChallengeC' : "Pitfall!"}
	RandomEvents = {'Rest': "Your legs feel rested", 'RestoreA': "You can jump one more time",'Power': "Hit a Power Block! Temporary infinite jumps", 'BadLuck' : "You lost one jump"}
	
	on = True
	stoneLegs = False;
	terminus = 0
	goal = 25
	SJumps = 15
	ceilingClock = 30
	GlobalJump = SJumps

	print("The Sky is falling")
	print("Run")
	print("\n")
	time.sleep(2.5)

	while(on == True):
		if(ceilingClock <= 0):
			print("Game Over, You were crushed by divine wrath")
			on = False
			break

		if(terminus >= 25):
			print("You Win!")
			on = False

		rdn = RNG()

		if(rdn == 0):
			ceilingClock = ClockBoost(RNG(),ceilingClock)
			print("Ceiling Time boosted: %s " % ceilingClock)
			time.sleep(2.5)

		if(rdn == 1):
			ceilingClock = ceilingClock - 1
			#SoundEffect - STALAGTITE
			print(LevelTwo['ChallengeA'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("Ceiling Time remaining: %s" % ceilingClock)
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				terminus = terminus + 1
				ceilingClock = ceilingClock - 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Ceiling Time remaining: %s" % ceilingClock)
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 2):
			#SoundEffect - DOOMBA
			ceilingClock = ceilingClock - 1
			print(LevelTwo['ChallengeB'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("Ceiling Time remaining: %s" % ceilingClock)
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				ceilingClock = ceilingClock - 1
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Ceiling Time remaining: %s" % ceilingClock)
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 3):
			#SoundEffect - PITTFALL
			ceilingClock = ceilingClock - 1
			print(LevelTwo['ChallengeC'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("Ceiling Time remaining: %s" % ceilingClock)
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				ceilingClock = ceilingClock - 1
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Ceiling Time remaining: %s" % ceilingClock)
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 4):
			ceilingClock = ceilingClock - 1
			RabbitHole(SJumps,False)
			print("Ceiling Time remaining: %s" % ceilingClock)
			time.sleep(2.5)
			

		if(rdn == 5):
			ceilingClock = ceilingClock - 1
			SJumps = Rewards(int(SJumps), RandomEvents)
			print("Ceiling Time remaining: %s" % ceilingClock)
			time.sleep(2.5)




def levelFour():
	LevelTwo = {'ChallengeA' : "Stalagmite! Jump out of the way!", 'ChallengeB' : "A Doomba appears, do you jump on it", 'ChallengeC' : "Pitfall!", 'ChallengeD' : "A Wild Wyvern Appears!"}
	RandomEvents = {'Rest': "Your legs feel rested", 'RestoreA': "You can jump one more time",'Power': "Hit a Power Block! Temporary infinite jumps", 'BadLuck' : "You lost one jump"}
	
	on = True
	terminus = 0
	goal = 25
	SJumps = 15
	GlobalJump = SJumps

	print("Salvation Lies near, Stay strong")
	print("\n")
	time.sleep(2.5)


	while(on == True):
		if(terminus >= 25):
			print("You Win!")
			on = False

		rdn = RNG()
		if(rdn == 0):
			time.sleep(2.5)

		if(rdn == 1):
			#SoundEffect - STALAGTITE
			print(LevelTwo['ChallengeA'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 2):
			#SoundEffect - DOOMBA
			print(LevelTwo['ChallengeB'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 3):
			#SoundEffect - PITTFALL
			print(LevelTwo['ChallengeC'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False

			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 4):
			RabbitHole(SJumps,False)
			time.sleep(2.5)
			
		if(rdn == 5):
			SJumps = Rewards(int(SJumps), RandomEvents)
			time.sleep(2.5)

		if(terminus >= 25):
			print("You Win!")
			on = false

		rdn = RNG()


def levelFive():
	LevelTwo = {'ChallengeA' : "Stalagmite! Jump out of the way!", 'ChallengeB' : "A Doomba appears, do you jump on it", 'ChallengeC' : "Pitfall!", 'ChallengeD' : "A Wild Wyvern Appears!"}
	RandomEvents = {'Rest': "Your legs feel rested", 'RestoreA': "You can jump one more time",'Power': "Hit a Power Block! Temporary infinite jumps", 'BadLuck' : "You lost one jump"}
	
	on = True
	terminus = 0
	goal = 25
	SJumps = 15
	GlobalJump = SJumps

	print("It Ends")
	print("\n")
	time.sleep(2.5)

	while(on == True):
		if(terminus >= 25):
			print("You Win!")
			on = False

		rdn = RNG()

		if(rdn == 0):
			ceilingClock = ClockBoost(RNG(),ceilingClock)
			print("Ceiling Time boosted: %s " % ceilingClock)
			time.sleep(2.5)

		if(rdn == 1):
			#SoundEffect - STALAGTITE
			print(LevelTwo['ChallengeA'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("Ceiling Time remaining: %s" % ceilingClock)
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Ceiling Time remaining: %s" % ceilingClock)
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 2):
			#SoundEffect - DOOMBA
			print(LevelTwo['ChallengeB'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("Ceiling Time remaining: %s" % ceilingClock)
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Ceiling Time remaining: %s" % ceilingClock)
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 3):
			#SoundEffect - PITTFALL
			print(LevelTwo['ChallengeC'])
			print("Jumps: %s remaining" % SJumps)
			print("Adversity: %s Passed" % terminus)
			print("Adversity: %s Remaining" % (goal - terminus))
			print("Ceiling Time remaining: %s" % ceilingClock)
			print("\n")

			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				userInputB = input("(1/0)")
				time.sleep(2.5)
				SJumps = reduceJumps(SJumps)
				Dead = isDead(userInputB)

			if(Dead == False):
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Ceiling Time remaining: %s" % ceilingClock)
				print("\n")
				time.sleep(2.5)
				continue

		if(rdn == 4):
			RabbitHole(SJumps,False)
			print("Ceiling Time remaining: %s" % ceilingClock)
			time.sleep(2.5)
			

		if(rdn == 5):
			SJumps = Rewards(int(SJumps), RandomEvents)
			print("Ceiling Time remaining: %s" % ceilingClock)
			time.sleep(2.5)
			
		if(terminus >= 25):
			print("You Win!")
			on = false

		rdn = RNG()

def Credits():
	cred = {}

def main():
	LevelOne = {'ChallengeA' : "There is a pipe ahead, would you like to enter?", 'ChallengeB' : "A Doomba appears, do you jump on it", 'ChallengeC' : "There's Lava!"}
	RandomEvents = {'Rest': "Your legs feel rested", 'RestoreA': "You can jump one more time",'Power': "Hit a Power Block! Temporary infinite jumps", 'BadLuck' : "You lost one jump"}
	
	on = True
	terminus = 0
	goal = 5
	Jumps = 7
	GlobalJump = Jumps
	print("Welcome to JumpnDie")
	userInput = input("Would you like to play? (1/0)")


	if(int(userInput) == 1):
		print("Starting")
		#on = False #for Debugging
		while(on == True):

			if(terminus >= 5):
				print("You Win!")
				print("\n")
				time.sleep(2.5)
				secondLevel()

			rdn = RNG()

			if(rdn == 0):
				print(LevelOne['ChallengeA'])
				userInputB = input("(1/0)")
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("\n")
				time.sleep(1.5)

			if(rdn == 1):
				print(LevelOne['ChallengeB'])
				print("Jumps: %s remaining" % Jumps)
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("\n")

				if(Jumps <= 0):
					print("You Died")
					on = False

				else:
					userInputB = input("(1/0)")
					if(userInputB == 1):	
						time.sleep(1.5)
						Jumps = reduceJumps(Jumps)
						Dead = isDead(userInputB)
					if(userInputB == 0):
						print("You Died")
						on = False

				if(Dead == False):
					terminus = terminus + 1
					print("Adversity: %s Passed" % terminus)
					print("Adversity: %s Remaining" % (goal - terminus))
					print("\n")
					continue

				else:
					print("You Died")
					print("\n")
					print("\n")
					on = False

			if(rdn == 2):
				print("You're walking")
				terminus = terminus + 1
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Jumps: %s remaining" % Jumps)
				print("\n")
				time.sleep(1.5)

			if(rdn == 3):
				print(LevelOne['ChallengeC'])
				print("\n")

				if(Jumps <= 0):
					print("You Died")
					on = False
				else:
					Jumps = reduceJumps(Jumps)
					terminus = terminus + 1
					print("Adversity: %s Passed" % terminus)
					print("Adversity: %s Remaining" % (goal - terminus))
					print("Jumps: %s remaining" % Jumps)
					print("\n")

					time.sleep(1.5)

			if(rdn == 4):
				Jumps = Rewards(int(Jumps), RandomEvents)
				time.sleep(1.5)

			if(rdn == 5):
				Jumps = Rewards(int(Jumps), RandomEvents)
				time.sleep(1.5)
			
			else:
				print("You're Walking, yet still going backwards")
				print("\n")
				time.sleep(1.5)


	elif(int(userInput) == 0):
		print("Maybe some other time")
		on = False

	elif(int(userInput) == 3):
		print("DEBUG LEVEL SELECTOR")
		print("Valid Inputs: 1, 2, 3, 4, 5")
		uimp = input("Input a Level Value")
		if(uimp == 1):
			LevelOne()
		elif(uimp == 2):
			LevelTwo()

		elif(uimp == 3):
			levelThree()

		elif(uimp == 4):
			levelFour()

		elif(uimp == 5):
			levelFive()


main()