#pyautogui
import pyautogui

print("Press Ctrl-C to quit.")
try:
	while True:
		x,y = pyautogui.position()
		posString = "X: " + str(x).rjust(4) + " Y:" + str(y).rjust(4)
		pixelColor = pyautogui.screenshot().getpixel((x, y))
		posString +=  "  RGB: (" + str(pixelColor[0]).rjust(3)
		posString += ", " + str(pixelColor[1]).rjust(3)
		posString += ", " + str(pixelColor[2]).rjust(3) + ")"
		print(posString, end= "")
		print('\b'*len(posString), end ='', flush = True)
except KeyboardInterrupt:
	print("\nDone.")