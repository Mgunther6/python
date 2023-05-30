#serveur UDP (CTRL+F2 pour stopper)
import socket

UDP_IP_MON_PC = "172.18.49.130"   #adresse de mon serveur
UDP_PORT_MON_PC = 5000        #port de mon serveur

# Crée un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_MON_PC, UDP_PORT_MON_PC))

boucle=True
while(boucle):
        try:
            octets, server = sock.recvfrom(1024)
        except socket.error as msg:
            data=None
            continue
        print ('received ', data)
        if (data.decode()=='q'):
            boucle=False
print('closing socket')
sock.close()


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import socket

UDP_IP_DU_BINOME = "172.18.49.130"   #adresse du client (la machine du binôme) à adapter
UDP_PORT_DU_BINOME = 5000        #port du client (la machine du binôme) à adapter

UDP_IP_MON_PC = "172.18.49.130"   #adresse de mon serveur
UDP_PORT_MON_PC = 5000        #port de mon serveur

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_MON_PC, UDP_PORT_MON_PC))

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi(chat.ui, self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.show()                     #affiche la fenêtre MainWindows

        self.pushButton_envoyer.clicked.connect(self.boutonEnvoi)
        self.timer = QTimer(self)   #déclaration du timer
        self.timer.timeout.connect(self.miseAJour) #déclenche la méthode mise à jour
        self.timer.start(100)      #toutes les secondes (100ms)

    def miseAJour(self):
        # A compléter
        # Reçoit (sock.recvfrom) et décode le message en str
        # Ajoute le message dans la listWidget -> méthode insertItem
        # self.listWidget.insertItem(0, message)
        # self.listWidget.item(0).setForeground(QtCore.Qt.blue)
        try:
            octets, server = sock.recvfrom(1024)
        except socket.error as msg:
            octet=None
        if octet!=None:
            message=octet,decode()
            print('reception:',message)
            self.listWidget.insertItem(0, message)
            self.listWidget.item(0).setForeground(QtCore.Qt.blue)

    def boutonEnvoi(self):
        # A compléter
        # Encode le message en bytes et envoie le message (sock.sendto…au binôme)
        msg=self.lineEdit_msg.text()
        print('texte envoyé', msg)
        message = 'I HATE NSI ctrl'
        octets = msg.encode("Utf8")
        sock.sendto(octets, (UDP_IP_DU_BINOME, UDP_PORT_DU_BINOME))

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()