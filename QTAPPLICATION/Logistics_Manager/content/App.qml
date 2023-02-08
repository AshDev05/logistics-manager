// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0

import QtQuick 6.2
import QtQuick.Window 6.2
import Logistics_Manager

Window {
    width: mainScreen.width
    height: mainScreen.height

    visible: true
    title: "Logistics_Manager"

    Screen01 {
        id: mainScreen
    }

}

