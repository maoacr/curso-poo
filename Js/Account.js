//Before ES6
/*
function Account(name, document) {
  this.id;
  this.name = name;
  this.document = document;
  this.email;
  this.password;
}
*/
//After ES6
class Account{
  constructor(name, document){
    this.id;
    this.name = name;
    this.document = document;
    this.email;
    this.password;
  }
}