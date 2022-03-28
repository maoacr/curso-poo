class Main {
  public static void main(String[] args) {
    
    Car car = new Car("MAO622", new Account("Mao", "1234556789"));
    car.passenger = 4;
    car.printDataCar();

    Car car2 = new Car("MA888", new Account("Mayito", "9999999"));;
    car2.passenger = 4;
    car2.printDataCar();
  }
}