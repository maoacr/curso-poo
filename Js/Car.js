//Befor ES6
/*
function Car(license, driver) {
  this.id;
  this.license = license;
  this.driver = driver;
  this.passenger;
}

Car.prototype.printDataCar = function () {
  console.log(this.driver)
  console.log(this.driver.name)
  console.log(this.driver.document)
}
*/
//After ES6

class Car {
  constructor(license, driver){
    this.id;
    this.license = license;
    this.driver = driver;
    this.passenger;
  }
  printDataCar() {
    console.log(this.driver)
    console.log(this.driver.name)
    console.log(this.driver.document)
  }
}