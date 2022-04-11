from account import Account
from car import Car

if __name__=="__main__":
    print("Hola mundo")
    car = Car("AM543", Account("Andres Herrera", "MNJ765"))
    print(vars(car))
    print(vars(car.driver))