import sys, os, console
from time import sleep
screenbuffer = ""
commandline = console.Console()
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

def build_screen():
    global MEM
    overview = ""
    for i in range(len(MEM)):
        if MEM[i] > 0:
            overview += "%d" % i + ": [%d" % MEM[i]
            if MEM[i] > 32 and MEM[i] < 126:
                overview += " -> " + chr(MEM[i])
            overview += "]\n"
    commandline.prompt = ""
    commandline.prompt += "Used memory:\n"
    commandline.prompt += overview + "\n"
    commandline.prompt += screenbuffer + "\n"
    commandline.prompt += "\n=>> "
    os.system("clear")
loop = False
whilebuff = ""
def default(line = ""):
    global loop
    global whilebuff
    j = line
    if "load" in j:
        load_program(j[5:])
        return
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

    build_screen()
commandline.default = default
commandline.emptyline = default
commandline.intro = "Welcome to Dafuk (Brainfuck interpeter)"
commandline.cmdloop()
