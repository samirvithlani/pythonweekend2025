def get_names(students):
    names =[]
    for i in students:
        names.append(i["name"])
        return names    
        
def get_avg_score(students):
    pass

def get_grade(students):
    pass

def process_students(students,cb):
    return cb(students)

students = [
    {"name": "Alice", "math": 78, "science": 89},
    {"name": "Bob", "math": 92, "science": 76},
    {"name": "Charlie", "math": 88, "science": 95},
    {"name": "David", "math": 65, "science": 70}
]


x = None
x = process_students(students, get_names)
# ['Alice', 'Bob', 'Charlie', 'David']
print(x)

process_students(students, get_avg_score)
# [83.5, 84.0, 91.5, 67.5]

process_students(students, get_grade)
# ['B', 'B', 'A', 'C']




