#include <avr/io.h>
#include <stdbool.h>
int main (void)
{

// bool U=1,V=1,W=1,Z=1,G;
 bool U,V,W,Z,G;
 
 DDRB =  0b00100000;  //  13 pin as output 
 DDRD =  0b11000011;
 PORTD = 0b00111100;   // 2,3,4,5 pins as inputs
 

while(1)
{  
U= (PIND & (1 << PIND2)) == (1 << PIND2);
V= (PIND & (1 << PIND3)) == (1 << PIND3);
W=(PIND & (1 << PIND4)) == (1 << PIND4);
Z=(PIND & (1 << PIND5)) == (1 << PIND5);

G=(W&&Z)||(V&&Z)||(U&&V&&!W)||(!U&&V&&W);
PORTB |=(G<<5);
}
return 0;
}
