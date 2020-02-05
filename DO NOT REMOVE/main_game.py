import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from map_change import *
import time
import math
import random
from pygame_functions import *



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font("arial")
        self.load_data()
        self.i = 0
        self.doorlist = []
        self.doortype = []
        self.IDList = []
        self.status = "start"
        self.newplayer = True
        self.text_true = False
        self.newpos = []
        self.health = 100
        self.magic = 100
        self.MapChange = MapChange(self, "town")

    def load_data(self):
        self.maps = ['Pygame_Map.tmx']
        self.game_folder = path.dirname(__file__)
        self.img_folder = path.join(self.game_folder, 'img')
        self.map_folder = path.join(self.game_folder, 'maps')
        self.sound_folder = path.join(self.game_folder, 'sounds')

##        pg.mixer.music.load("town_music1.wav")
##        pg.mixer.music.play(-1)

        self.map = TiledMap(path.join(self.map_folder, 'New_World.tmx'))
        self.map1 = TiledMap(path.join(self.map_folder, 'New_World.tmx'))
        self.map2 = TiledMap(path.join(self.map_folder, 'Inner_House1.tmx'))
        self.map3 = TiledMap(path.join(self.map_folder, 'Inner_House2.tmx'))

        self.map_img = self.map.make_map()
        self.map_img1 = self.map1.make_map()
        self.map_img2 = self.map2.make_map()
        self.map_img3 = self.map3.make_map()
        self.map_rect = self.map_img.get_rect()
        self.map1_rect = self.map_img1.get_rect()
        self.map2_rect = self.map_img2.get_rect()
        self.map3_rect = self.map_img3.get_rect()
        self.player_img = pg.image.load(path.join(self.img_folder, PLAYER_IMG4[0])).convert_alpha()
        self.npc_image = pg.image.load(path.join(self.img_folder, NPC_IMAGE1)).convert_alpha()
        self.wall_img = pg.image.load(path.join(self.img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        self.newpos = []
        self.doorlist = []
        self.doortype = []
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.doors = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.npc = pg.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                if self.newplayer == True:
                    self.player = Player(self, tile_object.x, tile_object.y, self.health, self.magic)
                    self.newplayer = False
                else:
                    self.player = Player(self, self.player.pos[0], self.player.pos[1], self.player.health, self.player.magic)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name == 'door':
                door = Door(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tile_object.name, tile_object.type)
                self.doorlist.append(door)
                self.doortype.append(tile_object.type)
            if tile_object.name == 'npc':
                NPC(self, tile_object.x, tile_object.y,tile_object.width, tile_object.height, tile_object.type)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False

    def run(self):
        self.playing = True
        while self.playing:
            self.vLocation = self.check_location()
            if self.vLocation:
                if self.vLocation.type == "inner_house1":
                    self.backtrack = self.vLocation
                    pg.mixer.music.load("close_door.wav")
                    pg.mixer.music.play(0)
                    time.sleep(0.5)
                    self.newplayer = True
                    self.MapChange.inner_house1()
                    self.new()
                    time.sleep(0.5)
                    
                    
                elif self.vLocation.type == "inner_house2":
                    self.backtrack = self.vLocation
                    pg.mixer.music.load("close_door.wav")
                    pg.mixer.music.play(0)
                    time.sleep(0.5)
                    self.newplayer = True
                    self.MapChange.inner_house2()
                    self.new()
                    time.sleep(0.5)
                    
                elif self.vLocation.type == "outside_town1":
                    print(self.backtrack.type)
                    pg.mixer.music.load("close_door.wav")
                    pg.mixer.music.play(0)
                    time.sleep(0.5)
                    self.newplayer = True
                    self.MapChange.outside_town1()
                    self.new()
                    self.player.pos = (self.backtrack.x + 0.5*(self.backtrack.w), self.backtrack.y+75)
                    pg.mixer.music.load("town_music1.wav")
                    pg.mixer.music.play(-1)
                    time.sleep(0.5)
                    
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.player.interact(self.player, self.npc)


            self.draw()

    def move_player(self, player, x, y):
        player.pos = vec(x, y)

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill((BLACK))
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.npc:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
##        if self.text_true == True:
##            self.draw_text(self.screen, "0", 18 , self.npc1.x, (self.npc1.y - 100))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    print(self.player.pos)
                if event.key == pg.K_SPACE:
                    if self.check_npc_close():
                        print(self.check_npc_close().name)
                        self.talk(self.check_npc_close())
                if event.key == pg.K_F1:
                    self.MapChange.brooktown()
                if event.key == pg.K_F2:
                    self.MapChange.house1()
                    #print(self.doorlist)

    def check_location(self):
        for i in self.doorlist:
            if math.sqrt((i.x - self.player.pos[0])**2 + (i.y - self.player.pos[1])**2) < 30:
                return i


    def check_npc_close(self):
        for i in self.npc:
            if math.sqrt((i.x - self.player.pos[0])**2 + (i.y - self.player.pos[1])**2) < 30:
                    return(i)

            
    def talk(self, npc):
        self.npc_obj = npc
        if self.npc_obj.name == "blacksmith":
            instructLabel = makeLabel(random.choice(self.npc_obj.text[0]), 40, 10, 10, "blue", "Agency FB", "yellow")
            showLabel(instructLabel)
            

            
##        print(random.choice(self.npc_obj.text))
    
        

    
    def draw_text(self, surf, text, size, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()








