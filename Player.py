#player health and energy
class Player:
    def __init__(self, health, tenergy):
        self.health = health
        self.tenergy = tenergy

    #getters and setters
    def get_health(self):
        return self.health

    def get_tenergy(self):
        return self.tenergy

    def damage(self, attack):
        self.health -= attack

    def heal(self, healing):
        self.health += healing

    def change_tenergy(self, tchange):
        self.tenergy += tchange

