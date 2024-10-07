class emp:
    def __init__(self,name, age,dept, sal,rating):
        self.name=name
        self.age=age
        self.dept=dept
        self.sal=sal
        self.rating=rating
    def is_bonus(self):
        if self.age>=60:
            self.sal+=1000
            print("salary is incresse 1000 now:" + str(self.sal) )
        else:
            print("no incress")
    def is_excelent(self):
        if self.rating==5:
            return True
        else:
           return False