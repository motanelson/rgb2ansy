print("\033c\033[40;37m\nansy:",end="")
def defs(n):
    nn=(n) & 15
    nn=bin(nn)
    nn="0000"+nn[2:]
    nn=nn[-4:]
    n=""+nn[0]+nn[3]+nn[2]+nn[1]
    i=int(n,2)
    return i
def binss(n):
    nn=(n) & 15
    nn=bin(nn)
    nn="0000"+nn[2:]
    nn=nn[-4:]
    n=nn
    i=int(n,2)
    return i

def putc(c):
    if c!="":
        print(c[0],end="")
def colors(colors:int):
    i=str(colors+40)
    s="\033[$0m".replace("$0",i)
    print(s,end="")
for a in range(8):
    colors(binss(a))
    putc(" ")
colors(0)
print("\nrgb :",end="")
for a in range(8):
    colors(defs(a))
    putc(" ")
colors(0)
print("")
