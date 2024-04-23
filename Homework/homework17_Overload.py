class Building:
    def __init__(self, Floors, Type):
        self.numberOfFloors = Floors
        self.buildingType = Type

    def __eq__(self, other):
        if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
            return True
        return False


build1 = Building(10, 'Panelka')
build2 = Building(11, 'Panelka')
if build1 == build2:
    print('Здания одинаковые')
else:
    print('Здания отличаются')
