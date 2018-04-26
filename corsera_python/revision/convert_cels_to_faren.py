def calculate_farenheit(cel):
    farenheit = cel*(9/5) + 32
    return farenheit


def convert_cel():
    while True:
        try:
            celsius = input('Enter celsius temp:')
            if celsius == 'Done':
                break
            cel = float(celsius)
            f = calculate_farenheit(cel)
            print(str(f) + '°F')
        except:
            print('Invalid input entered.')
