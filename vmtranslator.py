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



def main():
    print("VM Translator started")
    # Further implementation will go here
    text = read_vm_file("/home/ryheiser/Documents/Development/nand2tetris-pt2/07/BasicTest/BasicTest.vm")

    #Print initial text
    print("Initial text:")
    for line in text:
        print(line.strip())

    text = compact_text(text)
    print("\nCompacted text:")
    for line in text:
        print(line)

if __name__ == "__main__":
    main()