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
        MainWindow.resize(1301, 1047)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1301, 1047))
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
        self.plotFrame.setGeometry(QtCore.QRect(10, 10, 631, 411))
        self.plotFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.plotFrame.setObjectName(_fromUtf8("plotFrame"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(650, 0, 131, 311))
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
        self.groupBox_2.setGeometry(QtCore.QRect(790, 0, 131, 311))
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
        self.groupBox_3.setGeometry(QtCore.QRect(10, 430, 921, 201))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(770, 20, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.inflowLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.inflowLineEdit.setGeometry(QtCore.QRect(770, 40, 131, 21))
        self.inflowLineEdit.setObjectName(_fromUtf8("inflowLineEdit"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.outputDirectoryLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.outputDirectoryLineEdit.setGeometry(QtCore.QRect(10, 40, 601, 21))
        self.outputDirectoryLineEdit.setObjectName(_fromUtf8("outputDirectoryLineEdit"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(770, 70, 141, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.intervalsLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.intervalsLineEdit.setGeometry(QtCore.QRect(770, 90, 131, 21))
        self.intervalsLineEdit.setObjectName(_fromUtf8("intervalsLineEdit"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.templateFileLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.templateFileLineEdit.setGeometry(QtCore.QRect(10, 90, 601, 21))
        self.templateFileLineEdit.setObjectName(_fromUtf8("templateFileLineEdit"))
        self.outputDirectoryPushButton = QtGui.QPushButton(self.groupBox_3)
        self.outputDirectoryPushButton.setGeometry(QtCore.QRect(620, 40, 131, 21))
        self.outputDirectoryPushButton.setObjectName(_fromUtf8("outputDirectoryPushButton"))
        self.templateFilePushButton = QtGui.QPushButton(self.groupBox_3)
        self.templateFilePushButton.setGeometry(QtCore.QRect(620, 90, 131, 21))
        self.templateFilePushButton.setObjectName(_fromUtf8("templateFilePushButton"))
        self.scipPathLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.scipPathLineEdit.setGeometry(QtCore.QRect(10, 140, 601, 21))
        self.scipPathLineEdit.setObjectName(_fromUtf8("scipPathLineEdit"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 121, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.scipPathPushButton = QtGui.QPushButton(self.groupBox_3)
        self.scipPathPushButton.setGeometry(QtCore.QRect(620, 140, 131, 21))
        self.scipPathPushButton.setObjectName(_fromUtf8("scipPathPushButton"))
        self.cleanUpCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.cleanUpCheckBox.setGeometry(QtCore.QRect(770, 140, 99, 22))
        self.cleanUpCheckBox.setObjectName(_fromUtf8("cleanUpCheckBox"))
        self.computeFlowPushButton = QtGui.QPushButton(self.tab)
        self.computeFlowPushButton.setGeometry(QtCore.QRect(910, 750, 131, 71))
        self.computeFlowPushButton.setAutoDefault(False)
        self.computeFlowPushButton.setDefault(False)
        self.computeFlowPushButton.setFlat(False)
        self.computeFlowPushButton.setObjectName(_fromUtf8("computeFlowPushButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(670, 10, 271, 591))
        self.groupBox_5.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.plotEdgeFlowFrame = QtGui.QFrame(self.groupBox_5)
        self.plotEdgeFlowFrame.setGeometry(QtCore.QRect(10, 40, 251, 241))
        self.plotEdgeFlowFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotEdgeFlowFrame.setObjectName(_fromUtf8("plotEdgeFlowFrame"))
        self.plotEdgeQueueFrame = QtGui.QFrame(self.groupBox_5)
        self.plotEdgeQueueFrame.setGeometry(QtCore.QRect(10, 310, 251, 241))
        self.plotEdgeQueueFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotEdgeQueueFrame.setObjectName(_fromUtf8("plotEdgeQueueFrame"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(110, 560, 16, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 560, 61, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.setEdgeFlowRangePushButton = QtGui.QPushButton(self.groupBox_5)
        self.setEdgeFlowRangePushButton.setGeometry(QtCore.QRect(160, 560, 101, 21))
        self.setEdgeFlowRangePushButton.setObjectName(_fromUtf8("setEdgeFlowRangePushButton"))
        self.edgeFlowPlotLowerBoundLineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.edgeFlowPlotLowerBoundLineEdit.setGeometry(QtCore.QRect(70, 560, 31, 21))
        self.edgeFlowPlotLowerBoundLineEdit.setObjectName(_fromUtf8("edgeFlowPlotLowerBoundLineEdit"))
        self.edgeFlowPlotUpperBoundLineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.edgeFlowPlotUpperBoundLineEdit.setGeometry(QtCore.QRect(120, 560, 31, 21))
        self.edgeFlowPlotUpperBoundLineEdit.setText(_fromUtf8(""))
        self.edgeFlowPlotUpperBoundLineEdit.setObjectName(_fromUtf8("edgeFlowPlotUpperBoundLineEdit"))
        self.label_19 = QtGui.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 191, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_5)
        self.label_20.setGeometry(QtCore.QRect(10, 290, 191, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(970, 10, 291, 321))
        self.groupBox_6.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.plotNodeLabelFrame = QtGui.QFrame(self.groupBox_6)
        self.plotNodeLabelFrame.setGeometry(QtCore.QRect(10, 40, 251, 241))
        self.plotNodeLabelFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotNodeLabelFrame.setObjectName(_fromUtf8("plotNodeLabelFrame"))
        self.label_15 = QtGui.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(10, 290, 61, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(110, 290, 16, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.nodeLabelPlotLowerBoundLineEdit = QtGui.QLineEdit(self.groupBox_6)
        self.nodeLabelPlotLowerBoundLineEdit.setGeometry(QtCore.QRect(70, 290, 31, 21))
        self.nodeLabelPlotLowerBoundLineEdit.setObjectName(_fromUtf8("nodeLabelPlotLowerBoundLineEdit"))
        self.setNodeLabelRangePushButton = QtGui.QPushButton(self.groupBox_6)
        self.setNodeLabelRangePushButton.setGeometry(QtCore.QRect(160, 290, 101, 21))
        self.setNodeLabelRangePushButton.setObjectName(_fromUtf8("setNodeLabelRangePushButton"))
        self.nodeLabelPlotUpperBoundLineEdit = QtGui.QLineEdit(self.groupBox_6)
        self.nodeLabelPlotUpperBoundLineEdit.setGeometry(QtCore.QRect(120, 290, 31, 21))
        self.nodeLabelPlotUpperBoundLineEdit.setText(_fromUtf8(""))
        self.nodeLabelPlotUpperBoundLineEdit.setObjectName(_fromUtf8("nodeLabelPlotUpperBoundLineEdit"))
        self.label_21 = QtGui.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(10, 20, 221, 17))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 490, 651, 431))
        self.groupBox_4.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.plotNTFFrame = QtGui.QFrame(self.groupBox_4)
        self.plotNTFFrame.setGeometry(QtCore.QRect(10, 20, 631, 401))
        self.plotNTFFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotNTFFrame.setObjectName(_fromUtf8("plotNTFFrame"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 10, 651, 471))
        self.groupBox_7.setAutoFillBackground(False)
        self.groupBox_7.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.plotAnimationFrame = QtGui.QFrame(self.groupBox_7)
        self.plotAnimationFrame.setGeometry(QtCore.QRect(10, 20, 631, 391))
        self.plotAnimationFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotAnimationFrame.setObjectName(_fromUtf8("plotAnimationFrame"))
        self.timeSlider = QtGui.QSlider(self.groupBox_7)
        self.timeSlider.setGeometry(QtCore.QRect(10, 420, 631, 19))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName(_fromUtf8("timeSlider"))
        self.generateAnimationPushButton = QtGui.QPushButton(self.groupBox_7)
        self.generateAnimationPushButton.setGeometry(QtCore.QRect(250, 440, 99, 21))
        self.generateAnimationPushButton.setObjectName(_fromUtf8("generateAnimationPushButton"))
        self.label_13 = QtGui.QLabel(self.groupBox_7)
        self.label_13.setGeometry(QtCore.QRect(10, 440, 121, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.animationStartLineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.animationStartLineEdit.setGeometry(QtCore.QRect(140, 440, 41, 21))
        self.animationStartLineEdit.setText(_fromUtf8(""))
        self.animationStartLineEdit.setObjectName(_fromUtf8("animationStartLineEdit"))
        self.label_14 = QtGui.QLabel(self.groupBox_7)
        self.label_14.setGeometry(QtCore.QRect(190, 440, 21, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.animationEndLineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.animationEndLineEdit.setGeometry(QtCore.QRect(200, 440, 41, 21))
        self.animationEndLineEdit.setText(_fromUtf8(""))
        self.animationEndLineEdit.setObjectName(_fromUtf8("animationEndLineEdit"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(970, 340, 291, 241))
        self.groupBox_8.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.intervalsListWidget = QtGui.QListWidget(self.groupBox_8)
        self.intervalsListWidget.setGeometry(QtCore.QRect(10, 20, 251, 211))
        self.intervalsListWidget.setFrameShape(QtGui.QFrame.Box)
        self.intervalsListWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.intervalsListWidget.setObjectName(_fromUtf8("intervalsListWidget"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1301, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
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
        self.actionLoad_NashFlow.setObjectName(_fromUtf8("actionLoad_NashFlow"))
        self.actionSave_NashFlow = QtGui.QAction(MainWindow)
        self.actionSave_NashFlow.setObjectName(_fromUtf8("actionSave_NashFlow"))
        self.menuFile.addAction(self.actionNew_graph)
        self.menuFile.addAction(self.actionLoad_graph)
        self.menuFile.addAction(self.actionSave_graph)
        self.menuFile.addAction(self.actionLoad_NashFlow)
        self.menuFile.addAction(self.actionSave_NashFlow)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

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
        self.label_11.setText(_translate("MainWindow", "Template file", None))
        self.outputDirectoryPushButton.setText(_translate("MainWindow", "Select directory", None))
        self.templateFilePushButton.setText(_translate("MainWindow", "Select file", None))
        self.label_12.setText(_translate("MainWindow", "SCIP path", None))
        self.scipPathPushButton.setText(_translate("MainWindow", "Select binary", None))
        self.cleanUpCheckBox.setText(_translate("MainWindow", "Clean up", None))
        self.computeFlowPushButton.setText(_translate("MainWindow", "Compute Nashflow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Create/Load Graph", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Edge", None))
        self.label_17.setText(_translate("MainWindow", "-", None))
        self.label_18.setText(_translate("MainWindow", "Range:", None))
        self.setEdgeFlowRangePushButton.setText(_translate("MainWindow", "Set", None))
        self.edgeFlowPlotLowerBoundLineEdit.setText(_translate("MainWindow", "0", None))
        self.label_19.setText(_translate("MainWindow", "Cumulative in- and outflow", None))
        self.label_20.setText(_translate("MainWindow", "Queue size", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Node", None))
        self.label_15.setText(_translate("MainWindow", "Range:", None))
        self.label_16.setText(_translate("MainWindow", "-", None))
        self.nodeLabelPlotLowerBoundLineEdit.setText(_translate("MainWindow", "0", None))
        self.setNodeLabelRangePushButton.setText(_translate("MainWindow", "Set", None))
        self.label_21.setText(_translate("MainWindow", "Dynamic shortest path distances", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Normalized Thin Flows", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Nash Flow over time", None))
        self.generateAnimationPushButton.setText(_translate("MainWindow", "Generate", None))
        self.label_13.setText(_translate("MainWindow", "Animation range:", None))
        self.label_14.setText(_translate("MainWindow", "-", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "NTF list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Compute Nash flow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionLoad_Graph.setText(_translate("MainWindow", "Load Graph", None))
        self.actionSave_Graph.setText(_translate("MainWindow", "Save Graph", None))
        self.actionNew_graph.setText(_translate("MainWindow", "New graph", None))
        self.actionLoad_graph.setText(_translate("MainWindow", "Load graph", None))
        self.actionSave_graph.setText(_translate("MainWindow", "Save graph", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionLoad_NashFlow.setText(_translate("MainWindow", "Load NashFlow", None))
        self.actionSave_NashFlow.setText(_translate("MainWindow", "Save NashFlow", None))

