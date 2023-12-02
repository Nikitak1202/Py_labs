class Building:


    def __init__(self, cost, residents, square):
        self.cost_per_meter = cost
        self.amount_of_residents = residents
        self.square = square


    def total_cost(self):
        return self.square * self.cost_per_meter
    

    def total_cost_to_residents(self):
        return self.total_cost() / self.amount_of_residents
    

class Village_house(Building):


    def __init__(self, cost, residents, square, yard):
        self.yard_square = yard
        super().__init__(cost, residents, square)


    def yard_cost(self):
        return self.cost_per_meter * self.yard_square
    

class Apartment_building(Building):


    def __init__(self, cost, residents, square, flats):
        self.amount_of_flats = flats
        super().__init__(cost, residents, square)


    def mean_residents_in_flat(self):
        return self.amount_of_residents / self.amount_of_flats
    

home = Apartment_building(10000, 20000, 1000000, 5000)
print(home.mean_residents_in_flat())
print(home.total_cost_to_residents())
print(home.total_cost())