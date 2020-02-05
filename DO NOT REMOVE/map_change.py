class MapChange:
    def __init__(self, game, Map):
        self.game = game

    def inner_house1(self):
        self.game.map = self.game.map2
        self.game.map_img = self.game.map_img2
        self.game.map_rect = self.game.map2_rect
        self.game.new()

    def outside_town1(self):
        self.game.map = self.game.map1
        self.game.map_img = self.game.map_img1
        self.game.map_rect = self.game.map1_rect
        self.game.new()


    def inner_house2(self):
        self.game.map = self.game.map3
        self.game.map_img = self.game.map_img3
        self.game.map_rect = self.game.map3_rect
        self.game.new()
