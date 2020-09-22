import threading
import time

def listen(a):
    with open(a,'r') as f:
        while True:
            r=f.readline()
            print(a,r)
            time.sleep(0.1)

t=threading.Thread(target=listen,args=('stdout',))
t1=threading.Thread(target=listen,args=('stderr',))
t.setDaemon(True)
t1.setDaemon(True)

t.start()
t1.start()

# self-init.
while True:
    print('idle main thread')
    time.sleep(1)
