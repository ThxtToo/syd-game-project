import random


def rock_paper_or_scissors():
	rps_list = ['"rock"', '"paper"', '"scissors"']
	count = 0
	infinite = True
	print("\n---Welcome to the game of rock, paper, scissors.---\n")
	print("Hello, my name is Syd and you will be playing against me.")
	print("\nChoose rock, paper or scissors")

	while infinite == True:
		user = str(input("\n-----> "))
		for i in range(1):

			#statement for rock
			if all(c in 'rock' for c in user):
				syd = random.choice(rps_list)

				if syd == '"rock"':
					print("\nSyd chose", syd, "= Draw!")
					break

				elif syd == '"paper"':
					print("\nSyd chose", syd, "--> Syd won!")
					break

				elif syd == '"scissors"':
					print("\nSyd chose", syd, "--> You won!")
					break

			#statement for paper
			if all(c in 'paper' for c in user):
				syd = random.choice(rps_list)

				if syd == '"rock"':
					print("\nSyd chose", syd, "--> You won!")
					break

				elif syd == '"paper"':
					print("\nSyd chose", syd, "= Draw!")
					break

				elif syd == '"scissors"':
					print("\nSyd chose", syd, "--> Syd won!")
					break

			#statement for scissors
			if all(c in 'scissors' for c in user):
				syd = random.choice(rps_list)

				if syd == '"rock"':
					print("\nSyd chose", syd, "--> Syd won!")
					break

				elif syd == '"paper"':
					print("\nSyd chose", syd, "--> You won!")
					break

				elif syd == '"scissors"':
					print("\nSyd chose", syd, "= Draw!")
					break

			#exit for invalid input
			else:
				print("\nInvalid input.\n")

#::==================================================================================================

def heads_or_tails():
	heads_or_tails_list = ['"heads"', '"tails"']

	print("\n---Welcome to the game of heads or tails.---\n")
	print("Hello, my name is Syd and you will be playing against me.")
	print("Choose heads or tails")

	while True:
		user = str(input("\n-----> "))
		for i in range(1):

			if all(c in 'heads' for c in user):
				syd = random.choice(heads_or_tails_list)

				if syd == '"heads"':
					print("\nHas fallen", syd, "--> You won")

				elif syd == '"tails"':
					print("\nHas fallen", syd, "--> Syd won")

			elif all(c in 'tails' for c in user):
				syd = random.choice(heads_or_tails_list)

				if syd == '"tails"':
					print("\nHas fallen", syd, "--> You won")

				elif syd == '"heads"':
					print("\nHas fallen", syd, "--> Syd won")

			else:
				print("Error")




print("1 = Rock, Paper or Scissors\n2 = Heads or Tails")
game = input("\nEscoge el juego: ")
if game == "1":
	rock_paper_or_scissors()
elif game == "2":
	heads_or_tails()


