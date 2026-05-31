#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(115200);

  dht.begin();
}

void loop()
{
  float t = dht.readTemperature();

  float h = dht.readHumidity();

  if(isnan(t) || isnan(h))
  {
    Serial.println("ERROR");

    delay(2000);

    return;
  }

  Serial.print("Temp:");

  Serial.print(t);

  Serial.print(" Hum:");

  Serial.println(h);

  delay(3000);
}