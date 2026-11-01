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

def collect_student_details_get_list_of_dict():
	print("### Register students and scores.")
	student_quantity=ask_for_int("Enter the quantity of students that will be registering: ")
	counter=1
	students_list=[]
	while counter<=student_quantity:
		print("")
		print(f"Enter Student #{counter} details:")
		student_full_name=input("Enter the student's full name: ")
		student_section=input(f"Enter the section (Ex. 11B): ")
		spanish_score=ask_for_score("Enter the Spanish class score: ")
		english_score=ask_for_score("Enter the English class score: ")
		social_score=ask_for_score("Enter the Social Studies class score: ")
		science_score=ask_for_score("Enter the Science class score: ")
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
		avgs_list.append(get_avg_from_dict(student['scores']))
	
	overall_avg = get_avg_from_list(avgs_list)
	print(f"The overall average across all students is: {overall_avg:.2f}") #.2f will show only 2 decimal Ex. 78.25 not 78.255555


def view_top_three_students_highest_avg_notes(students_list):
	print("### View Top 3 with highest average score.")
	top_three_students_with_highest_avg_score=sorted(
		students_list,
		key=lambda student: get_avg_from_dict(student['scores']),
		reverse=True
	)[:3]

	print("Top 3 Students by Average Score:")
	for student in top_three_students_with_highest_avg_score:
		avg_score = get_avg_from_dict(student['scores'])
		print(f"Name: {student['student_name']} | Average: {avg_score:.2f}")


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