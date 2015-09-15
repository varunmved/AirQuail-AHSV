
var fbase = new firebase("https://airquail.firebaseio.com/");

function fire(fbase) {
  while(true)
  {
    var fkeyHumid = fbase.key();
    fkeyHumid = fbase.child("Sensor/Humidity").fkeyHumid();
    console.log(fkeyHumid);


    var fkeyTemp = fbase.key();
    fkeyTemp = fbase.child("Sensor/Temperature").fkeyTemp();
    console.log(fkeyTemp);

  }
}
