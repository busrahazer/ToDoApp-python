from PySide6.QtCore import QObject, Slot

class ItemFunctions(QObject):
    def __init__(self, directory="."):
        super().__init__()
        self.directory = directory

    @Slot(str, result=bool)
    def addTodoItem(self, todo_text):

        print("Todo item added:", todo_text)
        return True
