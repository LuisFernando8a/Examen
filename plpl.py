import pygame
import buttonimg
import buttontext

pygame.init()


#sonido de los botones
bnt_sound = pygame.mixer.Sound('boton.mp3')


#Creando ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 563

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Operaciones Desafiantes')

#Variables del juego
menu_state = "main"

#Cargando imagenes
img_start = pygame.image.load('start.png').convert_alpha()
img_exit = pygame.image.load('exit.png').convert_alpha()
img_suma = pygame.image.load('suma.png').convert_alpha()
img_resta = pygame.image.load('resta.png').convert_alpha()
img_multi = pygame.image.load('multiplicacion.png').convert_alpha()
img_div = pygame.image.load('division.png').convert_alpha()
img_volver = pygame.image.load('reg.png').convert_alpha()
img_lv1 = pygame.image.load('nivel1.png').convert_alpha()
img_lv2 = pygame.image.load('nivel2.png').convert_alpha()
img_lv3 = pygame.image.load('nivel3.png').convert_alpha()
img_fondo = pygame.image.load('fondo.png').convert_alpha()

#instancias botones operacion
btn_suma = buttonimg.Button_Img(100, 175, img_suma, 0.8)
btn_resta = buttonimg.Button_Img(518, 175, img_resta, 0.8)
btn_multi = buttonimg.Button_Img(100, 425, img_multi, 0.8)
btn_divi = buttonimg.Button_Img(518, 425, img_div, 0.8)

#instancias botones nivel
btn_lvl1 = buttonimg.Button_Img((SCREEN_WIDTH/2) - 110, 175, img_lv1, 0.8)
btn_lvl2 = buttonimg.Button_Img((SCREEN_WIDTH/2) - 110, 300, img_lv2, 0.8)
btn_lvl3 = buttonimg.Button_Img((SCREEN_WIDTH/2) - 110, 425, img_lv3, 0.8)
btn_return = buttonimg.Button_Img(0, 0, img_volver, 0.3)

#instancias botones suma1
btn_suma1 = buttontext.Button_Text(75, 200, "10")
btn_suma2 = buttontext.Button_Text(325, 200, "10")
btn_suma3 = buttontext.Button_Text(75, 350, "10")
btn_suma4 = buttontext.Button_Text(325, 350, "10")

#definiendo font
font = pygame.font.SysFont("arialblack", 30)
font2 = pygame.font.SysFont("arialblack", 20)

#definiendo color
TEXT_COL = (255, 153, 51)

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	img_width = img.get_width()

	screen.blit(img, ((SCREEN_WIDTH/2)-(img_width/2), y))

def nivel_resta():
	if btn_lvl1.draw(screen, bnt_sound):
		print("Nivel_resta1")

	if btn_lvl2.draw(screen, bnt_sound):
		print("Nivel_resta2")

	if btn_lvl3.draw(screen, bnt_sound):
		print("Nivel_resta3")


def nivel_multi():
	if btn_lvl1.draw(screen, bnt_sound):
		print("Nivel_multi1")

	if btn_lvl2.draw(screen, bnt_sound):
		print("Nivel_multi2")

	if btn_lvl3.draw(screen, bnt_sound):
		print("Nivel_multi3")


def nivel_divi():
	if btn_lvl1.draw(screen, bnt_sound):
		print("Nivel_divi1")

	if btn_lvl2.draw(screen, bnt_sound):
		print("Nivel_divi2")

	if btn_lvl3.draw(screen, bnt_sound):
		print("Nivel_divi3")

#game loop
run = True
while run:

	screen.fill((202, 228, 241))
	screen.blit(img_fondo,(0,0))
	x = 0

	if x == 1:
		menu_state = "suma1"

#menu principal
	if menu_state == "main":
		#draw menu principal
		draw_text("Bienvenido a las Operaciones Desafiantes!", font, TEXT_COL, 400, 50)
		if btn_suma.draw(screen, bnt_sound):
			print("Suma")
			menu_state = "niveles_suma"
		if btn_resta.draw(screen, bnt_sound):
			print("Resta")
			menu_state = "niveles_resta"
		if btn_multi.draw(screen, bnt_sound):
			print("Multi")
			menu_state = "niveles_multi"
		if btn_divi.draw(screen, bnt_sound):
			print("Divi")
			menu_state = "niveles_divi"

#eleccion de niveles
	elif menu_state == "niveles_suma":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		if btn_lvl1.draw(screen, bnt_sound):
			print("Nivel_suma1")
			menu_state = "suma1"

		if btn_lvl2.draw(screen, bnt_sound):
			print("Nivel_suma2")
			menu_state = "suma2"

		if btn_lvl3.draw(screen, bnt_sound):
			print("Nivel_suma3")
			menu_state = "suma3"

		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

	elif menu_state == "niveles_resta":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		nivel_resta()
		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

	elif menu_state == "niveles_multi":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		nivel_multi()
		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

	elif menu_state == "niveles_divi":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		nivel_divi()
		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

#nivel 1 suma
	elif menu_state == "suma1":
		draw_text("¿Cual es el resultado de esta suma? 10 + 15", font2, TEXT_COL, 145, 50)
		if btn_suma1.drawtxt(screen):
			print("20")
		if btn_suma2.drawtxt(screen):
			print("25")
		if btn_suma3.drawtxt(screen):
			print("11")
		if btn_suma4.drawtxt(screen):
			print("12")
		if btn_return.draw(screen, bnt_sound):
			menu_state = "niveles_suma"
   
#nivel 2 suma
	elif menu_state == "suma2":
		draw_text("¿Cual es el resultado de esta suma?", font2, TEXT_COL, 145, 50)
		if btn_suma1.drawtxt(screen):
			print("10")
		if btn_suma2.drawtxt(screen):
			print("10")
		if btn_suma3.drawtxt(screen):
			print("10")
		if btn_suma4.drawtxt(screen):
			print("10")
		if btn_return.draw(screen, bnt_sound):
			menu_state = "niveles_suma"
   
#nivel 3 suma
	elif menu_state == "suma3":
		draw_text("¿Cual es el resultado de esta suma?", font2, TEXT_COL, 145, 50)
		if btn_suma1.drawtxt(screen):
			print("10")
		if btn_suma2.drawtxt(screen):
			print("10")
		if btn_suma3.drawtxt(screen):
			print("10")
		if btn_suma4.drawtxt(screen):
			print("10")
		if btn_return.draw(screen, bnt_sound):
			menu_state = "niveles_suma"
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()

pygame.quit()
