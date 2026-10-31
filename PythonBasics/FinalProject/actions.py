def ask_for_int(prompt_message):
	while True:
		try:
			return int(input(prompt_message))
		except ValueError:
			print("Invalid input. Please enter a whole number.")

def ask_for_score(prompt_message):
	while True:
		try:
			value = float(input(prompt_message))

			if 0<= value <=100:
				return value
			else:
				print("Error: The number must be between 0 and 100.")
		except ValueError:
			print("Invalid input. Please enter number using decimals Ex. 6.0")

def ask_for_menu_option():
	while True:
		try:
			value = int(input("Enter a menu option: "))
			print("")

			if 0<= value <=6:
				return value
			else:
				print("Error: The number must be between 0 and 6.")
		except ValueError:
			print("Invalid input. Please enter number from the menu options.")

def get_avg_from_dict(my_dict):
    if not my_dict:
        return 0.0
    return sum(my_dict.values()) / len(my_dict)

def get_avg_from_list(my_list):
	if not my_list:
		return 0.0
	return sum(my_list) / len(my_list)