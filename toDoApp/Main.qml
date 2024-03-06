import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    title: "Todo App"

    Row {
        spacing: 10

        TextField {
            id: todoInput
            width: parent.width * 0.7
            placeholderText: "Enter todo..."
            focus: true // TextField'a klavye odaklanmasını sağlar
            Keys.onReturnPressed: {
                if (text !== "") {
                    todoApp.addTodoItem(text)
                    text = ""
                }
            }
        }

        Button {
            text: "Add"
            onClicked: {
                if (todoInput.text !== "") {
                    todoApp.addTodoItem(todoInput.text)
                    todoInput.text = ""
                }
            }
        }

        Button {
            text: "Remove"
            enabled: todoListView.currentIndex !== -1
            onClicked: {
                if (todoListView.currentIndex !== -1) {
                    todoApp.removeTodoItem(todoListView.currentIndex)
                }
            }
        }
    }

    ListView {
        id: todoListView
        width: parent.width
        height: parent.height - 50 // Altındaki butonlar için boşluk bırak
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        model: todoListModel
        delegate: todoDelegate
        focus: true
        Keys.onDeletePressed: {
            var index = currentIndex
            if (index >= 0 && index < count) {
                todoApp.removeTodoItem(index)
            }
        }
    }

    ListModel {
        id: todoListModel
    }

    Component {
        id: todoDelegate
        Rectangle {
            width: parent.width
            height: 30
            color: (index % 2 === 0) ? "lightgrey" : "white"
            Text {
                text: model.text
                anchors.centerIn: parent
            }
            MouseArea {
                anchors.fill: parent
                onClicked: todoListView.currentIndex = index
            }
        }
    }
}
