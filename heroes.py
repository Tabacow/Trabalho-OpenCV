import time

class Heroes:

    def __init__(self, one = False, two = False, three = False, four = False, five = False, six = False, seven = False, eight = False, nine = False, ten = False, eleven = False, twelve = False, thirteen = False, fourteen = False, fifteen = False):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.ten = ten
        self.eleven = eleven
        self.twelve = twelve
        self.thirteen = thirteen
        self.fourteen = fourteen
        self.fifteen = fifteen
        self.static_templates = {
            "1" : self.one,
            "2" : self.two,
            "3" : self.three,
            "4" : self.four,
            "5" : self.five,
            "6" : self.six,
            "7" : self.seven,
            "8" : self.eight,
            "9" : self.nine,
            "10" : self.ten,
            "11" : self.eleven,
            "12" : self.twelve,
            "13" : self.thirteen,
            "14" : self.fourteen,
            "15" : self.fifteen
        }

    def change_all_to_false(self):
        self.one = False
        self.two = False
        self.three = False
        self.four = False
        self.five = False
        self.six = False
        self.seven = False
        self.eight = False
        self.nine = False
        self.ten = False
        self.eleven = False
        self.twelve = False
        self.thirteen = False 
        self.fourteen = False
        self.fifteen = False

    def print_hero_status(self):
        print("heroes  | working? ")
        print("hero 1  |" + " " + str(self.one))
        print("hero 2  |" + " " + str(self.two))
        print("hero 3  |" + " " + str(self.three))
        print("hero 4  |" + " " + str(self.four))
        print("hero 5  |" + " " + str(self.five))
        print("hero 6  |" + " " + str(self.six))
        print("hero 7  |" + " " + str(self.seven))
        print("hero 8  |" + " " + str(self.eight))
        print("hero 9  |" + " " + str(self.nine))
        print("hero 10 |" + " " + str(self.ten))
        print("hero 11 |" + " " + str(self.eleven))
        print("hero 12 |" + " " + str(self.twelve))
        print("hero 13 |" + " " + str(self.thirteen))
        print("hero 14 |" + " " + str(self.fourteen))
        print("hero 15 |" + " " + str(self.fifteen))

    def is_all_heroes_working(self): 
        return (self.one 
        and self.two 
        and self.three 
        and self.four 
        and self.five 
        and self.six 
        and self.seven 
        and self.eight 
        and self.nine 
        and self.ten 
        and self.eleven 
        and self.twelve 
        and self.thirteen 
        and self.fourteen 
        and self.fifteen)

    def change_status(self, number, status):
        if(number == 1):
            self.one = status
        if(number == 2):
            self.two = status
        if(number == 3):
            self.three = status
        if(number == 4):
            self.four = status
        if(number == 5):
            self.five = status
        if(number == 6):
            self.six = status
        if(number == 7):
            self.seven = status
        if(number == 8):
            self.eight = status
        if(number == 9):
            self.nine = status
        if(number == 10):
            self.ten = status
        if(number == 11):
            self.eleven = status
        if(number == 12):
            self.twelve = status
        if(number == 13):
            self.thirteen = status
        if(number == 14):
            self.fourteen = status
        if(number == 15):
            self.fifteen = status