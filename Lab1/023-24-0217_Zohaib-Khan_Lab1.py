
# Week 1 Lab - Python Refresher + NumPy, Pandas, Matplotlib
# VS Code Python file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# DAY 1 - Variables, Data Types, Operators, Loops
# ============================================================

name = "Zohaib Khan"
age = 21
gpa = float("3.85")

print(type(name), type(age), type(gpa))

a, b = 17, 5

print(a // b)
print(a % b)
print(a ** 2)

print(3 in [1, 2, 3])

for i in range(1, 6):
    if i == 4:
        continue
    print(i)


# Practice Tasks

# 1. Take two numbers and print sum, difference, product,
#    quotient, floor division and remainder.

# 2. Take temperature in Fahrenheit and convert it to Celsius.

# 3. Print all prime numbers from 1 to 100.

# 4. Check whether a number is even or odd using bitwise operator.


# ============================================================
# DAY 2 - Functions, Data Structures, Comprehensions
# ============================================================

def greet(name, msg="Hello"):
    return f"{msg}, {name}!"


def total(*nums):
    return sum(nums)


square = lambda x: x ** 2


# List, tuple, set and dictionary

evens = [x for x in range(20) if x % 2 == 0]

word_len = {w: len(w) for w in ["cat", "elephant", "dog"]}

print(word_len)


# Practice Tasks

# 1. Create stats(*nums) that returns min, max and average.

# 2. Find squares of even numbers using list comprehension.

# 3. Find common and different values from two sets.

# 4. Remove duplicates from a list while keeping the order.

# 5. Create cubes from 1 to 10 using dictionary comprehension.


# ============================================================
# DAY 3 - NumPy Arrays, Indexing, Slicing, Operations
# ============================================================

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

m = np.array([[1, 2, 3], [4, 5, 6]])

print(m.sum(axis=0))
print(m[m > 3])


# Practice Tasks

# 1. Create an array of the first 15 natural numbers.
#    Print shape, size and dtype.

# 2. Create a 5x5 array of random numbers from 10 to 50.
#    Find maximum, minimum and mean.

# 3. Create an array of 20 elements and reshape it into 4x5.
#    Print the second and third columns.

# 4. Create an array of 15 exam scores.
#    Print scores above the average.

# 5. Use np.where() to replace negative values with 0
#    and positive values with 1.


# ============================================================
# DAY 4 - Pandas Series, DataFrames, Reading and Selecting Data
# ============================================================

data = {
    "name": ["Ali", "Sara", "Omar"],
    "marks": [78, 92, 65]
}

df = pd.DataFrame(data)

print(df.head())
print(df.describe())

top = df[df["marks"] > 70]

print(top.sort_values("marks", ascending=False))

print(df.loc[0, "name"])
print(df.iloc[1, 1])


# Practice Tasks

# 1. Create a DataFrame of 6 students with name, subject and marks.
#    Print info() and describe().

# 2. Load a small CSV file.
#    Print shape, columns and first 5 rows.

# 3. Find students who have marks above 80.

# 4. Use loc and iloc to select the same row.


# ============================================================
# DAY 5 - Cleaning, Grouping and Merging
# ============================================================

# Check missing values
# df.isna().sum()

# Fill missing marks
# df["marks"] = df["marks"].fillna(df["marks"].mean())

# Create grade column
# df["grade"] = df["marks"].apply(
#     lambda m: "A" if m >= 80 else "B"
# )

avg_by_name = df.groupby("name")["marks"].mean()

print(avg_by_name)


# Practice Tasks

# 1. Count missing marks and fill them with the mean.

# 2. Create a pass_fail column using apply() and lambda.

# 3. Group students by subject and find mean, minimum and maximum.

# 4. Merge students and attendance DataFrames using student ID.


# ============================================================
# DAY 6 - Matplotlib and Mini Project
# ============================================================

plt.bar(df["name"], df["marks"])

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Marks by Student")

plt.show()


# Practice Tasks

# 1. Create a line chart using 10 days of temperature data.

# 2. Create a 1x2 subplot.
#    Left: bar chart
#    Right: histogram

# 3. Create a boxplot and describe what it shows.


# ============================================================
# MINI END TO END TASK
# ============================================================

# 1. Load a class marks CSV file.

# 2. Check missing values and clean the data.

# 3. Find mean and standard deviation.

# 4. Find the top scorer in each subject.

# 5. Create a bar chart of average marks.

# 6. Create a histogram of marks.

# 7. Write one line about what each chart shows.


# ============================================================
# WEEKLY GRADED LAB
# 50 Marks - 25 Questions x 2 Marks
# ============================================================


# ============================================================
# SECTION A - PYTHON
# Q1 - Q8
# ============================================================

# Q1. Swap two variables without using a third variable.

# Q2. Create an is_prime(n) function.

# Q3. Print Fibonacci sequence for n terms.

# Q4. Remove duplicates from a list and keep the same order.

# Q5. Create multiply(*args) to find the product.

# Q6. Use dictionary comprehension to count characters in a string.

# Q7. Find the employee with the highest salary.

# Q8. Use lambda and filter() to find odd numbers.


# ============================================================
# SECTION B - NUMPY
# Q9 - Q17
# ============================================================

# Q9. Create an array from 1 to 30 and reshape it into 5x6.

# Q10. Create a 6x6 identity matrix.
#      Replace the diagonal with 1, 2, 3, 4, 5, 6.

# Q11. Create 25 random numbers from 1 to 100.
#      Find sum, mean and standard deviation.

# Q12. Create a 4x4 array.
#      Find the diagonal and its sum.

# Q13. Create two 3x3 arrays.
#      Show element-wise multiplication and matrix multiplication.

# Q14. Create daily temperatures for one month.
#      Count days above 35°C.

# Q15. Normalize an array between 0 and 1.

# Q16. Create a 5x3 array for 5 students and 3 subjects.
#      Find total and average for each student.

# Q17. Use np.where() to replace even numbers with -1.


# ============================================================
# SECTION C - PANDAS
# Q18 - Q22
# ============================================================

# Q18. Create a DataFrame of 8 students.
#      Columns: name, section, marks.
#      Print describe().

# Q19. Load a CSV file.
#      Check missing values and fill numeric missing values with mean.

# Q20. Use loc and filtering to find students with marks below 50.
#      Print only name and marks.

# Q21. Group students by section.
#      Find mean and maximum marks.

# Q22. Merge students and attendance DataFrames using student ID.
#      Find students with attendance below 75%.


# ============================================================
# SECTION D - MATPLOTLIB
# Q23 - Q25
# ============================================================

# Q23. Create a bar chart of average marks for each section.

# Q24. Create a histogram of marks.
#      Write one line about the distribution.

# Q25. Create a 1x2 subplot.
#      Left: line plot
#      Right: scatter plot

