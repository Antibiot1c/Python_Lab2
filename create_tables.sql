CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER PRIMARY KEY,
    group_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(group_id)
);

INSERT INTO groups (group_name) VALUES ('Група А1');

INSERT INTO students (student_name, group_id) VALUES ('Генадий Гена', 1);

DELETE FROM groups WHERE group_id = 1;

DELETE FROM students WHERE student_id = 1;

UPDATE students SET student_name = 'Арсен' WHERE student_id = 1;

SELECT * FROM groups;

SELECT * FROM students WHERE group_id = 1;
