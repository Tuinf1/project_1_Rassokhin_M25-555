#  для вспомогательных функций.
from labyrinth_game.constants import ROOMS

def describe_current_room(game_state):
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    print(f"\n== {room_name.upper()} ==")
    print(room['description'])

    # предметы
    if room.get('items'):
        print("Заметные предметы:", ", ".join(room['items']))

    # выходы
    exits = ", ".join(room['exits'].keys()) if room.get('exits') else "нет"
    print("Выходы:", exits)

    # загадка
    puzzle = room.get('puzzle')
    if puzzle and puzzle[0]:
        print("Кажется, здесь есть загадка (используйте команду solve).")

def solve_puzzle(game_state):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room] 
    room_puzzle = room_data.get('puzzle')
    if  room_puzzle is not None:
        # Добавляем предмет в инвентарь игрока
        question, answer = room_puzzle
        user_answer = input(f"{question}\nВаш ответ: ").strip().lower()
        if user_answer == answer.lower():
            print("Правильно! Загадка решена.")
            room_data['puzzle'] = None  
            reward = 'награда 1'
            if reward not in game_state['player_inventory']:
                game_state['player_inventory'].append(reward)
                print(f"Вы получили награду: {reward}")
            else:
                print(f"Награда {reward} уже есть в инвентаре.")
        else:
            print("Неправильный ответ. Попробуйте снова.")
    else:
        return print("Загадки здесь нет.")



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

    question, correct_code = room_puzzle
    user_code = input(f"{question}\nВведите код: ").strip()
    if user_code == correct_code:
        print("Код верный! Сундук открыт!")
        room_items.remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        print("Неверный код. Сундук остаётся закрытым.")