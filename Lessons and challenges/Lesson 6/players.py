import random
import math
import time


class Player:
    types = ["warrior", "mage", "bandit"]

    def __init__(self, x, y, name, player_type, current_health, attack_speed):
        self.__coords = (x, y)
        self.__name = name
        if player_type.lower() in self.types:
            self.__player_type = player_type
        else:
            raise ValueError("Wrong input for types, there are 3 (warrior, mage, bandit")
        if player_type.lower() == "warrior":
            self.__max_health = 200
        elif player_type.lower() == "mage":
            self.__max_health = 100
        elif player_type.lower() == "bandit":
            self.__max_health = 150
        self.__current_health = self.__max_health * current_health / 100
        if player_type.lower() == "warrior":
            self.__damage = 30
        elif player_type.lower() == "mage":
            self.__damage = 25
        elif player_type.lower() == "bandit":
            self.__damage = 20
        self.__attack_speed = attack_speed

    def __str__(self):
        return f"Hero {self.__name} has {self.__current_health} health currently"

    def attack(self, other_player):
        if not self.is_attack_valid(other_player):
            print(f"{self.__name} missed!")
            return
        current_damage = self.__damage
        if self.__player_type == "warrior":
            if random.randint(1, 10) == 1:
                self.__current_health += 20
                print(f"{self.__name} healed for 20!")
        elif self.__player_type == "mage":
            if random.randint(1, 20) == 1:
                current_damage = current_damage * 2
                print(f"{self.__name} did a special attack!")
        if random.randint(1, 20) == 1:
            current_damage = current_damage * 1.5
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

    def attack_speed(self):
        return self.__attack_speed


def gameplay(player_1, player_2):
    start_time = time.time()
    while player_1.is_alive() and player_2.is_alive():
        if (time.time() - start_time) % player_1.attack_speed() == 0:
            player_1.attack(player_2)
            player_1.move(random.randint(0, 50), random.randint(0, 50))
        if (time.time() - start_time) % player_2.attack_speed() == 0:
            if player_2.is_alive():
                player_2.attack(player_1)
                player_2.move(random.randint(0, 50), random.randint(0, 50))
        print("\n")
        print(player_1)
        print(player_2)


Anton = Player(0, 0, "Anton", "warrior", 100, 2)
Petur = Player(20, 20, "Petur", "mage", 100, 1.5)
Misho = Player(40, 40, "Misho", "bandit", 100, 1)

# gameplay(Anton, Petur)
gameplay(Anton, Misho)
# gameplay(Petur, Misho)
