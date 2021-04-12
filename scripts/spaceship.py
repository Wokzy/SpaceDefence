import pygame, images
from constants import *


class SpaceShip:
	def __init__(self):
		self.images = images.get_rocket()
		self.image = self.images['stay_image']
		self.size = ROCKET_SIZE

		self.rect = self.image.get_rect()
		self.rect.x = 20*OBJECT_MULTIPLYER_WIDTH
		self.rect.y = 120*OBJECT_MULTIPLYER_HEIGHT

		self.alive = True

		self.horizontal_speed = 10
		self.vertical_speed = 7
		self.move = False

		self.lives = 5

	def update(self):
		if self.move and not self.image == self.images['move_image']:
			self.image = self.images['move_image']
		if not self.move and not self.image == self.images['stay_image']:
			self.image = self.images['stay_image']

	def go_left(self):
		if self.rect.x - self.horizontal_speed >= 0:
			self.rect.x -= self.horizontal_speed
			self.move = True

	def go_right(self):
		if self.rect.x + self.horizontal_speed + self.size[0] <= WIDTH:
			self.rect.x += self.horizontal_speed
			self.move = True

	def go_down(self):
		if self.rect.y + self.vertical_speed + self.size[1] <= HEIGHT:
			self.rect.y += self.vertical_speed
			self.move = True

	def go_up(self):
		if self.rect.y - self.vertical_speed >= 0:
			self.rect.y -= self.vertical_speed
			self.move = True