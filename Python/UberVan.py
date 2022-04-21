from car import Car

class UberVan(Car):
  typeCarAccepted = []
  seatsMterial = []

  def ___init__(self, license, driver, typeCarAccepted, seatsMterial):
    super.__init__(license, driver)
    self.typeCarAccepted = typeCarAccepted
    self.seatsMterial = seatsMterial