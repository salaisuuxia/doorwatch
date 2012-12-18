/*
  Blink
 Turns on an LED on for one second, then off for one second, repeatedly.
 
 This example code is in the public domain.
 */

// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
boolean prevdoor=false;
boolean prevmove=false;
int led = 13;

// the setup routine runs once when you press reset:
void setup() {               
  Serial.begin(9600); 
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
  pinMode(2,INPUT);
  pinMode(3,INPUT);
}
// the loop routine runs over and over again forever:
void loop() {

  if (digitalRead(2) == HIGH)
  {
    if (prevmove==false){
      Serial.print("1");
      digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
      prevmove=true;
    }
  }
  else{
    prevmove=false;
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  }






  if (digitalRead(3)==HIGH)
  {
    if (prevdoor ==false)
    {
      prevdoor=true;
      Serial.print("2");
    }
  }
  else{
    if (prevdoor==true)
    {
      prevdoor=false;
      Serial.print("3");
    }
  }

  delay(100);
}




