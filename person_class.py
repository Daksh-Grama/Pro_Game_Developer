class Student():
    name = ""
    age = 11
    grade = 7
    house = "blue"
    teacher = "Hannah"

    #constructor
    def __init__(self):
        print("making a new student...")

    #creating another function
    def change_details(self):
        print("Please enter\t your name : \n")
        self.name = input()
        
        print("Please enter\t your age : \n")
        self.age = int(input())

    def show_details(self):
        print("the details of students are : \n")
        print(self.name, "\n", self.age, "\n", self.grade, "\n", self.house, "\n", self.teacher)

daksh = Student()
samuel = Student()

daksh.change_details()
daksh.show_details()







