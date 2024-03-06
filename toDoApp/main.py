# main.py

import sys
from PySide2.QtCore import QObject, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from itemfunctions import add_item, remove_item, update_item

class TodoApp(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.todo_list = []

    @Slot(str)
    def addTodoItem(self, item_text):
        add_item(item_text, self.todo_list)

    @Slot(int)
    def removeTodoItem(self, index):
        remove_item(index, self.todo_list)

    @Slot(int, str)
    def updateTodoItem(self, index, new_text):
        update_item(index, new_text, self.todo_list)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    todo_app = TodoApp()

    engine.rootContext().setContextProperty("todoApp", todo_app)
    engine.load("Main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
