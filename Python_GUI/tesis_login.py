from PyQt5 import QtCore, QtGui, QtWidgets
import sys, resources
from PyQt5.QtCore import pyqtSignal
from tesis_conexionSQL import ConectaDB
import bcrypt 
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame, QVBoxLayout, QMessageBox, QTableWidgetItem, QFileDialog



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 492)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 261, 461))
        self.widget.setStyleSheet("border-image: url(:/newPrefix/background.png);\n"
"border-top-left-radius: 50px;\n"
"")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(20, 20, 261, 461))
        self.widget_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius: 50px;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(284, 20, 281, 461))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 70, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(320, 140, 211, 41))
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 210, 211, 41))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 280, 190, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255); }\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(20, 90, 261, 111))
        self.widget_3.setStyleSheet("background-color:rgba(0,0,0,75);")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 145, 220, 50))
        self.label_4.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_4.setObjectName("label_4")
        
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Iniciar sesión"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Usuario"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Contraseña"))
        self.pushButton.setText(_translate("Form", "Iniciar sesión"))
        self.label_3.setText(_translate("Form", "BiomedCODE"))
        self.label_4.setText(_translate("Form", "Bienvenido(a) al programa realizado \n"
" por Emily Ventura"))

# Agregar un botón de salida
        self.exitButton = QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(Form.width() - 80, 10, 70, 25))  # Ajusta según necesites
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("X")
        self.exitButton.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)


class LoginWindow(QtWidgets.QWidget):
    sesion_exitosa = pyqtSignal(str)  # Emite el nombre del usuario

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = ConectaDB()
        self.esta_iniciada_sesion = False

        # Conectar los botones y eventos
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.lineEdit_2.returnPressed.connect(self.login)

        self.ui.exitButton.clicked.connect(self.close)

    def login(self):
        if self.esta_iniciada_sesion:
            return
        self.esta_iniciada_sesion = True

        usuario = self.ui.lineEdit.text()
        contraseña = self.ui.lineEdit_2.text()

        if not usuario or not contraseña:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña.")
            self.esta_iniciada_sesion = False
            return

        if self.validar_credenciales1(usuario, contraseña):
            # Emitir señal con el nombre del usuario autenticado
            self.sesion_exitosa.emit(usuario)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Credenciales inválidas")
            self.esta_iniciada_sesion = False

    def validar_credenciales1(self, usuario, contraseña):
        try:
            self.db.conecta_base_datos()
            query = "SELECT contrasena FROM administradores WHERE usuario = %s"
            self.db.cursor.execute(query, (usuario,))
            result = self.db.cursor.fetchone()

            if result is None:
                return False  # Usuario no encontrado

            hash_almacenado = result['contrasena']
            if bcrypt.checkpw(contraseña.encode('utf-8'), hash_almacenado.encode('utf-8')):
                return True  # Credenciales válidas
            else:
                return False  # Contraseña incorrecta

        except Exception as e:
            print(f"Error de autenticación: {e}")
            return False

        finally:
            self.db.cursor.close()
            self.db.con.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec_()