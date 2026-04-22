Anaconda Programming Language Documentation

Version: 1.0.R (Release)
Type: Line-based Imperative Scripting Language
Integrations: Lua, System Shell
1. Introduction

Anaconda is a lightweight, line-oriented programming language designed for simplicity and open-source transparency. It features a unique "slot-based" memory system and a native bridge to the Lua runtime.
2. Syntax Basics

    File Extension: Typically uses .txt (the standard input file is int.txt).

    Execution: The interpreter reads the file line-by-line. Every command and every argument must reside on its own individual line.

    Comments: Lines starting with -- or ## are ignored by the interpreter.

3. Memory Management (Slots)

Anaconda does not use named variables. Instead, it uses a fixed array of 1000 Data Slots (indexed 1–1000).

    Direct Reference: Use !slot followed by the index on the next line for commands that support it.

    String Interpolation: Use {index} inside a string to inject the value of a slot.

        Example: print Hello {1} will print "Hello" followed by the contents of Slot 1.

4. Core Command Reference
save

Stores data into a memory slot.

    Syntax (Manual):
    save
    [slot_index]
    !basic
    [value]

    Syntax (User Input):
    save
    [slot_index]
    !input
    [Prompt Message]

print

Displays text to the console.

    Syntax:
    print
    [Text or {slot}]

    Syntax (Raw Slot):
    print
    !slot
    [slot_index]

wait

Pauses the program for a specific duration.

    Syntax:
    wait
    [seconds]

clear

Clears the terminal screen. Works on both Windows (NT) and Linux/Unix systems.
r_key

Waits for a single keyboard keypress and saves the character to a slot.

    Syntax:
    r_key
    [slot_index]

return

Exits the program immediately.
customfetch

Displays the Anaconda branding, version information, and ASCII art.
5. Control Flow & Navigation
point

Records the current line number and saves it into a slot for later navigation.

    Syntax:
    point
    [slot_index]

move

Jumps the execution to a specific line number in the script.

    Syntax:
    move
    [line_number]

6. System & Lua Integration
exec_system

Executes a command in the host operating system shell.

    Syntax:
    exec_system
    [command or {slot}]

exec_lua

Runs a block of Lua code. This allows you to use complex logic within Anaconda.

    Syntax:
    exec_lua
    [Lua Code Line 1]
    [Lua Code Line 2]
    ...
    !end_mline

    Bridge Functions: Inside an exec_lua block, you can call these special functions:

        set(value, slot): Updates an Anaconda memory slot.

        wait(num): Accesses the Anaconda wait timer.

        clear(): Accesses the Anaconda screen clear.

        customfetch(): Runs the Anaconda branding display.

7. Error Handling

If a command is misspelled or the syntax is incorrect, Anaconda will display an error message including the line number and the faulty function name, then halt execution in a loop to prevent data corruption.
8. Example Script

The following script asks for a name, saves it, and uses Lua to set a value in another slot.

customfetch
print
What is your name?
save
1
!input
Name:
print
Hello {1}!
exec_lua
set("Lua was here", 2)
!end_mline
print
Slot 2 contains: {2}
wait
5
return
