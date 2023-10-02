class ToDoList:
    def __init__(self):
        self.List=[]
    def addTask(self,task,time):
        self.List.append({task:time})
    def show(self):
        print(self.List)
    def removeTask(self,task):
        for i in self.List[0]:
            if i==task:
                self.List.pop(i)
                break
            print("task is complete")

lst=ToDoList
lst.addTask("walk","8am")
lst.addTask("gym","9am")
lst.addTask("work","10am")
lst.show()

