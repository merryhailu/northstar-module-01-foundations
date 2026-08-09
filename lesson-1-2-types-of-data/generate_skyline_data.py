import random
import numpy as np
import pandas as pd
from datetime import date

random.seed(123)
np.random.seed(123)

n_skyline_enrollments = 100

enrollment_id = [f"ENR-{random.randint(100000,999999)}" for _ in range(n_skyline_enrollments)]

course_name = np.random.choice( 
    [ "Intro to Analytics", "Python for Beginners", "SQL Basics", "Tableau Fundamentals", "Statistics 101"],
    size = n_skyline_enrollments,
    p = [0.30, 0.25, 0.25, 0.12, 0.08])

enrollment_year = np.random.randint(2022, 2027, size=n_skyline_enrollments)

final_grade = np.random.choice(
    [ "F", "D", "C", "B", "A"],
    size = n_skyline_enrollments,
    p = [0.03, 0.07, 0.35, 0.35, 0.20])

hours_studied = np.random.normal(loc=30, scale = 3, size=n_skyline_enrollments)
hours_studied = np.round(hours_studied, 2)
hours_studied = np.maximum(hours_studied, 0)  # Ensure no negative hours

completion_status = np.random.choice(
    [ "Completed", "Dropped", "In Progress"],
    size = n_skyline_enrollments,
    p = [0.90, 0.03, 0.07])


skyline_enrollments = pd.DataFrame({
    'enrollment_id': enrollment_id,
    'course_name': course_name,
    'enrollment_year': enrollment_year,
    'final_grade': final_grade,
    'hours_studied': hours_studied,
    'completion_status': completion_status
})

print(skyline_enrollments.head(10))
print(f"\nShape: {skyline_enrollments.shape}")
print(f"\nColumn types:\n{skyline_enrollments.dtypes}")

output_path = 'skyline_enrollments.csv'
skyline_enrollments.to_csv(output_path, index=False)
print(f"\nSaved synthetic Skyline enrollments dataset to {output_path}")