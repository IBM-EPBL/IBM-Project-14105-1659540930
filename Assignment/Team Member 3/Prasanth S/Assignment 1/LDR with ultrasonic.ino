int value=0;
void setup() 
{
  pinMode(A0, INPUT);
  Serial.begin (9600);
  pinMode(13, OUTPUT);
  pinMode(12, INPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(A0, INPUT);
}
void loop() 
{
  long duration, distance;
  digitalWrite(13, LOW);        
  delayMicroseconds(2);              
  digitalWrite(13, HIGH);
  delayMicroseconds(10);           
  digitalWrite(13, LOW);
  duration = pulseIn(12, HIGH);
  distance = (duration/2) / 29.1;
  if (distance >= 200 || distance <= 0 )  
  {
    digitalWrite(2, LOW);
    Serial.println("Out of range");
  }
  else 
  {
    Serial.print(distance);
    Serial.println(" cm ultrasonic distance sensor value \n");
    digitalWrite(2,HIGH);
    Serial.print("LED ON");
    tone(4, 220, 100);
    delay(500);
    
  }
  delay(500);
  
  value= analogRead(A0);
  
  if(value<10)
  {
    digitalWrite(11, HIGH);
    Serial.println("\nLDR value");
    Serial.println(value);
  }
  else
  {
    digitalWrite(11, LOW);
    Serial.println("\nLDR value");
  }
}