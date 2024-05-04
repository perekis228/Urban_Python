class House:
    countOfHouses = 0
    def __init__(self, entrances, floors):
        House.countOfHouses += 1
        self.entrances = entrances
        self.floors = floors
        self.flats = self.entrances * self.floors * 4

    def __str__(self):
        return f'В данном доме {self.flats} {'квартиры' if self.flats == 4 else 'квартир'}'

    def __eq__(self, other):
        return 'Одинаковыe' if self.entrances == other.entrances and self.flats == other.flats else 'Разные'

    def __del__(self):
        House.countOfHouses -= 1

house1 = House(1, 1)
house2 = House(4, 5)
house3 = House(4, 5)
print(f'{house1}\n{house2}\n{house3}')
print(house2 == house3)
print(house1 == house3)
print(f'Всего домов в районе: {House.countOfHouses}')
