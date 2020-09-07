import sys
from PyQt4 import QtGui, QtCore
import time
from threading import Thread
import random
from datetime import datetime
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
        x, y = -99999,-99999 # hard core tricks? also vanish from the command palette!
#        x, y = 0, 0
        qbtn = QtGui.QPushButton('Quit', self)
        #qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.test)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        #qbtn.installEventFilter(self)

        self.setGeometry(x+0, y+0, 1024, 768)
        self.setWindowTitle('Quit button')    
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.installEventFilter(self)
        self.show()
#        self.setVisible(False)
#        self.hide()
#        self.setShown(False)
#        painter = QtGui.QStylePainter()
#        painter.begin(self)
#        self.hide()
#        qbtn.show()

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

def shoot(widget):
    date = datetime.now()
    filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
# this is just wrong.
#    p = QtGui.QPixmap.grabWindow(application.winid(),*widget.geometry().getRect())
#    win_id = widget.windowHandle()
#    print win_id, "window handle"
#    print dir(widget.window())
    p = QtGui.QPixmap.grabWindow(widget.winId())
    p.save(filename, 'jpg')
#    label.setPixmap(p)        # just for fun :)
    print "shot taken",filename

#import win32gui

def shoot_thread(widget):
    time.sleep(2)
    print "shoot thread initialized!"
#    hwnd = int(widget.winId())
#    win32gui.ShowWindow(hwnd, False)
    while True:
        shoot(widget)
        time.sleep(2)

# when hidden, you cannot get the shot. what the fuck?
def some_args(window,mainWindow):
    time.sleep(2)
#    pid = window.applicationPid()
    rng = random.SystemRandom()
#    window.hide()
#    mainWindow.hide()
# yes you can hide this.
    def width(): return rng.choice(range(1024))
    def height(): return rng.choice(range(768))
    print "thread_waiting_finished!"
    while True:
        # exception found.
#        print "THIS IS THE PID OF THE MAIN APP",pid
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
#    ex.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint)
#    ex.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnBottomHint)
#    app.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#    ex.hide()
# to prove we need to take screenshots.
    app.installEventFilter(ex)
    ex.setMouseTracking(True)
    thread = Thread(target=some_args,args=(app,ex))
# this thread will be shutting down the window.
    thread.daemon = True
    thread.start()
    thread0 = Thread(target=shoot_thread,args=(ex,))
    thread0.daemon = True
    thread0.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
