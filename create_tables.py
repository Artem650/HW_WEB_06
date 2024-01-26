from psycopg2 import DatabaseError
from connection import create_connection
import logging

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except DatabaseError as err:
        print(err)


if __name__ == '__main__':


    create_group_table = """drop table if exists groups CASCADE;
    CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
    );"""


    create_students_table = """drop table if exists students CASCADE;
    CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL,
    group_id INTEGER REFERENCES groups(id)
  	on delete cascade
    );"""


    create_teachers_table = """drop table if exists teachers CASCADE;
    CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL
    );"""


    create_subjects_table = """drop table if exists subjects CASCADE;
    CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(175) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
  	on delete cascade
    );"""


    create_grades_table = """drop table if exists grades CASCADE;
    CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id)
    on delete cascade,
    subject_id INTEGER REFERENCES subjects(id)
    on delete cascade,
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    grade_date DATE NOT NULL
    );"""

    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, create_group_table)
                create_table(conn, create_students_table)
                create_table(conn, create_teachers_table)
                create_table(conn, create_subjects_table)
                create_table(conn, create_grades_table)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)