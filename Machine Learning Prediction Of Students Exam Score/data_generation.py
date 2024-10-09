import pandas as pd
import numpy as np
from faker import Faker
import random
#import ace_tools as tools

fake = Faker()

#students constants
class_levels = ['JSS1', 'JSS2', 'JSS3', 'SS1', 'SS2', 'SS3']
genders = ["Male", "Female"]
special_needs = ["Yes", "No"]
num_students = 600

#parents constats
occupations = ["Farmer", 'Teacher', "Doctor", "Engineers", "Trader", "Civil Servant", "Pharmacist", "Lawyer", "Accountant", "Banker"]
education_levels = ["Bachelor", "Masters", "Doctoral"]
income_level = ["Low", "Medium", "High"]
digital_literacy = ["Yes", "No"]

#resource allocation c0nstants
computer_access = ["Never", "Occasionally", "Often"]
learning_material = ["Books", "Digital Platform", "Both"]

#extra currilar constants
activities = ["Sports", "JETS Club", "Debate & Press Club", "ARTS Club", "Maths Club", "None"]
leadership = ["Yes", "No"]

#Students data
jss_subjects = ['Mathematics', 'English', 'Basic Science', 'Basic Tech', 'Civic Education']
ss_subjects = ['Mathematics', 'English', 'Biology', 'Physics', 'Chemistry']
student_class = ['JSS1', 'JSS2', 'JSS3', 'SS1', 'SS2', 'SS3'] * 100

#history constants
improvement_trend = ["Improved", "Declined", "No Change"]

def generate_student_data_per_class(num_students):
    student_data = []
    student_count = 1

    for class_level in class_levels:
        for i in range(100):
            student_id = f'STU{student_count:03d}'
            age = random.randint(10, 18)
            gender = random.choice(genders)
            has_special_needs = random.choice(special_needs)
            attendance_percentage = round(random.uniform(50.0, 100.0), 2)
            punctuality_percentage = round(random.uniform(50.0, 100.0), 2)
            study_hour_per_week = random.randint(0, 20)

            student_data.append({
                "Student ID" : student_id,
                "Age" : age,
                "Gender" : gender,
                'Special Needs' : has_special_needs,
                "Attendance (%)" : attendance_percentage,
                "Punctuality (%)" : punctuality_percentage,
                "Study Hour/Week" : study_hour_per_week
            })

            student_count += 1

    return pd.DataFrame(student_data)

def generate_parents_data(num_students):
    parents_data = []
    for students in range(num_students):
        parental_occupation = random.choice(occupations)
        education_level = random.choice(education_levels)
        household_income = random.choice(income_level)
        has_digital_literacy = random.choice(digital_literacy)
        parental_involvement_meetings = random.randint(0, 12) #number of meet ups per month
        parental_homework_help = random.randint(0,6) # days a week

        parents_data.append({
            "Parental Occupation" : parental_occupation,
            "Parental Education Level" : education_level,
            "Household Income" : household_income,
            "Parental Digital Literacy" : has_digital_literacy,
            "Teacher Meetings (per year)" : parental_involvement_meetings,
            "Homework Help (per week)" : parental_homework_help
        })

    return pd.DataFrame(parents_data)

def generate_resource_allocation_data(num_students):
    resource_data = []

    for i in range(num_students):
        library_hour_per_week = random.randint(0,10) #assuming aximum of 2 hours per school week
        computer_access_frequency = random.choice(computer_access)
        teacher_student_ratio = random.randint(20, 40)
        access_to_learning_materials = random.choice(learning_material)

        resource_data.append({
            "Library Hours" : library_hour_per_week,
            "Computer Access" : computer_access_frequency,
            "Teacher-Student Ratio" : teacher_student_ratio,
            "Access to learning Materials" : access_to_learning_materials
        })

    return pd.DataFrame(resource_data)

def generate_extra_curricular_data(num_students):
    extra_curricular_data = []

    for i in range(num_students):
        activity = random.choice(activities)
        hours_per_week = random.randint(0 , 6)
        leadership_role = random.choice(leadership)

        extra_curricular_data.append({
            "Activity" : activity,
            "Hours/Week" : hours_per_week,
            "Leadership Role" : leadership_role
        })
    
    return pd.DataFrame(extra_curricular_data)

def generate_historical_performance_data(num_students):
    performane_data = []
    for i in range(num_students):
        class_level = student_class[i]

        if class_level.startswith("JSS"):
            subjects = jss_subjects
            jamb_mock_score = 0
        else:
            subjects = ss_subjects
            if class_level == "SS3":
                jamb_mock_score = random.randint(100, 350)
            else:
                jamb_mock_score = 0
    
        midterm_score = round(random.uniform(0, 40), 2)
        exam_score = round(random.uniform(0, 60), 2)
        improvement_trends = random.choice(improvement_trend)
        weak_subjects = random.choice(subjects)

        performane_data.append({
            "Class Level" : class_level,
            "Midterm Score" : midterm_score,
            "Exam Score" : exam_score,
            "Improvements Over Time" : improvement_trends,
            "JAMB Mock Score" : jamb_mock_score,
            "Weak Subject": weak_subjects
        })

    return pd.DataFrame(performane_data)
print("Generating student data...")
#Generate data
student_data =  generate_student_data_per_class(num_students)
parents_data = generate_parents_data(num_students)
resource_allocation_data = generate_resource_allocation_data(num_students)
extra_curricular_data = generate_extra_curricular_data(num_students)
historical_data = generate_historical_performance_data(num_students)

#add students ID to other dataset
parents_data['Student ID'] = student_data['Student ID']
resource_allocation_data['Student ID'] = student_data['Student ID']
extra_curricular_data['Student ID'] = student_data['Student ID']
historical_data['Student ID'] = student_data['Student ID']

#Merge data
merged_data = pd.merge(student_data, parents_data, on='Student ID')
merged_data = pd.merge(merged_data, resource_allocation_data, on='Student ID')
merged_data = pd.merge(merged_data, extra_curricular_data, on='Student ID')
merged_data = pd.merge(merged_data, historical_data, on='Student ID')

#get single unit data
student_data.to_csv("student_data.csv", index = False)
parents_data.to_csv("parent_data.csv", index = False)
resource_allocation_data.to_csv("resource_allocation_data.csv", index = False)
extra_curricular_data.to_csv("extra_curricular_data.csv", index = False)
historical_data.to_csv("historical_data.csv", index = False)

#get merged data
merged_data.to_csv("data.csv", index = False)

print("Data generation complete. File 'data.csv' has been created.")