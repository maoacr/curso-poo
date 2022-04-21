from car import Car

class UberX(Car):
  brand = str
  model = str

  def ___init__(self, license, driver, brand, model):
    super.__init__(license, driver)
    self.brand = brand
    self.model = model