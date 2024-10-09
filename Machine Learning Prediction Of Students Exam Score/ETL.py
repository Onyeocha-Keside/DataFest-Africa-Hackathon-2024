import pandas as pd

#load the csv files
student_data = pd.read_csv("student_data.csv")
parents_data = pd.read_csv("parent_data.csv")
resource_allocation_data = pd.read_csv("resource_allocation_data.csv")
extra_curricular_data = pd.read_csv("extra_curricular_data.csv")
historical_data = pd.read_csv("historical_data.csv")

#Tranform the data
#clean the data
# Replace missing numerical data with the mean or a sensible default
#student_data['Attendance (%)'].fillna(student_data['Attendance (%)'].mean(), inplace=True)
#student_data['Study Hour/Week'].fillna(student_data['Study Hour/Week'].mean(), inplace=True)

# Standardizing Categorical Variables (e.g., Yes/No -> 1/0)
#student_data['Special Needs'] = student_data['Special Needs'].apply(lambda x: 1 if x == 'Yes' else 0)

# Standardizing Other Categorical Variables (in Parent's Data)
#parents_data['Parental Digital Literacy'] = parents_data['Parental Digital Literacy'].apply(lambda x: 1 if x == 'Yes' else 0)

# Validation: Ensuring no missing or invalid values remain
#assert student_data.isnull().sum().sum() == 0, "There are still missing values!"

#Load
from sqlalchemy import Column, create_engine, Integer, String, Float, ForeignKey, Table, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/school_db"

#connect to a database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

#defining the student table schema
class Students(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key= True)
    age = Column(Integer)
    gender = Column(String)
    attendance = Column(Float)
    study_hours = Column(Float)
    special_needs = Column(Integer)

class Parents(Base):
    __tablename__ = "parents"

    parent_id = Column(Integer,primary_key=True)
    student_id = Column(String, ForeignKey('students.student_id'))
    education_level = Column(String)
    occupation = Column(String)
    income_level = Column(String)
    involvement = Column(Integer)

class ResourceAllocation(Base):
    __tablename__ = "resource_allocation"

    resource_id = Column(Integer, primary_key= True)
    student_id = Column(String, ForeignKey("students.student_id"))
    library_hours = Column(Float)
    computer_access = Column(String)
    teacher_student_ratio = Column(Float)

class ExtraCurricular(Base):
    __tablename__ = "extra_curricular"

    curricular_id = Column(Integer, primary_key= True)
    student_id = Column(String, ForeignKey("students.student_id"))
    activities = Column(String)
    hours_per_week = Column(Integer)
    leadership_role = Column(String)

class HistoricalPerformance(Base):
    __tablename__ = 'historical_performance'

    historical_id = Column(Integer, primary_key=True)
    student_id = Column(String, ForeignKey("students.student_id"))
    class_level = Column(String)
    midterm_score = Column(Float)
    exam_score = Column(Float)
    jamb_score = Column(Integer)
    improvements = Column(String)
    weakness = Column(String)

#create the table
Base.metadata.create_all(engine)

student_data.to_sql("students", engine, if_exists= "replace", index = False)
parents_data.to_sql("parents", engine, if_exists= "replace", index = False)
resource_allocation_data.to_sql("resource_allocation", engine, if_exists="replace", index= False)
extra_curricular_data.to_sql("extra_curricular", engine, if_exists="replace", index=False)
historical_data.to_sql("historical_performance", engine, if_exists="replace", index = False)

print("dataloaded to postgreSQL successfully..")