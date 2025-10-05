#!/usr/bin/env python3
from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room
def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
  }
    

    one_exict = describe_current_room(game_state)
    print(one_exict)

    while True:
        command_player = input("\nВведите команду: ").strip().lower()

        return     


if __name__ == "__main__":
    main()