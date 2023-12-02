import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 4

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize LCD class
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, address=0x27)

# Print a message to the LCD
lcd.message = "Hello, World!"