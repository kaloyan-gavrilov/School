import random
import math


class Player:
    types = ["warrior", "mage", "bandit"]

    def __init__(self, x, y, name, player_type, health, current_health, damage):
        self.__coords = (x, y)
        self.__name = name
        if player_type.lower() in self.types:
            self.__player_type = player_type
        else:
            raise ValueError("Wrong input for types, there are 3 (warrior, mage, bandit")
        self.__max_health = health
        self.__current_health = health * current_health / 100
        self.__damage = damage

    def __str__(self):
        return f"Hero {self.__name} has {self.__current_health} health currently"

    def attack(self, other_player):
        if not self.is_attack_valid(other_player):
            print(f"{self.__name} missed!")
            return
        crit_chance = random.randint(1, 10)
        current_damage = self.__damage
        if self.__player_type == "warrior":
            current_damage *= 1.5
        elif self.__player_type == "mage":
            if random.randint(1, 20) == 1:
                current_damage = current_damage * 2
                print(f"{self.__name} did a special attack!")
        if crit_chance == 1:
            current_damage = current_damage * 3
        other_player.take_damage(current_damage)

    def take_damage(self, damage):
        if self.__player_type == "bandit":
            if random.randint(1, 10) == 1:
                print(f"{self.__name} missed a hit :)")
                return
        self.__current_health -= damage
        print(f"{self.__name} is damaged by {damage}")
        if self.__current_health <= 0:
            self.__current_health = 0
            print(f"Hero {self.__name} died GG")

    def is_alive(self):
        return self.__current_health > 0

    def move(self, x, y):
        if x <= 50 and y <= 50:
            self.__coords = (x, y)
        else:
            raise ValueError("The map is 50 by 50. Enter correct coordinates!")

    def distance_to(self, other):
        x1, y1 = self.__coords
        x2, y2 = other.__coords
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def is_attack_valid(self, other):
        if self.is_alive():
            return True
        elif not self.is_alive():
            return False
        if self.__player_type == "warrior":
            if self.distance_to(other) <= 5:
                return True
            else:
                return False
        if self.__player_type == "mage":
            if self.distance_to(other) <= 20:
                return True
            else:
                return False
        if self.__player_type == "bandit":
            if self.distance_to(other) <= 3:
                return True
            else:
                return False


def gameplay(player_1, player_2):
    while player_1.is_alive() and player_2.is_alive():
        if random.randint(1, 2) == 1:
            player_1.attack(player_2)
            if not player_2.is_alive():
                break
            player_1.move(random.randint(0, 50), random.randint(0, 50))
        else:
            player_2.attack(player_1)
            if not player_1.is_alive():
                break
            player_2.move(random.randint(0, 50), random.randint(0, 50))

        print("\n")
        print(player_1)
        print(player_2)


Anton = Player(0, 0, "Anton", "warrior", 150, 100, 10)
Petur = Player(20, 20, "Petur", "mage", 100, 100, 10)
Misho = Player(40, 40, "Misho", "bandit", 120, 100, 10)

# gameplay(Anton, Petur)
gameplay(Anton, Misho)
# gameplay(Petur, Misho)