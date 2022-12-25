import requests

url = "http://localhost:8090"


def id_record(id, start_time, end_time):
    student_result = student_record(id, start_time, end_time)
    if student_result:
        return student_result
    else:
        return teacher_record(id, start_time, end_time)


def student_record(student_id, start_time, end_time):
    res = {
        "student_id": student_id,
        "start_time": start_time,
        "end_time": end_time,
    }
    returnData = requests.post(f"{url}/student_record", json=res)
    return returnData.text


def teacher_record(teacher_id, start_time, end_time):
    res = {
        "teacher_id": teacher_id,
        "start_time": start_time,
        "end_time": end_time,
    }
    returnData = requests.post(f"{url}/teacher_record", json=res)
    return returnData.text


def class_record(class_id, start_time, end_time):
    res = {
        "class_id": class_id,
        "start_time": start_time,
        "end_time": end_time,
    }
    returnData = requests.post(f"{url}/class_record", json=res)
    return returnData.text


def major_record(major_id, start_time, end_time):
    res = {
        "major_id": major_id,
        "start_time": start_time,
        "end_time": end_time,
    }
    returnData = requests.post(f"{url}/major_record", json=res)
    return returnData.text


def faculty_record(faculty_id, start_time, end_time):
    res = {
        "faculty_id": faculty_id,
        "start_time": start_time,
        "end_time": end_time,
    }
    returnData = requests.post(f"{url}/faculty_record", json=res)
    return returnData.text
