import re
from students import Student

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

def ask_for_true_or_false(prompt_message):
	while True:
		user_input=input(prompt_message)
		user_input = user_input.lower()
		if user_input in ('y','yes'):
			return True
		elif user_input in ('n','no'):
			return False

def get_avg_from_list(my_list):
	if not my_list:
		return 0.0
	return sum(my_list) / len(my_list)

def ask_student_name():
	while True:
		name=input("Enter the student's full name: ").strip()

		if not name:
			print("[ERROR]: The name cannot be empty!")
			continue

		if name_has_numbers(name):
			print("[ERROR]: The name cannot contain numbers!")
			continue

		return name.title()

def name_has_numbers(name):
	return any(char.isdigit() for char in name)

def student_exists_in_section(name, section, students_list):
    for student in students_list:
        if (name.lower() == student.name.lower() and 
            section.lower() == student.section.lower()):
            return True
    return False

def ask_student_section():
    while True:
        section = input("Enter the section (Ex. 11B, max 1000): ").strip()

        if not section:
            print("[ERROR]: Section cannot be empty!")
            continue

        if not re.match(r"^\d+[a-zA-Z]+$", section):
            print("[ERROR]: Section must start with numbers followed by a letter (Ex. 11B).")
            continue

        number_part = int(re.match(r"\d+", section).group())

        if not (1 <= number_part <= 1000):
            print("[ERROR]: The section number must be between 1 and 1000!")
            continue

        return section.upper()

def collect_student_details_and_create_objects(students_list):
	print("### Register students and scores.")
	student_quantity=ask_for_int("Enter the quantity of students that will be registering: ")
	counter=1

	while counter<=student_quantity:
		print("")
		print(f"Enter Student #{counter} details:")
		student_full_name=ask_student_name()
		student_section=ask_student_section()
		if student_exists_in_section(student_full_name, student_section, students_list):
			print(f"[ERROR]: A student named '{student_full_name}' is already registered in section '{student_section.upper()}'.")
			continue
		spanish_score=ask_for_score("Enter the Spanish class score: ")
		english_score=ask_for_score("Enter the English class score: ")
		social_score=ask_for_score("Enter the Social Studies class score: ")
		science_score=ask_for_score("Enter the Science class score: ")
		counter+=1
		students_list.append(
			Student(student_full_name, student_section, spanish_score, english_score, social_score, science_score)
		)


def view_overall_average(students_list):
	print("### View average score overall among all students.")
	print("")
	
	if not students_list:
		print("There are no registered students/scores.")
		return
	
	avgs_list=[]
	for student in students_list:
		scores = [
			student.spanish_score,
			student.english_score,
			student.social_score,
			student.science_score
		]
		student_avg = get_avg_from_list(scores)
		avgs_list.append(student_avg)
	
	overall_avg = get_avg_from_list(avgs_list)
	print(f"The overall average across all students is: {overall_avg:.2f}") #.2f will show only 2 decimal Ex. 78.25 not 78.255555


def view_top_three_students_highest_avg_notes(students_list):
	print("### View Top 3 with highest average score.")
	top_three_students_with_highest_avg_score=sorted(
		students_list,
		key=lambda s: get_avg_from_list([s.spanish_score, s.english_score, s.social_score, s.science_score]),
		reverse=True
	)[:3]

	print("Top 3 Students by Average Score:")
	for student in top_three_students_with_highest_avg_score:
		student_score = [
			student.spanish_score,
            student.english_score,
            student.social_score,
            student.science_score
		]
		avg_score = get_avg_from_list(student_score)
		print(f"Name: {student.name} | Average: {avg_score:.2f}")


def view_registered_students_details(students_list):
	print("### View recent registered students: ###")
	print("")

	if not students_list:
		print("There are no registered students.")
	else:
		for student in students_list:
			print(f"Student full name: {student.name}")
			print(f"Section: {student.section}")
			print(f"Spanish class score: {student.spanish_score}")
			print(f"English class score: {student.english_score}")
			print(f"Social Studies score: {student.social_score}")
			print(f"Science class score: {student.science_score}")
			print("------------")


def delete_student(students_list):
	print("### Delete student ###")
	print("")

	if not students_list:
		print("There are no registered students to remove.")
		return

	student_name_to_delete=input("Enter the name of the student to delete: ").strip().lower()
	student_section=input("Enter the student's section: ").strip().lower()
	found = False

	target_student = None
	for student in students_list:
		if student.name.lower()==student_name_to_delete and student.section.lower()==student_section:
			target_student=student
			break

	if target_student:
		if ask_for_true_or_false("Student found! - Please confirm if you want to remove the student (yes/no): "):
			students_list.remove(target_student)
			print(f"Successfully removed: {target_student.name} on section: {target_student.section}")
		else:
			print(f"Deletion aborted!")
	else:
		print(f"Could not find a student named: {student_name_to_delete} on section: {student_section}")


def view_failed_students(students_list):
	print("### View failed students ###")
	print("")

	if not students_list:
		print("There are no registered students to view.")
		return

	atleast_one_failed_found=False

	for student in students_list:
		subjects_and_scores = {
			"Spanish": student.spanish_score,
			"English": student.english_score,
			"Social Studies": student.social_score,
			"Science": student.science_score
		}
		
		for subject, score in subjects_and_scores.items():
			if score < 60:
				atleast_one_failed_found = True
				print(f"Student name: {student.name} | Section: {student.section} | Failed subject: {subject} (Score: {score})")

	if not atleast_one_failed_found:
		print(f"No students have failed any subject. Excellent performance overall!")