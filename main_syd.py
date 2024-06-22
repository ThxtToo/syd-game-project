import random


def rock_paper_scissors():
	rps_list = ['"rock"', '"paper"', '"scissors"']
	count = 0
	infinite = True
	print("---Welcome to the game of rock, paper, scissors.---\n")
	print("Hello, my name is Syd and you will be playing against me.")

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
				print("\nSea serio\n")


rock_paper_scissors()



