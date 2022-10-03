"""
Program checks number of points in test of certain person and based on it will assign a grade.
"""

people = "Jeff", "Jane", "George", "Ann", "Pete", "Monica"
points = 25, 47, 61, 55, 73, 67

for i in range(0, 5):
    print(f"{people[i]} has {points[i]} points.")
    if points[i] > 30 and points[i] <= 49:
        print("Grade C\n")
    elif points[i] > 49 and points[i] <= 64:
        print("Grade B\n")
    elif points[i] > 64:
        print("Grade A\n")
    elif points[i] <= 30:
        print("Test failed.\n")