-- SELECT 'CREATE DATABASE AccessControlSystem;'
-- WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '<db_name>')\gexec
CREATE DATABASE AccessControlSystem;

CREATE TABLE Faculty(
	FacultyID	integer	PRIMARY KEY,
	FacultyName	varchar(50)	NOT NULL
);

CREATE TABLE Major(
	MajorID integer	PRIMARY KEY,
	MajorName	varchar(50)	NOT NULL,
	FacultyID	integer	NOT NULL	references	Faculty(FacultyID)
);

CREATE TABLE Class(
	ClassID	integer	PRIMARY KEY,
	MajorID	integer	NOT NULL	references	Major(MajorID)
);

CREATE TYPE GenderType AS ENUM ('Male', 'Female');
CREATE TYPE PersonnelType AS ENUM ('Student', 'Teacher', 'Worker');

CREATE TABLE Person(
	ID	varchar(20)	PRIMARY KEY,
	Name	varchar(20)	NOT NULL,
	Gender	GenderType	NOT NULL,
	Age	smallint	NOT NULL	CHECK(Age >= 0),
	Phone varchar(20),
	PersonType	PersonnelType	NOT NULL
);

CREATE TABLE Student(
	StudentID	varchar(20)	PRIMARY KEY	references	Person(ID),
	FacultyID	integer	NOT NULL	references	Faculty(FacultyID),
	MajorID	integer	NOT NULL	references	Major(MajorID),
	ClassID	integer	NOT NULL	references	Class(ClassID)
);

CREATE TABLE Teacher(
	TeacherID	varchar(20)	PRIMARY KEY	references	Person(ID),
	FacultyID	integer	references	Faculty(FacultyID),
	Position	varchar(20)
);

CREATE TABLE Worker(
	WorkerID	varchar(20)	PRIMARY KEY	references	Person(ID),
	WorkerType	varchar(20)	NOT NULL
);

CREATE TABLE Door(
	DoorID	integer	PRIMARY KEY,
	DoorLocate	varchar(50)	NOT NULL
);

CREATE TYPE DoorDirection AS ENUM ('In', 'Out');

CREATE TABLE DoorRecord(
	RecordID	SERIAL  PRIMARY KEY,
	RecordTime	TIMESTAMP WITH TIME ZONE	DEFAULT ('now'::text)::timestamp with time zone,
    ResultID	varchar(20) references  Person(ID),
    ImageData   bytea	NOT NULL,
	DoorID	integer	NOT NULL	references  Door(DoorID),
	Direction	DoorDirection	NOT NULL
);

CREATE TABLE FaceImage(
	ID	varchar(20)	PRIMARY KEY,
	ImageData bytea	NOT NULL,
	FeatureVector	bytea	NOT NULL
);

CREATE INDEX PersonID ON Person(ID);
CREATE INDEX FaceID ON FaceImage(ID,FeatureVector);