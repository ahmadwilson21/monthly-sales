# reporter.py
import pandas 
import csv
import statistics
import os
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("READING GRADEBOOK CSV FILE")


###THIS IS THE RECOMMENDED FILE PATH CONSTRUCTION
other_csv_filepath = os.path.join(os.path.dirname(__file__), "data", "gradebook.csv")
print("FILEPATH:", os.path.abspath(other_csv_filepath))



"""
csv_filepath = os.environ.get("CSV_FILE")
grade_filepath = os.environ.get("GRADE_CSV_PATH")
"""

grades = pandas.read_csv(other_csv_filepath)
#print(dir(type))
print(grades.head())
grades_col = grades["final_grade"]
print("GRADES COLUMN", type(grades_col))
avg_grade =grades_col.mean()
print("AVG GRADE:",avg_grade)
#print ("GRADES:", type(grades))

for index, row in grades.iterrows(): #iterrows allows us to loop through rows like we're in a list
    print(index)
    print(row["final_grade"])
    print("-------")

grades_list = grades.to_dict("records") # "records" is a specific parameter of the to_dict() function, not a characteristic of the underlying data
print(type(grades_list))
print(type(grades_list[0]))
print(grades_list)

just_grades = [float(d["final_grade"]) for d in grades_list]
print(just_grades[0])

print("AVG GRADE", statistics.mean(just_grades))
