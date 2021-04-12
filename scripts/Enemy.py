import images, random
from constants import *
from scripts import objects


class Alien:
	def __init__(self, level):
		self.image = images.get_alien()

		self.rect = self.image.get_rect()

		self.rect.x = WIDTH - ALIEN_SIZE[0] - random.randint(0, 80*OBJECT_MULTIPLYER_WIDTH)
		self.rect.y = random.randint(0, HEIGHT-ALIEN_SIZE[1])

		self.shoot_speed = FPS * (2-(0.3*level))
		self.shoot_iteration = 0

		self.alive = True

	def update(self, gf):
		for bullet in gf.self_bullets:
			if bullet.rect.colliderect(self.rect):
				self.alive = False
				bullet.alive = False
				gf.score += 1
				return

		if self.shoot_iteration >= self.shoot_speed:
			self.shoot(gf)
			self.shoot_iteration = 0
		else: self.shoot_iteration += 1

		self.move(gf)

	def move(self, gf):
		if self.rect.x <= 0:
			self.alive = False
			return

		self.rect.x -= 2

		mv = random.randint(-2*gf.level, 2*gf.level)
		if mv < 0 and self.rect.y - mv >= 0:
			self.rect.y += mv
		elif mv >= 0 and self.rect.y + mv <= HEIGHT-ALIEN_SIZE[1]:
			self.rect.y += mv

	def shoot(self, gf):
		gf.enemy_bullets.append(objects.EnemyBullet((self.rect.x, self.rect.y + ALIEN_SIZE[1]//2)))