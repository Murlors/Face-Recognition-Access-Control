import asyncio

from SQL.ConnectionPool import ConnectionPool


class QueryProcessor:
    def __init__(self):
        # 与连接池连接
        self.conn_pool = ConnectionPool().conn_pool

    async def run_query(self, sql):
        # 从连接池中获取一个连接
        conn = self.conn_pool.getconn()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # 将连接放回连接池中
        self.conn_pool.putconn(conn)
        return result

    async def process_query(self, query):
        # 接收单独的SQL查询语句并返回相应的结果
        return await query_processor.run_query(query)

    def load_face_image_feature_vector(self):
        # 加载人脸图像特征向量
        sql = "SELECT ID,Name,FeatureVector FROM FaceImage NATURAL JOIN Person"
        return asyncio.run(self.process_query(sql))

    def query_door_record(self, door_id, direction, start_time, end_time):
        # 查询门禁记录
        sql = "SELECT * FROM DoorRecordView " \
              "WHERE DoorID = %s AND Direction = %s AND RecordTime BETWEEN %s AND %s", \
            (door_id, direction, start_time, end_time)
        return asyncio.run(self.process_query(sql))

    def query_student_face_recognition_record(self, student_id, start_time, end_time):
        # 通过学生ID查询学生的人脸识别记录
        sql = "SELECT StudentID,Name,RecordTime,DoorID,Direction " \
              "FROM StudentView,DoorRecordView " \
              "WHERE StudentID = %s AND RecordTime BETWEEN %s AND %s " \
              "AND StudentView.StudentID = DoorRecordView.ResultID", \
            (student_id, start_time, end_time)
        return asyncio.run(self.process_query(sql))

    def query_teacher_face_recognition_record(self, teacher_id, start_time, end_time):
        # 通过教师ID查询教师的人脸识别记录
        sql = "SELECT TeacherID,Name,RecordTime,DoorID,Direction " \
              "FROM TeacherView,DoorRecordView " \
              "WHERE TeacherID = %s AND RecordTime BETWEEN %s AND %s " \
              "AND TeacherView.TeacherID = DoorRecordView.ResultID", \
            (teacher_id, start_time, end_time)
        return asyncio.run(self.process_query(sql))

    def query_class_face_recognition_record(self, class_id, start_time, end_time):
        # 通过班级ID查询班级内所有学生的人脸识别记录
        sql = "SELECT ClassID,StudentID,Name,RecordTime,DoorID,Direction " \
              "FROM StudentView,DoorRecordView " \
              "WHERE ClassID = %s AND RecordTime BETWEEN %s AND %s " \
              "AND StudentView.StudentID = DoorRecordView.ResultID", \
            (class_id, start_time, end_time)
        return asyncio.run(self.process_query(sql))

    def query_major_face_recognition_record(self, major_id, start_time, end_time):
        # 通过专业ID查询专业内所有学生的人脸识别记录
        major_id_sql = "SELECT MajorID,StudentID,Name,RecordTime,DoorID,Direction " \
                       "FROM StudentView,DoorRecordView " \
                       "WHERE MajorID = %s AND RecordTime BETWEEN %s AND %s " \
                       "AND StudentView.StudentID = DoorRecordView.ResultID", \
            (major_id, start_time, end_time)
        sql = "SELECT MajorName,MajorRecord.* " \
              "FROM Major NATURAL JOIN %s AS MajorRecord", (major_id_sql,)
        return asyncio.run(self.process_query(sql))

    def query_faculty_face_recognition_record(self, faculty_id, start_time, end_time):
        # 通过学院ID查询学院内所有学生的人脸识别记录
        faculty_id_sql = "SELECT FacultyID,StudentID,Name,RecordTime,DoorID,Direction " \
                         "FROM StudentView,DoorRecordView " \
                         "WHERE FacultyID = %s AND RecordTime BETWEEN %s AND %s " \
                         "AND StudentView.StudentID = DoorRecordView.ResultID", \
            (faculty_id, start_time, end_time)
        sql = "SELECT FacultyName,FacultyRecord.* " \
              "FROM Faculty NATURAL JOIN %s AS FacultyRecord", (faculty_id_sql,)
        return asyncio.run(self.process_query(sql))


query_processor = QueryProcessor()

# import time
# from timeit import timeit
#
# @timeit
# def test():
#     queries = ["SELECT * FROM course", "SELECT * FROM dept", "SELECT * FROM sc", "SELECT * FROM student"]
#     for query in queries:
#         results = asyncio.run(query_processor.process_query(query))
#         print(f"Query: {query}")
#         print(f"Result: {results}")
#
# if __name__ == '__main__':
#     start = time.time()
#     for i in range(100):
#         test()
#     end = time.time()
#     print(f"Time: {end - start}")
