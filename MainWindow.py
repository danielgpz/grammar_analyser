# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Asignaturas\Compilacion\Proyectos\Grammar Analyser\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(843, 612)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGrammar = QtWidgets.QWidget()
        self.tabGrammar.setObjectName("tabGrammar")
        self.gridLayout = QtWidgets.QGridLayout(self.tabGrammar)
        self.gridLayout.setObjectName("gridLayout")
        self.textEditGrammar = QtWidgets.QPlainTextEdit(self.tabGrammar)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.textEditGrammar.setFont(font)
        self.textEditGrammar.setPlainText("")
        self.textEditGrammar.setObjectName("textEditGrammar")
        self.gridLayout.addWidget(self.textEditGrammar, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabGrammar, "")
        self.tabResults = QtWidgets.QWidget()
        self.tabResults.setObjectName("tabResults")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabResults)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textResults = QtWebEngineWidgets.QWebEngineView(self.tabResults)
        self.textResults.setObjectName("textResults")
        self.gridLayout_2.addWidget(self.textResults, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabResults, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(795, 40))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNewGrammar = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/ui-tab--plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewGrammar.setIcon(icon1)
        self.actionNewGrammar.setObjectName("actionNewGrammar")
        self.actionSaveGrammar = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveGrammar.setIcon(icon2)
        self.actionSaveGrammar.setObjectName("actionSaveGrammar")
        self.actionLoadGrammar = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/blue-folder-open-document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadGrammar.setIcon(icon3)
        self.actionLoadGrammar.setObjectName("actionLoadGrammar")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/arrow-000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionHowToUse = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/lifebuoy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHowToUse.setIcon(icon5)
        self.actionHowToUse.setObjectName("actionHowToUse")
        self.actionAboutAuthor = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAboutAuthor.setIcon(icon6)
        self.actionAboutAuthor.setObjectName("actionAboutAuthor")
        self.actionAboutGrammarAnalyser = QtWidgets.QAction(MainWindow)
        self.actionAboutGrammarAnalyser.setIcon(icon6)
        self.actionAboutGrammarAnalyser.setObjectName("actionAboutGrammarAnalyser")
        self.actionSaveGrammarAs = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/disk--pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveGrammarAs.setIcon(icon7)
        self.actionSaveGrammarAs.setObjectName("actionSaveGrammarAs")
        self.actionAnalyse = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalyse.setIcon(icon8)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionAnalyse.setFont(font)
        self.actionAnalyse.setObjectName("actionAnalyse")
        self.actionQuickAnalyse = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/controlx2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuickAnalyse.setIcon(icon9)
        self.actionQuickAnalyse.setObjectName("actionQuickAnalyse")
        self.menuFile.addAction(self.actionNewGrammar)
        self.menuFile.addAction(self.actionLoadGrammar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveGrammar)
        self.menuFile.addAction(self.actionSaveGrammarAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHowToUse)
        self.menuHelp.addAction(self.actionAboutAuthor)
        self.menuHelp.addAction(self.actionAboutGrammarAnalyser)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAnalyse)
        self.toolBar.addAction(self.actionQuickAnalyse)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewGrammar)
        self.toolBar.addAction(self.actionLoadGrammar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSaveGrammar)
        self.toolBar.addAction(self.actionSaveGrammarAs)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHowToUse)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grammar Analyser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGrammar), _translate("MainWindow", "Gramática"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResults), _translate("MainWindow", "Resultados"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Herramientas"))
        self.actionNewGrammar.setText(_translate("MainWindow", "Nueva Gramática"))
        self.actionNewGrammar.setStatusTip(_translate("MainWindow", "Nueva Gramática"))
        self.actionNewGrammar.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSaveGrammar.setText(_translate("MainWindow", "Guardar Gramática"))
        self.actionSaveGrammar.setStatusTip(_translate("MainWindow", "Guardar Gramática"))
        self.actionSaveGrammar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoadGrammar.setText(_translate("MainWindow", "Cargar Gramática"))
        self.actionLoadGrammar.setStatusTip(_translate("MainWindow", "Cargar Gramática"))
        self.actionLoadGrammar.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Salir"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionHowToUse.setText(_translate("MainWindow", "¿Cómo usar?"))
        self.actionHowToUse.setStatusTip(_translate("MainWindow", "¿Cómo usar?"))
        self.actionAboutAuthor.setText(_translate("MainWindow", "Acerca del autor"))
        self.actionAboutGrammarAnalyser.setText(_translate("MainWindow", "Acerca de Grammar Analyser"))
        self.actionSaveGrammarAs.setText(_translate("MainWindow", "Guardar Gramática Como ..."))
        self.actionSaveGrammarAs.setStatusTip(_translate("MainWindow", "Guardar Gramática Como"))
        self.actionAnalyse.setText(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setToolTip(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setStatusTip(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setShortcut(_translate("MainWindow", "F5"))
        self.actionQuickAnalyse.setText(_translate("MainWindow", "Análisis rápido"))
        self.actionQuickAnalyse.setToolTip(_translate("MainWindow", "Análisis rápido"))
        self.actionQuickAnalyse.setStatusTip(_translate("MainWindow", "Análisis rápido"))
        self.actionQuickAnalyse.setShortcut(_translate("MainWindow", "F9"))

class Ui_DialogWords(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.wordsText = QtWidgets.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.wordsText.setFont(font)
        self.wordsText.setObjectName("wordsText")
        self.gridLayout.addWidget(self.wordsText, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadenas de Prueba"))
        self.label.setText(_translate("Dialog", "Escriba algunas cadenas:"))

class Ui_DialogHowToUse(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1044, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "¿Cómo usar?"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Para analizar una gramática siga los siguientes pasos:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">1. </span><span style=\" font-size:14pt; text-decoration: underline;\">La grámatica debe ser libre del contexto y se escribe en el siguiente formato:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">S --&gt; A | B</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">A --&gt; a A | epsilon</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">B --&gt; b B | epsilon</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">Usa \'</span><span style=\" font-size:14pt; font-weight:600;\">--&gt;</span><span style=\" font-size:14pt;\">\' para indicar una </span><span style=\" font-size:14pt; font-weight:600;\">producción</span><span style=\" font-size:14pt;\">, y \'</span><span style=\" font-size:14pt; font-weight:600;\">|</span><span style=\" font-size:14pt;\">\' para indicar multiples pruducciones con la misma cabecera.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">Usa \'</span><span style=\" font-size:14pt; font-weight:600;\">epsilon</span><span style=\" font-size:14pt;\">\' para indicar el símbolo </span><span style=\" font-size:14pt; font-weight:600;\">Terminal</span><span style=\" font-size:14pt;\"> especial de la </span><span style=\" font-size:14pt; font-weight:600;\">grámatica</span><span style=\" font-size:14pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">Todos los símbolos que sean cabecera de alguna </span><span style=\" font-size:14pt; font-weight:600;\">producción</span><span style=\" font-size:14pt;\"> serán los </span><span style=\" font-size:14pt; font-weight:600;\">No Terminales</span><span style=\" font-size:14pt;\">, el resto serán considerados como </span><span style=\" font-size:14pt; font-weight:600;\">Terminales</span><span style=\" font-size:14pt;\">. Use de ser posible solo letras en la defeinición de los </span><span style=\" font-size:14pt; font-weight:600;\">No Terminales</span><span style=\" font-size:14pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">Entre dos símbolos contiguos deje siempre al menos un espacio.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">Se le notificará si la </span><span style=\" font-size:14pt; font-weight:600;\">gramática</span><span style=\" font-size:14pt;\"> no se encuentra en el formato apropiado.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">2. </span><span style=\" font-size:14pt; text-decoration: underline;\">Si no desea analizar ninguna cadena, continue con &quot;Análisis rápido&quot;(F9).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">Verá los resultados en la pestaña &quot;Resultados&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">3. </span><span style=\" font-size:14pt; text-decoration: underline;\">Si desea analizar además algunas cadenas, continue con &quot;Analizar&quot;(F5).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">A continuación deberá entrar las cadenas deseadas, debe dejar al menos un espacio entre dos tokens contiguos.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">Luego verá los resultados en la pestaña &quot;Resultados&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">4. </span><span style=\" font-size:14pt; text-decoration: underline;\">Al finalizar, usted puede además guardar la gramática en formato de texto, para su uso futuro.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:18pt; color:#000000;\">•</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#e6db74;\"> </span><span style=\" font-size:14pt;\">De igual forma se puede cargar una gramática en formato de texto, en cuyo caso deberá realizar los</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">pasos desde el inicio.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#005500;\">¡GRACIAS POR USAR GRAMMAR ANALYSER!</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "¿Cómo usar?"))

class Ui_DialogAboutAuthor(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 213)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Acerca del Autor"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#000000;\">Estudiante:</span><span style=\" font-size:24pt; color:#005500;\"> Daniel Alberto García Pérez</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#000000;\">Grupo:</span><span style=\" font-size:24pt; color:#005500;\"> C312</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#000000;\">Curso:</span><span style=\" font-size:24pt; color:#005500;\"> COMPILACIÓN I</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Acerca del Autor"))

class Ui_DialogAboutGrammarAnalyser(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 174)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Acerca de Grammar Analyser"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#005500;\">Grammar Analyser V1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#000000;\">Hecho con</span><span style=\" font-size:24pt; color:#005500;\"> </span><span style=\" font-size:24pt; color:#aa0000;\">PyQt5. </span><a href=\"https://pypi.org/project/PyQt5/\"><span style=\" font-size:24pt; text-decoration: underline; color:#0000ff;\">Sitio Oficial de PyQt5</span></a></p></body></html>"))
        self.label.setText(_translate("Dialog", "Acerca de Grammar Analyser"))


