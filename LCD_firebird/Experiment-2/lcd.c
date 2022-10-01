
/* 
 * lcd.c
 * Created: 10/07/2018 10:47:03
 * Author: e-Yantra Team
 */

#define F_CPU 14745600

#include <avr/io.h>
#include <util/delay.h>
#include "lcd.h"

#define RS 0
#define RW 1
#define EN 2
#define lcd_port PORTC
#define sbit(reg,bit)	reg |= (1<<bit)			// Macro defined for Setting a bit of any register
#define cbit(reg,bit)	reg &= ~(1<<bit)		// Macro defined for Clearing a bit of any register

unsigned int temp;
unsigned int unit;
unsigned int tens;
unsigned int hundred;
unsigned int thousand;
unsigned int million;


/* 
 * Function Name: lcd_port_config
 * Input: None
 * Output: None
 * Logic: This function configures the LCD port pins as output and sets them to 0 initially
 * Example Call: lcd_port_config();
 */
void lcd_port_config(void)
{
	DDRC = DDRC | 0xF7;		// all LCD pins direction set as output
	PORTC = PORTC & 0x08;	// all LCD pins set to logic 0 except PC.3 (Buzzer pin)
}

/* 
 * Function Name: lcd_set_4bit
 * Input: None
 * Output: None
 * Logic: This function configures the LCD to work in 4 bit mode instead of 8 bit mode
 *		  to reduce the number of data lines required to be used
 * Example Call: lcd_set_4bit();
 */
void lcd_set_4bit (void)
{
	_delay_ms(1);
	cbit(lcd_port,RS);				// RS=0 --- Command Input
	cbit(lcd_port,RW);				// RW=0 --- Writing to LCD
	lcd_port = 0x30;				// Sending 3
	sbit(lcd_port,EN);				// Set Enable Pin
	_delay_ms(5);					// Delay
	cbit(lcd_port,EN);				// Clear Enable Pin

	_delay_ms(1);
	cbit(lcd_port,RS);				// RS=0 --- Command Input
	cbit(lcd_port,RW);				// RW=0 --- Writing to LCD
	lcd_port = 0x30;				// Sending 3
	sbit(lcd_port,EN);				// Set Enable Pin
	_delay_ms(5);					// Delay
	cbit(lcd_port,EN);				// Clear Enable Pin

	_delay_ms(1);
	cbit(lcd_port,RS);				// RS=0 --- Command Input
	cbit(lcd_port,RW);				// RW=0 --- Writing to LCD
	lcd_port = 0x30;				// Sending 3
	sbit(lcd_port,EN);				// Set Enable Pin
	_delay_ms(5);					// Delay
	cbit(lcd_port,EN);				// Clear Enable Pin

	_delay_ms(1);
	cbit(lcd_port,RS);				// RS=0 --- Command Input
	cbit(lcd_port,RW);				// RW=0 --- Writing to LCD
	lcd_port = 0x20;				// Sending 2 to initialize LCD in 4-bit mode
	sbit(lcd_port,EN);				// Set Enable Pin
	_delay_ms(5);					// Delay
	cbit(lcd_port,EN);				// Clear Enable Pin
}

/* 
 * Function Name: lcd_wr_command
 * Input: cmd => hex value of the command to be given to LCD
 * Output: None
 * Logic: This function gives specific command values to the LCD to perform necessary functions
 * Example Call: lcd_wr_command(0x80); => to bring cursor at home position
 */
void lcd_wr_command (unsigned char cmd)
{
	unsigned char temp;
	temp = cmd;
	temp = temp & 0xF0;
	lcd_port &= 0x0F;
	lcd_port |= temp;
	cbit(lcd_port,RS);
	cbit(lcd_port,RW);
	sbit(lcd_port,EN);
	_delay_ms(5);
	cbit(lcd_port,EN);
	
	cmd = cmd & 0x0F;
	cmd = cmd<<4;
	lcd_port &= 0x0F;
	lcd_port |= cmd;
	cbit(lcd_port,RS);
	cbit(lcd_port,RW);
	sbit(lcd_port,EN);
	_delay_ms(5);
	cbit(lcd_port,EN);
}

/* 
 * Function Name: lcd_init
 * Input: None
 * Output: None
 * Logic: This function initializes the LCD
 * Example Call: lcd_init();
 */
void lcd_init (void)
{
	lcd_set_4bit();
	_delay_ms(1);
	lcd_wr_command(0x28);		// LCD 4-bit mode and 2 lines
	lcd_wr_command(0x01);       // Clear display screen
	lcd_wr_command(0x06);       // Entry mode
	lcd_wr_command(0x0E);       // Display On and Cursor On
	lcd_wr_command(0x80);       // LCD cursor set to Home position		
}

/* 
 * Function Name: lcd_home
 * Input: None
 * Output: This function sets the cursor's to home i.e. 1st row, 1st column
 * Logic: Passes 0x80 command to LCD using lcd_wr_command
 * Example Call: lcd_home();
 */
void lcd_home (void)
{
	lcd_wr_command(0x80);		// LCD cursor set to Home position
}

/* 
 * Function Name: lcd_cursor
 * Input: row, column => where you want the cursor to be positioned on LCD
 * Output: This function sets the cursor to the specified position
 * Logic: Position the LCD cursor at position (row, column) by passing
 *        the required commands to the lcd_wr_command function
 * col >     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
 *         1 . . . . . . . . .  .  .  .  .  .  .  .
 *         2 . . . . . . . . .  .  .  .  .  .  .  .
 *         ^
 *        row
 *
 * Example Call: lcd_cursor(2, 3);
 */
void lcd_cursor (char row, char column)
{
	switch (row)
	{
		case 1: lcd_wr_command (0x80 + column - 1); break;
		case 2: lcd_wr_command (0xC0 + column - 1); break;
		case 3: lcd_wr_command (0x94 + column - 1); break;
		case 4: lcd_wr_command (0xD4 + column - 1); break;
		default: break;
	}
}


/*
 * Function Name: lcd_clear
 * Input: None
 * Output: LCD is cleared
 * Logic: This function clears LCD by giving specific command as input to lcd_wr_command() function
 * Example Call: lcd_clear();
 */
void lcd_clear (void)
{
	lcd_wr_command(0x01);
}

/*
 * Function Name: lcd_wr_char
 * Input: row, column => where you want the cursor to be positioned on LCD
 *        alpha_num_char => alpha-numeric type data to be printed on the LCD at the specified (row, column) position
 * Output: None
 * Logic: This function prints an alpha-numeric character at specified (row, column) position on LCD
 * Example Call: lcd_wr_char(1, 4, 'A') => to write character 'A' to the LCD
 */
void lcd_wr_char(char row, char column, char alpha_num_char)
{
	lcd_cursor (row, column);
	
	char temp;
	temp = alpha_num_char;
	temp = (temp & 0xF0);
	lcd_port &= 0x0F;
	lcd_port |= temp;
	sbit(lcd_port,RS);
	cbit(lcd_port,RW);
	sbit(lcd_port,EN);
	_delay_ms(5);
	cbit(lcd_port,EN);

	alpha_num_char = alpha_num_char & 0x0F;
	alpha_num_char = alpha_num_char << 4;
	lcd_port &= 0x0F;
	lcd_port |= alpha_num_char;
	sbit(lcd_port,RS);
	cbit(lcd_port,RW);
	sbit(lcd_port,EN);
	_delay_ms(5);
	cbit(lcd_port,EN);
}

/*
 * Function Name: lcd_string
 * Input: row, column => where you want the cursor to be positioned on LCD
 *        *str => pointer of the char data type which points to the address of first character of the string
 * Output: This function prints the given string on the LCD at the specified (row, column) position
 * Logic: Positions the cursor and prints each character on LCD in a while loop until EOF is reached
 * Example Call: lcd_string(1, 1, "Hello !");
 */
void lcd_string(char row, char column, char *str)
{
	while(*str != '\0')
	{
		lcd_wr_char(row, column, *str);
		str++;
		column+=1;
	}
}

/* Function Name: lcd_numeric_value
 * Input: row, column => where you want the cursor to be positioned on LCD
 *        value => any integer value or value in a variable as integer
 *        digits => number of digits of value to display
 * Output: This function prints any integer value or value in a variable as integer
  *        on the specified location and up to the specified number of digits on LCD
 * Example Call: lcd_numeric_value(1, 1, -20, 2);
 */
void lcd_numeric_value(char row, char column, int val, int digits)
{
	lcd_cursor(row, column);
	
	if (val < 0)
	{
		val = 0 - val;
		lcd_string(row, column, "-");
		column+=1;
	}
		
	unsigned char flag = 0;
	
	if(row == 0 || column == 0)
	{
		lcd_home();
	}
	
	else
	{
		lcd_cursor(row, column);
	}
	
	if(digits == 5 || flag == 1)
	{
		million = val/10000+48;
		lcd_wr_char(row ,column, million);
		column+=1;
		flag = 1;
	}
	
	if(digits == 4 || flag == 1)
	{
		temp = val/1000;
		thousand = temp%10 + 48;
		lcd_wr_char(row, column, thousand);
		column+=1;
		flag = 1;
	}
	
	if(digits == 3 || flag == 1)
	{
		temp = val/100;
		hundred = temp%10 + 48;
		lcd_wr_char(row, column, hundred);
		column+=1;
		flag = 1;
	}
	
	if(digits == 2 || flag == 1)
	{
		temp = val/10;
		tens = temp%10 + 48;
		lcd_wr_char(row, column, tens);
		column+=1;
		flag = 1;
	}
	
	if(digits == 1 || flag == 1)
	{
		unit = val%10 + 48;
		lcd_wr_char(row, column, unit);
		column+=1;
	}
	
	if(digits > 5)
	{
		lcd_wr_char(row, column, 'E');
		column+=1;
	}
}

