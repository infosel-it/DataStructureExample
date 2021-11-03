

class Student():
    def __init__(self, appNo, name, dept,spl):
        self.appNo = appNo
        self.name = name
        self.dept = dept
        self.spl = spl


s1 = Student(629,"Selva", "IT","IT")
s2 = Student(630,"Arun", "IT","IT Multimedia")
s3 = Student(631,"Santhosh", "CS", "CS Big Data")

print("# Student 1 Details #")
print(s1.appNo)
print(s1.name)
print(s1.spl)

print()

print("# Student 3 Details #")
print(s3.appNo)
print(s3.name)
print(s3.spl)