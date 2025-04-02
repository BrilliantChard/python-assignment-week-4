# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# 1. File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file

# Open the original file in read mode and read it
file = open("file1.txt", "r")
print(file.read())
file.close()

# Writing a modified version to a new file
file = open("file1.txt", "r")
file1 = open("file2.txt", "w")

for data in file:
    file1.write(data)  # Writing each line from file1.txt to file2.txt
file.close()  # Close file1.txt after reading
file1.close()  # Close file2.txt after writing
