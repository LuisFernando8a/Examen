import pygame

pygame.init()

blanco = (255, 255, 255)
negro = (0, 0, 0)
font = pygame.font.SysFont("arialblack", 20)

class Button_Text():
	button_color = (255, 255, 255)
	txt_color = (0, 0, 0)
	width = 180
	height = 40

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text
		self.clicked = False

	def drawtxt(self, surface):

		accion = False

		#posicion del mouse
		pos = pygame.mouse.get_pos()

		button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

		#sobre y click
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				accion = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		pygame.draw.line(surface, blanco, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(surface, blanco, (self.x, self.y), (self.x, self.height + self.y), 2)
		pygame.draw.line(surface, negro, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(surface, negro, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#dibujar boton
		text_img = font.render(self.text, True, self.txt_color)
		text_len = text_img.get_width()
		surface.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 5))

		return accion