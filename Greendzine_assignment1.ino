
#include <avr/io.h>

const float V_REF = 5.0;  // Reference voltage (5V )


void setup() {
  Serial.begin(9600);  // Initialize serial communication for output . Even if we remove too no change in our program
  pinMode(5,OUTPUT);
}

void loop() {
  int sensorValue = analogRead(A0);  // Read from analog pin A0
  float voltage = sensorValue * (V_REF / 1024.0);  // Converting ADC value  to voltage
  float temperature = (voltage - 0.55) / 0.01;  // Converting  to temperature in °C


    if(temperature <= 30)  //  I am assuming lessthan or equal as in question nothing is mention what to do at 30 °C
     {     digitalWrite(5,LOW); // making LED to glove 
          f1(3906);  //  creating a delay of  250 milliseconds 
          digitalWrite(5,HIGH); // making LED to glove 
          digitalWrite(5,LOW); // making LED to glove 
         
     }
     else
     {
      digitalWrite(5,LOW); // making LED to glove 
          f1(7812);  //  creating a delay of  500 milliseconds 
          digitalWrite(5,HIGH); // LED ON 
          digitalWrite(5,LOW); // LED OFF
     }
}

 void f1(int No_of_Pulses )
 {
    
  TCCR1B = (TCCR1B = (1 << CS12) | (1 << CS10));  // Set prescaler to 1024 
  TCNT1 = 0;  // Initialize the timer count value  from  0

    // Wait for the timer to reach the desired delay duration
  while (TCNT1 < No_of_Pulses) {
         //Creating a delay of 250 or 500 milli seconds as   argument given
  }
 }