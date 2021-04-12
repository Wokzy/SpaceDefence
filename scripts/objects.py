import images
from constants import *



class Button:
	def __init__(self, name, image, position):
		self.name = name
		self.image = image

		self.rect = self.image.get_rect()

		self.rect.x = position[0]
		self.rect.y = position[1]

	def action(self, gf):
		if self.name == 'start':
			gf.begin_game()


class EnemyBullet:
	def __init__(self, position):
		self.image = images.get_red_bullet()

		self.rect = self.image.get_rect()

		self.rect.x = position[0]
		self.rect.y = position[1]

		self.alive = True

	def update(self, gf):
		if self.rect.x <= 0:
			self.alive = False
			return
		self.rect.x -= gf.level*12


class SelfBullet:
	def __init__(self, position):
		self.image = images.get_yellow_bullet()

		self.rect = self.image.get_rect()

		self.rect.x = position[0]
		self.rect.y = position[1]

		self.alive = True

	def update(self):
		if self.rect.x >= WIDTH:
			self.alive = False
			return
		self.rect.x += 12


class BackgroundObject:
	def __init__(self, image, size, position, speed):
		self.image = image
		self.rect = self.image.get_rect()
		self.size = size

		self.rect.x = position[0]
		self.rect.y = position[1]

		self.speed = speed*AVERAGE_MULTIPLYER # In pixels

	def update(self):
		if self.rect.x >= WIDTH:
			self.rect.x = - self.size[0]
			return

		self.rect.x += self.speed