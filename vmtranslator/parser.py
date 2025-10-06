class Parser:
    def __init__(self, input_file):

        with open(input_file, 'r') as file:
            self.lines = file.readlines()

        #Remove comments and whitespace
        self.commands = []
        for line in self.lines:
            line = line.split('//')[0].strip()  # Remove comments and whitespace
            if line:  # Only add non-empty lines
                self.commands.append(line)

        self.current_command = None
        self.current_index = -1

    def has_more_commands(self):
        return self.current_index + 1 < len(self.commands)
    
    def advance(self):
        # Move to the next command - make it the current one
        self.current_index += 1
        self.current_command = self.commands[self.current_index]

    def commandType(self):
        # Return the type of the current command
        parts = self.current_command.split()
        cmd = parts[0]
        arithmetic_commands = {
            'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'
        }

        if cmd in arithmetic_commands:
            return 'C_ARITHMETIC'
        elif cmd == 'push':
            return 'C_PUSH'
        elif cmd == 'pop':
            return 'C_POP'
        elif cmd == 'label':
            return 'C_LABEL'
        elif cmd == 'goto':
            return 'C_GOTO'
        elif cmd == 'if-goto':
            return 'C_IF'
        elif cmd == 'function':
            return 'C_FUNCTION'
        elif cmd == 'call':
            return 'C_CALL'
        elif cmd == 'return':
            return 'C_RETURN'
        else:
            return 'C_UNKNOWN'
        
    def arg1(self):
        # Return the first argument of the current command
        if self.commandType() == 'C_RETURN':
            raise ValueError("C_RETURN does not have arguments")
        parts = self.current_command.split()
        if self.commandType() == 'C_ARITHMETIC':
            return parts[0]  # The command itself is the argument
        else:
            return parts[1]  # The first argument
        
    def arg2(self):
        # Return the second argument of the current command
        if self.commandType() in {'C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'}:
            parts = self.current_command.split()
            return int(parts[2])  # The second argument is an integer
        else:
            raise ValueError(f"{self.commandType()} does not have a second argument")