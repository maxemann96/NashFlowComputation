# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWdw.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1159, 1019)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.plotFrame = QtGui.QFrame(self.tab)
        self.plotFrame.setGeometry(QtCore.QRect(10, 10, 841, 531))
        self.plotFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.plotFrame.setObjectName(_fromUtf8("plotFrame"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(860, 10, 131, 311))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 68, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 68, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tailLineEdit = QtGui.QLineEdit(self.groupBox)
        self.tailLineEdit.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.tailLineEdit.setObjectName(_fromUtf8("tailLineEdit"))
        self.headLineEdit = QtGui.QLineEdit(self.groupBox)
        self.headLineEdit.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.headLineEdit.setObjectName(_fromUtf8("headLineEdit"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 81, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.transitTimeLineEdit = QtGui.QLineEdit(self.groupBox)
        self.transitTimeLineEdit.setGeometry(QtCore.QRect(10, 190, 111, 21))
        self.transitTimeLineEdit.setObjectName(_fromUtf8("transitTimeLineEdit"))
        self.capacityLineEdit = QtGui.QLineEdit(self.groupBox)
        self.capacityLineEdit.setGeometry(QtCore.QRect(10, 140, 111, 21))
        self.capacityLineEdit.setObjectName(_fromUtf8("capacityLineEdit"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 81, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.updateEdgeButton = QtGui.QPushButton(self.groupBox)
        self.updateEdgeButton.setGeometry(QtCore.QRect(10, 230, 111, 31))
        self.updateEdgeButton.setAutoDefault(False)
        self.updateEdgeButton.setDefault(False)
        self.updateEdgeButton.setFlat(False)
        self.updateEdgeButton.setObjectName(_fromUtf8("updateEdgeButton"))
        self.deleteEdgeButton = QtGui.QPushButton(self.groupBox)
        self.deleteEdgeButton.setGeometry(QtCore.QRect(10, 270, 111, 31))
        self.deleteEdgeButton.setAutoDefault(False)
        self.deleteEdgeButton.setDefault(False)
        self.deleteEdgeButton.setFlat(False)
        self.deleteEdgeButton.setObjectName(_fromUtf8("deleteEdgeButton"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(1000, 10, 131, 311))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 68, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.nodeNameLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.nodeNameLineEdit.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.nodeNameLineEdit.setObjectName(_fromUtf8("nodeNameLineEdit"))
        self.nodeXLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.nodeXLineEdit.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.nodeXLineEdit.setObjectName(_fromUtf8("nodeXLineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 68, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 68, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.nodeYLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.nodeYLineEdit.setGeometry(QtCore.QRect(10, 140, 111, 21))
        self.nodeYLineEdit.setObjectName(_fromUtf8("nodeYLineEdit"))
        self.updateNodeButton = QtGui.QPushButton(self.groupBox_2)
        self.updateNodeButton.setGeometry(QtCore.QRect(10, 230, 111, 31))
        self.updateNodeButton.setAutoDefault(False)
        self.updateNodeButton.setDefault(False)
        self.updateNodeButton.setFlat(False)
        self.updateNodeButton.setObjectName(_fromUtf8("updateNodeButton"))
        self.deleteNodeButton = QtGui.QPushButton(self.groupBox_2)
        self.deleteNodeButton.setGeometry(QtCore.QRect(10, 270, 111, 31))
        self.deleteNodeButton.setAutoDefault(False)
        self.deleteNodeButton.setDefault(False)
        self.deleteNodeButton.setFlat(False)
        self.deleteNodeButton.setObjectName(_fromUtf8("deleteNodeButton"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 550, 1121, 181))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(950, 40, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.inflowLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.inflowLineEdit.setGeometry(QtCore.QRect(950, 60, 131, 21))
        self.inflowLineEdit.setObjectName(_fromUtf8("inflowLineEdit"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.outputDirectoryLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.outputDirectoryLineEdit.setGeometry(QtCore.QRect(10, 40, 601, 21))
        self.outputDirectoryLineEdit.setObjectName(_fromUtf8("outputDirectoryLineEdit"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(950, 90, 141, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.intervalsLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.intervalsLineEdit.setGeometry(QtCore.QRect(950, 110, 131, 21))
        self.intervalsLineEdit.setObjectName(_fromUtf8("intervalsLineEdit"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 171, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.outputDirectoryPushButton = QtGui.QPushButton(self.groupBox_3)
        self.outputDirectoryPushButton.setGeometry(QtCore.QRect(620, 40, 131, 21))
        self.outputDirectoryPushButton.setObjectName(_fromUtf8("outputDirectoryPushButton"))
        self.scipPathLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.scipPathLineEdit.setGeometry(QtCore.QRect(10, 90, 601, 21))
        self.scipPathLineEdit.setObjectName(_fromUtf8("scipPathLineEdit"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.scipPathPushButton = QtGui.QPushButton(self.groupBox_3)
        self.scipPathPushButton.setGeometry(QtCore.QRect(620, 90, 131, 21))
        self.scipPathPushButton.setObjectName(_fromUtf8("scipPathPushButton"))
        self.cleanUpCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.cleanUpCheckBox.setGeometry(QtCore.QRect(770, 40, 151, 22))
        self.cleanUpCheckBox.setObjectName(_fromUtf8("cleanUpCheckBox"))
        self.timeoutLabel = QtGui.QLabel(self.groupBox_3)
        self.timeoutLabel.setEnabled(False)
        self.timeoutLabel.setGeometry(QtCore.QRect(770, 100, 101, 17))
        self.timeoutLabel.setObjectName(_fromUtf8("timeoutLabel"))
        self.timeoutLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.timeoutLineEdit.setEnabled(False)
        self.timeoutLineEdit.setGeometry(QtCore.QRect(770, 120, 131, 21))
        self.timeoutLineEdit.setObjectName(_fromUtf8("timeoutLineEdit"))
        self.activateTimeoutCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.activateTimeoutCheckBox.setGeometry(QtCore.QRect(770, 70, 151, 22))
        self.activateTimeoutCheckBox.setObjectName(_fromUtf8("activateTimeoutCheckBox"))
        self.templateComboBox = QtGui.QComboBox(self.groupBox_3)
        self.templateComboBox.setGeometry(QtCore.QRect(10, 140, 741, 31))
        self.templateComboBox.setObjectName(_fromUtf8("templateComboBox"))
        self.templateComboBox.addItem(_fromUtf8(""))
        self.templateComboBox.addItem(_fromUtf8(""))
        self.templateComboBox.addItem(_fromUtf8(""))
        self.computeFlowPushButton = QtGui.QPushButton(self.tab)
        self.computeFlowPushButton.setGeometry(QtCore.QRect(730, 750, 401, 181))
        self.computeFlowPushButton.setAutoDefault(False)
        self.computeFlowPushButton.setDefault(False)
        self.computeFlowPushButton.setFlat(False)
        self.computeFlowPushButton.setObjectName(_fromUtf8("computeFlowPushButton"))
        self.nodeSelectionListWidget = QtGui.QListWidget(self.tab)
        self.nodeSelectionListWidget.setGeometry(QtCore.QRect(1000, 330, 131, 211))
        self.nodeSelectionListWidget.setObjectName(_fromUtf8("nodeSelectionListWidget"))
        self.edgeSelectionListWidget = QtGui.QListWidget(self.tab)
        self.edgeSelectionListWidget.setGeometry(QtCore.QRect(860, 330, 131, 211))
        self.edgeSelectionListWidget.setObjectName(_fromUtf8("edgeSelectionListWidget"))
        self.logPlainTextEdit = QtGui.QPlainTextEdit(self.tab)
        self.logPlainTextEdit.setGeometry(QtCore.QRect(10, 750, 701, 181))
        self.logPlainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.logPlainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logPlainTextEdit.setObjectName(_fromUtf8("logPlainTextEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(670, 10, 461, 491))
        self.groupBox_5.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.plotDiagramFrame = QtGui.QFrame(self.groupBox_5)
        self.plotDiagramFrame.setGeometry(QtCore.QRect(10, 20, 441, 401))
        self.plotDiagramFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotDiagramFrame.setObjectName(_fromUtf8("plotDiagramFrame"))
        self.exportDiagramPushButton = QtGui.QPushButton(self.groupBox_5)
        self.exportDiagramPushButton.setGeometry(QtCore.QRect(230, 430, 221, 21))
        self.exportDiagramPushButton.setObjectName(_fromUtf8("exportDiagramPushButton"))
        self.exportComboBox = QtGui.QComboBox(self.groupBox_5)
        self.exportComboBox.setGeometry(QtCore.QRect(14, 430, 211, 21))
        self.exportComboBox.setObjectName(_fromUtf8("exportComboBox"))
        self.exportComboBox.addItem(_fromUtf8(""))
        self.exportComboBox.addItem(_fromUtf8(""))
        self.currentSliderTimeLabel = QtGui.QLabel(self.groupBox_5)
        self.currentSliderTimeLabel.setGeometry(QtCore.QRect(120, 460, 61, 21))
        self.currentSliderTimeLabel.setObjectName(_fromUtf8("currentSliderTimeLabel"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(20, 460, 91, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.setTimePushButton = QtGui.QPushButton(self.groupBox_5)
        self.setTimePushButton.setGeometry(QtCore.QRect(230, 460, 221, 21))
        self.setTimePushButton.setObjectName(_fromUtf8("setTimePushButton"))
        self.setTimeLineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.setTimeLineEdit.setGeometry(QtCore.QRect(160, 460, 61, 21))
        self.setTimeLineEdit.setText(_fromUtf8(""))
        self.setTimeLineEdit.setObjectName(_fromUtf8("setTimeLineEdit"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 510, 851, 431))
        self.groupBox_4.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.plotNTFFrame = QtGui.QFrame(self.groupBox_4)
        self.plotNTFFrame.setGeometry(QtCore.QRect(10, 20, 631, 401))
        self.plotNTFFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotNTFFrame.setObjectName(_fromUtf8("plotNTFFrame"))
        self.intervalsListWidget = QtGui.QListWidget(self.groupBox_4)
        self.intervalsListWidget.setGeometry(QtCore.QRect(650, 20, 191, 351))
        self.intervalsListWidget.setFrameShape(QtGui.QFrame.Box)
        self.intervalsListWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.intervalsListWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.intervalsListWidget.setObjectName(_fromUtf8("intervalsListWidget"))
        self.showEdgesWithoutFlowCheckBox = QtGui.QCheckBox(self.groupBox_4)
        self.showEdgesWithoutFlowCheckBox.setGeometry(QtCore.QRect(648, 390, 191, 22))
        self.showEdgesWithoutFlowCheckBox.setChecked(True)
        self.showEdgesWithoutFlowCheckBox.setObjectName(_fromUtf8("showEdgesWithoutFlowCheckBox"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 10, 651, 491))
        self.groupBox_7.setAutoFillBackground(False)
        self.groupBox_7.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.plotAnimationFrame = QtGui.QFrame(self.groupBox_7)
        self.plotAnimationFrame.setGeometry(QtCore.QRect(10, 20, 630, 400))
        self.plotAnimationFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotAnimationFrame.setObjectName(_fromUtf8("plotAnimationFrame"))
        self.timeSlider = QtGui.QSlider(self.groupBox_7)
        self.timeSlider.setGeometry(QtCore.QRect(10, 420, 631, 19))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName(_fromUtf8("timeSlider"))
        self.generateAnimationPushButton = QtGui.QPushButton(self.groupBox_7)
        self.generateAnimationPushButton.setGeometry(QtCore.QRect(298, 440, 131, 21))
        self.generateAnimationPushButton.setObjectName(_fromUtf8("generateAnimationPushButton"))
        self.label_13 = QtGui.QLabel(self.groupBox_7)
        self.label_13.setGeometry(QtCore.QRect(10, 440, 121, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.animationStartLineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.animationStartLineEdit.setGeometry(QtCore.QRect(140, 440, 61, 21))
        self.animationStartLineEdit.setText(_fromUtf8(""))
        self.animationStartLineEdit.setObjectName(_fromUtf8("animationStartLineEdit"))
        self.label_14 = QtGui.QLabel(self.groupBox_7)
        self.label_14.setGeometry(QtCore.QRect(210, 440, 21, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.animationEndLineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.animationEndLineEdit.setGeometry(QtCore.QRect(230, 440, 61, 21))
        self.animationEndLineEdit.setText(_fromUtf8(""))
        self.animationEndLineEdit.setObjectName(_fromUtf8("animationEndLineEdit"))
        self.label_18 = QtGui.QLabel(self.groupBox_7)
        self.label_18.setGeometry(QtCore.QRect(10, 460, 51, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.currentFocusLabel = QtGui.QLabel(self.groupBox_7)
        self.currentFocusLabel.setGeometry(QtCore.QRect(60, 460, 71, 21))
        self.currentFocusLabel.setObjectName(_fromUtf8("currentFocusLabel"))
        self.currentCapacityLabel = QtGui.QLabel(self.groupBox_7)
        self.currentCapacityLabel.setGeometry(QtCore.QRect(210, 460, 71, 21))
        self.currentCapacityLabel.setObjectName(_fromUtf8("currentCapacityLabel"))
        self.label_19 = QtGui.QLabel(self.groupBox_7)
        self.label_19.setGeometry(QtCore.QRect(140, 460, 71, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_7)
        self.label_20.setGeometry(QtCore.QRect(300, 460, 91, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.currentTransitTimeLabel = QtGui.QLabel(self.groupBox_7)
        self.currentTransitTimeLabel.setGeometry(QtCore.QRect(390, 460, 71, 21))
        self.currentTransitTimeLabel.setObjectName(_fromUtf8("currentTransitTimeLabel"))
        self.playPushButton = QtGui.QPushButton(self.groupBox_7)
        self.playPushButton.setGeometry(QtCore.QRect(470, 440, 51, 41))
        self.playPushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/playpausestop/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playPushButton.setIcon(icon)
        self.playPushButton.setObjectName(_fromUtf8("playPushButton"))
        self.pausePushButton = QtGui.QPushButton(self.groupBox_7)
        self.pausePushButton.setGeometry(QtCore.QRect(530, 440, 51, 41))
        self.pausePushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/playpausestop/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pausePushButton.setIcon(icon1)
        self.pausePushButton.setObjectName(_fromUtf8("pausePushButton"))
        self.stopPushButton = QtGui.QPushButton(self.groupBox_7)
        self.stopPushButton.setGeometry(QtCore.QRect(590, 440, 51, 41))
        self.stopPushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/playpausestop/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopPushButton.setIcon(icon2)
        self.stopPushButton.setObjectName(_fromUtf8("stopPushButton"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(860, 510, 271, 301))
        self.groupBox_6.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_21 = QtGui.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(10, 40, 151, 17))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.groupBox_6)
        self.label_22.setGeometry(QtCore.QRect(10, 60, 151, 17))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.groupBox_6)
        self.label_23.setGeometry(QtCore.QRect(10, 180, 151, 17))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(10, 160, 151, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.groupBox_6)
        self.label_25.setGeometry(QtCore.QRect(10, 200, 151, 17))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.groupBox_6)
        self.label_26.setGeometry(QtCore.QRect(10, 90, 151, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.groupBox_6)
        self.label_27.setGeometry(QtCore.QRect(10, 130, 151, 17))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.groupBox_6)
        self.label_28.setGeometry(QtCore.QRect(10, 110, 151, 17))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.groupBox_6)
        self.label_29.setGeometry(QtCore.QRect(10, 20, 151, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.groupBox_6)
        self.label_30.setGeometry(QtCore.QRect(10, 230, 151, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.groupBox_6)
        self.label_31.setGeometry(QtCore.QRect(10, 270, 151, 17))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.groupBox_6)
        self.label_32.setGeometry(QtCore.QRect(10, 250, 151, 17))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.statNumberOfNodesLabel = QtGui.QLabel(self.groupBox_6)
        self.statNumberOfNodesLabel.setGeometry(QtCore.QRect(170, 40, 68, 17))
        self.statNumberOfNodesLabel.setObjectName(_fromUtf8("statNumberOfNodesLabel"))
        self.statNumberOfEdgesLabel = QtGui.QLabel(self.groupBox_6)
        self.statNumberOfEdgesLabel.setGeometry(QtCore.QRect(170, 60, 68, 17))
        self.statNumberOfEdgesLabel.setObjectName(_fromUtf8("statNumberOfEdgesLabel"))
        self.statAvgDeletedEdgesLabel = QtGui.QLabel(self.groupBox_6)
        self.statAvgDeletedEdgesLabel.setGeometry(QtCore.QRect(170, 130, 68, 17))
        self.statAvgDeletedEdgesLabel.setObjectName(_fromUtf8("statAvgDeletedEdgesLabel"))
        self.statAvgDeletedNodesLabel = QtGui.QLabel(self.groupBox_6)
        self.statAvgDeletedNodesLabel.setGeometry(QtCore.QRect(170, 110, 68, 17))
        self.statAvgDeletedNodesLabel.setObjectName(_fromUtf8("statAvgDeletedNodesLabel"))
        self.statTotalSolvedIPsLabel = QtGui.QLabel(self.groupBox_6)
        self.statTotalSolvedIPsLabel.setGeometry(QtCore.QRect(170, 200, 68, 17))
        self.statTotalSolvedIPsLabel.setObjectName(_fromUtf8("statTotalSolvedIPsLabel"))
        self.statAvgSolvedIPsLabel = QtGui.QLabel(self.groupBox_6)
        self.statAvgSolvedIPsLabel.setGeometry(QtCore.QRect(170, 180, 68, 17))
        self.statAvgSolvedIPsLabel.setObjectName(_fromUtf8("statAvgSolvedIPsLabel"))
        self.statTotalTimeLabel = QtGui.QLabel(self.groupBox_6)
        self.statTotalTimeLabel.setGeometry(QtCore.QRect(170, 270, 68, 17))
        self.statTotalTimeLabel.setObjectName(_fromUtf8("statTotalTimeLabel"))
        self.statAvgTimeLabel = QtGui.QLabel(self.groupBox_6)
        self.statAvgTimeLabel.setGeometry(QtCore.QRect(170, 250, 68, 17))
        self.statAvgTimeLabel.setObjectName(_fromUtf8("statAvgTimeLabel"))
        self.computeIntervalPushButton = QtGui.QPushButton(self.tab_2)
        self.computeIntervalPushButton.setGeometry(QtCore.QRect(860, 820, 271, 121))
        self.computeIntervalPushButton.setAutoDefault(False)
        self.computeIntervalPushButton.setDefault(False)
        self.computeIntervalPushButton.setFlat(False)
        self.computeIntervalPushButton.setObjectName(_fromUtf8("computeIntervalPushButton"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1159, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad_Graph = QtGui.QAction(MainWindow)
        self.actionLoad_Graph.setObjectName(_fromUtf8("actionLoad_Graph"))
        self.actionSave_Graph = QtGui.QAction(MainWindow)
        self.actionSave_Graph.setObjectName(_fromUtf8("actionSave_Graph"))
        self.actionNew_graph = QtGui.QAction(MainWindow)
        self.actionNew_graph.setObjectName(_fromUtf8("actionNew_graph"))
        self.actionLoad_graph = QtGui.QAction(MainWindow)
        self.actionLoad_graph.setObjectName(_fromUtf8("actionLoad_graph"))
        self.actionSave_graph = QtGui.QAction(MainWindow)
        self.actionSave_graph.setObjectName(_fromUtf8("actionSave_graph"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionLoad_NashFlow = QtGui.QAction(MainWindow)
        self.actionLoad_NashFlow.setEnabled(False)
        self.actionLoad_NashFlow.setVisible(False)
        self.actionLoad_NashFlow.setObjectName(_fromUtf8("actionLoad_NashFlow"))
        self.actionSave_NashFlow = QtGui.QAction(MainWindow)
        self.actionSave_NashFlow.setVisible(False)
        self.actionSave_NashFlow.setObjectName(_fromUtf8("actionSave_NashFlow"))
        self.actionOpen_manual = QtGui.QAction(MainWindow)
        self.actionOpen_manual.setObjectName(_fromUtf8("actionOpen_manual"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew_graph)
        self.menuFile.addAction(self.actionLoad_graph)
        self.menuFile.addAction(self.actionSave_graph)
        self.menuFile.addAction(self.actionLoad_NashFlow)
        self.menuFile.addAction(self.actionSave_NashFlow)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionOpen_manual)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Edge", None))
        self.label_4.setText(_translate("MainWindow", "Head", None))
        self.label_5.setText(_translate("MainWindow", "Tail", None))
        self.label_6.setText(_translate("MainWindow", "Transit time", None))
        self.label_7.setText(_translate("MainWindow", "Capacity", None))
        self.updateEdgeButton.setText(_translate("MainWindow", "Add/Upd. edge", None))
        self.deleteEdgeButton.setText(_translate("MainWindow", "Delete edge", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Node", None))
        self.label.setText(_translate("MainWindow", "Name", None))
        self.label_2.setText(_translate("MainWindow", "X-position", None))
        self.label_3.setText(_translate("MainWindow", "Y-position", None))
        self.updateNodeButton.setText(_translate("MainWindow", "Update node", None))
        self.deleteNodeButton.setText(_translate("MainWindow", "Delete node", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Config", None))
        self.label_8.setText(_translate("MainWindow", "Inflow Rate", None))
        self.inflowLineEdit.setText(_translate("MainWindow", "0", None))
        self.label_9.setText(_translate("MainWindow", "Output directory", None))
        self.label_10.setText(_translate("MainWindow", "# Intervals (-1 = all)", None))
        self.intervalsLineEdit.setText(_translate("MainWindow", "-1", None))
        self.label_11.setText(_translate("MainWindow", "Algorithm & Template", None))
        self.outputDirectoryPushButton.setText(_translate("MainWindow", "Select directory", None))
        self.label_12.setText(_translate("MainWindow", "SCIP path", None))
        self.scipPathPushButton.setText(_translate("MainWindow", "Select binary", None))
        self.cleanUpCheckBox.setText(_translate("MainWindow", "Activate Clean-up", None))
        self.timeoutLabel.setText(_translate("MainWindow", "Timeout (in s)", None))
        self.timeoutLineEdit.setText(_translate("MainWindow", "300", None))
        self.activateTimeoutCheckBox.setText(_translate("MainWindow", "Activate timeout", None))
        self.templateComboBox.setItemText(0, _translate("MainWindow", "1. Basic algorithm by Cominetti, Correa and Larré", None))
        self.templateComboBox.setItemText(1, _translate("MainWindow", "2. Solve only LP/IP", None))
        self.templateComboBox.setItemText(2, _translate("MainWindow", "3. Advanced algorithm", None))
        self.computeFlowPushButton.setText(_translate("MainWindow", "Compute Nashflow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Create/Load Graph", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Diagram", None))
        self.exportDiagramPushButton.setText(_translate("MainWindow", "Export", None))
        self.exportComboBox.setItemText(0, _translate("MainWindow", "Export as .PDF", None))
        self.exportComboBox.setItemText(1, _translate("MainWindow", "Export as .PGF", None))
        self.currentSliderTimeLabel.setText(_translate("MainWindow", "0", None))
        self.label_17.setText(_translate("MainWindow", "Current time:", None))
        self.setTimePushButton.setText(_translate("MainWindow", "Set time", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Normalized Thin Flows", None))
        self.showEdgesWithoutFlowCheckBox.setText(_translate("MainWindow", "Show edges w/out flow", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Nash Flow over time", None))
        self.generateAnimationPushButton.setText(_translate("MainWindow", "Generate", None))
        self.label_13.setText(_translate("MainWindow", "Animation range:", None))
        self.label_14.setText(_translate("MainWindow", "-", None))
        self.label_18.setText(_translate("MainWindow", "Focus:", None))
        self.currentFocusLabel.setText(_translate("MainWindow", "N/A", None))
        self.currentCapacityLabel.setText(_translate("MainWindow", "N/A", None))
        self.label_19.setText(_translate("MainWindow", "Capacity:", None))
        self.label_20.setText(_translate("MainWindow", "Transit time:", None))
        self.currentTransitTimeLabel.setText(_translate("MainWindow", "N/A", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Statistics", None))
        self.label_21.setText(_translate("MainWindow", "Number of nodes:", None))
        self.label_22.setText(_translate("MainWindow", "Number of edges:", None))
        self.label_23.setText(_translate("MainWindow", "Avg. # per interval:", None))
        self.label_24.setText(_translate("MainWindow", "Solved IPs", None))
        self.label_25.setText(_translate("MainWindow", "Total # solved IPs:", None))
        self.label_26.setText(_translate("MainWindow", "Preprocessing", None))
        self.label_27.setText(_translate("MainWindow", "Avg. # deleted edges:", None))
        self.label_28.setText(_translate("MainWindow", "Avg. # deleted nodes:", None))
        self.label_29.setText(_translate("MainWindow", "General", None))
        self.label_30.setText(_translate("MainWindow", "Time", None))
        self.label_31.setText(_translate("MainWindow", "Total time:", None))
        self.label_32.setText(_translate("MainWindow", "Avg. time per interval:", None))
        self.statNumberOfNodesLabel.setText(_translate("MainWindow", "N/A", None))
        self.statNumberOfEdgesLabel.setText(_translate("MainWindow", "N/A", None))
        self.statAvgDeletedEdgesLabel.setText(_translate("MainWindow", "N/A", None))
        self.statAvgDeletedNodesLabel.setText(_translate("MainWindow", "N/A", None))
        self.statTotalSolvedIPsLabel.setText(_translate("MainWindow", "N/A", None))
        self.statAvgSolvedIPsLabel.setText(_translate("MainWindow", "N/A", None))
        self.statTotalTimeLabel.setText(_translate("MainWindow", "N/A", None))
        self.statAvgTimeLabel.setText(_translate("MainWindow", "N/A", None))
        self.computeIntervalPushButton.setText(_translate("MainWindow", "Compute next interval", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Compute Nash flow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionLoad_Graph.setText(_translate("MainWindow", "Load Graph", None))
        self.actionSave_Graph.setText(_translate("MainWindow", "Save Graph", None))
        self.actionNew_graph.setText(_translate("MainWindow", "New graph", None))
        self.actionLoad_graph.setText(_translate("MainWindow", "Load graph", None))
        self.actionSave_graph.setText(_translate("MainWindow", "Save graph", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionLoad_NashFlow.setText(_translate("MainWindow", "Load NashFlow", None))
        self.actionSave_NashFlow.setText(_translate("MainWindow", "Save NashFlow", None))
        self.actionOpen_manual.setText(_translate("MainWindow", "Open manual", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

import icons_rc
