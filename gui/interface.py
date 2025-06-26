# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BLDC_ResFixed.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import resources_rc

class Ui_UserInterface(object):
    def setupUi(self, UserInterface):
        if not UserInterface.objectName():
            UserInterface.setObjectName(u"UserInterface")
        UserInterface.resize(1017, 1018)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserInterface.sizePolicy().hasHeightForWidth())
        UserInterface.setSizePolicy(sizePolicy)
        self.actionLoad = QAction(UserInterface)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(UserInterface)
        self.actionSave.setObjectName(u"actionSave")
        self.action12 = QAction(UserInterface)
        self.action12.setObjectName(u"action12")
        self.action14 = QAction(UserInterface)
        self.action14.setObjectName(u"action14")
        self.action16 = QAction(UserInterface)
        self.action16.setObjectName(u"action16")
        self.action18 = QAction(UserInterface)
        self.action18.setObjectName(u"action18")
        self.action20 = QAction(UserInterface)
        self.action20.setObjectName(u"action20")
        self.action22 = QAction(UserInterface)
        self.action22.setObjectName(u"action22")
        self.action10 = QAction(UserInterface)
        self.action10.setObjectName(u"action10")
        self.font12 = QAction(UserInterface)
        self.font12.setObjectName(u"font12")
        self.font14 = QAction(UserInterface)
        self.font14.setObjectName(u"font14")
        self.font16 = QAction(UserInterface)
        self.font16.setObjectName(u"font16")
        self.font18 = QAction(UserInterface)
        self.font18.setObjectName(u"font18")
        self.font20 = QAction(UserInterface)
        self.font20.setObjectName(u"font20")
        self.font22 = QAction(UserInterface)
        self.font22.setObjectName(u"font22")
        self.centralwidget = QWidget(UserInterface)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget_gridLayout_1 = QGridLayout(self.centralwidget)
        self.centralwidget_gridLayout_1.setSpacing(0)
        self.centralwidget_gridLayout_1.setObjectName(u"centralwidget_gridLayout_1")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_tab_1_scrollWrapper = QVBoxLayout(self.tab_1)
        self.verticalLayout_tab_1_scrollWrapper.setObjectName(u"verticalLayout_tab_1_scrollWrapper")
        self.scrollArea_tab_1 = QScrollArea(self.tab_1)
        self.scrollArea_tab_1.setObjectName(u"scrollArea_tab_1")
        self.scrollArea_tab_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tab_1 = QWidget()
        self.scrollAreaWidgetContents_tab_1.setObjectName(u"scrollAreaWidgetContents_tab_1")
        self.scrollAreaWidgetContents_tab_1.setGeometry(QRect(0, 0, 950, 918))
        self.tab_1_gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_tab_1)
        self.tab_1_gridLayout_2.setSpacing(0)
        self.tab_1_gridLayout_2.setObjectName(u"tab_1_gridLayout_2")
        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents_tab_1)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setFont(font)
        self.groupBox_18_gridLayout_9 = QGridLayout(self.groupBox_18)
        self.groupBox_18_gridLayout_9.setSpacing(0)
        self.groupBox_18_gridLayout_9.setObjectName(u"groupBox_18_gridLayout_9")
        self.Magnet_Material = QComboBox(self.groupBox_18)
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.addItem("")
        self.Magnet_Material.setObjectName(u"Magnet_Material")
        self.Magnet_Material.setLayoutDirection(Qt.LeftToRight)
        self.Magnet_Material.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.groupBox_18_gridLayout_9.addWidget(self.Magnet_Material, 0, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_18)
        self.label_40.setObjectName(u"label_40")

        self.groupBox_18_gridLayout_9.addWidget(self.label_40, 0, 0, 1, 1)

        self.Iron_Material = QComboBox(self.groupBox_18)
        self.Iron_Material.addItem("")
        self.Iron_Material.addItem("")
        self.Iron_Material.addItem("")
        self.Iron_Material.addItem("")
        self.Iron_Material.addItem("")
        self.Iron_Material.addItem("")
        self.Iron_Material.addItem("")
        self.Iron_Material.setObjectName(u"Iron_Material")

        self.groupBox_18_gridLayout_9.addWidget(self.Iron_Material, 1, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_18)
        self.label_42.setObjectName(u"label_42")

        self.groupBox_18_gridLayout_9.addWidget(self.label_42, 2, 0, 1, 1)

        self.label_41 = QLabel(self.groupBox_18)
        self.label_41.setObjectName(u"label_41")

        self.groupBox_18_gridLayout_9.addWidget(self.label_41, 1, 0, 1, 1)

        self.Lamination_Material = QComboBox(self.groupBox_18)
        self.Lamination_Material.addItem("")
        self.Lamination_Material.addItem("")
        self.Lamination_Material.setObjectName(u"Lamination_Material")

        self.groupBox_18_gridLayout_9.addWidget(self.Lamination_Material, 2, 1, 1, 1)


        self.tab_1_gridLayout_2.addWidget(self.groupBox_18, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_tab_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox_gridLayout_5 = QGridLayout(self.groupBox)
        self.groupBox_gridLayout_5.setSpacing(0)
        self.groupBox_gridLayout_5.setObjectName(u"groupBox_gridLayout_5")
        self.R_MagneticLossCoef1_2 = QDoubleSpinBox(self.groupBox)
        self.R_MagneticLossCoef1_2.setObjectName(u"R_MagneticLossCoef1_2")
        self.R_MagneticLossCoef1_2.setDecimals(5)
        self.R_MagneticLossCoef1_2.setSingleStep(0.000100000000000)
        self.R_MagneticLossCoef1_2.setValue(0.001180000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagneticLossCoef1_2, 5, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.groupBox_gridLayout_5.addWidget(self.label_6, 6, 0, 1, 1)

        self.R_MagnetOutR_2 = QDoubleSpinBox(self.groupBox)
        self.R_MagnetOutR_2.setObjectName(u"R_MagnetOutR_2")
        self.R_MagnetOutR_2.setDecimals(4)
        self.R_MagnetOutR_2.setMaximum(10000.000000000000000)
        self.R_MagnetOutR_2.setSingleStep(0.000100000000000)
        self.R_MagnetOutR_2.setValue(5.100000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetOutR_2, 3, 3, 1, 1)

        self.R_MagnetRadialLength_2 = QDoubleSpinBox(self.groupBox)
        self.R_MagnetRadialLength_2.setObjectName(u"R_MagnetRadialLength_2")
        self.R_MagnetRadialLength_2.setDecimals(4)
        self.R_MagnetRadialLength_2.setMaximum(10000.000000000000000)
        self.R_MagnetRadialLength_2.setSingleStep(0.000100000000000)
        self.R_MagnetRadialLength_2.setValue(1.600000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetRadialLength_2, 2, 3, 1, 1)

        self.R_MagneticLossCoef3_1 = QDoubleSpinBox(self.groupBox)
        self.R_MagneticLossCoef3_1.setObjectName(u"R_MagneticLossCoef3_1")
        self.R_MagneticLossCoef3_1.setDecimals(5)
        self.R_MagneticLossCoef3_1.setSingleStep(0.000100000000000)
        self.R_MagneticLossCoef3_1.setValue(1.500000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagneticLossCoef3_1, 7, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.groupBox_gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.R_MagnetOutR_unit = QComboBox(self.groupBox)
        self.R_MagnetOutR_unit.addItem("")
        self.R_MagnetOutR_unit.addItem("")
        self.R_MagnetOutR_unit.addItem("")
        self.R_MagnetOutR_unit.setObjectName(u"R_MagnetOutR_unit")

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetOutR_unit, 3, 1, 1, 1)

        self.R_MagnetBackIronInnerR_2 = QDoubleSpinBox(self.groupBox)
        self.R_MagnetBackIronInnerR_2.setObjectName(u"R_MagnetBackIronInnerR_2")
        self.R_MagnetBackIronInnerR_2.setDecimals(4)
        self.R_MagnetBackIronInnerR_2.setSingleStep(0.000100000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetBackIronInnerR_2, 4, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.groupBox_gridLayout_5.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.groupBox_gridLayout_5.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.groupBox_gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.groupBox_gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.I_PolePair_1 = QSpinBox(self.groupBox)
        self.I_PolePair_1.setObjectName(u"I_PolePair_1")
        self.I_PolePair_1.setValue(2)

        self.groupBox_gridLayout_5.addWidget(self.I_PolePair_1, 1, 2, 1, 1)

        self.R_MagnetOutR_1 = QDoubleSpinBox(self.groupBox)
        self.R_MagnetOutR_1.setObjectName(u"R_MagnetOutR_1")
        self.R_MagnetOutR_1.setDecimals(4)
        self.R_MagnetOutR_1.setMaximum(10000.000000000000000)
        self.R_MagnetOutR_1.setSingleStep(0.000100000000000)
        self.R_MagnetOutR_1.setValue(5.000000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetOutR_1, 3, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.groupBox_gridLayout_5.addWidget(self.label_7, 7, 0, 1, 1)

        self.R_MagneticLossCoef2_2 = QDoubleSpinBox(self.groupBox)
        self.R_MagneticLossCoef2_2.setObjectName(u"R_MagneticLossCoef2_2")
        self.R_MagneticLossCoef2_2.setDecimals(5)
        self.R_MagneticLossCoef2_2.setSingleStep(0.000100000000000)
        self.R_MagneticLossCoef2_2.setValue(1.880000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagneticLossCoef2_2, 6, 3, 1, 1)

        self.R_MagnetRadialLength_1 = QDoubleSpinBox(self.groupBox)
        self.R_MagnetRadialLength_1.setObjectName(u"R_MagnetRadialLength_1")
        self.R_MagnetRadialLength_1.setDecimals(4)
        self.R_MagnetRadialLength_1.setMaximum(10000.000000000000000)
        self.R_MagnetRadialLength_1.setSingleStep(0.000100000000000)
        self.R_MagnetRadialLength_1.setValue(1.500000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetRadialLength_1, 2, 2, 1, 1)

        self.I_PolePair_2 = QSpinBox(self.groupBox)
        self.I_PolePair_2.setObjectName(u"I_PolePair_2")
        self.I_PolePair_2.setMaximum(999)
        self.I_PolePair_2.setValue(2)

        self.groupBox_gridLayout_5.addWidget(self.I_PolePair_2, 1, 3, 1, 1)

        self.R_MagnetRadialLength_unit = QComboBox(self.groupBox)
        self.R_MagnetRadialLength_unit.addItem("")
        self.R_MagnetRadialLength_unit.addItem("")
        self.R_MagnetRadialLength_unit.addItem("")
        self.R_MagnetRadialLength_unit.setObjectName(u"R_MagnetRadialLength_unit")
        self.R_MagnetRadialLength_unit.setLayoutDirection(Qt.LeftToRight)
        self.R_MagnetRadialLength_unit.setEditable(True)

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetRadialLength_unit, 2, 1, 1, 1)

        self.R_MagneticLossCoef2_1 = QDoubleSpinBox(self.groupBox)
        self.R_MagneticLossCoef2_1.setObjectName(u"R_MagneticLossCoef2_1")
        self.R_MagneticLossCoef2_1.setDecimals(5)
        self.R_MagneticLossCoef2_1.setSingleStep(0.000100000000000)
        self.R_MagneticLossCoef2_1.setValue(1.880000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagneticLossCoef2_1, 6, 2, 1, 1)

        self.R_MagneticLossCoef3_2 = QDoubleSpinBox(self.groupBox)
        self.R_MagneticLossCoef3_2.setObjectName(u"R_MagneticLossCoef3_2")
        self.R_MagneticLossCoef3_2.setDecimals(5)
        self.R_MagneticLossCoef3_2.setSingleStep(0.000100000000000)
        self.R_MagneticLossCoef3_2.setValue(1.500000000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagneticLossCoef3_2, 7, 3, 1, 1)

        self.R_MagneticLossCoef1_1 = QDoubleSpinBox(self.groupBox)
        self.R_MagneticLossCoef1_1.setObjectName(u"R_MagneticLossCoef1_1")
        self.R_MagneticLossCoef1_1.setDecimals(5)
        self.R_MagneticLossCoef1_1.setSingleStep(0.000100000000000)
        self.R_MagneticLossCoef1_1.setValue(0.001180000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagneticLossCoef1_1, 5, 2, 1, 1)

        self.R_MagnetBackIronInnerR_unit = QComboBox(self.groupBox)
        self.R_MagnetBackIronInnerR_unit.addItem("")
        self.R_MagnetBackIronInnerR_unit.addItem("")
        self.R_MagnetBackIronInnerR_unit.addItem("")
        self.R_MagnetBackIronInnerR_unit.setObjectName(u"R_MagnetBackIronInnerR_unit")

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetBackIronInnerR_unit, 4, 1, 1, 1)

        self.R_MagnetBackIronInnerR_1 = QDoubleSpinBox(self.groupBox)
        self.R_MagnetBackIronInnerR_1.setObjectName(u"R_MagnetBackIronInnerR_1")
        self.R_MagnetBackIronInnerR_1.setDecimals(4)
        self.R_MagnetBackIronInnerR_1.setSingleStep(0.000100000000000)

        self.groupBox_gridLayout_5.addWidget(self.R_MagnetBackIronInnerR_1, 4, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_16.setFont(font1)
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setFrameShape(QFrame.Box)
        self.label_16.setTextFormat(Qt.RichText)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.groupBox_gridLayout_5.addWidget(self.label_16, 0, 2, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setLayoutDirection(Qt.LeftToRight)
        self.label_18.setFrameShape(QFrame.Box)
        self.label_18.setFrameShadow(QFrame.Plain)
        self.label_18.setTextFormat(Qt.RichText)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.groupBox_gridLayout_5.addWidget(self.label_18, 0, 3, 1, 1)


        self.tab_1_gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_tab_1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.groupBox_4_gridLayout_7 = QGridLayout(self.groupBox_4)
        self.groupBox_4_gridLayout_7.setSpacing(0)
        self.groupBox_4_gridLayout_7.setObjectName(u"groupBox_4_gridLayout_7")
        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")

        self.groupBox_4_gridLayout_7.addWidget(self.label_31, 0, 0, 1, 1)

        self.R_MtrLength_unit = QComboBox(self.groupBox_4)
        self.R_MtrLength_unit.addItem("")
        self.R_MtrLength_unit.addItem("")
        self.R_MtrLength_unit.addItem("")
        self.R_MtrLength_unit.setObjectName(u"R_MtrLength_unit")

        self.groupBox_4_gridLayout_7.addWidget(self.R_MtrLength_unit, 0, 1, 1, 1)

        self.R_MtrLength_1 = QDoubleSpinBox(self.groupBox_4)
        self.R_MtrLength_1.setObjectName(u"R_MtrLength_1")
        self.R_MtrLength_1.setDecimals(5)
        self.R_MtrLength_1.setMaximum(10000.000000000000000)
        self.R_MtrLength_1.setSingleStep(0.000100000000000)
        self.R_MtrLength_1.setValue(20.000000000000000)

        self.groupBox_4_gridLayout_7.addWidget(self.R_MtrLength_1, 0, 2, 1, 1)

        self.R_MtrLength_2 = QDoubleSpinBox(self.groupBox_4)
        self.R_MtrLength_2.setObjectName(u"R_MtrLength_2")
        self.R_MtrLength_2.setDecimals(5)
        self.R_MtrLength_2.setMaximum(10000.000000000000000)
        self.R_MtrLength_2.setSingleStep(0.000100000000000)
        self.R_MtrLength_2.setValue(21.000000000000000)

        self.groupBox_4_gridLayout_7.addWidget(self.R_MtrLength_2, 0, 3, 1, 1)

        self.label_32 = QLabel(self.groupBox_4)
        self.label_32.setObjectName(u"label_32")

        self.groupBox_4_gridLayout_7.addWidget(self.label_32, 1, 0, 1, 1)

        self.R_LoadInertia_unit = QComboBox(self.groupBox_4)
        self.R_LoadInertia_unit.addItem("")
        self.R_LoadInertia_unit.addItem("")
        self.R_LoadInertia_unit.addItem("")
        self.R_LoadInertia_unit.addItem("")
        self.R_LoadInertia_unit.addItem("")
        self.R_LoadInertia_unit.addItem("")
        self.R_LoadInertia_unit.setObjectName(u"R_LoadInertia_unit")

        self.groupBox_4_gridLayout_7.addWidget(self.R_LoadInertia_unit, 1, 1, 1, 1)

        self.R_LoadInertia_1 = QDoubleSpinBox(self.groupBox_4)
        self.R_LoadInertia_1.setObjectName(u"R_LoadInertia_1")
        self.R_LoadInertia_1.setDecimals(5)
        self.R_LoadInertia_1.setMaximum(10000.000000000000000)
        self.R_LoadInertia_1.setSingleStep(0.000100000000000)

        self.groupBox_4_gridLayout_7.addWidget(self.R_LoadInertia_1, 1, 2, 1, 1)

        self.R_LoadInertia_2 = QDoubleSpinBox(self.groupBox_4)
        self.R_LoadInertia_2.setObjectName(u"R_LoadInertia_2")
        self.R_LoadInertia_2.setDecimals(5)
        self.R_LoadInertia_2.setMaximum(10000.000000000000000)
        self.R_LoadInertia_2.setSingleStep(0.000100000000000)

        self.groupBox_4_gridLayout_7.addWidget(self.R_LoadInertia_2, 1, 3, 1, 1)

        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")

        self.groupBox_4_gridLayout_7.addWidget(self.label_33, 2, 0, 1, 1)

        self.R_GearRatio_2 = QDoubleSpinBox(self.groupBox_4)
        self.R_GearRatio_2.setObjectName(u"R_GearRatio_2")
        self.R_GearRatio_2.setMaximum(10000.000000000000000)
        self.R_GearRatio_2.setValue(15.000000000000000)

        self.groupBox_4_gridLayout_7.addWidget(self.R_GearRatio_2, 2, 3, 1, 1)

        self.R_GearRatio_1 = QDoubleSpinBox(self.groupBox_4)
        self.R_GearRatio_1.setObjectName(u"R_GearRatio_1")
        self.R_GearRatio_1.setMaximum(10000.000000000000000)
        self.R_GearRatio_1.setValue(15.000000000000000)

        self.groupBox_4_gridLayout_7.addWidget(self.R_GearRatio_1, 2, 2, 1, 1)


        self.tab_1_gridLayout_2.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_tab_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFocusPolicy(Qt.NoFocus)
        self.groupBox_2_gridLayout_6 = QGridLayout(self.groupBox_2)
        self.groupBox_2_gridLayout_6.setSpacing(0)
        self.groupBox_2_gridLayout_6.setObjectName(u"groupBox_2_gridLayout_6")
        self.I_NumElecPhase_1 = QSpinBox(self.groupBox_2)
        self.I_NumElecPhase_1.setObjectName(u"I_NumElecPhase_1")
        self.I_NumElecPhase_1.setValue(3)

        self.groupBox_2_gridLayout_6.addWidget(self.I_NumElecPhase_1, 0, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.groupBox_2_gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.R_PhaseCurrentAmp_2 = QDoubleSpinBox(self.groupBox_2)
        self.R_PhaseCurrentAmp_2.setObjectName(u"R_PhaseCurrentAmp_2")
        self.R_PhaseCurrentAmp_2.setMaximum(100000.000000000000000)
        self.R_PhaseCurrentAmp_2.setSingleStep(0.000100000000000)
        self.R_PhaseCurrentAmp_2.setValue(9000.000000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_PhaseCurrentAmp_2, 1, 3, 1, 1)

        self.R_PhaseCurrentAmp_1 = QDoubleSpinBox(self.groupBox_2)
        self.R_PhaseCurrentAmp_1.setObjectName(u"R_PhaseCurrentAmp_1")
        self.R_PhaseCurrentAmp_1.setMaximum(100000.000000000000000)
        self.R_PhaseCurrentAmp_1.setSingleStep(0.000100000000000)
        self.R_PhaseCurrentAmp_1.setValue(9000.000000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_PhaseCurrentAmp_1, 1, 2, 1, 1)

        self.I_NumElecPhase_2 = QSpinBox(self.groupBox_2)
        self.I_NumElecPhase_2.setObjectName(u"I_NumElecPhase_2")
        self.I_NumElecPhase_2.setValue(3)

        self.groupBox_2_gridLayout_6.addWidget(self.I_NumElecPhase_2, 0, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.groupBox_2_gridLayout_6.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.groupBox_2_gridLayout_6.addWidget(self.label_13, 6, 0, 1, 1)

        self.R_FillFactor_2 = QDoubleSpinBox(self.groupBox_2)
        self.R_FillFactor_2.setObjectName(u"R_FillFactor_2")
        self.R_FillFactor_2.setMaximum(1.000000000000000)
        self.R_FillFactor_2.setSingleStep(0.010000000000000)
        self.R_FillFactor_2.setValue(0.590000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_FillFactor_2, 5, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.groupBox_2_gridLayout_6.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.groupBox_2_gridLayout_6.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.groupBox_2_gridLayout_6.addWidget(self.label_12, 5, 0, 1, 1)

        self.R_WireCopperR_1 = QDoubleSpinBox(self.groupBox_2)
        self.R_WireCopperR_1.setObjectName(u"R_WireCopperR_1")
        self.R_WireCopperR_1.setDecimals(6)
        self.R_WireCopperR_1.setMaximum(10000.000000000000000)
        self.R_WireCopperR_1.setSingleStep(0.000100000000000)
        self.R_WireCopperR_1.setValue(0.500000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_WireCopperR_1, 2, 2, 1, 1)

        self.R_WireCopperR_unit = QComboBox(self.groupBox_2)
        self.R_WireCopperR_unit.addItem("")
        self.R_WireCopperR_unit.addItem("")
        self.R_WireCopperR_unit.addItem("")
        self.R_WireCopperR_unit.setObjectName(u"R_WireCopperR_unit")

        self.groupBox_2_gridLayout_6.addWidget(self.R_WireCopperR_unit, 2, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.groupBox_2_gridLayout_6.addWidget(self.label_15, 8, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.groupBox_2_gridLayout_6.addWidget(self.label_14, 7, 0, 1, 1)

        self.R_PhaseCurrentAmp_unit = QComboBox(self.groupBox_2)
        self.R_PhaseCurrentAmp_unit.addItem("")
        self.R_PhaseCurrentAmp_unit.addItem("")
        self.R_PhaseCurrentAmp_unit.setObjectName(u"R_PhaseCurrentAmp_unit")

        self.groupBox_2_gridLayout_6.addWidget(self.R_PhaseCurrentAmp_unit, 1, 1, 1, 1)

        self.R_InsulThick_2 = QDoubleSpinBox(self.groupBox_2)
        self.R_InsulThick_2.setObjectName(u"R_InsulThick_2")
        self.R_InsulThick_2.setDecimals(6)
        self.R_InsulThick_2.setMaximum(10000.000000000000000)
        self.R_InsulThick_2.setSingleStep(0.000100000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_InsulThick_2, 3, 3, 1, 1)

        self.R_InsulThick_1 = QDoubleSpinBox(self.groupBox_2)
        self.R_InsulThick_1.setObjectName(u"R_InsulThick_1")
        self.R_InsulThick_1.setDecimals(6)
        self.R_InsulThick_1.setMaximum(10000.000000000000000)
        self.R_InsulThick_1.setSingleStep(0.000100000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_InsulThick_1, 3, 2, 1, 1)

        self.R_FillFactor_1 = QDoubleSpinBox(self.groupBox_2)
        self.R_FillFactor_1.setObjectName(u"R_FillFactor_1")
        self.R_FillFactor_1.setMaximum(1.000000000000000)
        self.R_FillFactor_1.setSingleStep(0.010000000000000)
        self.R_FillFactor_1.setValue(0.590000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_FillFactor_1, 5, 2, 1, 1)

        self.R_InsulThick_unit = QComboBox(self.groupBox_2)
        self.R_InsulThick_unit.addItem("")
        self.R_InsulThick_unit.addItem("")
        self.R_InsulThick_unit.addItem("")
        self.R_InsulThick_unit.setObjectName(u"R_InsulThick_unit")

        self.groupBox_2_gridLayout_6.addWidget(self.R_InsulThick_unit, 3, 1, 1, 1)

        self.R_WireCopperR_2 = QDoubleSpinBox(self.groupBox_2)
        self.R_WireCopperR_2.setObjectName(u"R_WireCopperR_2")
        self.R_WireCopperR_2.setDecimals(6)
        self.R_WireCopperR_2.setMaximum(10000.000000000000000)
        self.R_WireCopperR_2.setSingleStep(0.000100000000000)
        self.R_WireCopperR_2.setValue(0.500000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_WireCopperR_2, 2, 3, 1, 1)

        self.R_LaminatR_unit = QComboBox(self.groupBox_2)
        self.R_LaminatR_unit.addItem("")
        self.R_LaminatR_unit.addItem("")
        self.R_LaminatR_unit.addItem("")
        self.R_LaminatR_unit.setObjectName(u"R_LaminatR_unit")

        self.groupBox_2_gridLayout_6.addWidget(self.R_LaminatR_unit, 7, 1, 1, 1)

        self.R_LaminatToothWedgeThickness_unit = QComboBox(self.groupBox_2)
        self.R_LaminatToothWedgeThickness_unit.addItem("")
        self.R_LaminatToothWedgeThickness_unit.addItem("")
        self.R_LaminatToothWedgeThickness_unit.addItem("")
        self.R_LaminatToothWedgeThickness_unit.setObjectName(u"R_LaminatToothWedgeThickness_unit")

        self.groupBox_2_gridLayout_6.addWidget(self.R_LaminatToothWedgeThickness_unit, 6, 1, 1, 1)

        self.R_LaminatToothWedgeThickness_1 = QDoubleSpinBox(self.groupBox_2)
        self.R_LaminatToothWedgeThickness_1.setObjectName(u"R_LaminatToothWedgeThickness_1")
        self.R_LaminatToothWedgeThickness_1.setDecimals(6)
        self.R_LaminatToothWedgeThickness_1.setMaximum(10000.000000000000000)
        self.R_LaminatToothWedgeThickness_1.setSingleStep(0.000100000000000)
        self.R_LaminatToothWedgeThickness_1.setValue(0.276000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_LaminatToothWedgeThickness_1, 6, 2, 1, 1)

        self.R_LaminatR_1 = QDoubleSpinBox(self.groupBox_2)
        self.R_LaminatR_1.setObjectName(u"R_LaminatR_1")
        self.R_LaminatR_1.setDecimals(6)
        self.R_LaminatR_1.setMaximum(10000.000000000000000)
        self.R_LaminatR_1.setSingleStep(0.000100000000000)
        self.R_LaminatR_1.setValue(10.000000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_LaminatR_1, 7, 2, 1, 1)

        self.R_LaminatR_2 = QDoubleSpinBox(self.groupBox_2)
        self.R_LaminatR_2.setObjectName(u"R_LaminatR_2")
        self.R_LaminatR_2.setDecimals(6)
        self.R_LaminatR_2.setMaximum(10000.000000000000000)
        self.R_LaminatR_2.setSingleStep(0.000100000000000)
        self.R_LaminatR_2.setValue(10.100000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_LaminatR_2, 7, 3, 1, 1)

        self.R_LamSlotLinerThick_2 = QDoubleSpinBox(self.groupBox_2)
        self.R_LamSlotLinerThick_2.setObjectName(u"R_LamSlotLinerThick_2")
        self.R_LamSlotLinerThick_2.setDecimals(6)
        self.R_LamSlotLinerThick_2.setMaximum(10000.000000000000000)
        self.R_LamSlotLinerThick_2.setSingleStep(0.000100000000000)
        self.R_LamSlotLinerThick_2.setValue(0.010000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_LamSlotLinerThick_2, 8, 3, 1, 1)

        self.R_LaminatToothWedgeThickness_2 = QDoubleSpinBox(self.groupBox_2)
        self.R_LaminatToothWedgeThickness_2.setObjectName(u"R_LaminatToothWedgeThickness_2")
        self.R_LaminatToothWedgeThickness_2.setDecimals(6)
        self.R_LaminatToothWedgeThickness_2.setMaximum(10000.000000000000000)
        self.R_LaminatToothWedgeThickness_2.setSingleStep(0.000100000000000)
        self.R_LaminatToothWedgeThickness_2.setValue(0.276000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_LaminatToothWedgeThickness_2, 6, 3, 1, 1)

        self.R_LamSlotLinerThick_1 = QDoubleSpinBox(self.groupBox_2)
        self.R_LamSlotLinerThick_1.setObjectName(u"R_LamSlotLinerThick_1")
        self.R_LamSlotLinerThick_1.setDecimals(6)
        self.R_LamSlotLinerThick_1.setMaximum(10000.000000000000000)
        self.R_LamSlotLinerThick_1.setSingleStep(0.000100000000000)
        self.R_LamSlotLinerThick_1.setValue(0.010000000000000)

        self.groupBox_2_gridLayout_6.addWidget(self.R_LamSlotLinerThick_1, 8, 2, 1, 1)

        self.R_LamSlotLinerThick_unit = QComboBox(self.groupBox_2)
        self.R_LamSlotLinerThick_unit.addItem("")
        self.R_LamSlotLinerThick_unit.addItem("")
        self.R_LamSlotLinerThick_unit.addItem("")
        self.R_LamSlotLinerThick_unit.setObjectName(u"R_LamSlotLinerThick_unit")

        self.groupBox_2_gridLayout_6.addWidget(self.R_LamSlotLinerThick_unit, 8, 1, 1, 1)


        self.tab_1_gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_17 = QGroupBox(self.scrollAreaWidgetContents_tab_1)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setFont(font)
        self.groupBox_17_gridLayout_8 = QGridLayout(self.groupBox_17)
        self.groupBox_17_gridLayout_8.setSpacing(0)
        self.groupBox_17_gridLayout_8.setObjectName(u"groupBox_17_gridLayout_8")
        self.R_FluidSpecificGrav_2 = QDoubleSpinBox(self.groupBox_17)
        self.R_FluidSpecificGrav_2.setObjectName(u"R_FluidSpecificGrav_2")
        self.R_FluidSpecificGrav_2.setDecimals(5)
        self.R_FluidSpecificGrav_2.setSingleStep(0.000100000000000)
        self.R_FluidSpecificGrav_2.setValue(0.001000000000000)

        self.groupBox_17_gridLayout_8.addWidget(self.R_FluidSpecificGrav_2, 1, 3, 1, 1)

        self.R_FluidKinVisc_unit = QComboBox(self.groupBox_17)
        self.R_FluidKinVisc_unit.addItem("")
        self.R_FluidKinVisc_unit.addItem("")
        self.R_FluidKinVisc_unit.setObjectName(u"R_FluidKinVisc_unit")

        self.groupBox_17_gridLayout_8.addWidget(self.R_FluidKinVisc_unit, 2, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox_17)
        self.label_35.setObjectName(u"label_35")

        self.groupBox_17_gridLayout_8.addWidget(self.label_35, 1, 0, 1, 1)

        self.R_AirgapRadialLength_1 = QDoubleSpinBox(self.groupBox_17)
        self.R_AirgapRadialLength_1.setObjectName(u"R_AirgapRadialLength_1")
        self.R_AirgapRadialLength_1.setDecimals(6)
        self.R_AirgapRadialLength_1.setMaximum(10000.000000000000000)
        self.R_AirgapRadialLength_1.setSingleStep(0.000100000000000)
        self.R_AirgapRadialLength_1.setValue(0.025000000000000)

        self.groupBox_17_gridLayout_8.addWidget(self.R_AirgapRadialLength_1, 0, 2, 1, 1)

        self.R_FluidSpecificGrav_1 = QDoubleSpinBox(self.groupBox_17)
        self.R_FluidSpecificGrav_1.setObjectName(u"R_FluidSpecificGrav_1")
        self.R_FluidSpecificGrav_1.setDecimals(5)
        self.R_FluidSpecificGrav_1.setSingleStep(0.000100000000000)
        self.R_FluidSpecificGrav_1.setValue(0.001000000000000)

        self.groupBox_17_gridLayout_8.addWidget(self.R_FluidSpecificGrav_1, 1, 2, 1, 1)

        self.label_37 = QLabel(self.groupBox_17)
        self.label_37.setObjectName(u"label_37")

        self.groupBox_17_gridLayout_8.addWidget(self.label_37, 0, 0, 1, 1)

        self.R_AirgapRadialLength_2 = QDoubleSpinBox(self.groupBox_17)
        self.R_AirgapRadialLength_2.setObjectName(u"R_AirgapRadialLength_2")
        self.R_AirgapRadialLength_2.setDecimals(6)
        self.R_AirgapRadialLength_2.setMaximum(10000.000000000000000)
        self.R_AirgapRadialLength_2.setSingleStep(0.000100000000000)
        self.R_AirgapRadialLength_2.setValue(0.025000000000000)

        self.groupBox_17_gridLayout_8.addWidget(self.R_AirgapRadialLength_2, 0, 3, 1, 1)

        self.R_FluidKinVisc_1 = QDoubleSpinBox(self.groupBox_17)
        self.R_FluidKinVisc_1.setObjectName(u"R_FluidKinVisc_1")
        self.R_FluidKinVisc_1.setMaximum(1000000.000000000000000)
        self.R_FluidKinVisc_1.setValue(15.000000000000000)

        self.groupBox_17_gridLayout_8.addWidget(self.R_FluidKinVisc_1, 2, 2, 1, 1)

        self.R_AirgapRadialLength_unit = QComboBox(self.groupBox_17)
        self.R_AirgapRadialLength_unit.addItem("")
        self.R_AirgapRadialLength_unit.addItem("")
        self.R_AirgapRadialLength_unit.addItem("")
        self.R_AirgapRadialLength_unit.setObjectName(u"R_AirgapRadialLength_unit")

        self.groupBox_17_gridLayout_8.addWidget(self.R_AirgapRadialLength_unit, 0, 1, 1, 1)

        self.label_36 = QLabel(self.groupBox_17)
        self.label_36.setObjectName(u"label_36")

        self.groupBox_17_gridLayout_8.addWidget(self.label_36, 2, 0, 1, 1)

        self.R_FluidKinVisc_2 = QDoubleSpinBox(self.groupBox_17)
        self.R_FluidKinVisc_2.setObjectName(u"R_FluidKinVisc_2")
        self.R_FluidKinVisc_2.setMaximum(1000000.000000000000000)
        self.R_FluidKinVisc_2.setValue(15.000000000000000)

        self.groupBox_17_gridLayout_8.addWidget(self.R_FluidKinVisc_2, 2, 3, 1, 1)


        self.tab_1_gridLayout_2.addWidget(self.groupBox_17, 3, 0, 1, 1)

        self.scrollArea_tab_1.setWidget(self.scrollAreaWidgetContents_tab_1)

        self.verticalLayout_tab_1_scrollWrapper.addWidget(self.scrollArea_tab_1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_tab_2_scrollWrapper = QVBoxLayout(self.tab_2)
        self.verticalLayout_tab_2_scrollWrapper.setObjectName(u"verticalLayout_tab_2_scrollWrapper")
        self.scrollArea_tab_2 = QScrollArea(self.tab_2)
        self.scrollArea_tab_2.setObjectName(u"scrollArea_tab_2")
        self.scrollArea_tab_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tab_2 = QWidget()
        self.scrollAreaWidgetContents_tab_2.setObjectName(u"scrollAreaWidgetContents_tab_2")
        self.scrollAreaWidgetContents_tab_2.setGeometry(QRect(0, 0, 971, 680))
        self.tab_2_gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_tab_2)
        self.tab_2_gridLayout_3.setSpacing(0)
        self.tab_2_gridLayout_3.setObjectName(u"tab_2_gridLayout_3")
        self.groupBox_21 = QGroupBox(self.scrollAreaWidgetContents_tab_2)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setFont(font)
        self.groupBox_21_gridLayout_12 = QGridLayout(self.groupBox_21)
        self.groupBox_21_gridLayout_12.setSpacing(0)
        self.groupBox_21_gridLayout_12.setObjectName(u"groupBox_21_gridLayout_12")
        self.TorqueOpt = QCheckBox(self.groupBox_21)
        self.TorqueOpt.setObjectName(u"TorqueOpt")
        self.TorqueOpt.setEnabled(True)
        self.TorqueOpt.setCheckable(True)
        self.TorqueOpt.setChecked(False)
        self.TorqueOpt.setTristate(False)

        self.groupBox_21_gridLayout_12.addWidget(self.TorqueOpt, 0, 0, 1, 1)

        self.Efficinecy_minOpt = QCheckBox(self.groupBox_21)
        self.Efficinecy_minOpt.setObjectName(u"Efficinecy_minOpt")

        self.groupBox_21_gridLayout_12.addWidget(self.Efficinecy_minOpt, 1, 0, 1, 1)

        self.Efficinecy_maxOpt = QCheckBox(self.groupBox_21)
        self.Efficinecy_maxOpt.setObjectName(u"Efficinecy_maxOpt")

        self.groupBox_21_gridLayout_12.addWidget(self.Efficinecy_maxOpt, 2, 0, 1, 1)

        self.WeightOpt = QCheckBox(self.groupBox_21)
        self.WeightOpt.setObjectName(u"WeightOpt")

        self.groupBox_21_gridLayout_12.addWidget(self.WeightOpt, 3, 0, 1, 1)

        self.MagWeightOpt = QCheckBox(self.groupBox_21)
        self.MagWeightOpt.setObjectName(u"MagWeightOpt")

        self.groupBox_21_gridLayout_12.addWidget(self.MagWeightOpt, 4, 0, 1, 1)

        self.VoltageOpt = QCheckBox(self.groupBox_21)
        self.VoltageOpt.setObjectName(u"VoltageOpt")

        self.groupBox_21_gridLayout_12.addWidget(self.VoltageOpt, 5, 0, 1, 1)

        self.MtrLengthOpt = QCheckBox(self.groupBox_21)
        self.MtrLengthOpt.setObjectName(u"MtrLengthOpt")

        self.groupBox_21_gridLayout_12.addWidget(self.MtrLengthOpt, 6, 0, 1, 1)

        self.MtrRadiusOpt = QCheckBox(self.groupBox_21)
        self.MtrRadiusOpt.setObjectName(u"MtrRadiusOpt")

        self.groupBox_21_gridLayout_12.addWidget(self.MtrRadiusOpt, 7, 0, 1, 1)


        self.tab_2_gridLayout_3.addWidget(self.groupBox_21, 2, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.scrollAreaWidgetContents_tab_2)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setFont(font)
        self.groupBox_20_gridLayout_11 = QGridLayout(self.groupBox_20)
        self.groupBox_20_gridLayout_11.setSpacing(0)
        self.groupBox_20_gridLayout_11.setObjectName(u"groupBox_20_gridLayout_11")
        self.label_52 = QLabel(self.groupBox_20)
        self.label_52.setObjectName(u"label_52")

        self.groupBox_20_gridLayout_11.addWidget(self.label_52, 2, 0, 1, 1)

        self.VDC_unit = QComboBox(self.groupBox_20)
        self.VDC_unit.addItem("")
        self.VDC_unit.setObjectName(u"VDC_unit")

        self.groupBox_20_gridLayout_11.addWidget(self.VDC_unit, 4, 1, 1, 1)

        self.label_54 = QLabel(self.groupBox_20)
        self.label_54.setObjectName(u"label_54")

        self.groupBox_20_gridLayout_11.addWidget(self.label_54, 3, 0, 1, 1)

        self.MinTor = QLineEdit(self.groupBox_20)
        self.MinTor.setObjectName(u"MinTor")

        self.groupBox_20_gridLayout_11.addWidget(self.MinTor, 1, 2, 1, 1)

        self.label_51 = QLabel(self.groupBox_20)
        self.label_51.setObjectName(u"label_51")

        self.groupBox_20_gridLayout_11.addWidget(self.label_51, 1, 0, 1, 1)

        self.MaxWeight = QDoubleSpinBox(self.groupBox_20)
        self.MaxWeight.setObjectName(u"MaxWeight")
        self.MaxWeight.setMaximum(20000.000000000000000)
        self.MaxWeight.setValue(1000.000000000000000)

        self.groupBox_20_gridLayout_11.addWidget(self.MaxWeight, 3, 2, 1, 1)

        self.VDC = QDoubleSpinBox(self.groupBox_20)
        self.VDC.setObjectName(u"VDC")
        self.VDC.setMaximum(2000.000000000000000)
        self.VDC.setValue(1000.000000000000000)

        self.groupBox_20_gridLayout_11.addWidget(self.VDC, 4, 2, 1, 1)

        self.SpeedReq = QLineEdit(self.groupBox_20)
        self.SpeedReq.setObjectName(u"SpeedReq")
        self.SpeedReq.setFocusPolicy(Qt.StrongFocus)

        self.groupBox_20_gridLayout_11.addWidget(self.SpeedReq, 0, 2, 1, 2)

        self.SpeedReq_unit = QComboBox(self.groupBox_20)
        self.SpeedReq_unit.addItem("")
        self.SpeedReq_unit.addItem("")
        self.SpeedReq_unit.addItem("")
        self.SpeedReq_unit.setObjectName(u"SpeedReq_unit")

        self.groupBox_20_gridLayout_11.addWidget(self.SpeedReq_unit, 0, 1, 1, 1)

        self.MinEff_unit = QComboBox(self.groupBox_20)
        self.MinEff_unit.addItem("")
        self.MinEff_unit.setObjectName(u"MinEff_unit")

        self.groupBox_20_gridLayout_11.addWidget(self.MinEff_unit, 2, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox_20)
        self.label_50.setObjectName(u"label_50")

        self.groupBox_20_gridLayout_11.addWidget(self.label_50, 0, 0, 1, 1)

        self.label_55 = QLabel(self.groupBox_20)
        self.label_55.setObjectName(u"label_55")

        self.groupBox_20_gridLayout_11.addWidget(self.label_55, 4, 0, 1, 1)

        self.MinTor_unit = QComboBox(self.groupBox_20)
        self.MinTor_unit.addItem("")
        self.MinTor_unit.addItem("")
        self.MinTor_unit.addItem("")
        self.MinTor_unit.setObjectName(u"MinTor_unit")

        self.groupBox_20_gridLayout_11.addWidget(self.MinTor_unit, 1, 1, 1, 1)

        self.MinEff_ = QDoubleSpinBox(self.groupBox_20)
        self.MinEff_.setObjectName(u"MinEff_")
        self.MinEff_.setSingleStep(0.050000000000000)
        self.MinEff_.setValue(0.500000000000000)

        self.groupBox_20_gridLayout_11.addWidget(self.MinEff_, 2, 2, 1, 1)

        self.MaxWeigh_unit = QComboBox(self.groupBox_20)
        self.MaxWeigh_unit.addItem("")
        self.MaxWeigh_unit.addItem("")
        self.MaxWeigh_unit.setObjectName(u"MaxWeigh_unit")

        self.groupBox_20_gridLayout_11.addWidget(self.MaxWeigh_unit, 3, 1, 1, 1)


        self.tab_2_gridLayout_3.addWidget(self.groupBox_20, 1, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.scrollAreaWidgetContents_tab_2)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setFont(font)
        self.groupBox_19_gridLayout_10 = QGridLayout(self.groupBox_19)
        self.groupBox_19_gridLayout_10.setSpacing(0)
        self.groupBox_19_gridLayout_10.setObjectName(u"groupBox_19_gridLayout_10")
        self.label_48 = QLabel(self.groupBox_19)
        self.label_48.setObjectName(u"label_48")

        self.groupBox_19_gridLayout_10.addWidget(self.label_48, 4, 0, 1, 1)

        self.label_45 = QLabel(self.groupBox_19)
        self.label_45.setObjectName(u"label_45")

        self.groupBox_19_gridLayout_10.addWidget(self.label_45, 1, 0, 1, 1)

        self.label_46 = QLabel(self.groupBox_19)
        self.label_46.setObjectName(u"label_46")

        self.groupBox_19_gridLayout_10.addWidget(self.label_46, 6, 0, 1, 1)

        self.npop = QSpinBox(self.groupBox_19)
        self.npop.setObjectName(u"npop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.npop.sizePolicy().hasHeightForWidth())
        self.npop.setSizePolicy(sizePolicy1)
        self.npop.setMaximum(10000)
        self.npop.setValue(10)

        self.groupBox_19_gridLayout_10.addWidget(self.npop, 0, 2, 1, 1)

        self.ngens = QSpinBox(self.groupBox_19)
        self.ngens.setObjectName(u"ngens")
        sizePolicy1.setHeightForWidth(self.ngens.sizePolicy().hasHeightForWidth())
        self.ngens.setSizePolicy(sizePolicy1)
        self.ngens.setMaximum(10000)
        self.ngens.setValue(10)

        self.groupBox_19_gridLayout_10.addWidget(self.ngens, 1, 2, 1, 1)

        self.label_44 = QLabel(self.groupBox_19)
        self.label_44.setObjectName(u"label_44")

        self.groupBox_19_gridLayout_10.addWidget(self.label_44, 0, 0, 1, 1)

        self.eta_help = QPushButton(self.groupBox_19)
        self.eta_help.setObjectName(u"eta_help")

        self.groupBox_19_gridLayout_10.addWidget(self.eta_help, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.groupBox_19_gridLayout_10.addItem(self.horizontalSpacer, 3, 3, 1, 1)

        self.ProbMut = QDoubleSpinBox(self.groupBox_19)
        self.ProbMut.setObjectName(u"ProbMut")
        sizePolicy1.setHeightForWidth(self.ProbMut.sizePolicy().hasHeightForWidth())
        self.ProbMut.setSizePolicy(sizePolicy1)
        self.ProbMut.setMaximum(1.000000000000000)
        self.ProbMut.setSingleStep(0.010000000000000)
        self.ProbMut.setValue(0.100000000000000)

        self.groupBox_19_gridLayout_10.addWidget(self.ProbMut, 3, 2, 1, 1)

        self.label_49 = QLabel(self.groupBox_19)
        self.label_49.setObjectName(u"label_49")

        self.groupBox_19_gridLayout_10.addWidget(self.label_49, 3, 0, 1, 1)

        self.nprocesses = QSpinBox(self.groupBox_19)
        self.nprocesses.setObjectName(u"nprocesses")
        sizePolicy1.setHeightForWidth(self.nprocesses.sizePolicy().hasHeightForWidth())
        self.nprocesses.setSizePolicy(sizePolicy1)
        self.nprocesses.setMaximum(20)
        self.nprocesses.setValue(2)

        self.groupBox_19_gridLayout_10.addWidget(self.nprocesses, 6, 2, 1, 1)

        self.DisMut = QDoubleSpinBox(self.groupBox_19)
        self.DisMut.setObjectName(u"DisMut")
        sizePolicy1.setHeightForWidth(self.DisMut.sizePolicy().hasHeightForWidth())
        self.DisMut.setSizePolicy(sizePolicy1)
        self.DisMut.setMaximum(100.000000000000000)
        self.DisMut.setValue(5.000000000000000)

        self.groupBox_19_gridLayout_10.addWidget(self.DisMut, 4, 2, 1, 1)


        self.tab_2_gridLayout_3.addWidget(self.groupBox_19, 0, 0, 1, 1)

        self.scrollArea_tab_2.setWidget(self.scrollAreaWidgetContents_tab_2)

        self.verticalLayout_tab_2_scrollWrapper.addWidget(self.scrollArea_tab_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_tab_3_scrollWrapper = QVBoxLayout(self.tab_3)
        self.verticalLayout_tab_3_scrollWrapper.setObjectName(u"verticalLayout_tab_3_scrollWrapper")
        self.scrollArea_tab_3 = QScrollArea(self.tab_3)
        self.scrollArea_tab_3.setObjectName(u"scrollArea_tab_3")
        self.scrollArea_tab_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tab_3 = QWidget()
        self.scrollAreaWidgetContents_tab_3.setObjectName(u"scrollAreaWidgetContents_tab_3")
        self.scrollAreaWidgetContents_tab_3.setGeometry(QRect(0, 0, 971, 680))
        self.tab_3_gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_tab_3)
        self.tab_3_gridLayout_4.setSpacing(0)
        self.tab_3_gridLayout_4.setObjectName(u"tab_3_gridLayout_4")
        self.Execution = QPushButton(self.scrollAreaWidgetContents_tab_3)
        self.Execution.setObjectName(u"Execution")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Execution.sizePolicy().hasHeightForWidth())
        self.Execution.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.Execution.setPalette(palette)
        self.Execution.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.Execution.setAutoDefault(False)
        self.Execution.setFlat(False)

        self.tab_3_gridLayout_4.addWidget(self.Execution, 1, 0, 1, 1)

        self.stopButton = QPushButton(self.scrollAreaWidgetContents_tab_3)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy2.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy2)
        self.stopButton.setStyleSheet(u"background-color: rgb(255, 123, 132);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.tab_3_gridLayout_4.addWidget(self.stopButton, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_tab_3)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)

        self.tab_3_gridLayout_4.addWidget(self.tableWidget, 4, 0, 1, 2)

        self.progressBar = QProgressBar(self.scrollAreaWidgetContents_tab_3)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy4)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.tab_3_gridLayout_4.addWidget(self.progressBar, 0, 0, 1, 2)

        self.scrollArea_tab_3.setWidget(self.scrollAreaWidgetContents_tab_3)

        self.verticalLayout_tab_3_scrollWrapper.addWidget(self.scrollArea_tab_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_tab_4_scrollWrapper = QVBoxLayout(self.tab_4)
        self.verticalLayout_tab_4_scrollWrapper.setObjectName(u"verticalLayout_tab_4_scrollWrapper")
        self.scrollArea_tab_4 = QScrollArea(self.tab_4)
        self.scrollArea_tab_4.setObjectName(u"scrollArea_tab_4")
        self.scrollArea_tab_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tab_4 = QWidget()
        self.scrollAreaWidgetContents_tab_4.setObjectName(u"scrollAreaWidgetContents_tab_4")
        self.scrollAreaWidgetContents_tab_4.setGeometry(QRect(0, 0, 971, 680))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_tab_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_22 = QGroupBox(self.scrollAreaWidgetContents_tab_4)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setFont(font)
        self.groupBox_22_gridLayout_13 = QGridLayout(self.groupBox_22)
        self.groupBox_22_gridLayout_13.setSpacing(0)
        self.groupBox_22_gridLayout_13.setObjectName(u"groupBox_22_gridLayout_13")
        self.MinTrqMargin_Percent = QCheckBox(self.groupBox_22)
        self.MinTrqMargin_Percent.setObjectName(u"MinTrqMargin_Percent")

        self.groupBox_22_gridLayout_13.addWidget(self.MinTrqMargin_Percent, 0, 0, 1, 1)

        self.MaxTotalLoss_W = QCheckBox(self.groupBox_22)
        self.MaxTotalLoss_W.setObjectName(u"MaxTotalLoss_W")

        self.groupBox_22_gridLayout_13.addWidget(self.MaxTotalLoss_W, 9, 0, 1, 1)

        self.ParallelPlot = QPushButton(self.groupBox_22)
        self.ParallelPlot.setObjectName(u"ParallelPlot")
        self.ParallelPlot.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.groupBox_22_gridLayout_13.addWidget(self.ParallelPlot, 13, 0, 1, 1)

        self.R_MtrLength_m = QCheckBox(self.groupBox_22)
        self.R_MtrLength_m.setObjectName(u"R_MtrLength_m")

        self.groupBox_22_gridLayout_13.addWidget(self.R_MtrLength_m, 7, 0, 1, 1)

        self.dropdown3 = QComboBox(self.groupBox_22)
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.addItem("")
        self.dropdown3.setObjectName(u"dropdown3")

        self.groupBox_22_gridLayout_13.addWidget(self.dropdown3, 12, 0, 1, 1)

        self.MeanTrqMargin_Percent = QCheckBox(self.groupBox_22)
        self.MeanTrqMargin_Percent.setObjectName(u"MeanTrqMargin_Percent")

        self.groupBox_22_gridLayout_13.addWidget(self.MeanTrqMargin_Percent, 1, 0, 1, 1)

        self.R_LaminatR_m = QCheckBox(self.groupBox_22)
        self.R_LaminatR_m.setObjectName(u"R_LaminatR_m")

        self.groupBox_22_gridLayout_13.addWidget(self.R_LaminatR_m, 8, 0, 1, 1)

        self.MeanEffMtr_Percent = QCheckBox(self.groupBox_22)
        self.MeanEffMtr_Percent.setObjectName(u"MeanEffMtr_Percent")

        self.groupBox_22_gridLayout_13.addWidget(self.MeanEffMtr_Percent, 3, 0, 1, 1)

        self.dropdown1 = QComboBox(self.groupBox_22)
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.addItem("")
        self.dropdown1.setObjectName(u"dropdown1")

        self.groupBox_22_gridLayout_13.addWidget(self.dropdown1, 10, 0, 1, 1)

        self.MagVol_m3 = QCheckBox(self.groupBox_22)
        self.MagVol_m3.setObjectName(u"MagVol_m3")

        self.groupBox_22_gridLayout_13.addWidget(self.MagVol_m3, 6, 0, 1, 1)

        self.Weight_kg = QCheckBox(self.groupBox_22)
        self.Weight_kg.setObjectName(u"Weight_kg")

        self.groupBox_22_gridLayout_13.addWidget(self.Weight_kg, 4, 0, 1, 1)

        self.MinEffMtr_Percent = QCheckBox(self.groupBox_22)
        self.MinEffMtr_Percent.setObjectName(u"MinEffMtr_Percent")

        self.groupBox_22_gridLayout_13.addWidget(self.MinEffMtr_Percent, 2, 0, 1, 1)

        self.VDC_2 = QCheckBox(self.groupBox_22)
        self.VDC_2.setObjectName(u"VDC_2")

        self.groupBox_22_gridLayout_13.addWidget(self.VDC_2, 5, 0, 1, 1)

        self.dropdown2 = QComboBox(self.groupBox_22)
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.addItem("")
        self.dropdown2.setObjectName(u"dropdown2")

        self.groupBox_22_gridLayout_13.addWidget(self.dropdown2, 11, 0, 1, 1)

        self.ThreeDPlot = QPushButton(self.groupBox_22)
        self.ThreeDPlot.setObjectName(u"ThreeDPlot")
        self.ThreeDPlot.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);")

        self.groupBox_22_gridLayout_13.addWidget(self.ThreeDPlot, 13, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.scrollArea_tab_4.setWidget(self.scrollAreaWidgetContents_tab_4)

        self.verticalLayout_tab_4_scrollWrapper.addWidget(self.scrollArea_tab_4)

        self.tabWidget.addTab(self.tab_4, "")

        self.centralwidget_gridLayout_1.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(972, 16777215))
        self.label_17.setPixmap(QPixmap(u":/ParkerLogo_80p.jpg"))
        self.label_17.setScaledContents(True)

        self.centralwidget_gridLayout_1.addWidget(self.label_17, 1, 0, 1, 1)

        UserInterface.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(UserInterface)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1017, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuScale = QMenu(self.menubar)
        self.menuScale.setObjectName(u"menuScale")
        UserInterface.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(UserInterface)
        self.statusbar.setObjectName(u"statusbar")
        UserInterface.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuScale.menuAction())
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuScale.addAction(self.font12)
        self.menuScale.addAction(self.font14)
        self.menuScale.addAction(self.font16)
        self.menuScale.addAction(self.font18)
        self.menuScale.addAction(self.font20)
        self.menuScale.addAction(self.font22)

        self.retranslateUi(UserInterface)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(UserInterface)
    # setupUi

    def retranslateUi(self, UserInterface):
        UserInterface.setWindowTitle(QCoreApplication.translate("UserInterface", u"200015SSW - Genetic Algorithm Motor Optimizer Tool (GAMOT) ", None))
        self.actionLoad.setText(QCoreApplication.translate("UserInterface", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("UserInterface", u"Save", None))
        self.action12.setText(QCoreApplication.translate("UserInterface", u"12", None))
        self.action14.setText(QCoreApplication.translate("UserInterface", u"14", None))
        self.action16.setText(QCoreApplication.translate("UserInterface", u"16", None))
        self.action18.setText(QCoreApplication.translate("UserInterface", u"18", None))
        self.action20.setText(QCoreApplication.translate("UserInterface", u"20", None))
        self.action22.setText(QCoreApplication.translate("UserInterface", u"22", None))
        self.action10.setText(QCoreApplication.translate("UserInterface", u"10", None))
        self.font12.setText(QCoreApplication.translate("UserInterface", u"12", None))
        self.font14.setText(QCoreApplication.translate("UserInterface", u"14", None))
        self.font16.setText(QCoreApplication.translate("UserInterface", u"16", None))
        self.font18.setText(QCoreApplication.translate("UserInterface", u"18", None))
        self.font20.setText(QCoreApplication.translate("UserInterface", u"20", None))
        self.font22.setText(QCoreApplication.translate("UserInterface", u"22", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("UserInterface", u"MATERIAL", None))
        self.Magnet_Material.setItemText(0, QCoreApplication.translate("UserInterface", u"Recoma 18", None))
        self.Magnet_Material.setItemText(1, QCoreApplication.translate("UserInterface", u"Recoma 20", None))
        self.Magnet_Material.setItemText(2, QCoreApplication.translate("UserInterface", u"Recoma 22", None))
        self.Magnet_Material.setItemText(3, QCoreApplication.translate("UserInterface", u"Recoma 25", None))
        self.Magnet_Material.setItemText(4, QCoreApplication.translate("UserInterface", u"Recoma 24HE", None))
        self.Magnet_Material.setItemText(5, QCoreApplication.translate("UserInterface", u"Recoma 26", None))
        self.Magnet_Material.setItemText(6, QCoreApplication.translate("UserInterface", u"Recoma 26HE", None))
        self.Magnet_Material.setItemText(7, QCoreApplication.translate("UserInterface", u"Recoma 28", None))
        self.Magnet_Material.setItemText(8, QCoreApplication.translate("UserInterface", u"Recoma 28HE", None))
        self.Magnet_Material.setItemText(9, QCoreApplication.translate("UserInterface", u"Recoma 30", None))
        self.Magnet_Material.setItemText(10, QCoreApplication.translate("UserInterface", u"Recoma 30HE", None))
        self.Magnet_Material.setItemText(11, QCoreApplication.translate("UserInterface", u"Recoma 30S", None))
        self.Magnet_Material.setItemText(12, QCoreApplication.translate("UserInterface", u"Recoma 32", None))
        self.Magnet_Material.setItemText(13, QCoreApplication.translate("UserInterface", u"Recoma 32S", None))
        self.Magnet_Material.setItemText(14, QCoreApplication.translate("UserInterface", u"Recoma 33E", None))
        self.Magnet_Material.setItemText(15, QCoreApplication.translate("UserInterface", u"Recoma 35E", None))

        self.label_40.setText(QCoreApplication.translate("UserInterface", u"Magnet Material", None))
        self.Iron_Material.setItemText(0, QCoreApplication.translate("UserInterface", u"M19", None))
        self.Iron_Material.setItemText(1, QCoreApplication.translate("UserInterface", u"430 Stainless Steel", None))
        self.Iron_Material.setItemText(2, QCoreApplication.translate("UserInterface", u"1215 Steel", None))
        self.Iron_Material.setItemText(3, QCoreApplication.translate("UserInterface", u"1018 Steel", None))
        self.Iron_Material.setItemText(4, QCoreApplication.translate("UserInterface", u"1008 Steel", None))
        self.Iron_Material.setItemText(5, QCoreApplication.translate("UserInterface", u"1010 Steel", None))
        self.Iron_Material.setItemText(6, QCoreApplication.translate("UserInterface", u"Hiperco 50", None))

        self.label_42.setText(QCoreApplication.translate("UserInterface", u"Lamination Material", None))
        self.label_41.setText(QCoreApplication.translate("UserInterface", u"Iron Material", None))
        self.Lamination_Material.setItemText(0, QCoreApplication.translate("UserInterface", u"M19", None))
        self.Lamination_Material.setItemText(1, QCoreApplication.translate("UserInterface", u"Hiperco 50", None))

        self.groupBox.setTitle(QCoreApplication.translate("UserInterface", u"ROTOR", None))
        self.label_6.setText(QCoreApplication.translate("UserInterface", u"Magnetic Loss Coefficient, a2", None))
        self.label.setText(QCoreApplication.translate("UserInterface", u"Number of Pole Pairs", None))
        self.R_MagnetOutR_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_MagnetOutR_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_MagnetOutR_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.label_4.setText(QCoreApplication.translate("UserInterface", u"Magnet Assembly Backiron Inner Radius                    ", None))
        self.label_5.setText(QCoreApplication.translate("UserInterface", u"Magnetic Loss Coefficient, a1", None))
        self.label_3.setText(QCoreApplication.translate("UserInterface", u"Magnet Outer Radius", None))
        self.label_2.setText(QCoreApplication.translate("UserInterface", u"Radial Length of Magnet", None))
        self.label_7.setText(QCoreApplication.translate("UserInterface", u"Magnetic Loss Coefficient, a3", None))
        self.R_MagnetRadialLength_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_MagnetRadialLength_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_MagnetRadialLength_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.R_MagnetBackIronInnerR_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_MagnetBackIronInnerR_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_MagnetBackIronInnerR_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.label_16.setText(QCoreApplication.translate("UserInterface", u"Minimum Value", None))
        self.label_18.setText(QCoreApplication.translate("UserInterface", u"Maximum Value", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("UserInterface", u"MECHANICAL", None))
        self.label_31.setText(QCoreApplication.translate("UserInterface", u"Motor Length", None))
        self.R_MtrLength_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_MtrLength_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_MtrLength_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.label_32.setText(QCoreApplication.translate("UserInterface", u"Load Inertia Reflected to Motor                                ", None))
        self.R_LoadInertia_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"ozm-in^2", None))
        self.R_LoadInertia_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"ozf-in-s^2", None))
        self.R_LoadInertia_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"lbm-in^2", None))
        self.R_LoadInertia_unit.setItemText(3, QCoreApplication.translate("UserInterface", u"lbm-ft^2", None))
        self.R_LoadInertia_unit.setItemText(4, QCoreApplication.translate("UserInterface", u"kg-m^2", None))
        self.R_LoadInertia_unit.setItemText(5, QCoreApplication.translate("UserInterface", u"N-m-s^2", None))

        self.label_33.setText(QCoreApplication.translate("UserInterface", u"Gear Ratio", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("UserInterface", u"STATOR", None))
        self.label_8.setText(QCoreApplication.translate("UserInterface", u"Number of Electrical Phase", None))
        self.label_9.setText(QCoreApplication.translate("UserInterface", u"Phase Current Amplitude at Max. Torque", None))
        self.label_13.setText(QCoreApplication.translate("UserInterface", u"Lamination Tooth Tip and Wedge Thickness               ", None))
        self.label_10.setText(QCoreApplication.translate("UserInterface", u"Wire Copper Radius", None))
        self.label_11.setText(QCoreApplication.translate("UserInterface", u"Wire Insulation Thickness", None))
        self.label_12.setText(QCoreApplication.translate("UserInterface", u"Fill Factor", None))
        self.R_WireCopperR_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_WireCopperR_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_WireCopperR_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.label_15.setText(QCoreApplication.translate("UserInterface", u"Lamination Slot Liner Thickness", None))
        self.label_14.setText(QCoreApplication.translate("UserInterface", u"Lamination Outer Radius", None))
        self.R_PhaseCurrentAmp_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"Apk", None))
        self.R_PhaseCurrentAmp_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"Arms", None))

        self.R_InsulThick_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_InsulThick_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_InsulThick_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.R_LaminatR_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_LaminatR_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_LaminatR_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.R_LaminatToothWedgeThickness_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_LaminatToothWedgeThickness_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_LaminatToothWedgeThickness_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.R_LamSlotLinerThick_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_LamSlotLinerThick_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_LamSlotLinerThick_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.groupBox_17.setTitle(QCoreApplication.translate("UserInterface", u"AIRGAP", None))
        self.R_FluidKinVisc_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"cSt", None))
        self.R_FluidKinVisc_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m^2/s", None))

        self.label_35.setText(QCoreApplication.translate("UserInterface", u"Airgap Fluid Specific Gravity", None))
        self.label_37.setText(QCoreApplication.translate("UserInterface", u"Airgap Length", None))
        self.R_AirgapRadialLength_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"in", None))
        self.R_AirgapRadialLength_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"m", None))
        self.R_AirgapRadialLength_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"mm", None))

        self.label_36.setText(QCoreApplication.translate("UserInterface", u"Airgap Fluid Viscosity                                                ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("UserInterface", u"Motor Parameters", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("UserInterface", u"TO BE OPTIMIZED (select at least one)", None))
        self.TorqueOpt.setText(QCoreApplication.translate("UserInterface", u"Maximize Gearbox Output Torque", None))
        self.Efficinecy_minOpt.setText(QCoreApplication.translate("UserInterface", u"Maximize Motor Efficiency (Min. Among Operating Points)", None))
        self.Efficinecy_maxOpt.setText(QCoreApplication.translate("UserInterface", u"Maximize Motor Efficiency (Max. Among Operating Points)", None))
        self.WeightOpt.setText(QCoreApplication.translate("UserInterface", u"Minimize Motor Weight", None))
        self.MagWeightOpt.setText(QCoreApplication.translate("UserInterface", u"Minimize Magnet Material Volume", None))
        self.VoltageOpt.setText(QCoreApplication.translate("UserInterface", u"Minimize Phase Voltage", None))
        self.MtrLengthOpt.setText(QCoreApplication.translate("UserInterface", u"Minimize Motor Length", None))
        self.MtrRadiusOpt.setText(QCoreApplication.translate("UserInterface", u"Minimize Motor Radius", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("UserInterface", u"PERFORMANCE REQUIREMENT", None))
        self.label_52.setText(QCoreApplication.translate("UserInterface", u"Minimum Acceptable Motor Efficiency", None))
        self.VDC_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"VDC", None))

        self.label_54.setText(QCoreApplication.translate("UserInterface", u"Maximum Acceptable Motor Weight", None))
        self.MinTor.setText(QCoreApplication.translate("UserInterface", u"51079.0, 4000.0, 11782.0, 25261.0", None))
        self.label_51.setText(QCoreApplication.translate("UserInterface", u"Gearbox Output Min. Torque Points (Comma-Separated)    ", None))
        self.SpeedReq.setInputMask("")
        self.SpeedReq.setText(QCoreApplication.translate("UserInterface", u"30.0, 562.0, 706.0, 417.0", None))
        self.SpeedReq_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"rpm", None))
        self.SpeedReq_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"rad/s", None))
        self.SpeedReq_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"Hz", None))

        self.MinEff_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"Fraction", None))

        self.label_50.setText(QCoreApplication.translate("UserInterface", u"Gearbox Output Speed Points (Comma-Separated)", None))
        self.label_55.setText(QCoreApplication.translate("UserInterface", u"Minimum Available Bus Voltage", None))
        self.MinTor_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"N-m", None))
        self.MinTor_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"in-lb", None))
        self.MinTor_unit.setItemText(2, QCoreApplication.translate("UserInterface", u"ft-lb", None))

        self.MaxWeigh_unit.setItemText(0, QCoreApplication.translate("UserInterface", u"kg", None))
        self.MaxWeigh_unit.setItemText(1, QCoreApplication.translate("UserInterface", u"lbm", None))

        self.groupBox_19.setTitle(QCoreApplication.translate("UserInterface", u"OPTIMIZATION CONFIGURATION", None))
        self.label_48.setText(QCoreApplication.translate("UserInterface", u"Distribution of Mutation     ", None))
        self.label_45.setText(QCoreApplication.translate("UserInterface", u"Number of Generations", None))
        self.label_46.setText(QCoreApplication.translate("UserInterface", u"Number of Processors", None))
        self.label_44.setText(QCoreApplication.translate("UserInterface", u"Population Size", None))
        self.eta_help.setText(QCoreApplication.translate("UserInterface", u"Help", None))
        self.label_49.setText(QCoreApplication.translate("UserInterface", u"Probability of Mutation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("UserInterface", u"Optimization", None))
        self.Execution.setText(QCoreApplication.translate("UserInterface", u"Execute Optimization", None))
        self.stopButton.setText(QCoreApplication.translate("UserInterface", u"Stop Optimization", None))
#if QT_CONFIG(tooltip)
        self.progressBar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.progressBar.setFormat(QCoreApplication.translate("UserInterface", u"%p% Progress", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("UserInterface", u"Execution", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("UserInterface", u"SELECT SIGNALS FOR PLOTTING", None))
        self.MinTrqMargin_Percent.setText(QCoreApplication.translate("UserInterface", u"Minimum Torque Margin", None))
        self.MaxTotalLoss_W.setText(QCoreApplication.translate("UserInterface", u"Maximum Motor Loss", None))
        self.ParallelPlot.setText(QCoreApplication.translate("UserInterface", u"Parallel Plot", None))
        self.R_MtrLength_m.setText(QCoreApplication.translate("UserInterface", u"Motor Length", None))
        self.dropdown3.setItemText(0, QCoreApplication.translate("UserInterface", u"# of pole pairs", None))
        self.dropdown3.setItemText(1, QCoreApplication.translate("UserInterface", u"Radial length of magnet", None))
        self.dropdown3.setItemText(2, QCoreApplication.translate("UserInterface", u"Wire copper radius", None))
        self.dropdown3.setItemText(3, QCoreApplication.translate("UserInterface", u"Fill factor", None))
        self.dropdown3.setItemText(4, QCoreApplication.translate("UserInterface", u"Lamination tooth tip and wedge thickness", None))
        self.dropdown3.setItemText(5, QCoreApplication.translate("UserInterface", u"Lamination slot liner thickness", None))
        self.dropdown3.setItemText(6, QCoreApplication.translate("UserInterface", u"Gear ratio", None))
        self.dropdown3.setItemText(7, QCoreApplication.translate("UserInterface", u"Magnet backiron inner radius", None))
        self.dropdown3.setItemText(8, QCoreApplication.translate("UserInterface", u"Magnet backiron outer radius", None))
        self.dropdown3.setItemText(9, QCoreApplication.translate("UserInterface", u"Tooth width", None))
        self.dropdown3.setItemText(10, QCoreApplication.translate("UserInterface", u"Lamination tooth tip radius", None))
        self.dropdown3.setItemText(11, QCoreApplication.translate("UserInterface", u"Lamination slot radius", None))
        self.dropdown3.setItemText(12, QCoreApplication.translate("UserInterface", u"Magnet inner radius", None))
        self.dropdown3.setItemText(13, QCoreApplication.translate("UserInterface", u"Backiron thickness, lamination", None))
        self.dropdown3.setItemText(14, QCoreApplication.translate("UserInterface", u"Backiron thickness, magnet assembly", None))
        self.dropdown3.setItemText(15, QCoreApplication.translate("UserInterface", u"Lamination slot outer", None))
        self.dropdown3.setItemText(16, QCoreApplication.translate("UserInterface", u"Lamination slot area", None))
        self.dropdown3.setItemText(17, QCoreApplication.translate("UserInterface", u"Winding Slot area", None))
        self.dropdown3.setItemText(18, QCoreApplication.translate("UserInterface", u"Arc length of lamination ID", None))
        self.dropdown3.setItemText(19, QCoreApplication.translate("UserInterface", u"Arc length of one tooth pitch", None))
        self.dropdown3.setItemText(20, QCoreApplication.translate("UserInterface", u"Approx width of slot opening", None))
        self.dropdown3.setItemText(21, QCoreApplication.translate("UserInterface", u"# of turns", None))
        self.dropdown3.setItemText(22, QCoreApplication.translate("UserInterface", u"Actual flux density", None))
        self.dropdown3.setItemText(23, QCoreApplication.translate("UserInterface", u"Actual coil flux", None))
        self.dropdown3.setItemText(24, QCoreApplication.translate("UserInterface", u"Rated Torque per phase", None))
        self.dropdown3.setItemText(25, QCoreApplication.translate("UserInterface", u"Torque constant", None))
        self.dropdown3.setItemText(26, QCoreApplication.translate("UserInterface", u"BackEMF constant", None))
        self.dropdown3.setItemText(27, QCoreApplication.translate("UserInterface", u"Phase inductance", None))
        self.dropdown3.setItemText(28, QCoreApplication.translate("UserInterface", u"Phase resistance", None))
        self.dropdown3.setItemText(29, QCoreApplication.translate("UserInterface", u"Inertia", None))
        self.dropdown3.setItemText(30, QCoreApplication.translate("UserInterface", u"torque/inertia", None))
        self.dropdown3.setItemText(31, QCoreApplication.translate("UserInterface", u"Motor volume", None))
        self.dropdown3.setItemText(32, QCoreApplication.translate("UserInterface", u"Stator surface area", None))
        self.dropdown3.setItemText(33, QCoreApplication.translate("UserInterface", u"Fe weight", None))
        self.dropdown3.setItemText(34, QCoreApplication.translate("UserInterface", u"Cu weight", None))
        self.dropdown3.setItemText(35, QCoreApplication.translate("UserInterface", u"Rotor weight", None))
        self.dropdown3.setItemText(36, QCoreApplication.translate("UserInterface", u"Current density", None))
        self.dropdown3.setItemText(37, QCoreApplication.translate("UserInterface", u"Mean resistive losses", None))
        self.dropdown3.setItemText(38, QCoreApplication.translate("UserInterface", u"Mean back iron losses", None))
        self.dropdown3.setItemText(39, QCoreApplication.translate("UserInterface", u"Mean fluid losses", None))

        self.MeanTrqMargin_Percent.setText(QCoreApplication.translate("UserInterface", u"Average Torque Margin", None))
        self.R_LaminatR_m.setText(QCoreApplication.translate("UserInterface", u"Motor Radius", None))
        self.MeanEffMtr_Percent.setText(QCoreApplication.translate("UserInterface", u"Average Efficiency", None))
        self.dropdown1.setItemText(0, QCoreApplication.translate("UserInterface", u"# of pole pairs", None))
        self.dropdown1.setItemText(1, QCoreApplication.translate("UserInterface", u"Radial length of magnet", None))
        self.dropdown1.setItemText(2, QCoreApplication.translate("UserInterface", u"Wire copper radius", None))
        self.dropdown1.setItemText(3, QCoreApplication.translate("UserInterface", u"Fill factor", None))
        self.dropdown1.setItemText(4, QCoreApplication.translate("UserInterface", u"Lamination tooth tip and wedge thickness", None))
        self.dropdown1.setItemText(5, QCoreApplication.translate("UserInterface", u"Lamination slot liner thickness", None))
        self.dropdown1.setItemText(6, QCoreApplication.translate("UserInterface", u"Gear ratio", None))
        self.dropdown1.setItemText(7, QCoreApplication.translate("UserInterface", u"Magnet backiron inner radius", None))
        self.dropdown1.setItemText(8, QCoreApplication.translate("UserInterface", u"Magnet backiron outer radius", None))
        self.dropdown1.setItemText(9, QCoreApplication.translate("UserInterface", u"Tooth width", None))
        self.dropdown1.setItemText(10, QCoreApplication.translate("UserInterface", u"Lamination tooth tip radius", None))
        self.dropdown1.setItemText(11, QCoreApplication.translate("UserInterface", u"Lamination slot radius", None))
        self.dropdown1.setItemText(12, QCoreApplication.translate("UserInterface", u"Magnet inner radius", None))
        self.dropdown1.setItemText(13, QCoreApplication.translate("UserInterface", u"Backiron thickness, lamination", None))
        self.dropdown1.setItemText(14, QCoreApplication.translate("UserInterface", u"Backiron thickness, magnet assembly", None))
        self.dropdown1.setItemText(15, QCoreApplication.translate("UserInterface", u"Lamination slot outer", None))
        self.dropdown1.setItemText(16, QCoreApplication.translate("UserInterface", u"Lamination slot area", None))
        self.dropdown1.setItemText(17, QCoreApplication.translate("UserInterface", u"Winding Slot area", None))
        self.dropdown1.setItemText(18, QCoreApplication.translate("UserInterface", u"Arc length of lamination ID", None))
        self.dropdown1.setItemText(19, QCoreApplication.translate("UserInterface", u"Arc length of one tooth pitch", None))
        self.dropdown1.setItemText(20, QCoreApplication.translate("UserInterface", u"Approx width of slot opening", None))
        self.dropdown1.setItemText(21, QCoreApplication.translate("UserInterface", u"# of turns", None))
        self.dropdown1.setItemText(22, QCoreApplication.translate("UserInterface", u"Actual flux density", None))
        self.dropdown1.setItemText(23, QCoreApplication.translate("UserInterface", u"Actual coil flux", None))
        self.dropdown1.setItemText(24, QCoreApplication.translate("UserInterface", u"Rated Torque per phase", None))
        self.dropdown1.setItemText(25, QCoreApplication.translate("UserInterface", u"Torque constant", None))
        self.dropdown1.setItemText(26, QCoreApplication.translate("UserInterface", u"BackEMF constant", None))
        self.dropdown1.setItemText(27, QCoreApplication.translate("UserInterface", u"Phase inductance", None))
        self.dropdown1.setItemText(28, QCoreApplication.translate("UserInterface", u"Phase resistance", None))
        self.dropdown1.setItemText(29, QCoreApplication.translate("UserInterface", u"Inertia", None))
        self.dropdown1.setItemText(30, QCoreApplication.translate("UserInterface", u"torque/inertia", None))
        self.dropdown1.setItemText(31, QCoreApplication.translate("UserInterface", u"Motor volume", None))
        self.dropdown1.setItemText(32, QCoreApplication.translate("UserInterface", u"Stator surface area", None))
        self.dropdown1.setItemText(33, QCoreApplication.translate("UserInterface", u"Fe weight", None))
        self.dropdown1.setItemText(34, QCoreApplication.translate("UserInterface", u"Cu weight", None))
        self.dropdown1.setItemText(35, QCoreApplication.translate("UserInterface", u"Rotor weight", None))
        self.dropdown1.setItemText(36, QCoreApplication.translate("UserInterface", u"Current density", None))
        self.dropdown1.setItemText(37, QCoreApplication.translate("UserInterface", u"Mean resistive losses", None))
        self.dropdown1.setItemText(38, QCoreApplication.translate("UserInterface", u"Mean back iron losses", None))
        self.dropdown1.setItemText(39, QCoreApplication.translate("UserInterface", u"Mean fluid losses", None))

        self.MagVol_m3.setText(QCoreApplication.translate("UserInterface", u"Magnet Volume", None))
        self.Weight_kg.setText(QCoreApplication.translate("UserInterface", u"Motor Weight", None))
        self.MinEffMtr_Percent.setText(QCoreApplication.translate("UserInterface", u"Minimum Efficiency", None))
        self.VDC_2.setText(QCoreApplication.translate("UserInterface", u"Phase Voltage", None))
        self.dropdown2.setItemText(0, QCoreApplication.translate("UserInterface", u"# of pole pairs", None))
        self.dropdown2.setItemText(1, QCoreApplication.translate("UserInterface", u"Radial length of magnet", None))
        self.dropdown2.setItemText(2, QCoreApplication.translate("UserInterface", u"Wire copper radius", None))
        self.dropdown2.setItemText(3, QCoreApplication.translate("UserInterface", u"Fill factor", None))
        self.dropdown2.setItemText(4, QCoreApplication.translate("UserInterface", u"Lamination tooth tip and wedge thickness", None))
        self.dropdown2.setItemText(5, QCoreApplication.translate("UserInterface", u"Lamination slot liner thickness", None))
        self.dropdown2.setItemText(6, QCoreApplication.translate("UserInterface", u"Gear ratio", None))
        self.dropdown2.setItemText(7, QCoreApplication.translate("UserInterface", u"Magnet backiron inner radius", None))
        self.dropdown2.setItemText(8, QCoreApplication.translate("UserInterface", u"Magnet backiron outer radius", None))
        self.dropdown2.setItemText(9, QCoreApplication.translate("UserInterface", u"Tooth width", None))
        self.dropdown2.setItemText(10, QCoreApplication.translate("UserInterface", u"Lamination tooth tip radius", None))
        self.dropdown2.setItemText(11, QCoreApplication.translate("UserInterface", u"Lamination slot radius", None))
        self.dropdown2.setItemText(12, QCoreApplication.translate("UserInterface", u"Magnet inner radius", None))
        self.dropdown2.setItemText(13, QCoreApplication.translate("UserInterface", u"Backiron thickness, lamination", None))
        self.dropdown2.setItemText(14, QCoreApplication.translate("UserInterface", u"Backiron thickness, magnet assembly", None))
        self.dropdown2.setItemText(15, QCoreApplication.translate("UserInterface", u"Lamination slot outer", None))
        self.dropdown2.setItemText(16, QCoreApplication.translate("UserInterface", u"Lamination slot area", None))
        self.dropdown2.setItemText(17, QCoreApplication.translate("UserInterface", u"Winding Slot area", None))
        self.dropdown2.setItemText(18, QCoreApplication.translate("UserInterface", u"Arc length of lamination ID", None))
        self.dropdown2.setItemText(19, QCoreApplication.translate("UserInterface", u"Arc length of one tooth pitch", None))
        self.dropdown2.setItemText(20, QCoreApplication.translate("UserInterface", u"Approx width of slot opening", None))
        self.dropdown2.setItemText(21, QCoreApplication.translate("UserInterface", u"# of turns", None))
        self.dropdown2.setItemText(22, QCoreApplication.translate("UserInterface", u"Actual flux density", None))
        self.dropdown2.setItemText(23, QCoreApplication.translate("UserInterface", u"Actual coil flux", None))
        self.dropdown2.setItemText(24, QCoreApplication.translate("UserInterface", u"Rated Torque per phase", None))
        self.dropdown2.setItemText(25, QCoreApplication.translate("UserInterface", u"Torque constant", None))
        self.dropdown2.setItemText(26, QCoreApplication.translate("UserInterface", u"BackEMF constant", None))
        self.dropdown2.setItemText(27, QCoreApplication.translate("UserInterface", u"Phase inductance", None))
        self.dropdown2.setItemText(28, QCoreApplication.translate("UserInterface", u"Phase resistance", None))
        self.dropdown2.setItemText(29, QCoreApplication.translate("UserInterface", u"Inertia", None))
        self.dropdown2.setItemText(30, QCoreApplication.translate("UserInterface", u"torque/inertia", None))
        self.dropdown2.setItemText(31, QCoreApplication.translate("UserInterface", u"Motor volume", None))
        self.dropdown2.setItemText(32, QCoreApplication.translate("UserInterface", u"Stator surface area", None))
        self.dropdown2.setItemText(33, QCoreApplication.translate("UserInterface", u"Fe weight", None))
        self.dropdown2.setItemText(34, QCoreApplication.translate("UserInterface", u"Cu weight", None))
        self.dropdown2.setItemText(35, QCoreApplication.translate("UserInterface", u"Rotor weight", None))
        self.dropdown2.setItemText(36, QCoreApplication.translate("UserInterface", u"Current density", None))
        self.dropdown2.setItemText(37, QCoreApplication.translate("UserInterface", u"Mean resistive losses", None))
        self.dropdown2.setItemText(38, QCoreApplication.translate("UserInterface", u"Mean back iron losses", None))
        self.dropdown2.setItemText(39, QCoreApplication.translate("UserInterface", u"Mean fluid losses", None))

        self.ThreeDPlot.setText(QCoreApplication.translate("UserInterface", u"3D Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("UserInterface", u"Results", None))
        self.label_17.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("UserInterface", u"File", None))
        self.menuScale.setTitle(QCoreApplication.translate("UserInterface", u"Scale", None))
    # retranslateUi

