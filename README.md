# Face-Recognition-Access-Control

Face Recognition Access Control System based on the characteristics of students going to and coming from class.

## Overview

This project is developed using Python, with a front-end developed using PySide6 and a back-end using the Flask framework. The database used is PostgreSQL.

The project file structure is as follows:

```struct
├── Client
│   ├── form.ui
│   ├── Gate.py
│   ├── main.py
│   ├── QueryRecord.py
│   ├── record.ui
│   ├── requirements.txt
│   ├── ui_form.py
│   └── ui_record.py
├── Server
|   ├── _init_paths.py
│   ├── FacenetModel.py
│   ├── ImgServer.py
│   └── requirements.txt
├── SQL
│   ├── __init__.py
│   ├── ConnectionPool.py
│   ├── Create.sql
│   ├── InsertProcessor.py
│   └── QueryProcessor.py
├── ERdiagram.excalidraw
├── LICENSE
├── README.md
└── _timeit.py
```

## System Functionality

- Uses face recognition technology (MTCNN and FaceNet) to verify identity
- Records information about people entering and exiting doors, including the time, location, and direction of entry/exit
- Maintains a database of personnel information, including student, teacher, and staff information

- Maintains a database of face images for use in face recognition
- Maintains a log of face recognition results, recording the time and result of each recognition

## Installation Instructions

Installation of this system is divided into two parts: the front-end client and the back-end server.

### Client Installation

1. Download and unzip the source code for this project, and navigate to the `Client` directory.
2. Install dependencies: run `pip install -r requirements.txt`.
3. Run the client: in the Client directory, run `python main.py` to start the client.

### Server Installation

1. Download and unzip the source code for this project, and navigate to the `Server` directory.
2. Install dependencies: run `pip install -r requirements.txt`. (ps. If you want to use CUDA to accelerate the model, you need to install the corresponding version of PyTorch and Torchvision. <https://pytorch.org/get-started/locally/>)
3. Install PostgreSQL and create a database with the file `Create.sql`.
4. Run the server: in the Server directory, run `python ImgServer.py` to start the server.

### Database Design

This system uses a PostgreSQL database, with the following tables:

- Faculty (FacultyName, FacultyID)
- Major (MajorName, MajorID, FacultyID)
- Class (ClassID, MajorID)
- Person (ID, Name, Gender, Age, Phone, PersonType)
- Student (ID, FacultyID, MajorID, ClassID)
- Teacher (ID, FacultyID, Position)
- Worker (ID, Type)
- Record (ID, Time, DoorID, Direction, Data, Result)
- Door (DoorID, DoorLocate)
- FaceImage (ID, Data, Feature Vector)
