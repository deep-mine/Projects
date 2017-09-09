#stan
import pyautogui, time
time.sleep(5)
pyautogui.typewrite(['space'])

count1 = 0
count2 = 0
count3 = 0

try:
	while True:
		
		screen = pyautogui.screenshot()
		tree1   = screen.getpixel((519,240))
		tree2   = screen.getpixel((522,240))
		tree3   = screen.getpixel((521,240))
		sky	   = screen.getpixel((454,212))
		white1  = (247,247,247)                 #round1
		black1  = (83,83,83)					#round1
		white2  = (172,172,172)					#round2
		black2  = (0,0,0)						#round2
		ptero   = screen.getpixel((521,217))
		'''
		if tree1 == black1:
			count1 += 1
		if tree2 == black1:
			count2 += 1
		if tree3 == black1:
			count3 += 1
		
		if tree1 == white2:
			count1 += 1
		if tree2 == white2:
			count2 += 1
		if tree3 == white2:
			count3 += 1
		'''	
		if tree1 == black1 or tree2 == black1 or tree3 == black1 or ptero == black1 and sky == white1 or tree1 == white2 or tree2 == white2 or tree3 == white2  or ptero == white2 and sky == black2:
			pyautogui.typewrite(['space'])
except KeyboardInterrupt:
	print('close : ',count1)
	print('medium: ',count2)
	print('far   : ',count3)
	print("\nFin.")
	
'''	

				   white           black
initial colours = 247,247,247    83,83,83
round 2 colours = 172,172,172      0,0,0

medium pterodactyl = y:217

'''