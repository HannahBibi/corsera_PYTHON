file_name = input("Enter file name: ")
file_handle = open(file_name)

for i in file_handle:
    i = i.strip()
    print(i. upper())

