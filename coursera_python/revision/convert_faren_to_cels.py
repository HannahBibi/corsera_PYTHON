def calculate_celsius(faren):
    cels = (faren - 32) * 5/9
    decimal_value = round(cels, 3)
    return decimal_value


def convert_to_celsius():
    while True:
        try:
            temp = input('Enter farenheit temp:')
            if temp == 'Done':
                break
            faren = float(temp)
            c = calculate_celsius(faren)
            print(c + '°C')
        except:
            print('Invalid input entered.')
