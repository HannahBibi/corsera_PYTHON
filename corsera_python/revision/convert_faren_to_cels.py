def calculate_celsius(faren):
    cels = (faren - 32) * 5/9
    return cels


def convert_faren():
    while True:
        try:
            temp = input('Enter farenheit temp:')
            if temp == 'Done':
                break
            faren = float(temp)
            c = calculate_celsius(faren)
            print(str(c) + '°C')
        except:
            print('Invalid input entered.')
