import QtQuick 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "To Do App"

    // Model to keep ToDo list
    ListModel {
        id: todoModel
    }

    ListView {
        id: todoListView
        anchors.fill: parent
        model: todoModel
        delegate: Item {
            width: parent.width
            height: 40
            Text {
                anchors.centerIn: parent
                text: model.title
            }
        }
    }
    // To Do input field
    TextField {
        id: todoInput
        anchors {
            left: parent.left
            right: parent.right
            bottom: addButton.top
        }
    }
    // Adds to the list when the button is pressed
    Button {
        id: addButton
        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
        text: "Add"
        onClicked: {
            // Call the function specified in the Python code
            ToDoApp.addItem(todoInput.text,todoModel)
            todoInput.text = ""
            console.log("listeye eklendi")
            todoListView.model = todoModel
        }
    }
}
