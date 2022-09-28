int baselineTemp = 0;
int celsius = 0;
void setup() 
{
  pinMode(A0, INPUT);
  Serial.begin (9600);
  pinMode(13, OUTPUT);
  pinMode(12, INPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
}
void loop() 
{
  baselineTemp = 40;
  celsius = map(((analogRead(A0) - 20) * 3.04), 0, 1023, -40, 125);
  Serial.print(celsius);
  Serial.print(" \n");
  long duration, distance;
  digitalWrite(13, LOW);        
  delayMicroseconds(2);              
  digitalWrite(13, HIGH);
  delayMicroseconds(10);           
  digitalWrite(13, LOW);
  duration = pulseIn(12, HIGH);
  distance = (duration/2) / 29.1;
  if (distance >= 200 || distance <= 0 && celsius < baselineTemp)  
  {
    digitalWrite(2, LOW);
    Serial.println("Out of range");
  }
  else 
  {
    Serial.print(distance);
    Serial.println(" cm \n");
    digitalWrite(2,HIGH);
    Serial.print("LED ON");
    tone(4, 220, 100);
    delay(500);
    
  }
  delay(500);
}