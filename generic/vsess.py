import virtualbox
import time
import signal, sys
#from gevent import monkey
#monkey.patch_all()
# consider taking that too.
# the pipe must be initialized. use another thread to initialize the pipe.
import threading
import subprocess
# or you can be careless anyway.
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
machine=vbox.find_machine("TinyPlus")
def sigint_handler(signal,frame):
    print("interrupted!")
    session.console.power_down()
    time.sleep(0.1)
    sys.exit(0)

def my_except_hook(exctype,value,traceback):
    session.console.power_down()
    time.sleep(0.1)
    sys.__excepthook__(exctype,value,traceback)
    sys.exit(0)
    # is it lethal?
sys.excepthook = my_except_hook
signal.signal(signal.SIGINT,sigint_handler)
#signal.signal(signal.SIGKILL,sigint_handler)
#virtualbox.library_ext.machine.IMachine
#print(dir(machine),type(machine))
# you can close this window anyway, or minimize it using another thread?
progress=machine.launch_vm_process(session,"headless","")
progress.wait_for_completion()
# how to pass it around?
# must be keys. but what is keys?
time.sleep(5)
# not receiving shit.
# connect to existing session if possible? or close that thing.
def init():
    time.sleep(0.2)
    subprocess.run(["./init.sh"])

"""def shot(sess):
    s=sess.console.display"""

t=threading.Thread(target=init)
t.setDaemon(True)
t.start()
guest_session = session.console.guest.create_session("tc","root")
with open("lazero","r") as f:
    while True:
        r=f.readline()
        # another process!
        def checker(r):
            try:
                proc, stdout, stderr = guest_session.execute("/bin/bash", r.split())
        # be properly decoded.
                print(stdout)
            except:
                print("minor error")
                pass
        t0 = threading.Thread(target=checker,args=(r,))
        t0.setDaemon(True)
        t0.start()
        time.sleep(0.1)
        print(">>> visible delay?",time.time())
#session.console.keyboard.put_keys("Hello, world!")
# maybe a dedicated image for dos and more.
# first we have to check how to read chars from the canvas or something.
# remember that is way too slow to parse info from console. i mean THAT.
