from sys import argv

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        # Add your code here to process input commands.
        output = "" #process the input command and get the output
        # Once it is processed print the output using the command System.out.println()
        print(output)
    
if __name__ == "__main__":
    main()