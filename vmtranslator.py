#This is the main entry point for the VM translator program.

def read_vm_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()



def main():
    print("VM Translator started")
    # Further implementation will go here
    text = read_vm_file("/home/ryheiser/Documents/Development/nand2tetris-pt2/07/BasicTest/BasicTest.vm")
    print(text)

if __name__ == "__main__":
    main()