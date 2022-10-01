/*
* File name: Experiment-2
* Author: e-Yantra Team
* Description: This experiment is part of Task-3. It is aimed to get you familiar with the LCD interfacing.
* 			   Messages are displayed whenever the boot switch is pressed or released .

LCD Connections:
 			  LCD	  Microcontroller Pins
 			  RS  --> PC0
			  RW  --> PC1
			  EN  --> PC2
			  DB7 --> PC7
			  DB6 --> PC6
			  DB5 --> PC5
			  DB4 --> PC4

*/

#define __OPTIMIZE__ -O0			// set optimization level to 0. Change only if you know what it does
#define F_CPU 14745600
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "lcd.h"

/*
/////////////////////////////////////////////////////////////////////////////////////////////
///////////////////// Declare any required global variable here//////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////
*/


void boot_switch_config()
{
	 DDRE= DDRE & 0x7F; // Boot Switch is interfaced on Port E Pin no.7 (PE7). Write Suitable value to set this pin as input.
	 PORTE= PORTE | 0x80; // Write suitable value to enable pull up resistor for PORTE Pin no.7
}


/*
* Function Name: main()
* Input: none
* Output: none
* Logic: Initialize LCD and display message on LCD
*/
int main(void)
{
	boot_switch_config();//This function configures the boot switch as input
	
	lcd_port_config();	// This function configures LCD pins as output

	lcd_init();			// This function initializes the LCD in 4-bit mode 
	while(1)
		{
			if((PINE & 0x80) == 0x80)
			{
				
				lcd_string(1,4,"NOT PRESSED");
			}
			else
			{
				lcd_clear();
				lcd_string(1,4,"PRESSED");
				_delay_ms(1000);
			}
		}

}
