from car import Car

if __name__=="__main__":
    print("Hola mundo")
    car = Car()
    car.license = "MAO123"
    car.driver = "Mario Crespo"
    print(vars(car))

    car2 = Car()
    car2.license = "123MAO"
    car2.driver = "Alejandro Reyes"
    print(vars(car2))