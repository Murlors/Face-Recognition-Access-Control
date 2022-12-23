class DBInserts:
    def __init__(self, conn):
        # 传递与数据库的连接
        self.conn = conn
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def insert_faculty(self, faculty_id, faculty_name):
        self.cursor.execute("INSERT INTO Faculty (FacultyID, FacultyName) VALUES (%s, %s)",
                            (faculty_id, faculty_name))
        self.conn.commit()

    def insert_major(self, major_id, major_name, faculty_id):
        self.cursor.execute("INSERT INTO Major (MajorID, MajorName, FacultyID) VALUES (%s, %s, %s)",
                            (major_id, major_name, faculty_id))
        self.conn.commit()

    def insert_class(self, class_id, major_id):
        self.cursor.execute("INSERT INTO Class (ClassID, MajorID) VALUES (%s, %s)",
                            (class_id, major_id))
        self.conn.commit()

    def insert_person(self, id, name, gender, age, phone, person_type):
        self.cursor.execute(
            "INSERT INTO Person (ID, Name, Gender, Age, Phone, PersonType) VALUES (%s, %s, %s, %s, %s, %s)",
            (id, name, gender, age, phone, person_type))
        self.conn.commit()

    def insert_student(self, student_id, faculty_id, major_id, class_id):
        self.cursor.execute("INSERT INTO Student (StudentID, FacultyID, MajorID, ClassID) VALUES (%s, %s, %s, %s)",
                            (student_id, faculty_id, major_id, class_id))
        self.conn.commit()

    def insert_teacher(self, teacher_id, faculty_id, position):
        self.cursor.execute("INSERT INTO Teacher (TeacherID, FacultyID, Position) VALUES (%s, %s, %s)",
                            (teacher_id, faculty_id, position))
        self.conn.commit()

    def insert_worker(self, worker_id, worker_type):
        self.cursor.execute("INSERT INTO Worker (WorkerID, WorkerType) VALUES (%s, %s)",
                            (worker_id, worker_type))
        self.conn.commit()

    def insert_door(self, door_id, door_locate):
        self.cursor.execute("INSERT INTO Door (DoorID, DoorLocate) VALUES (%s, %s)",
                            (door_id, door_locate))
        self.conn.commit()

    def insert_door_record(self, id, record_time, door_id, direction, image_data, result_id):
        self.cursor.execute(
            "INSERT INTO DoorRecord (ID, RecordTime, DoorID, Direction, ImageData, ResultID)"
            " VALUES (%s, %s, %s, %s, %s, %s)", (id, record_time, door_id, direction, image_data, result_id))
        self.conn.commit()

    def insert_face_image(self, id, image_data, feature_vector):
        self.cursor.execute("INSERT INTO FaceImage (ID, ImageData, FeatureVector) VALUES (%s, %s, %s)",
                            (id, image_data, feature_vector))
        self.conn.commit()
