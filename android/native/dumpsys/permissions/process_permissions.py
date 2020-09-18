magic="android.permission"
import copy
def process_me(a):
    for x in range(len(a)):
        a[x] = "        <permission name=\"{}\"/>".format(a[x])

def read_me(a):
    with open(a,"r") as f:
        return f.read().split("\n")

def filter_me(a):
    a=list(filter(lambda x:len(x)>len("permission:"),a))
    for x in range(len(a)):
        a[x] = a[x][len("permission:"):]
    a=list(filter(lambda x:len(x)>len(magic),a))
    a=list(filter(lambda x:x[0:len(magic)]==magic,a))
    return copy.deepcopy(a)

r=read_me("permissions.xml")
r=filter_me(r)
process_me(r)
j="\n".join(r)
print(j)