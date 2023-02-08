

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2
import Logistics_Manager

Rectangle {
    id: background
    width: Constants.width
    height: Constants.height
    color: "#505050"

    Button {
        id: new_game
        x: 301
        y: 152
        width: 208
        height: 35
        text: qsTr("New Game")
        flat: false
        display: AbstractButton.TextOnly
        font.bold: true
        checkable: false

        Connections {
            target: new_game
            onClicked: animation.start()
        }
    }

    Text {
        id: title1
        x: 261
        y: 28
        width: 291
        height: 45
        text: qsTr("WELCOME TO")
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 32
        font.bold: true
        font.family: Constants.font.family

        SequentialAnimation {
            id: animation

            ColorAnimation {
                id: colorAnimation1
                target: background
                property: "color"
                to: "#2294c6"
                from: Constants.backgroundColor
            }

            ColorAnimation {
                id: colorAnimation2
                target: background
                property: "color"
                to: Constants.backgroundColor
                from: "#2294c6"
            }
        }
    }

    Label {
        id: label
        x: 284
        y: 79
        width: 243
        height: 44
        color: "#000000"
        text: qsTr("Logistics Manager")
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 20
        font.bold: true
    }
    states: [
        State {
            name: "clicked"
            when: new_game.checked

            PropertyChanges {
                target: title1
                text: qsTr("Button Checked")
            }
        }
    ]
}
