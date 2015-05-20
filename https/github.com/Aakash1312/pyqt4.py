#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

# Create an PyQT4 application object.
'''
class sub(QtGui.QWidget):
    def mousePressEvent(self,event):
        print "yes"
        QtGui.QWidget.mousePressEvent(self, event)
        
    def __init__(self):
        super(sub,self).__init__()          
        self.label=QLabel()
    def Label(self):
        return self.label
'''
a = QApplication(sys.argv) 
icon=QIcon()
w2=QGridLayout()

container=QWidget()
w=QGridLayout()

scroll=QScrollArea()


def update(position):
    label=Newlabel()
    label.setPixmap(icon.pixmap(128,QIcon.Selected,QIcon.On))
    QtCore.QObject.connect(label, QtCore.SIGNAL('clicked()'), label.lp)
    w.addWidget(label,*position)


class Newlabel(QLabel):
    position=[]
    layout=QGridLayout()
    def lp(self):
        update(self.position)
    def mousePressEvent(self,event):
        self.emit(QtCore.SIGNAL('clicked()'))
        #QtGui.QWidget.mousePressEvent(self, event)
class Main(QtGui.QMainWindow):
    

    def __init__(self, parent = None):
            super(Main, self).__init__(parent)
            self.centralWidget=QWidget()
            self.setCentralWidget(self.centralWidget)
            
            size=128
            
            mode=QIcon.Normal
            state=QIcon.Off
            pixma = QPixmap('folder.png') 
            icon.addPixmap(pixma,mode,state)
            
            
            positions = [(i,j) for i in range(5) for j in range(4)]
            button=QtCore.Qt.LeftButton
            event=QtCore.QEvent.MouseButtonPress
            #pos1=QMouseEvent.pos()
            #m=QMouseEvent()
            
            for position in positions:
                h=QVBoxLayout()
                label=Newlabel()
                txtlabel=QLabel()
                txtlabel.setText("Documents")
                h.addWidget(txtlabel)
                label.position=position
                label.setPixmap(icon.pixmap(size,QIcon.Normal,state))
                QtCore.QObject.connect(label, QtCore.SIGNAL('clicked()'), label.lp)
                w.addWidget(label,*position)
                h.addStretch(1)
                w.addItem(h,*position)
            container.setLayout(w)
            scroll.setWidget(container)
            w2.addWidget(scroll)    
            self.centralWidget.setLayout(w2)
            self.centralWidget.setMinimumSize(300,300)
            

# Set window size. 
            
 
# Set window title  
            
 
# Add a button
'''
            
            

            w.addWidget(s,0,0,0)

btn.setToolTip('Click to quit!')
btn.clicked.connect(exit)
btn.resize(btn.sizeHint())
      
 '''
# Show window
if __name__ == "__main__":
    
    q=Main() 
    q.show() 
    sys.exit(a.exec_())
