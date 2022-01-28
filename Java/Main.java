class Main {
  public static void main(String[] args) {
    System.out.println("Hello world");
    
    Car car = new Car();
    car.license = "MAO622";
    car.driver = "Mao";
    car.passenger = 4;
    car.printDataCar();

    Car car2 = new Car();
    car2.license = "MAO444";
    car2.driver = "Teo";
    car2.passenger = 4;
    car.printDataCar();
  }
}