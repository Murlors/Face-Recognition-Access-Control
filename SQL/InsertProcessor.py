import asyncio

import psycopg2

from SQL import ConnectionPool


class InsertProcessor:
    def __init__(self):
        # 与连接池连接
        self.conn_pool = ConnectionPool().conn_pool

    async def run_insert(self, sql):
        # 从连接池中获取一个连接
        conn = self.conn_pool.getconn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        # 将连接放回连接池中
        self.conn_pool.putconn(conn)

    def insert_into_faculty(self, faculty_id, faculty_name):
        sql = "INSERT INTO Faculty (FacultyID, FacultyName) " \
              "VALUES (%s, %s)", (faculty_id, faculty_name)
        asyncio.run(self.run_insert(sql))

    def insert_into_major(self, major_id, major_name, faculty_id):
        sql = "INSERT INTO Major (MajorID, MajorName, FacultyID) " \
              "VALUES (%s, %s, %s)", (major_id, major_name, faculty_id)
        asyncio.run(self.run_insert(sql))

    def insert_into_class(self, class_id, major_id):
        sql = "INSERT INTO Class (ClassID, MajorID) VALUES (%s, %s)", (class_id, major_id)
        asyncio.run(self.run_insert(sql))

    def insert_into_person(self, id, name, gender, age, phone, person_type):
        sql = "INSERT INTO Person (ID, Name, Gender, Age, Phone, PersonType) " \
              "VALUES (%s, %s, %s, %s, %s, %s)", (id, name, gender, age, phone, person_type)
        asyncio.run(self.run_insert(sql))

    def insert_into_student(self, student_id, faculty_id, major_id, class_id):
        sql = "INSERT INTO Student (StudentID, FacultyID, MajorID, ClassID) " \
              "VALUES (%s, %s, %s, %s)", (student_id, faculty_id, major_id, class_id)
        asyncio.run(self.run_insert(sql))

    def insert_into_teacher(self, teacher_id, faculty_id, position):
        sql = "INSERT INTO Teacher (TeacherID, FacultyID, Position) " \
              "VALUES (%s, %s, %s)", (teacher_id, faculty_id, position)
        asyncio.run(self.run_insert(sql))

    def insert_into_worker(self, worker_id, worker_type):
        sql = "INSERT INTO Worker (WorkerID, WorkerType) " \
              "VALUES (%s, %s)", (worker_id, worker_type)
        asyncio.run(self.run_insert(sql))

    def insert_into_door(self, door_id, door_locate):
        sql = "INSERT INTO Door (DoorID, DoorLocate) " \
              "VALUES (%s, %s)", (door_id, door_locate)
        asyncio.run(self.run_insert(sql))

    def store_face_image(self, id, image_data, feature_vector):
        sql = "INSERT INTO FaceImage VALUES (%s, %s, %s)", \
            (id, psycopg2.Binary(image_data), psycopg2.Binary(feature_vector))
        asyncio.run(self.run_insert(sql))

    def store_face_recognized_record(self, door_id, direction, image_data, result_id):
        sql = "INSERT INTO DoorRecord (DoorID, Direction, ImageData, ResultID) VALUES (%s, %s, %s, %s, %s)", \
            (door_id, direction, psycopg2.Binary(image_data), result_id)
        asyncio.run(self.run_insert(sql))


insert_processor = InsertProcessor()
