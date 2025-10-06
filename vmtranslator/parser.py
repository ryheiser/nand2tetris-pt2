def find_command_type(command):
    parts = command.split()
    op = parts[0]
    arithmetic_commands = {'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'}
    
    if op in arithmetic_commands:
        return 'C_ARITHMETIC'
    elif op == 'push':
        return 'C_PUSH'
    elif op == 'pop':
        return 'C_POP'
    else:
        return 'C_UNKNOWN'