import actions
import data


def ask_for_menu_option():
	while True:
		try:
			value = int(input("Enter a menu option: "))
			print("")

			if 0<= value <=8:
				return value
			else:
				print("Error: The number must be between 0 and 8.")
		except ValueError:
			print("Invalid input. Please enter number from the menu options.")


def view_menu_options():
	menu={
			1:'Register students and scores.',
			2:'View recent registered students',
			3:'View Top 3 with highest average score.',
			4:'View average score overall among all students.',
			5:'Export registered students to CSV file.',
			6:'Import registered students from CSV file.',
			7:'Delete student.',
			8:'View failed students.',
			0:'Exit'
	}
	for key,value in menu.items():
		print(f"{key}. {value}")
	print("")


def handle_menu_choice(picked_menu_option, students_list):
	menu_actions = {
		1: lambda: actions.collect_student_details_and_create_objects(students_list),
		2: lambda: actions.view_registered_students_details(students_list),
		3: lambda: actions.view_top_three_students_highest_avg_notes(students_list),
		4: lambda: actions.view_overall_average(students_list),
		5: lambda: data.export_to_csv(students_list),
		6: lambda: data.import_from_csv(students_list),
		7: lambda: actions.delete_student(students_list),
		8: lambda: actions.view_failed_students(students_list)
	}
	selected_action = menu_actions.get(picked_menu_option)
	
	if selected_action:
		selected_action()
	else:
		print("Invalid option. Please choose a valid number from the menu.")