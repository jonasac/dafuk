import sys, os
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
#    sys.stdout.write(chr(MEM[pointer]))
def rd():
    global pointer
    MEM[pointer] = ord(sys.stdin.read(1))
def junk():
    pass
def runthis(this):
    for count in range(MEM[pointer]):
        for thing in this:
            try:
                INTERP.get(thing)()
            except:
                pass
INTERP = {'+': inc_deref_ptr, '>': inc_ptr,'<': dec_ptr, '-':
        dec_deref_ptr, '.': wr, ',': rd, '\n': junk, ' ': junk}

MEM = [0 for i in range(30000)]

loop = False
whilebuff = ""
while 1:
    os.system("clear")
    print screenbuffer
    print ">>> ",
    j = raw_input()
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
