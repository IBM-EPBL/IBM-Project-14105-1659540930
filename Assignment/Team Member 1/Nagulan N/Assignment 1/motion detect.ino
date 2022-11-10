int pirState = LOW; 
int val = 0;
 
void setup() {
pinMode(5, OUTPUT); 
pinMode(6, OUTPUT);
pinMode(2, INPUT); 
 
Serial.begin(9600);
}
 
void loop(){
val = digitalRead(2); 
int value_ldr = analogRead(A0); 
if((300>value_ldr) && ( val==HIGH) ){
if (val == HIGH) { 
digitalWrite(5, HIGH); 
digitalWrite(6, 1); 
delay(5000);
if (pirState == LOW) {
Serial.println("Motion detected!");
pirState = HIGH;
}
} else {
digitalWrite(5, LOW); 
digitalWrite(6, 0); 
if (pirState == HIGH){
Serial.println("Motion ended!");
pirState = LOW;
}
}
}
}