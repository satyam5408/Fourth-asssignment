# FIRST TASK

try:
    with open("sample.txt", 'r') as file:
        print("Reading file content:")
        result1 = file.readline()
        print("line1:",result1)
        result2 = file.readline()
        print("line2:",result2)

except FileNotFoundError:
    print("Error: sample.txt doesn't exist")


#SECOND TASK

data = input("enter text to write in the file:")

def write():
    with open("output.txt", 'w') as file:
        file.write(data+"\n")
    print("text successfully written in output.txt")

write()

appended_data = input("enter append text:")

def append():
    with open("output.txt", 'a') as file:
        file.write(appended_data)
    print("text successfully appended in output.txt")

append()

def read():
    with open("output.txt", 'r') as file:
        result = file.read()
        print("final content of output.txt:\n",result)

read()