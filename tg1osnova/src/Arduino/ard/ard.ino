#include <DHT.h>      // подключаем библиотеку для датчика
DHT dht(2, DHT11);  // сообщаем на каком порту будет датчик




void setup() {
   dht.begin();                // запускаем датчик DHT11
   Serial.begin(9600);
   pinMode(7, INPUT);  // подключаем монитор порта
}

String readdht() {
  digitalWrite(7, HIGH);
  float h = dht.readHumidity();

  float t = dht.readTemperature();
  String temph = String(t) + " " + String(h);
  // выводим температуру (t) и влажность (h) на монитор порта
  Serial.println(temph);
  delay(500);
}



void loop() {

  readdht();

}