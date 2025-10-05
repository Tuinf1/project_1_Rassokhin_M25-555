#  для функций, связанных с действиями игрока.

# from labyrinth_game.main import game_state
from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


def show_inventory(game_state):
    player_inventory = game_state['player_inventory']

    if not player_inventory:
        print('Инвентарь игрока пуст')
    else:
        print('В инвентаре:', ', '.join(player_inventory))
# 

def get_input(prompt="> "):
    try:
        
        z = None
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 

# Функция перемещения 2
def move_player(game_state, direction: str):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

     # Проверяем, есть ли выход в указанном направлении
    if direction in room_data.get('exits', {}):
        # Меняем текущую комнату
        new_room = room_data['exits'][direction]
        game_state['current_room'] = new_room
        game_state['steps_taken'] += 1

        random_event(game_state)
        # Показываем описание новой комнаты
        describe_current_room(game_state)

    else:
        print("Нельзя пойти в этом направлении.")
    
# Функция взятия предмета 3
def take_item(game_state, item_name):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room] 
    room_items = room_data.get('items', [])
    if item_name in room_items:
        # Добавляем предмет в инвентарь игрока
        game_state['player_inventory'].append(item_name)
        # Убираем предмет из комнаты
        room_items.remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

# def use_item(game_state, item_name):
#     inventory = game_state.get('player_inventory', [])

#     if item_name not in inventory:
#         print("У вас нет такого предмета.")
#         return

#     match item_name:
#         case 'torch':
#             print("Вы зажгли факел. Стало светлее вокруг.")
#         case 'sword':
#             print("Вы берёте меч в руки. Вы чувствуете уверенность.")
#         case 'bronze box':
#             print("Вы открыли бронзовую шкатулку.")
#             if 'rusty key' not in inventory:
#                 inventory.append('rusty key')
#                 print("Внутри вы нашли rusty key и положили его в инвентарь.")
#             else:
#                 print("Шкатулка пуста.")
#         case _:
#             print(f"Вы не знаете, как использовать {item_name}.")


