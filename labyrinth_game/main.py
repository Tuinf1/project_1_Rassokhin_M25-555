#!/usr/bin/env python3
from labyrinth_game.constants import COMMANDS
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)


def main():

    """Основной цикл игры: инициализирует состояние,
      описывает комнату и обрабатывает команды игрока."""

    print("Добро пожаловать в Лабиринт сокровищ!")

    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
    }
    
    def process_command(game_state, command):
        """Обрабатывает введённую игроком команду, 
        изменяя состояние игры в зависимости от действия."""


        parts = command.strip().lower().split(maxsplit=1)
        action = parts[0] 
        arg = parts[1] if len(parts) > 1 else action
        # print(arg)
        # print(action)
        # directions = ['north', 'south', 'east', 'west']

        match action:
            case 'help':
                show_help(COMMANDS)
            case 'look' | 'осмотреться':
                describe_current_room(game_state)

            case 'inventory' | 'инвентарь':
                show_inventory(game_state)

            case 'go' | 'north' | 'south' | 'east' | 'west':
                if arg:
                    move_player(game_state, arg)
                else:
                    print("Укажите направление через пробел 'go..':" \
                    " north, south, east, west")

            case 'take' | 'взять':
                if arg:
                    take_item(game_state, arg)
                else:
                    print("Укажите предмет, который хотите взять")

            case 'solve':
                if game_state['current_room'] == 'treasure_room':
                    attempt_open_treasure(game_state)
                else:
                    solve_puzzle(game_state)
            case 'use':
                if arg == 'treasure_chest' and game_state['current_' \
                'room'] == 'treasure_room':
                    attempt_open_treasure(game_state)
                else:
                    print("У вас нет нужного предмета для treasure_room.")



            case 'quit':
                print("Вы покидаете лабиринт.")
                game_state['game_over'] = True

            case _:
                print("Неизвестная команда. Доступные: look, go, take, inventory, quit")



    describe_current_room(game_state)

    while not game_state['game_over']:
        command_player = get_input("\nВведите команду: ")
        process_command(game_state, command_player)
    

if __name__ == "__main__":
    main()