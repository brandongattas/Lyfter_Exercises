import csv
from pathlib import Path

def export_students_to_csv(file_path, students_data):
    if not students_data:
        return
    
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

def import_students_from_csv_as_list_of_dicts(file_path):
    if not file_path.exists():
        return []
        
    students_list = []
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

def get_absolute_file_path(file_name):
	script_dir = Path(__file__).resolve().parent
	return script_dir / file_name