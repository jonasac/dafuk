import sys, os
from time import sleep
screenbuffer = ""
pointer = 0
def inc_ptr():
    global pointer
    pointer += 1
def inc_deref_ptr():
    global pointer
    MEM[pointer] += 1
def dec_ptr():
    global pointer
    pointer -= 1
def dec_deref_ptr():
    global pointer
    MEM[pointer] -= 1
def wr():
    global pointer, screenbuffer
    screenbuffer += chr(MEM[pointer])
def rd():
    global pointer
    MEM[pointer] = ord(sys.stdin.read(1))

def runthis(this):
    for count in range(MEM[pointer]):
        for thing in this:
            try:
                INTERP.get(thing)()
            except:
                pass
def load_program(filename):
    whilebuff = ""
    loop = False
    try:
        with open(filename) as f:
            for j in f:
                for i in j:
                    if i is '[' or loop:
                        loop = True
                        if i == ']':
                            runthis(whilebuff[1:])
                            loop = False
                        whilebuff += i
                    else:

                        try:
                            INTERP.get(i)()
                        except:
                            pass
    except:
        print "File not found"
        sleep(0.5)

INTERP = {'+': inc_deref_ptr, '>': inc_ptr,'<': dec_ptr, '-':
        dec_deref_ptr, '.': wr, ',': rd}

MEM = [0 for i in range(30000)]

loop = False
whilebuff = ""
while 1:
    os.system("clear")
    print screenbuffer
    print ">>> ",
    j = raw_input()
    if "load" in j:
        load_program(j[5:])
        continue
    for i in j:
        if i is '[' or loop:
            loop = True
            if i == ']':
                runthis(whilebuff[1:])
                loop = False
            whilebuff += i
        else:
            try:
                INTERP.get(i)()
            except:
                pass
