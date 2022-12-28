#include <Arduino.h>
//Declaring all variables as integers
int U=1,V=1,W=1,Z=1;
int A;
void setup() {
    pinMode(2, OUTPUT);  
 
}

// the loop function runs over and over again forever
void loop() {
  A=(W&&Z) ||(V&&Z) || (U&&V&&!W) ||(!U&&V&&W);
digitalWrite(2,A);
  }

