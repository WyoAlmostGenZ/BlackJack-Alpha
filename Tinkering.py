import random
game_is_on = True
cards = [11, 10, 10, 10, 2, 3, 4, 5, 6, 7, 8, 9]


def deal_card():
	random_card = random.choice(cards)
	return random_card


user_cards = []
computer_cards = []

for i in range(0, 2):
	user_cards.append(deal_card())

for i in range(0, 1):
	computer_cards.append(deal_card())



def computer():
	sum_of_user_score = sum(user_cards)
	sum_of_cpu_score = sum(computer_cards)
	if 11 in user_cards and sum_of_user_score > 21:
		user_cards.remove(11)
		user_cards.append(1)
	if 11 in computer_cards and sum_of_cpu_score > 21:
		computer_cards.remove(11)
		computer_cards.append(1)
		if 11 in computer_cards and sum_of_cpu_score <= 17:
			computer_cards.append(deal_card())
	if sum(user_cards) == sum(computer_cards):
		print("Draw check")
	elif sum(computer_cards) == 21 and sum(user_cards) < 21:
		print("Black jack check cpu")
	elif sum(user_cards) == 21 and sum(computer_cards) < 21:
		print("Blackjack check user")
	elif sum(user_cards) == 21 and sum(computer_cards) > 21:
		print("black jakk check user")
	elif sum(computer_cards) > 21 and sum(user_cards) < 21:
		print("User wins !")
	elif sum(computer_cards) > sum(user_cards):
		print("computer wins ")
	elif sum(user_cards) > sum(computer_cards):
		print("user wins !")




def game():
	user_sum = sum(user_cards)
	cpu_card = sum(computer_cards)
	if 11 in user_cards and user_sum > 21:
		user_cards.remove(11)
		user_cards.append(1)
	print(f"Your cards {user_cards} the score is {user_sum}")
	print(f"Computer cards {computer_cards}")

	inputeroni = input("1Do you wish to draw another card ?")

	if inputeroni == "y":
		user_cards.append(deal_card())
		sum_of_inputeroni = sum(user_cards)
		if 11 in user_cards and sum_of_inputeroni > 21:
			user_cards.remove(11)
			user_cards.append(1)
			print(f"Your score is {sum_of_inputeroni} do you wish to draw or stand")
		elif sum_of_inputeroni > 21:
			print(f"You Lose , you've gone over 21 , don't ever play in a casino this game is rigged {user_cards}")
		else:
			inputeroni1 = input(f"2Do you wish to Draw or Stand\n"
								f"Your cards : {user_cards} the sum -> {sum_of_inputeroni}\n"
								f"Computer cards : {computer_cards}")
			if inputeroni1 == "y":
				user_cards.append(deal_card())
				sum_of_inputeroni1 = sum(user_cards)
				if 11 in user_cards and sum_of_inputeroni1 > 21:
					user_cards.remove(11)
					user_cards.append(1)
					print(f"Your score is {sum_of_inputeroni1} do you wish to draw or stand")
				elif sum_of_inputeroni1 > 21:
					print("You Lose , you've gone over 21 , don't ever play in a casino this game is rigged")
				else:
					inputeroni2 = input(f"2Do you wish to Draw Another card or do u want to stand on {user_cards}\n"
										f"Your cards : {user_cards} the sum -> {sum_of_inputeroni1}\n"
										f"Computer cards : {computer_cards}")
					if inputeroni2 == "y":
						user_cards.append(deal_card())
						sum_of_inputeroni2 = sum(user_cards)
						if 11 in user_cards and sum_of_inputeroni2 > 21:
							user_cards.remove(11)
							user_cards.append(1)
							print(f"Your score is {sum_of_inputeroni2} do you wish to draw or stand")
						elif sum_of_inputeroni2 > 21:
							print("You Lose , you've gone over 21 , don't ever play in a casino this game is rigged")
						else:
							inputeroni3 = input(
								f"2Do you wish to Draw Another card or do u want to stand on {user_cards}\n"
								f"Your cards : {user_cards} the sum -> {sum_of_inputeroni2}\n"
								f"Computer cards : {computer_cards}")

					else:
						cpu_on = True
						while cpu_on:
							sum_of_cpu = sum(computer_cards)
							computer_cards.append(deal_card())
							sum_of_cpu2 = sum(computer_cards)
							sum_of_cpu3 = sum(computer_cards) - 10
							if 11 in computer_cards and sum_of_cpu2 > 21:
								print(f"Computer cards {computer_cards} the score is {sum_of_cpu3}")
								computer()
								break
							elif sum_of_cpu2 >= 17:
								print(f"Computer card's {computer_cards} the score is {sum_of_cpu2}")
								computer()
								break

			else:
				cpu_on = True
				while cpu_on:
					sum_of_cpu = sum(computer_cards)
					computer_cards.append(deal_card())
					sum_of_cpu2 = sum(computer_cards)
					sum_of_cpu3 = sum(computer_cards) - 10
					if 11 in computer_cards and sum_of_cpu2 > 21:
						print(f"Computer cards {computer_cards} the score is {sum_of_cpu3}")
						computer()
						break
					elif sum_of_cpu2 >= 17:
						print(f"Computer card's {computer_cards} the score is {sum_of_cpu2}")
						computer()
						break
# ELSE = IF INPUT == "no" or anything else
	else:
		cpu_on = True
		while cpu_on:
			sum_of_cpu = sum(computer_cards)
			computer_cards.append(deal_card())
			sum_of_cpu2 = sum(computer_cards)
			sum_of_cpu3 = sum(computer_cards) - 10
			if 11 in computer_cards and sum_of_cpu2 > 21:
				print(f"Computer cards {computer_cards} the score is {sum_of_cpu3}")
				computer()
				break
			elif sum_of_cpu2 >= 17:
				print(f"Computer card's {computer_cards} the score is {sum_of_cpu2}")
				computer()
				break



game()
