import actions
import data

def view_registered_students_details(students_list):
	print("### View recent registered students: ###")
	print("")

	if not students_list:
		print("There are no registered students.")
	else:
		for student in students_list:
			print(f"Student full name: {student['student_name']}")
			print(f"Section: {student['student_section']}")
			print(f"Spanish class score: {student['scores']['spanish']}")
			print(f"English class score: {student['scores']['english']}")
			print(f"Social Studies score: {student['scores']['social']}")
			print(f"Science class score: {student['scores']['science']}")
			print("------------")

def view_top_three_students_highest_avg_notes(students_list):
	print("### View Top 3 with highest average score.")
	top_three_students_with_highest_avg_score=sorted(
		students_list,
		key=lambda student: actions.get_avg_from_dict(student['scores']),
		reverse=True
	)[:3]

	print("Top 3 Students by Average Score:")
	for student in top_three_students_with_highest_avg_score:
		avg_score = actions.get_avg_from_dict(student['scores'])
		print(f"Name: {student['student_name']} | Average: {avg_score:.2f}")

def collect_student_details_get_list_of_dict():
	print("### Register students and scores.")
	qty_games=actions.ask_for_int("Enter the quantity of students that will be registering: ")
	counter=1
	students_list=[]
	while counter<=qty_games:
		print("")
		print(f"Enter Student #{counter} details:")
		student_full_name=input("Enter the student's full name: ")
		student_section=input(f"Enter the section (Ex. 11B): ")
		spanish_score=actions.ask_for_score("Enter the Spanish class score: ")
		english_score=actions.ask_for_score("Enter the English class score: ")
		social_score=actions.ask_for_score("Enter the Social Studies class score: ")
		science_score=actions.ask_for_score("Enter the Science class score: ")
		students_dict={
			'student_name':student_full_name,
			'student_section':student_section,
			'scores':{
				'spanish':spanish_score,
				'english':english_score,
				'social':social_score,
				'science':science_score
			}
		}
		students_list.append(students_dict)
		counter+=1
	return students_list

def view_overall_average(students_list):
	print("### View average score overall among all students.")
	print("")
	
	if not students_list:
		print("There are no registered students/scores.")
		return
	
	avgs_list=[]
	for student in students_list:
		avgs_list.append(actions.get_avg_from_dict(student['scores']))
	
	overal_avg = actions.get_avg_from_list(avgs_list)
	print(f"The overall average across all students is: {overal_avg:.2f}") #.2f will show only 2 decimal Ex. 78.25 not 78.255555

def export_to_csv(students_list):
	print("")
	if not students_list:
		print("There are no registered students to export.")
		return
	
	file_name = input("Enter file name to be saved (Ex. students): ")

	if not file_name.endswith('.csv'):
		file_name += '.csv'
		
	file_path = data.get_absolute_file_path(file_name)
	data.export_students_to_csv(file_path, students_list)
	print(f"Students successfully exported to {file_name}")

def import_from_csv(students_list):
	print("")
	file_name = input("Enter file name to be imported (Ex. students): ")

	if not file_name.endswith('csv'):
		file_name += '.csv'
	
	file_path = data.get_absolute_file_path(file_name)
	imported_data = data.import_students_from_csv_as_list_of_dicts(file_path)
	
	if not imported_data:
		print(f"There are no CSV file previously exported with that name: {file_name}")
		return
	
	students_list.clear()
	students_list.extend(imported_data)

	print(f"Successfully imported {len(imported_data)} student(s) from {file_name}")


def view_menu_options():
	menu={
			1:'Register students and scores.',
			2:'View recent registered students',
			3:'View Top 3 with highest average score.',
			4:'View average score overall among all students.',
			5:'Export registered students to CSV file.',
			6:'Import registered students from CSV file.',
			0:'Exit'
	}
	for key,value in menu.items():
		print(f"{key} - {value}")
	print("")

def handle_menu_choice(picked_menu_option, students_list):
	menu_actions = {
		1: lambda: students_list.extend(collect_student_details_get_list_of_dict()),
		2: lambda: view_registered_students_details(students_list),
		3: lambda: view_top_three_students_highest_avg_notes(students_list),
		4: lambda: view_overall_average(students_list),
		5: lambda: export_to_csv(students_list),
		6: lambda: import_from_csv(students_list)
	}
	selected_action = menu_actions.get(picked_menu_option)
	
	if selected_action:
		selected_action()
	else:
		print("Invalid option. Please choose a valid number from the menu.")