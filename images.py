import pygame
from constants import *


def get_rocket():
	global ROCKET_IMAGES
	return ROCKET_IMAGES

def get_alien():
	global ALIEN
	return ALIEN

def get_yellow_bullet():
	global YELLOW_BULLET
	return YELLOW_BULLET

def get_red_bullet():
	global RED_BULLET
	return RED_BULLET

def get_start_button():
	global START_BUTTON
	return START_BUTTON

def get_heart():
	global HEART
	return HEART

def get_white_star():
	global WHITE_STAR
	return WHITE_STAR

def get_pink_star():
	global PINK_STAR
	return PINK_STAR

def get_blue_planet():
	global BLUE_PLANET
	return BLUE_PLANET

def get_simple_purple_planet():
	global SIMPLE_PURPLE_PLANET
	return SIMPLE_PURPLE_PLANET

def get_diff_colours_planet():
	global DIFF_COLOURS_PLANET
	return DIFF_COLOURS_PLANET

def get_orange_planet():
	global ORANGE_PLANET
	return ORANGE_PLANET

def get_earth():
	global EARTH
	return EARTH

def get_bright_blue_star():
	global BRIGHT_BLUE_STAR
	return BRIGHT_BLUE_STAR


def init():
	global ROCKET_IMAGES, ALIEN, YELLOW_BULLET, RED_BULLET, START_BUTTON, ALIEN, HEART, WHITE_STAR, PINK_STAR, BLUE_PLANET, SIMPLE_PURPLE_PLANET, DIFF_COLOURS_PLANET
	global ORANGE_PLANET, EARTH, BRIGHT_BLUE_STAR

	ROCKET_IMAGES = {"stay_image":pygame.transform.scale(pygame.image.load('sprites/rocket_stay.png'), ROCKET_SIZE), "move_image":pygame.transform.scale(pygame.image.load('sprites/rocket_move.png'), ROCKET_SIZE)}
	ALIEN = pygame.transform.scale(pygame.image.load('sprites/alien.png'), ALIEN_SIZE)
	YELLOW_BULLET = pygame.transform.scale(pygame.image.load('sprites/shot.png'), SHOT_SIZE)
	RED_BULLET = pygame.transform.scale(pygame.image.load('sprites/shot_red.png'), SHOT_SIZE)
	START_BUTTON = pygame.transform.scale(pygame.image.load('sprites/start_button.png'), START_BUTTON_SIZE)
	HEART = pygame.transform.scale(pygame.image.load('sprites/heart.png'), HEART_SIZE)

	WHITE_STAR = pygame.transform.scale(pygame.image.load('sprites/background_objects/white_star.png'), WHITE_STAR_SIZE)
	PINK_STAR = pygame.transform.scale(pygame.image.load('sprites/background_objects/pink_star.png'), PINK_STAR_SIZE)
	BLUE_PLANET = pygame.transform.scale(pygame.image.load('sprites/background_objects/Blue_planet.png'), BLUE_PLANET_SIZE)
	SIMPLE_PURPLE_PLANET = pygame.transform.scale(pygame.image.load('sprites/background_objects/simple_purple_planet.png'), SIMPLE_PURPLE_PLANET_SIZE)
	DIFF_COLOURS_PLANET = pygame.transform.scale(pygame.image.load('sprites/background_objects/diff_colours_planet.png'), DIFF_COLOURS_PLANET_SIZE)
	ORANGE_PLANET = pygame.transform.scale(pygame.image.load('sprites/background_objects/orange_planet.png'), ORANGE_PLANET_SIZE)
	EARTH = pygame.transform.scale(pygame.image.load('sprites/background_objects/Earth.png'), EARTH_SIZE)
	BRIGHT_BLUE_STAR = pygame.transform.scale(pygame.image.load('sprites/background_objects/bright_blue_star.png'), BRIGHT_BLUE_STAR_SIZE)

init()