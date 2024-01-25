import sys
import pygame

from config import *
from src.object import Object
from datetime import datetime, timedelta

class GUI:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Planet Simulation")

        self.font = pygame.font.SysFont("consolas", 16)
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.init_objects()
        self.select = None
        self.line_length = 10000
        self.timestep = ONE_YEAR / FPS
        self.elapsed_time = 0
        self.simulate = True
        self.temp_object_position = None
        
        self.lines_toggle = True
        self.distance_text_toggle = False
        # self.zoom_slider = Slider(self.window, WINDOW_WIDTH - 20, 20, 10, 100, min=1, max=200, step=1, handleColour=(255, 255, 255))
        
    def init_objects(self):
        self.objects = [Object(**obj) for obj in list(PLANETS.values()) + [SUN]]

    def calculate_time(self):
        sec = timedelta(seconds=self.elapsed_time)
        d = datetime(1,1,1) + sec

        format_text = self.font.render(f"yyyy:mm:dd:hh:mm:ss", 0.5, 'white')
        elapsed_text = self.font.render(f"{d.year-1:04d}:{d.month-1:02d}:{d.day-1:02d}:{d.hour:02d}:{d.minute:02d}:{d.second:02d}", 0.5, 'white')
        
        self.window.blit(format_text, (100, 80))
        self.window.blit(elapsed_text, (100, 100))

    def reset_orbits(self):
        for planet in self.objects:
            planet.orbit = []
            
    def show_fps(self):
        fps_text = self.font.render(f'{self.clock.get_fps():.2f}', 1, 'white')
        
        self.window.blit(fps_text, (720, 10))

    def run_simulation(self):
            for planet in self.objects:
                if self.simulate:
                    planet.update_position(self.objects, timestep=self.timestep, line_length=self.line_length)
                planet.draw(
                    self.window, 
                    draw_lines=self.lines_toggle, 
                    render_distance_text=self.distance_text_toggle, 
                    font=self.font
                )
                
    def spawn_object(self, location, mouse):
        t_x, t_y = location
        m_x, m_y = mouse
        vel_x = (m_x - t_x) / VEL_SCALE / SCALE
        vel_y = (m_y - t_y) / VEL_SCALE / SCALE
        obj = Object(
            t_x, 
            t_y, 
            3, 
            'white', 
            5.9742 * 10**22, 
            x_vel=vel_x, 
            y_vel=vel_y, 
            spawned=True
        )
        
        return obj, t_x, t_y

    def run(self):
        frame = 0
        while True:
            frame += 1
            self.clock.tick(FPS)
            self.window.fill('black')
            self.calculate_time()
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.lines_toggle = not self.lines_toggle
                        self.reset_orbits()
                    
                    if event.key == pygame.K_t:
                        self.distance_text_toggle = not self.distance_text_toggle

                    if event.key == pygame.K_SPACE:
                        self.simulate = not self.simulate
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.temp_object_position:
                        obj, t_x, t_y = self.spawn_object(self.temp_object_position, mouse_pos)
                        self.objects.append(obj)
                        self.temp_object_position = None
                    else:
                        self.temp_object_position = mouse_pos
            if self.temp_object_position:
                pygame.draw.line(self.window, 'white', self.temp_object_position, mouse_pos, 2)
                pygame.draw.circle(self.window, 'red', self.temp_object_position, 5)
            self.run_simulation()
            # print(self.zoom_slider.getValue())
            if self.simulate:
                self.elapsed_time += self.timestep
            
            if frame % FPS == 0:
                print(f'{self.elapsed_time / ONE_DAY} days in real time')
            # pygame_widgets.update(events)
            self.show_fps()
            pygame.display.update()

