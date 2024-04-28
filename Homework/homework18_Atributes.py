from random import choice

class Building:
    total = 0
    types = ['Panelka', 'Cottage', 'Villa', 'Temple']

    def __init__(self):
        Building.total += 1
        self.type = choice(Building.types)

    def check_type(self):
        return self.type

for i in range(1, 41):
    build = Building()
    print(f'{i} -- {build.check_type()}')
