largest = None
smallest = None
while True:
    num = input("Enter number: ")
    if num == "done":
        break

    try:
        num = int(num)

        if largest is None:
            largest = num

        if smallest is None:
            smallest = num

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    except:
        print("Invalid input")

print("Maximum is", largest)
print("Smallest is", smallest)
