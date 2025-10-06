from vmtranslator import parser

#This is the main entry point for the VM translator program.




def main():
    print("VM Translator started")
    # Further implementation will go here
    p = parser.Parser("07\BasicTest\BasicTest.vm")

    while p.has_more_commands():
        p.advance()
        cmd_type = p.commandType()
        print(f"Type: {cmd_type} '{p.current_command}'")

if __name__ == "__main__":
    main()