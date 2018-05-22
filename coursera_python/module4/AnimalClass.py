class Animal:

    def __init__(self, colour, sex):
        self.colour = colour
        self.sex = sex
        self.number_of_meals_eaten = 0
        self.distance_moved = 0

    def move(self):
        print('Animal move() method called.')
        self.distance_moved = self.distance_moved + 1

    def eat(self):
        print('Animal eat() method called.')
        self.number_of_meals_eaten = self.number_of_meals_eaten + 1
