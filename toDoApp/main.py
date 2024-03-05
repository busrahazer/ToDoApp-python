import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot
from itemfunctions import ItemFunctions

class ToDoApp(QObject):
    def __init__(self):
        super().__init__()

    @Slot(str)
    def addItem(self, text):
        item_functions = ItemFunctions()
        success = item_functions.addTodoItem(text)
        if success:
            print("Item added successfully!")
        else:
            print("Failed to add item!")

if __name__ == '__main__':
    app = QApplication(sys.argv) # A QApplication instance is created for the PySide6 application. This is usually the first step when starting a Qt application.
    engine = QQmlApplicationEngine() # An instance of QQmlApplicationEngine is created. This engine loads and executes QML files.

    to_do_app = ToDoApp() # An instance of the ToDoApp class is created. This instance represents the Python code that will be used in the QML file.
    engine.rootContext().setContextProperty("ToDoApp", to_do_app) # The ToDoApp instance is bound to the QML engine so that it can be used in the QML file.
    engine.load('main.qml')  # The QML file is loaded and the engine is started.

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec()) #app.exec() starts the main loop of the application and the application continues to run until this loop ends. sys.exit() terminates the application when this loop ends.
