class Person:
    university_name = "Codegnan University"

    def __init__(self,name,age,dept,edu_bg,mobile_no,gender):
        self.name = name
        self.age = age
        self.dept = dept
        self.edu_bg = edu_bg
        self.mobile_no = mobile_no
        self.gender = gender

    def display_info(self):
        pass


class Student(Person):
    student_count = 0

    def __init__(self,name,age,stu_id,dept,edu_bg,pass_year,mobile_no,gender):
        super().__init__(name,age,dept,edu_bg,mobile_no,gender)
        self.stu_id = stu_id
        self.pass_year = pass_year
        Student.student_count += 1

    def display_info(self):
        print("STUDENT DETAILS")
        print(f"""
Name: {self.name}
Age: {self.age}
Student ID: {self.stu_id}
Gender: {self.gender}
Department: {self.dept}
Education: {self.edu_bg}
Pass Year: {self.pass_year}
Mobile No: {self.mobile_no}
University: {Person.university_name}
""")


class Faculty(Person):
    faculty_count = 0

    def __init__(self, name,age,exp,dept,edu_bg,faculty_id,mobile_no,gender):
        super().__init__(name,age,dept,edu_bg,mobile_no,gender)
        self.exp = exp
        self.faculty_id = faculty_id
        Faculty.faculty_count += 1

    def display_info(self):
        print("FACULTY DETAILS")
        print(f"""
Name: {self.name}
Age: {self.age}
Faculty ID: {self.faculty_id}
Gender: {self.gender}
Department: {self.dept}
Education: {self.edu_bg}
Experience: {self.exp} years
Mobile No: {self.mobile_no}
University: {Person.university_name}
""")



s1 = Student("Deepansha", 18, 6785, "IT", "CSE", 2025, 9876543210, "Female")

f1 = Faculty("Prakash", 40, 15, "IT", "MCA", 1001, 9754321000, "Male")


s1.display_info()
f1.display_info()

print("Total Students:", Student.student_count)
print("Total Faculty:", Faculty.faculty_count)

            
            
        
        
     
