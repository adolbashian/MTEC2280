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
		print("You Died")
		return True

def resetJumps(inputA):
	inputA = 5

def reduceJumps(inputC):
	inputC -= 1
	return inputC

def Rewards(Jumper, RandomEvent):
	rwn = RNG()
	if(rwn == 0):
		print(RandomEvent['Rest'])
		Jumper = GlobalJump
		return Jumper
	if(rwn == 1):
		print(RandomEvent['RestoreA'])
		Jumper = Jumper + 1
		return Jumper
	if(rwn == 2):
		print(RandomEvent['BadLuck'])
		Jumper = Jumper - 1
		return Jumper
	else:
		print("No Rewards, Just a case of Bad Luck")
		return Jumper

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
			print("Game Over")
			aPlayer = False
			GlobalTruth = False
			return False

		if(cPlayerState == PlayerStates['Attack']):
				print("It's your Turn! Attack?")
				userInputB = input("(1/0)")
				
				if(userInputB == 1):
					rdmroll = RNG()

					if(rdmroll == 0):
						print("Missed Wyvern !")
						print("Jumps: %s remaining" % Jumps)
						print("\n")
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']
						time.sleep(2.5)

					if(rdmroll == 1):
						WyvernHP -= 1
						Jumps -= 1
						print("Hit Wyvern !")
						print("Jumps: %s remaining" % Jumps)
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 2):
						WyvernHP -= 3
						print("Critical Hit on Wyvern !")
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 3):
						WyvernHP -= 1
						Jumps -= 1
						print("Hit Wyvern !")
						print("Jumps: %s remaining" % Jumps)
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 4):
						WyvernHP -= 3
						print("Critical Hit on Wyvern !")
						print("Wyvern Health: %s remaining" % WyvernHP)
						print("\n")
						
						time.sleep(2.5)
						cPlayerState = PlayerStates['Rest']
						cWyvernState = WyvernStates['Attack']

					if(rdmroll == 5):
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
				print("Wyvern missed!")
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 1):
				print("Wyvern hit!")
				Jumps -= 1
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 2):
				print("Wyvern missed!")
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 3):
				print("Wyvern missed!")
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

			if(rdmroll == 4):
				print("Critical hit!")
				Jumps -= 4
				print("Jumps: %s remaining" % Jumps)
				print("Wyvern Health: %s remaining" % WyvernHP)
				print("\n")

				cPlayerState = PlayerStates['Attack']
				cWyvernState = WyvernStates['Rest']
			if(rdmroll == 5):
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
			on = false

		rdn = RNG()

		if(rdn == 0):
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
			print("You're walking")
			time.sleep(2.5)

		if(rdn == 3):
			print(LevelTwo['ChallengeC'])
			
			if(SJumps < 1):
				print("You Died")
				on = False
			else:
				print("Adversity: %s Passed" % terminus)
				print("Adversity: %s Remaining" % (goal - terminus))
				print("Jumps: %s remaining" % SJumps)
				print("\n")
				SJumps = reduceJumps(SJumps)
				terminus = terminus + 1
				time.sleep(2.5)

		if(rdn == 4):
			SJumps = Rewards(int(SJumps), RandomEvents)
			time.sleep(2.5)

		if(rdn == 5):
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

main()