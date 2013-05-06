import sys, os, console
from time import sleep
screenbuffer = ""
commandline = console.Console()
pointer = 0
REPR = {
"000": ["NUL", "(Null char.)"], 
"001": ["SOH", "(Start of Header)"], 
"002": ["STX", "(Start of Text)"], 
"003": ["ETX", "(End of Text)"], 
"004": ["EOT", "(End of Transmission)"], 
"005": ["ENQ", "(Enquiry)"], 
"006": ["ACK", "(Acknowledgment)"], 
"007": ["BEL", "(Bell)"], 
"008": ["BS", "(Backspace)"], 
"009": ["HT", "(Horizontal Tab)"], 
"010": ["LF", "(Line Feed)"], 
"011": ["VT", "(Vertical Tab)"], 
"012": ["FF", "(Form Feed)"], 
"013": ["CR", "(Carriage Return)"], 
"014": ["SO", "(Shift Out)"], 
"015": ["SI", "(Shift In)"], 
"016": ["DLE", "(Data Link Escape)"], 
"017": ["DC1", "(XON)(Device Control 1)"], 
"018": ["DC2", "(Device Control 2)"], 
"019": ["DC3", "(XOFF)(Device Control 3)"], 
"020": ["DC4", "(Device Control 4)"], 
"021": ["NAK", "(Negative Acknowledgement)"], 
"022": ["SYN", "(Synchronous Idle)"], 
"023": ["ETB", "(End of Trans. Block)"], 
"024": ["CAN", "(Cancel)"], 
"025": ["EM", "(End of Medium)"], 
"026": ["SUB", "(Substitute)"], 
"027": ["ESC", "(Escape)"], 
"028": ["FS", "(File Separator)"], 
"029": ["GS", "(Group Separator)"], 
"030": ["RS", "(Request to Send)(Record Separator)"], 
"031": ["US", "(Unit Separator)"], 
"032": ["SP", "(Space)"], 
"127": ["DEL", "(delete)"]
}
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
            else:
                rep = REPR["%03d" % MEM[i]]
                overview += " -> " + rep[0] + " " + rep[1]
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
