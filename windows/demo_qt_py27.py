import sys
from PyQt4 import QtGui, QtCore
import time
from threading import Thread
import random
'''
def rejectExternal(event):
    if event.spontaneous():
        event.ignore()
        # not rejecting. wtf?
        print("spontaneous event ignored!")
    else:
        event.accept()
        print("internal event accepted!")
'''
class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):               

        qbtn = QtGui.QPushButton('Quit', self)
        #qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.test)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        qbtn.show()
        #qbtn.installEventFilter(self)

        self.setGeometry(0, 0, 1024, 768)
        self.setWindowTitle('Quit button')    
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.installEventFilter(self)
        self.show()

    def eventFilter(self,object,event):
	if event.type() in [QtCore.QEvent.MouseButtonPress,QtCore.QEvent.MouseButtonRelease,QtCore.QEvent.MouseButtonDblClick,QtCore.QEvent.MouseMove,QtCore.QEvent.KeyRelease,QtCore.QEvent.KeyPress,QtCore.QEvent.ShortcutOverride]:
	    return event.spontaneous()
        else:
            return False

    def test(self):
        print "show the position of mouse cursor in screen resolution: x is ?? , y is ??"

    def mousePressEvent(self, QMouseEvent):
        print 'press: (', QMouseEvent.x(), ', ', QMouseEvent.y(), ')',time.time()
        if not QMouseEvent.spontaneous():
            print("internal event accepted!")
            super(Example,self).mousePressEvent(QMouseEvent)
        else:
            print("spontaneous event ignored!")
            pass

    def mouseReleaseEvent(self, QMouseEvent):
        print 'release: (', QMouseEvent.x(), ', ', QMouseEvent.y(), ')',time.time()
        if not QMouseEvent.spontaneous():
            print("internal event accepted!")
            super(Example,self).mouseReleaseEvent(QMouseEvent)
        else:
            print("spontaneous event ignored!")
            pass

    def mouseMoveEvent(self, QMouseEvent):
        print 'moving!: ','(', QMouseEvent.x(), ', ', QMouseEvent.y(), ')',time.time()
        print 'isSpontaneous: ',QMouseEvent.spontaneous()
        if not QMouseEvent.spontaneous():
            print("internal event accepted!")
            super(Example,self).mouseMoveEvent(QMouseEvent)
        else:
            print("spontaneous event ignored!")
            pass
# this one is totally black, and cannot be used for fun.
# we shall consider some hide?
def some_args(window,mainWindow):
    time.sleep(2)
    rng = random.SystemRandom()
    def width(): return rng.choice(range(1024))
    def height(): return rng.choice(range(768))
    print "thread_waiting_finished!"
    while True:
        # exception found.
        info = (width(),height())
        point = QtCore.QPoint(*info)
        print "Random moving destination",point
        event = QtGui.QMouseEvent(QtCore.QEvent.MouseMove,point,QtCore.Qt.NoButton,QtCore.Qt.MouseButtons(),QtCore.Qt.KeyboardModifiers())
        window.sendEvent(mainWindow,event)
        time.sleep(0.3)


def main():
    # do threading here. wait till ready?
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.installEventFilter(ex)
    ex.setMouseTracking(True)
    thread = Thread(target=some_args,args=(app,ex))
    thread.daemon = True
    thread.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
