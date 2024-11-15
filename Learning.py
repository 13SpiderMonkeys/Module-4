filepath = "C:/Users/shado/OneDrive/Desktop/learning_python.txt"

#  Read the entire file and print its content
with open(filepath, "r") as file:
    content = file.read()
    print("Reading the entire file:")
    print(content)

print("\n" + '=' * 50 + '\n')

#  Print contents by looping over the file
with open(filepath, 'r') as file:
    print("Looping over the file:")
    for line in file:
        print(line.strip())

print("\n" + '=' * 50 + '\n')

#  Print contents by storing lines in a list
with open(filepath, "r") as file:
    lines = file.readlines()

print("Printing lines stored in a list:")
for line in lines:
    print(line.strip())

print("\n" + '=' * 50 + '\n')

# Print modified lines by replacing 'Python' with 'PHP'
print("Modified Lines (replacing 'Python' with 'PHP'):")
for line in lines:
    modified_line = line.replace('Python', 'PHP')
    print(modified_line.strip())
