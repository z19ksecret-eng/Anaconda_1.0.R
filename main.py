import os
import time
import lupa
lua = lupa.LuaRuntime(unpack_returned_tuples=True)
int_a = open('int.txt',
             "r+")
str_rn = ""
last_str = ""
temp_str = int_a.read().strip()

start_1 = 1

temp_slot_data = None

t_data = [""] * 1000

rn_line = 0

def set(value,slot): t_data[slot] = value

def customfetch():
    print("                                !Anaconda  ")
    print(" &&      ##  ")
    print("   &&  ##    safe language for typing open source code/software")
    print("     #&      open source!")
    print("   ##  &&    u can without problems read any code typen on anaconda")
    print(" ##      &&  ")
    print("                                                                    v1.0.R") ## v(version).1.0.R(Release) or v(version).1.0.B(Beta)

def move(xD,xD2):
    xD2.seek(0)
    for i in range(xD-1):
        int_a.readline().strip()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def wait(num2):
    time.sleep(int(num2))

def r_key():
    str_rn = int_a.readline().strip()
    import sys
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getwch()
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
lua.globals().wait = wait
lua.globals().clear = clear
lua.globals().customfetch = customfetch
lua.globals().set = set

try:
    int_a.seek(0)
    while True:
        str_rn = int_a.readline().strip()
        if '--' in str_rn or '##' in str_rn:
            rn_line += 1
        else:
            if str_rn == 'print':
                str_rn = int_a.readline().strip()
                if str_rn == '!slot':
                    str_rn = int(int_a.readline().strip())
                    rn_line += 1
                    print(t_data[str_rn])
                else:
                    start_1 = 1
                    if "{" in str_rn and "}" in str_rn:
                        while start_1 < 1001:
                            if "{" + str(start_1) + "}" in str_rn:
                                str_rn = str_rn.replace("{" + f'{str(start_1)}' + "}", t_data[start_1])
                            start_1 = start_1 + 1
                        print(str_rn)
                    else:
                        print(str_rn)
            elif str_rn == 'clear':
                clear()
            elif str_rn == 'save':
                str_rn = int_a.readline().strip()
                rn_line += 1
                temp_slot_data = str_rn
                str_rn = int_a.readline().strip()
                rn_line += 1
                if str_rn == '!basic':
                    str_rn = int_a.readline().strip()
                    rn_line += 1
                    t_data[int(temp_slot_data)] = str_rn
                elif str_rn == "!input":
                    str_rn = int_a.readline().strip()
                    rn_line += 1
                    t_data[int(temp_slot_data)] = input(str_rn)
            elif str_rn == 'return':
                break
            elif str_rn == 'wait':
                str_rn = int_a.readline().strip()
                rn_line += 1
                time.sleep(int(str_rn))
            elif str_rn == 'exec_system':
                str_rn = int_a.readline().strip()
                rn_line += 1
                if str_rn == '!slot':
                    str_rn = int(int_a.readline().strip())
                    rn_line += 1
                    os.system(t_data[str_rn])
                else:
                    start_1 = 1
                    if "{" in str_rn and "}" in str_rn:
                        while start_1 < 1001:
                            if "{" + str(start_1) + "}" in str_rn:
                                str_rn = str_rn.replace("{" + f'{str(start_1)}' + "}", t_data[start_1])
                            start_1 = start_1 + 1
                        os.system(str_rn)
                    else:
                        os.system(str_rn)
            elif str_rn == 'exec_lua':
                lua_stuff = ""
                while True:
                    str_rn = int_a.readline().rstrip()
                    rn_line += 1
                    if str_rn == "!end_mline":
                        break
                    else:
                        if str_rn == '!slot':
                            str_rn = int(int_a.readline().strip())
                            rn_line += 1
                            lua.execute(t_data[str_rn])
                        else:
                            start_1 = 1
                            if "{" in str_rn and "}" in str_rn:
                                while start_1 < 1001:
                                    if "{" + str(start_1) + "}" in str_rn:
                                        str_rn = str_rn.replace("{" + f'{str(start_1)}' + "}", t_data[start_1])
                                    start_1 = start_1 + 1
                                lua_stuff = lua_stuff + f"\n{str_rn}"
                            else:
                                lua_stuff = lua_stuff + f"\n{str_rn}"
                lua.execute(lua_stuff)
            elif str_rn == 'customfetch':
                customfetch()
            elif str_rn == 'r_key':
                str_rn = int_a.readline().strip()
                rn_line += 1
                import sys
                if os.name == 'nt':
                    import msvcrt
                    t_data[int(str_rn)] = msvcrt.getwch()
                else:
                    import tty, termios
                    fd = sys.stdin.fileno()
                    old = termios.tcgetattr(fd)
                    try:
                        tty.setraw(fd)
                        t_data[int(str_rn)] = sys.stdin.read(1)
                    finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old)
            elif str_rn == "point":
                rn_line += 1
                str_rn = int_a.readline().strip()
                t_data[int(str_rn)] = rn_line+1
            elif str_rn == "move":
                str_rn = int(int_a.readline().strip())
                move(str_rn,int_a)
            elif str_rn == "":
                pass
            else:
                rn_line += 1
                print("         Anaconda got error in code!")
                print(f"     incorrect command at line {rn_line}")
                print("      incorrect function named "+str(str_rn))
                print("     if the script has no errors then it's\n     probably wrong version")
                while True:
                    pass
        last_str = str_rn
except Exception as e:
    print(e)
