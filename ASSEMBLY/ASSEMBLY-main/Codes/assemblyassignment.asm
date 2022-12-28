.include "/sdcard/Download/codes/m328Pdef.inc"

ldi r16,0b00000100  ;2 pins
out DDRD,r16

ldi r17, 0b11110000 ; identifying input pins 8,9,10,11
	out DDRB,r17		; declaring pins as input
ldi r17, 0b11111011;
	out PORTB,r17		; activating internal pullup for pins 8,9,10,11

ldi r18,0b00000001 ; value
ldi r19,0b00000001 ; value
ldi r20,0b00000001 ; value
ldi r21,0b00000001 ; value



and r18,r17 ; Z
lsr r17
and r19,r17; W
lsr r17
and r20,r17; V
lsr r17
and r21,r17; U
lsr r17

ldi r22,0b00000001;
eor r22,r18;  Z'
ldi r23,0b00000001;
eor r23,r19; W'
ldi r24,0b00000001;
eor r24,r20; V'
ldi r25,0b00000001;
eor r25,r21; U'


mov r16,r18   ;for Z
and r16,r19   ; for WZ
mov r26,r20   ;for V
and r26,r18   ; for VZ    
or  r16,r26   ;for WZ+VZ
mov r27,r21   ;for U
and r27,r20   ;for UV
and r27,r23   ;for UVW'
or  r16,r27  ;for WZ+VZ+UVW'
mov r28,r25   ;for U'
and r28,r20   ;for U'V
and r28,r19   ;U'VW
or r16,r28    ;WZ+VZ+UVW'+U'VW
lsl r16
lsl r16

out PORTD,r16             ;F output

start:
rjmp start
