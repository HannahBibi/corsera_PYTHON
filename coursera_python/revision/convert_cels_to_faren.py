def calculate_farenheit(cel):
    farenheit = cel*(9/5) + 32
    heit = round(farenheit, 3)
    return heit


def convert_to_farenheit():
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
