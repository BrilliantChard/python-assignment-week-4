
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

# 1. Asking the user for a file name:
filename = input("Please enter the filename: \n")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation completed.")


