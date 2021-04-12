import pygame, sys, images, pickle
from constants import *

from scripts import GameFunctions, objects


pygame.init()
pygame.font.init()



class Main:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('Space Defence')

		self.clock = pygame.time.Clock()

	def main(self, gf):
		self.load_state(gf)
		while True:
			self.screen.fill((0, 0, 0))

			self.update()
			self.blit_objects()

			self.update_event()

			self.clock.tick(FPS)
			pygame.display.update()
			pygame.event.pump()

	def update(self):
		if gf.in_game:
			gf.rocket.update()
			gf.update_game()

	def blit_objects(self):
		if gf.in_game:
			for obj in gf.background_objects:
				self.screen.blit(obj.image, obj.rect)

			self.screen.blit(gf.rocket.image, gf.rocket.rect)

			for enemy in gf.enemyes:
				self.screen.blit(enemy.image, enemy.rect)
			for bullet in gf.self_bullets:
				self.screen.blit(bullet.image, bullet.rect)
			for bullet in gf.enemy_bullets:
				self.screen.blit(bullet.image, bullet.rect)

			for i in range(gf.rocket.lives):
				self.screen.blit(images.get_heart(), (HEART_SIZE[0]*i+1, 0))

			self.screen.blit(gf.info_font.render(f'SCORE - {gf.score}', False, (255, 255, 255)), (0, HEIGHT - 30*AVERAGE_MULTIPLYER))
			self.screen.blit(gf.info_font.render(f'LEVEL - {gf.level}', False, (255, 255, 255)), (WIDTH-len(f'LEVEL - {gf.level}')*30, HEIGHT - 30*AVERAGE_MULTIPLYER))

		for obj in gf.additional_objects:
			self.screen.blit(obj.image, obj.rect)

	def update_event(self):
		pressed_keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mos_pos = pygame.mouse.get_pos()

				for obj in gf.additional_objects:
					if obj.rect.collidepoint(mos_pos):
						obj.action(gf)
						break

		if gf.in_game:
			if pressed_keys[pygame.K_DOWN]:
				gf.rocket.go_down()
			elif pressed_keys[pygame.K_UP]:
				gf.rocket.go_up()
			elif pressed_keys[pygame.K_RIGHT]:
				gf.rocket.go_right()
			elif pressed_keys[pygame.K_LEFT]:
				gf.rocket.go_left()
			else:
				if gf.rocket.move:
					gf.rocket.move = False
			if pressed_keys[pygame.K_SPACE]:
				if gf.attack_iteration >= gf.attack_speed:
					gf.attack_iteration = 0
					gf.self_bullets.append(objects.SelfBullet((gf.rocket.rect.x+ROCKET_SIZE[0], gf.rocket.rect.y+ROCKET_SIZE[1]//2)))
		else:
			if pressed_keys[pygame.K_1]:
				gf.begin_game()

	def load_state(self, gf):
		mx_score = 0
		try:
			with open('data_save.bin', 'rb') as f:
				mx_score = pickle.load(f)
				f.close()
		except: pass
		gf.max_score = mx_score





gf = GameFunctions.GameFunctions()

Main().main(gf)