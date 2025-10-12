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
        None
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 

# Функция перемещения 2
def move_player(game_state, direction: str):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

     # Проверяем, есть ли выход в указанном направлении
    

        # # Меняем текущую комнату
        # 
        # game_state['current_room'] = new_room
        # game_state['steps_taken'] += 1

        # random_event(game_state)
        # # Показываем описание новой комнаты
        # describe_current_room(game_state)

    if direction not in room_data.get('exits', {}):
        print("Нельзя пойти в этом направлении.")
        return
        
    next_room = room_data['exits'][direction]
    # 🔒 Проверка: если это комната сокровищ
    if next_room == 'treasure_room':
        if 'rusty_key' in game_state['player_inventory']:
            print("\nВы используете найденный ключ, " \
            "чтобы открыть путь в комнату сокровищ.")
            game_state['current_room'] = next_room
            game_state['steps_taken'] += 1

            # Описание новой комнаты
            describe_current_room(game_state)

            # 🎲 Проверка случайных событий
            random_event(game_state)
            return
        else:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
            return  # остаёмся в текущей комнате

    
    
    game_state['current_room'] = next_room
    game_state['steps_taken'] += 1

    # Описание новой комнаты
    describe_current_room(game_state)

    # 🎲 Проверка случайных событий
    random_event(game_state)

    

# Функция взятия предмета 3
def take_item(game_state, item_name):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room] 
    room_items = room_data.get('items', [])

    if item_name in room_items:
        # Добавляем предмет в инвентарь игрока
        if item_name == 'treasure_chest':
            print('Игрок ленивый и слабый, поэтому не может поднять этот предмет')
            return
        game_state['player_inventory'].append(item_name)
        # Убираем предмет из комнаты
        room_items.remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


