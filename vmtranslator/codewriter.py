class CodeWriter:
    def __init__(self, output_file):
        self.output_file = output_file
        self.file = open(output_file, 'w')
        self.label_counter = 0  # For generating unique labels

    def write_arithmetic(self, command):
        if command == 'add':
            #Pop y into D
            asm = "@SP\nAM=M-1\nD=M\n"
            #Pop x into M
            asm = asm + "@SP\nA=M-1\nM=D+M"
            print(asm)