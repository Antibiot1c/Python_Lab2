def add_group(group_name):
    cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group_name,))
    conn.commit()
    print(f"Група '{group_name}' успішно додана.")

def add_student(student_name, group_id):
    cursor.execute('INSERT INTO students (student_name, group_id) VALUES (?, ?)', (student_name, group_id))
    conn.commit()
    print(f"Студент '{student_name}' успішно доданий до групи.")

def delete_group(group_id):
    cursor.execute('DELETE FROM groups WHERE group_id = ?', (group_id,))
    conn.commit()
    print(f"Група з ID {group_id} успішно видалена.")

def delete_student(student_id):
    cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()
    print(f"Студент з ID {student_id} успішно видалений.")

def update_student_name(student_id, new_name):
    cursor.execute('UPDATE students SET student_name = ? WHERE student_id = ?', (new_name, student_id))
    conn.commit()
    print(f"Ім'я студента з ID {student_id} оновлено на '{new_name}'.")

def list_groups():
    cursor.execute('SELECT * FROM groups')
    groups = cursor.fetchall()
    if groups:
        print("Список груп:")
        for group in groups:
            print(f"ID - {group[0]}, Назва - {group[1]}")
    else:
        print("Груп не знайдено.")

def list_students_in_group(group_id):
    cursor.execute('SELECT * FROM students WHERE group_id = ?', (group_id,))
    students = cursor.fetchall()
    if students:
        print(f"Студенти у групі з ID {group_id}:")
        for student in students:
            print(f"ID - {student[0]}, Ім'я - {student[1]}")
    else:
        print(f"Студентів у групі з ID {group_id} не знайдено.")

add_group('Група A1')
add_student('Генадий Гена', 2)
list_groups()
list_students_in_group(1)
update_student_name(2, 'Арсен')
delete_student(1)
delete_group(1)

conn.close()
