int sensorValue;

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  sensorValue=analogRead(0);
  Serial.print(sensorValue, DEC);
  if(sensorValue>280)
  {
    tone(8,3500,200);
    }
   delay(6000);
}
