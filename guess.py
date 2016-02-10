import sys

filename = sys.argv[0]
guess = sys.argv[1]

print(type(guess))
converGuess = int(guess)
intGuess = int(guess)



answer = 12345


if(intGuess == answer):
	print("You won!")

if(intGuess != answer):
	print("LOSER!!!")