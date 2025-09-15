#This is the main entry point for the VM translator program.

def read_vm_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    
# This function compacts the text by removing comments and empty lines
def compact_text(text):
    compacted = []
    for line in text:
        line = line.split('//')[0].strip()  # Remove comments and whitespace
        if line:  # Only add non-empty lines
            compacted.append(line)
    return compacted

def find_command_type(command):
    arithmetic_commands = {'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'}
    if command in arithmetic_commands:
        return 'C_ARITHMETIC'
    elif command.startswith('push'):
        return 'C_PUSH'
    elif command.startswith('pop'):
        return 'C_POP'
    elif command.startswith('label'):
        return 'C_LABEL'
    elif command.startswith('goto'):
        return 'C_GOTO'
    elif command.startswith('if-goto'):
        return 'C_IF'
    elif command.startswith('function'):
        return 'C_FUNCTION'
    elif command.startswith('call'):
        return 'C_CALL'
    elif command.startswith('return'):
        return 'C_RETURN'
    else:
        return 'C_UNKNOWN'



def main():
    print("VM Translator started")
    # Further implementation will go here
    text = read_vm_file("/home/ryheiser/Documents/Development/nand2tetris-pt2/07/BasicTest/BasicTest.vm")

    commands = compact_text(text)
    for command in commands:
        type = find_command_type(command)
        print(f"Type: {type} '{command}")

if __name__ == "__main__":
    main()