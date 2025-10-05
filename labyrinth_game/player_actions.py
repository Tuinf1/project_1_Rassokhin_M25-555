#  для функций, связанных с действиями игрока.

# from labyrinth_game.main import game_state
from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room


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

def use_item(game_state, item_name):
    inventory = game_state.get('player_inventory', [])

    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    match item_name:
        case 'torch':
            print("Вы зажгли факел. Стало светлее вокруг.")
        case 'sword':
            print("Вы берёте меч в руки. Вы чувствуете уверенность.")
        case 'bronze box':
            print("Вы открыли бронзовую шкатулку.")
            if 'rusty key' not in inventory:
                inventory.append('rusty key')
                print("Внутри вы нашли rusty key и положили его в инвентарь.")
            else:
                print("Шкатулка пуста.")
        case _:
            print(f"Вы не знаете, как использовать {item_name}.")


def attempt_open_treasure(game_state):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    room_items = room_data.get('items', [])

    # 1️⃣ Проверка наличия сундука
    if 'treasure_chest' not in room_items:
        print("Сундук уже открыт или отсутствует.")
        return

    # 2️⃣ Проверка ключей
    inventory = game_state.get('player_inventory', [])
    if 'treasure_key' in inventory or 'rusty_key' in inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room_items.remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
        return

    # 3️⃣ Предложение ввести код
    use_code = input("Сундук заперт. У вас нет ключа. Хотите попробовать ввести код? (да/нет) ").strip().lower()
    if use_code != 'да':
        print("Вы отступаете от сундука.")
        return

    # 4️⃣ Ввод и проверка кода
    room_puzzle = room_data.get('puzzle')
    if room_puzzle is None:
        print("Код неизвестен. Сундук остаётся закрытым.")
        return

    question, correct_code = room_puzzle
    user_code = input(f"{question}\nВведите код: ").strip()
    if user_code == correct_code:
        print("Код верный! Сундук открыт!")
        room_items.remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        print("Неверный код. Сундук остаётся закрытым.")