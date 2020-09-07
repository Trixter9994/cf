import subprocess
import win32gui
import time

proc = subprocess.Popen(["notepad.exe"])
# lets wait a bit to app to start
time.sleep(3)

def enumWindowFunc(hwnd, windowList):
    """ win32gui.EnumWindows() callback """
    text = win32gui.GetWindowText(hwnd)
    className = win32gui.GetClassName(hwnd)
    #print hwnd, text, className
    if text.find("Notepad") >= 0:
        windowList.append((hwnd, text, className))

myWindows = []
# enumerate thru all top windows and get windows which are ours
win32gui.EnumWindows(enumWindowFunc, myWindows)

# now hide my windows, we can actually check process info from GetWindowThreadProcessId
# http://msdn.microsoft.com/en-us/library/ms633522(VS.85).aspx
for hwnd, text, className in myWindows:
    print hwnd,type(hwnd)
    win32gui.ShowWindow(hwnd, False)

# as our notepad is now hidden
# you will have to kill notepad in taskmanager to get past next line
proc.wait()
print "finished."