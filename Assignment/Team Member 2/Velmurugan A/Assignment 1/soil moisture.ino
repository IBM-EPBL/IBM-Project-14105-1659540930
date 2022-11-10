int baselinetemp = 0;
int celsius = 0;
int sensorpin = A1; 
int sensorvalue; 
void setup()
{
  pinMode(2, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600);
  pinMode(4, OUTPUT);
  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop()
{
  
  sensorvalue = analogRead(sensorpin); 
  Serial.println("Analog Value : ");
  Serial.println(sensorvalue);
  
  baselinetemp = 40;
  digitalWrite(2, HIGH);
  celsius = map(((analogRead(A0) - 20) * 3.04), 0, 1023, -40, 125);
  Serial.print(celsius);
  Serial.print(" C, ");
  
  if (celsius < baselinetemp) {
    digitalWrite(2, LOW);
  }else{
  digitalWrite(2, HIGH);
  tone(4, 100, 1000); // Send 100 Hz sound signal
  delay(1000); 
  }
  
}