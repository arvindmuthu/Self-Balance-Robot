# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Jul  1 00:46:46 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(429, 445)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_server_settings = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_server_settings.setGeometry(QtCore.QRect(10, 10, 201, 111))
        self.groupBox_server_settings.setMouseTracking(False)
        self.groupBox_server_settings.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox_server_settings.setAutoFillBackground(True)
        self.groupBox_server_settings.setObjectName(_fromUtf8("groupBox_server_settings"))
        self.label_serverIP = QtGui.QLabel(self.groupBox_server_settings)
        self.label_serverIP.setGeometry(QtCore.QRect(0, 30, 66, 17))
        self.label_serverIP.setObjectName(_fromUtf8("label_serverIP"))
        self.label_serverPort = QtGui.QLabel(self.groupBox_server_settings)
        self.label_serverPort.setGeometry(QtCore.QRect(0, 60, 66, 17))
        self.label_serverPort.setObjectName(_fromUtf8("label_serverPort"))
        self.lineEdit_serverIP = QtGui.QLineEdit(self.groupBox_server_settings)
        self.lineEdit_serverIP.setGeometry(QtCore.QRect(70, 20, 113, 27))
        self.lineEdit_serverIP.setObjectName(_fromUtf8("lineEdit_serverIP"))
        self.lineEdit_serverPort = QtGui.QLineEdit(self.groupBox_server_settings)
        self.lineEdit_serverPort.setGeometry(QtCore.QRect(70, 50, 51, 27))
        self.lineEdit_serverPort.setInputMask(_fromUtf8(""))
        self.lineEdit_serverPort.setObjectName(_fromUtf8("lineEdit_serverPort"))
        self.pushButton_serverEnable = QtGui.QPushButton(self.groupBox_server_settings)
        self.pushButton_serverEnable.setGeometry(QtCore.QRect(70, 80, 111, 23))
        self.pushButton_serverEnable.setObjectName(_fromUtf8("pushButton_serverEnable"))
        self.groupBox_PID = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_PID.setGeometry(QtCore.QRect(10, 130, 251, 141))
        self.groupBox_PID.setMouseTracking(False)
        self.groupBox_PID.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox_PID.setAutoFillBackground(True)
        self.groupBox_PID.setObjectName(_fromUtf8("groupBox_PID"))
        self.label_KpAngle = QtGui.QLabel(self.groupBox_PID)
        self.label_KpAngle.setGeometry(QtCore.QRect(0, 30, 66, 17))
        self.label_KpAngle.setObjectName(_fromUtf8("label_KpAngle"))
        self.label_KiAngle = QtGui.QLabel(self.groupBox_PID)
        self.label_KiAngle.setGeometry(QtCore.QRect(0, 60, 66, 17))
        self.label_KiAngle.setObjectName(_fromUtf8("label_KiAngle"))
        self.doubleSpinBox_KpAngle = QtGui.QDoubleSpinBox(self.groupBox_PID)
        self.doubleSpinBox_KpAngle.setGeometry(QtCore.QRect(40, 20, 62, 27))
        self.doubleSpinBox_KpAngle.setDecimals(1)
        self.doubleSpinBox_KpAngle.setSingleStep(0.1)
        self.doubleSpinBox_KpAngle.setObjectName(_fromUtf8("doubleSpinBox_KpAngle"))
        self.doubleSpinBox_KiAngle = QtGui.QDoubleSpinBox(self.groupBox_PID)
        self.doubleSpinBox_KiAngle.setGeometry(QtCore.QRect(40, 50, 62, 27))
        self.doubleSpinBox_KiAngle.setDecimals(1)
        self.doubleSpinBox_KiAngle.setSingleStep(0.1)
        self.doubleSpinBox_KiAngle.setObjectName(_fromUtf8("doubleSpinBox_KiAngle"))
        self.label_KdAngle = QtGui.QLabel(self.groupBox_PID)
        self.label_KdAngle.setGeometry(QtCore.QRect(0, 90, 66, 17))
        self.label_KdAngle.setObjectName(_fromUtf8("label_KdAngle"))
        self.doubleSpinBox_KdAngle = QtGui.QDoubleSpinBox(self.groupBox_PID)
        self.doubleSpinBox_KdAngle.setGeometry(QtCore.QRect(40, 80, 62, 27))
        self.doubleSpinBox_KdAngle.setDecimals(1)
        self.doubleSpinBox_KdAngle.setSingleStep(0.1)
        self.doubleSpinBox_KdAngle.setObjectName(_fromUtf8("doubleSpinBox_KdAngle"))
        self.pushButton_sendPID = QtGui.QPushButton(self.groupBox_PID)
        self.pushButton_sendPID.setGeometry(QtCore.QRect(120, 110, 101, 23))
        self.pushButton_sendPID.setObjectName(_fromUtf8("pushButton_sendPID"))
        self.label_KiSpeed = QtGui.QLabel(self.groupBox_PID)
        self.label_KiSpeed.setGeometry(QtCore.QRect(120, 60, 66, 17))
        self.label_KiSpeed.setObjectName(_fromUtf8("label_KiSpeed"))
        self.label_KpSpeed = QtGui.QLabel(self.groupBox_PID)
        self.label_KpSpeed.setGeometry(QtCore.QRect(120, 30, 66, 17))
        self.label_KpSpeed.setObjectName(_fromUtf8("label_KpSpeed"))
        self.doubleSpinBox_KiSpeed = QtGui.QDoubleSpinBox(self.groupBox_PID)
        self.doubleSpinBox_KiSpeed.setGeometry(QtCore.QRect(160, 50, 62, 27))
        self.doubleSpinBox_KiSpeed.setDecimals(1)
        self.doubleSpinBox_KiSpeed.setSingleStep(0.1)
        self.doubleSpinBox_KiSpeed.setObjectName(_fromUtf8("doubleSpinBox_KiSpeed"))
        self.label_KdSpeed = QtGui.QLabel(self.groupBox_PID)
        self.label_KdSpeed.setGeometry(QtCore.QRect(120, 90, 66, 17))
        self.label_KdSpeed.setObjectName(_fromUtf8("label_KdSpeed"))
        self.doubleSpinBox_KdSpeed = QtGui.QDoubleSpinBox(self.groupBox_PID)
        self.doubleSpinBox_KdSpeed.setGeometry(QtCore.QRect(160, 80, 62, 27))
        self.doubleSpinBox_KdSpeed.setDecimals(1)
        self.doubleSpinBox_KdSpeed.setSingleStep(0.1)
        self.doubleSpinBox_KdSpeed.setObjectName(_fromUtf8("doubleSpinBox_KdSpeed"))
        self.doubleSpinBox_KpSpeed = QtGui.QDoubleSpinBox(self.groupBox_PID)
        self.doubleSpinBox_KpSpeed.setGeometry(QtCore.QRect(160, 20, 62, 27))
        self.doubleSpinBox_KpSpeed.setDecimals(1)
        self.doubleSpinBox_KpSpeed.setSingleStep(0.1)
        self.doubleSpinBox_KpSpeed.setObjectName(_fromUtf8("doubleSpinBox_KpSpeed"))
        self.pushButton_sendPID_Zero = QtGui.QPushButton(self.groupBox_PID)
        self.pushButton_sendPID_Zero.setGeometry(QtCore.QRect(0, 110, 101, 23))
        self.pushButton_sendPID_Zero.setObjectName(_fromUtf8("pushButton_sendPID_Zero"))
        self.groupBox_Orientation = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Orientation.setGeometry(QtCore.QRect(10, 280, 121, 121))
        self.groupBox_Orientation.setMouseTracking(False)
        self.groupBox_Orientation.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox_Orientation.setAutoFillBackground(True)
        self.groupBox_Orientation.setObjectName(_fromUtf8("groupBox_Orientation"))
        self.label_roll = QtGui.QLabel(self.groupBox_Orientation)
        self.label_roll.setGeometry(QtCore.QRect(0, 30, 66, 17))
        self.label_roll.setObjectName(_fromUtf8("label_roll"))
        self.label_pitch = QtGui.QLabel(self.groupBox_Orientation)
        self.label_pitch.setGeometry(QtCore.QRect(0, 60, 66, 17))
        self.label_pitch.setObjectName(_fromUtf8("label_pitch"))
        self.label_yaw = QtGui.QLabel(self.groupBox_Orientation)
        self.label_yaw.setGeometry(QtCore.QRect(0, 90, 66, 17))
        self.label_yaw.setObjectName(_fromUtf8("label_yaw"))
        self.lineEdit_roll = QtGui.QLineEdit(self.groupBox_Orientation)
        self.lineEdit_roll.setGeometry(QtCore.QRect(40, 20, 71, 27))
        self.lineEdit_roll.setObjectName(_fromUtf8("lineEdit_roll"))
        self.lineEdit_pitch = QtGui.QLineEdit(self.groupBox_Orientation)
        self.lineEdit_pitch.setGeometry(QtCore.QRect(40, 50, 71, 27))
        self.lineEdit_pitch.setObjectName(_fromUtf8("lineEdit_pitch"))
        self.lineEdit_yaw = QtGui.QLineEdit(self.groupBox_Orientation)
        self.lineEdit_yaw.setGeometry(QtCore.QRect(40, 80, 71, 27))
        self.lineEdit_yaw.setObjectName(_fromUtf8("lineEdit_yaw"))
        self.groupBox_Motor = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Motor.setGeometry(QtCore.QRect(270, 130, 121, 181))
        self.groupBox_Motor.setMouseTracking(False)
        self.groupBox_Motor.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox_Motor.setAutoFillBackground(True)
        self.groupBox_Motor.setObjectName(_fromUtf8("groupBox_Motor"))
        self.label_speedPid = QtGui.QLabel(self.groupBox_Motor)
        self.label_speedPid.setGeometry(QtCore.QRect(0, 30, 66, 17))
        self.label_speedPid.setObjectName(_fromUtf8("label_speedPid"))
        self.label_speedRun = QtGui.QLabel(self.groupBox_Motor)
        self.label_speedRun.setGeometry(QtCore.QRect(0, 60, 66, 17))
        self.label_speedRun.setObjectName(_fromUtf8("label_speedRun"))
        self.label_speedTurn = QtGui.QLabel(self.groupBox_Motor)
        self.label_speedTurn.setGeometry(QtCore.QRect(0, 90, 66, 17))
        self.label_speedTurn.setObjectName(_fromUtf8("label_speedTurn"))
        self.lineEdit_speedPID = QtGui.QLineEdit(self.groupBox_Motor)
        self.lineEdit_speedPID.setGeometry(QtCore.QRect(40, 20, 71, 27))
        self.lineEdit_speedPID.setObjectName(_fromUtf8("lineEdit_speedPID"))
        self.lineEdit_speedRun = QtGui.QLineEdit(self.groupBox_Motor)
        self.lineEdit_speedRun.setGeometry(QtCore.QRect(40, 50, 71, 27))
        self.lineEdit_speedRun.setObjectName(_fromUtf8("lineEdit_speedRun"))
        self.lineEdit_speedTurn = QtGui.QLineEdit(self.groupBox_Motor)
        self.lineEdit_speedTurn.setGeometry(QtCore.QRect(40, 80, 71, 27))
        self.lineEdit_speedTurn.setObjectName(_fromUtf8("lineEdit_speedTurn"))
        self.label_speedLeft = QtGui.QLabel(self.groupBox_Motor)
        self.label_speedLeft.setGeometry(QtCore.QRect(0, 120, 66, 17))
        self.label_speedLeft.setObjectName(_fromUtf8("label_speedLeft"))
        self.lineEdit_speedLeft = QtGui.QLineEdit(self.groupBox_Motor)
        self.lineEdit_speedLeft.setGeometry(QtCore.QRect(40, 110, 71, 27))
        self.lineEdit_speedLeft.setObjectName(_fromUtf8("lineEdit_speedLeft"))
        self.label_speedRight = QtGui.QLabel(self.groupBox_Motor)
        self.label_speedRight.setGeometry(QtCore.QRect(0, 150, 66, 17))
        self.label_speedRight.setObjectName(_fromUtf8("label_speedRight"))
        self.lineEdit_speedRight = QtGui.QLineEdit(self.groupBox_Motor)
        self.lineEdit_speedRight.setGeometry(QtCore.QRect(40, 140, 71, 27))
        self.lineEdit_speedRight.setObjectName(_fromUtf8("lineEdit_speedRight"))
        self.groupBox_client_settings = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_client_settings.setGeometry(QtCore.QRect(220, 10, 201, 111))
        self.groupBox_client_settings.setMouseTracking(False)
        self.groupBox_client_settings.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox_client_settings.setAutoFillBackground(True)
        self.groupBox_client_settings.setObjectName(_fromUtf8("groupBox_client_settings"))
        self.label_clientIP = QtGui.QLabel(self.groupBox_client_settings)
        self.label_clientIP.setGeometry(QtCore.QRect(0, 30, 66, 17))
        self.label_clientIP.setObjectName(_fromUtf8("label_clientIP"))
        self.label_clientPort = QtGui.QLabel(self.groupBox_client_settings)
        self.label_clientPort.setGeometry(QtCore.QRect(0, 60, 66, 17))
        self.label_clientPort.setObjectName(_fromUtf8("label_clientPort"))
        self.lineEdit_clientIP = QtGui.QLineEdit(self.groupBox_client_settings)
        self.lineEdit_clientIP.setGeometry(QtCore.QRect(70, 20, 113, 27))
        self.lineEdit_clientIP.setObjectName(_fromUtf8("lineEdit_clientIP"))
        self.lineEdit_clientPort = QtGui.QLineEdit(self.groupBox_client_settings)
        self.lineEdit_clientPort.setGeometry(QtCore.QRect(70, 50, 51, 27))
        self.lineEdit_clientPort.setObjectName(_fromUtf8("lineEdit_clientPort"))
        self.pushButton_clientEnable = QtGui.QPushButton(self.groupBox_client_settings)
        self.pushButton_clientEnable.setGeometry(QtCore.QRect(70, 80, 111, 23))
        self.pushButton_clientEnable.setObjectName(_fromUtf8("pushButton_clientEnable"))
        self.pushButton_restartUDP = QtGui.QPushButton(self.centralwidget)
        self.pushButton_restartUDP.setGeometry(QtCore.QRect(280, 360, 111, 23))
        self.pushButton_restartUDP.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pushButton_restartUDP.setObjectName(_fromUtf8("pushButton_restartUDP"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_server_settings.setTitle(_translate("MainWindow", "Connection settings - Server", None))
        self.label_serverIP.setText(_translate("MainWindow", "IP Addr:", None))
        self.label_serverPort.setText(_translate("MainWindow", "Port:", None))
        self.lineEdit_serverIP.setText(_translate("MainWindow", "192.168.1.35", None))
        self.lineEdit_serverPort.setText(_translate("MainWindow", "5000", None))
        self.pushButton_serverEnable.setText(_translate("MainWindow", "Enable", None))
        self.groupBox_PID.setTitle(_translate("MainWindow", "PID - Angle and Speed Parameters", None))
        self.label_KpAngle.setText(_translate("MainWindow", "Kp:", None))
        self.label_KiAngle.setText(_translate("MainWindow", "Ki:", None))
        self.label_KdAngle.setText(_translate("MainWindow", "Kd:", None))
        self.pushButton_sendPID.setText(_translate("MainWindow", "Send...", None))
        self.label_KiSpeed.setText(_translate("MainWindow", "Ki:", None))
        self.label_KpSpeed.setText(_translate("MainWindow", "Kp:", None))
        self.label_KdSpeed.setText(_translate("MainWindow", "Kd:", None))
        self.pushButton_sendPID_Zero.setText(_translate("MainWindow", "Zero", None))
        self.groupBox_Orientation.setTitle(_translate("MainWindow", "Orientation", None))
        self.label_roll.setText(_translate("MainWindow", "Roll:", None))
        self.label_pitch.setText(_translate("MainWindow", "Pitch:", None))
        self.label_yaw.setText(_translate("MainWindow", "Yaw:", None))
        self.groupBox_Motor.setTitle(_translate("MainWindow", "Motor speed", None))
        self.label_speedPid.setText(_translate("MainWindow", "PID", None))
        self.label_speedRun.setText(_translate("MainWindow", "Run", None))
        self.label_speedTurn.setText(_translate("MainWindow", "Turn", None))
        self.label_speedLeft.setText(_translate("MainWindow", "Left", None))
        self.label_speedRight.setText(_translate("MainWindow", "Right", None))
        self.groupBox_client_settings.setTitle(_translate("MainWindow", "Connection settings - Client", None))
        self.label_clientIP.setText(_translate("MainWindow", "IP Addr:", None))
        self.label_clientPort.setText(_translate("MainWindow", "Port:", None))
        self.lineEdit_clientIP.setText(_translate("MainWindow", "192.168.1.49", None))
        self.lineEdit_clientPort.setText(_translate("MainWindow", "5001", None))
        self.pushButton_clientEnable.setText(_translate("MainWindow", "Enable", None))
        self.pushButton_restartUDP.setText(_translate("MainWindow", "Restart UDP...", None))

