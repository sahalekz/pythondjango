class student:
    def __init__(self):

        self.name = ""
        self.dept=""
        self.year=""
        self.__marks_obtained = []
        self.total = 0
        self.percent= 0
       

    def grade_calc(self):
        self.name = input("Enter Name: ")
        self.dept = input("Enter Dept: ")
        self.year = input("Enter Year: ")
        print("Enter 6 subjects marks: ")
        for n in range(6):
            self.__marks_obtained.append(int(input("Subject " + str(n + 1) + ": ")))
        self.total = sum(self.__marks_obtained)
        self.percent = (self.total/600)*100
    def showgrade(self):
        print("----------Grade Card----------")
        print("Name: ", self.name)
        print("Dept: ", self.dept)
        print("Year: ", self.year)
        print("Total: ", self.total)
        print("Percentage: ", self.percent)
        print("----------------------------")