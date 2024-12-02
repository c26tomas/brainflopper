import sys

# Initialize memory and pointer
brainArray = [0] * 1024
brainPtr = 0

def interpret(filename):
    global brainArray, brainPtr

    # Load the code from the file
    with open(filename, "r") as file:
        code = file.read()

    # Ensure we interpret command-by-command
    code = ''.join(code.split())  # Remove any whitespace
    
    # Execution pointer for the program
    codePtr = 0

    while codePtr < len(code):
        command = code[codePtr]

        if command == '+':
            brainArray[brainPtr] = (brainArray[brainPtr] + 1)
        
        elif command == '-':
            brainArray[brainPtr] = (brainArray[brainPtr] - 1)
        
        elif command == '<':
            brainPtr = (brainPtr - 1)
        
        elif command == '>':
            brainPtr = (brainPtr + 1)
        
        elif command == '*':
            if brainArray[brainPtr] == 0:
                # Input if current cell is 0
                brainArray[brainPtr] = ord(input("Input a character: ")[0])
            else:
                # Print the ASCII character of the current cell value
                print(chr(brainArray[brainPtr]), end='')
        
        elif command == '/':
            if brainArray[brainPtr] == 0:
                codePtr += 1  # Skip the next command
            else:
                # Jump by the value of the cell to the right of the current pointer
                jump = brainArray[(brainPtr + 1)]
                codePtr += jump
        
        elif command == '#':
            brainArray[brainPtr] = 0  # Reset the current cell to 0

        # Move to the next command
        codePtr += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 brainflopper.py <filename>")
        sys.exit(1)
    
    interpret(sys.argv[1])