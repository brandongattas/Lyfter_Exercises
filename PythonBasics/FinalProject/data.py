import csv
from pathlib import Path

def export_students_to_csv(file_path, students_data):
	if not students_data:
		return False

	try:
		flattened_data = []
		for student in students_data:
			flat_student = {
				'student_name': student['student_name'],
				'student_section': student['student_section'],
				'spanish': student['scores']['spanish'],
				'english': student['scores']['english'],
				'social': student['scores']['social'],
				'science': student['scores']['science']
			}
			flattened_data.append(flat_student)

		with file_path.open('w', encoding='utf-8', newline='') as file:
			headers = flattened_data[0].keys()
			writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
			writer.writeheader()
			writer.writerows(flattened_data)
		return True
	except PermissionError:
		print(f"[Error] Permission denied. Please ensure the file is closed in Excel or other programs.")
		return False
	except OSError as e:
		print(f"[Error] An OS error ocurred while saving the file: {e}")

def import_students_from_csv_as_list_of_dicts(file_path):
	if not file_path.exists():
		return []
		
	students_list = []
	try:
		with file_path.open('r', encoding='utf-8') as file:
			reader = csv.DictReader(file, delimiter='\t')
			
			for row in reader:
				student_dict = {
					'student_name': row['student_name'],
					'student_section': row['student_section'],
					'scores': {
						'spanish': float(row['spanish']),
						'english': float(row['english']),
						'social': float(row['social']),
						'science': float(row['science'])
					}
				}
				students_list.append(student_dict)
			
		return students_list
	
	except PermissionError:
		print("[Error] Permission denied when trying to read the file.")
		return None
	except (KeyError, ValueError) as e:
		print(f"[Error] The CSV file is corrupted, missing columns, or contains invalid score numbers. Details: {e}")
		return None
	except OSError as e:
		print(f"[Error] An OS error ocurred while reading the file: {e}")
		return None
	

def get_absolute_file_path(file_name):
	script_dir = Path(__file__).resolve().parent
	return script_dir / file_name


def import_from_csv(students_list):
	print("")
	file_name = input("Enter file name to be imported (Ex. students): ")

	if not file_name.endswith('csv'):
		file_name += '.csv'
	
	file_path = get_absolute_file_path(file_name)

	if not file_path.exists():
		print(f"There is no CSV file previously exported with that name: {file_name}")
		return
	
	imported_data = import_students_from_csv_as_list_of_dicts(file_path)

	if imported_data is None:
		return
	
	if not imported_data:
		print(f"The file '{file_name}' is empty.")
		return
	
	students_list.clear()
	students_list.extend(imported_data)

	print(f"Successfully imported {len(imported_data)} student(s) from {file_name}")


def export_to_csv(students_list):
	print("")
	if not students_list:
		print("There are no registered students to export.")
		return
	
	file_name = input("Enter file name to be saved (Ex. students): ")
	if not file_name.endswith('.csv'):
		file_name += '.csv'
		
	file_path = get_absolute_file_path(file_name)

	try:
		success = export_students_to_csv(file_path, students_list)

		if success:
			print(f"Students successfully exported to {file_name}")
		else:
			print(f"Export failed for {file_name}.")
			
	except Exception as e:
		print(f"\n[Error] An unexpected error occurred while exporting: {e}")