class Vehicle:
    name=""
    kind="car"
    color=""
    value=100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % ( self.name, self.kind, self.color, self.value)
        return desc_str

print dir(Vehicle)
