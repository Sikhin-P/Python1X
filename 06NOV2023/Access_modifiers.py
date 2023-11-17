class MyCar:
    def __init__(self):
        self.color = 'Red'
        self._brand = 'Tata'
        self.__segment = 'SUV'

    def change_brand(self, brand):
        self._brand = 'Hyundai'

    def change_segment(self, seg):
        self.__segment = 'Hatchback'


def car_details():
    my_car = MyCar()
    print(f'Color : {my_car.color}')
    print(f'Brand : {my_car._brand}')
    # print(f'Segment : {my_car.__segment}')


car_details()
