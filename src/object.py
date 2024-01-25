import pygame
import math
# from config import WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_SIZE, FONT, SCALE
from config import *

class Object:
    def __init__(self, x, y, radius, color, mass, sun=False, x_vel=0, y_vel=0, spawned=False, *args, **kwargs):
        if spawned:
            self.x = (x - (WINDOW_WIDTH / 2)) / SCALE
            self.y = (y - (WINDOW_HEIGHT / 2)) / SCALE
        else:
            self.x = x * AU
            self.y = y * AU
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit= []
        self.sun = sun 
        self.distance_to_sun = 0

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.hovered = False
        self.selected = False
        self.spawned = spawned
        self.calculate_draw_pos()

    def calculate_draw_pos(self):
        self.x_draw = self.x * SCALE + WINDOW_WIDTH / 2
        self.y_draw = self.y * SCALE + WINDOW_HEIGHT / 2

    def draw(self, window, font=None, draw_lines=False, render_distance_text=False):
        self.calculate_draw_pos()
        pygame.draw.circle(window, self.color, (self.x_draw, self.y_draw), self.radius)
        if len(self.orbit) > 2 and draw_lines:
            updated_points = []

            for point in self.orbit:
                self.x_draw, self.y_draw = point
                self.x_draw = self.x_draw * SCALE + WINDOW_WIDTH / 2
                self.y_draw = self.y_draw * SCALE + WINDOW_HEIGHT / 2
                updated_points.append((self.x_draw, self.y_draw))

            pygame.draw.lines(window, self.color, False, updated_points, 2)

        if not self.sun and render_distance_text:
            distance_text = font.render(f"{self.distance_to_sun/1000:.0f}km", 0.5, 'white')
            window.blit(distance_text, (self.x_draw - distance_text.get_width() / 2, self.y_draw - distance_text.get_width()/2))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y

        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)

        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets, timestep=3600, line_length=100):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * timestep
        self.y_vel += total_fy / self.mass * timestep

        self.x += self.x_vel * timestep
        self.y += self.y_vel * timestep
        self.orbit.append((self.x, self.y))
        if len(self.orbit) >= line_length:
            self.orbit = self.orbit[-line_length:]