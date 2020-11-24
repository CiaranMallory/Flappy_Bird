import pygame
import random2

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((500, 750))

# Bird parameters
BIRD_COLOR = (52, 177, 235)
bird_x = 50
bird_y = 300
bird_height_change = 0

# Obstacle parameters
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random2.randint(150, 450)
OBSTACLE_COLOR = (209, 60, 44)
OBSTACLE_X_CHANGE = -4
OBSTACLE_X = 500

def draw_bird(x,y):
	pygame.draw.circle(SCREEN, BIRD_COLOR, (bird_x, bird_y), 64)

def boundary_handling(bird_y):
	if bird_y <= 0:
		bird_y = 0
	if bird_y >= 750:
		bird_y = 750
	return bird_y

def draw_obstacle(height):
	pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (OBSTACLE_X, 0, OBSTACLE_WIDTH, height))
	bottom_obstacle_height = 750 - height - 200
	pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (OBSTACLE_X, 750, OBSTACLE_WIDTH, -bottom_obstacle_height))

def collision_detection(OBSTACLE_X, OBSTACLE_HEIGHT, bird_y, bottom_obstacle_height):
	if OBSTACLE_X >= 50 and OBSTACLE_X <= (50 + 64):
		if bird_y <= OBSTACLE_HEIGHT or bird_y >= (bottom_obstacle_height - 64):
			return True
	return False


run = True
while run:

	SCREEN.fill((255,255,255))

	# Checking for key presses
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_height_change = -6

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				bird_height_change = 3


	bird_y += bird_height_change

	bird_y = boundary_handling(bird_y)

	OBSTACLE_X += OBSTACLE_X_CHANGE
	if OBSTACLE_X <= -10:
		OBSTACLE_X = 500
		OBSTACLE_HEIGHT = random2.randint(200,400)
	draw_obstacle(OBSTACLE_HEIGHT)

	collision = collision_detection(OBSTACLE_X, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 200)

	if collision:
		pygame.quit()

	draw_bird(bird_x, bird_y)

	clock.tick(30)

	pygame.display.update()

pygame.quit()