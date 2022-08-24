class car(object):
    def __init__(self, make, model, year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
        
    def display(self, showAll):
        if showAll:
            print("This car is a {} from {}, it is {} and has {} kms." .format(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a {} {} from {}." .format(self.make, self.model, self.year))
            
test1 = car('Mistubishi', 'Mirage', 2015, 'New', 0)
test1.display(True)