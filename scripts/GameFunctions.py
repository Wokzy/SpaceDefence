import pygame, images, math, random, pickle
from constants import *

from scripts import spaceship, objects, Enemy



class GameFunctions:
	def __init__(self):
		self.rocket = spaceship.SpaceShip()

		self.self_bullets = []
		self.enemy_bullets = []

		self.enemyes = []

		self.additional_objects = [objects.Button('start', images.get_start_button(), (WIDTH//2 - START_BUTTON_SIZE[0]//2, HEIGHT//2 - START_BUTTON_SIZE[1]//2))]
		self.background_objects = []
		self.init_background_objects()

		self.in_game = False

		self.level = 1
		self.adding_enemyes_speed = FPS*5 - self.level
		self.adding_enemyes_iteration = self.adding_enemyes_speed

		self.attack_speed = FPS*0.5
		self.attack_iteration = 0

		self.score = 0

		self.info_font = pygame.font.SysFont('Comic Sans MS', 25*AVERAGE_MULTIPLYER)
		self.max_score = 0

	def begin_game(self):
		self.in_game = True
		self.additional_objects = []

	def update_game(self):
		self.update_enemy()
		self.update_self_bullets()
		self.update_enemy_bullets()
		self.update_background_objects()
		self.update_complexity_level()

		self.add_enemyes()
		self.attack_iteration += 1

		if self.rocket.lives <= 0:
			self.stop_game()

	def update_background_objects(self):
		for obj in self.background_objects:
			obj.update()

	def update_enemy(self):
		remove_list = []
		for enemy in self.enemyes:
			enemy.update(self)
			if enemy.rect.colliderect(self.rocket.rect):
				self.rocket.lives -= 1
				enemy.alive = False
			if not enemy.alive:
				remove_list.append(enemy)
				continue

		for obj in remove_list:
			self.enemyes.remove(obj)

	def update_self_bullets(self):
		remove_list = []
		for bullet in self.self_bullets:
			bullet.update()
			if not bullet.alive:
				remove_list.append(bullet)

		for obj in remove_list:
			self.self_bullets.remove(obj)

	def update_enemy_bullets(self):
		remove_list = []
		for bullet in self.enemy_bullets:
			bullet.update(self)
			if bullet.rect.colliderect(self.rocket.rect):
				self.rocket.lives -= 1
				bullet.alive = False
			if not bullet.alive:
				remove_list.append(bullet)

		for obj in remove_list:
			self.enemy_bullets.remove(obj)

	def add_enemyes(self):
		if self.adding_enemyes_iteration >= self.adding_enemyes_speed:
			for i in range(random.randint(1, 2)):
				self.enemyes.append(Enemy.Alien(self.level))
			self.adding_enemyes_iteration = 0
		else: self.adding_enemyes_iteration += 1

	def stop_game(self):
		if self.score > self.max_score:
			self.save_state()
		self.__init__()

	def update_complexity_level(self):
		self.level = self.score//10 + 1
		if FPS*5 - self.level >= 0:
			self.adding_enemyes_speed = FPS*5 - self.level*FPS
			#print(self.adding_enemyes_speed)

	def init_background_objects(self):
		self.background_objects.append(objects.BackgroundObject(images.get_white_star(), WHITE_STAR_SIZE, (120*OBJECT_MULTIPLYER_WIDTH, 60*OBJECT_MULTIPLYER_HEIGHT), 4))
		self.background_objects.append(objects.BackgroundObject(images.get_pink_star(), PINK_STAR_SIZE, (160*OBJECT_MULTIPLYER_WIDTH, 290*OBJECT_MULTIPLYER_HEIGHT), 5))
		self.background_objects.append(objects.BackgroundObject(images.get_blue_planet(), BLUE_PLANET_SIZE, (70*OBJECT_MULTIPLYER_WIDTH, 280*OBJECT_MULTIPLYER_HEIGHT), 2))
		self.background_objects.append(objects.BackgroundObject(images.get_simple_purple_planet(), SIMPLE_PURPLE_PLANET_SIZE, (320*OBJECT_MULTIPLYER_WIDTH, 10*OBJECT_MULTIPLYER_HEIGHT), 3))
		self.background_objects.append(objects.BackgroundObject(images.get_diff_colours_planet(), DIFF_COLOURS_PLANET_SIZE, (510*OBJECT_MULTIPLYER_WIDTH, 50*OBJECT_MULTIPLYER_HEIGHT), 2))
		self.background_objects.append(objects.BackgroundObject(images.get_orange_planet(), ORANGE_PLANET_SIZE, (40*OBJECT_MULTIPLYER_WIDTH, 210*OBJECT_MULTIPLYER_HEIGHT), 2))
		self.background_objects.append(objects.BackgroundObject(images.get_earth(), EARTH_SIZE, (290*OBJECT_MULTIPLYER_WIDTH, 110*OBJECT_MULTIPLYER_HEIGHT), 1))
		self.background_objects.append(objects.BackgroundObject(images.get_bright_blue_star(), BRIGHT_BLUE_STAR_SIZE, (0*OBJECT_MULTIPLYER_WIDTH, 150*OBJECT_MULTIPLYER_HEIGHT), 3))

	def save_state(self):
		with open('data_save.bin', 'wb') as f:
			pickle.dump(self.score, f)
			f.close()