#  для вспомогательных функций.
import math
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
        
        alternatives = {
        '10': ['10', 'десять']
       # можно расширить
    }
        user_answer = input(f"{question}\nВаш ответ: ").strip().lower()
        valid_answers = alternatives.get(answer.lower(), [answer.lower()])

        # # удалить
        # print(valid_answers)


        if user_answer in valid_answers:
            print("Правильно! Загадка решена.")
            room_data['puzzle'] = None  # 

            if current_room == 'hall':
                reward = 'treasure_key'
            elif current_room == 'library':
                reward = 'rusty_key'
            else:
                reward = 'кинжал'
            
            if reward not in game_state['player_inventory']:
                game_state['player_inventory'].append(reward)
                print(f"Вы получили награду: {reward}")
            else:
                print(f"Награда {reward} уже есть в инвентаре.")
        else:
            print("Неправильный ответ. Попробуйте снова.")
            if current_room == 'trap_room':
                trigger_trap(game_state)
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
    if 'treasure_key' in inventory:
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

# def show_help():
#     print("\nДоступные команды:")
#     print("  go <direction>  - перейти в направлении (north/south/east/west)")
#     print("  look            - осмотреть текущую комнату")
#     print("  take <item>     - поднять предмет")
#     print("  use <item>      - использовать предмет из инвентаря")
#     print("  inventory       - показать инвентарь")
#     print("  solve           - попытаться решить загадку в комнате")
#     print("  quit            - выйти из игры")
#     print("  help            - показать это сообщение") 


def show_help(commands):
    print("\nСписок доступных команд:")
    for cmd, desc in commands.items():
        print(f"{cmd:<16} — {desc}")



def pseudo_random(seed: int, modulo: int) -> int:
    """
    Генератор псевдослучайных чисел на основе синуса.
    Возвращает целое число в диапазоне [0, modulo).
    """
    x = math.sin(seed * 12.9898) * 43758.5453
    fractional = x - math.floor(x)
    return int(fractional * modulo)

def trigger_trap(game_state):
    
    print("⚠️ Ловушка активирована! Пол начал дрожать...")
    inventory = game_state.get('inventory', [])

    #  Если есть предметы — теряем случайный
    if inventory:
        idx = pseudo_random(game_state['steps_taken'], len(inventory))
        lost_item = inventory.pop(idx)
        print(f"Вы потеряли предмет: {lost_item}!")
    else:
        #  Если инвентарь пуст — шанс умереть
        roll = pseudo_random(game_state['steps_taken'], 10)
        if roll < 3:
            print("💀 Ловушка оказалась смертельной! Вы погибли.")
            game_state['game_over'] = True
        else:
            print("😰 Вам повезло — вы чудом уцелели!")

    return game_state

def random_event(game_state):

    # Проверяем вероятность срабатывания (10%)
    
    if pseudo_random(game_state['steps_taken'], 7) != 0:
        # print('efe')
        return  # событие не происходит
    print('ОЙ-ОЙ, кажется вы наткнулись на ловушку!')
    current_room = game_state['current_room']
    inventory = game_state.get('inventory', [])
    room_data = ROOMS[current_room]
    # print(room_data)

    event_type = pseudo_random(game_state['steps_taken'] + 1, 3)

    if event_type == 0:
        # 🪙 Находка
        print("Вы замечаете что-то блестящее на полу — это монетка!")
        room_data['items'].append('coin')

    elif event_type == 1:
        # 
        print("Вы слышите странный шорох где-то поблизости...")

        if 'sword' in inventory or 'кинжал' in inventory:
            weapon = 'меч' if 'sword' in inventory else 'кинжал'
            print(f"Вы выхватываете {weapon} — существо отступает в темноту.")
        else:
            print('Вы в страхе убежали от противника, но никто этого не видел, можно сказать, что этого не было')
    elif event_type == 2:
        # ⚠️ Ловушка (только в trap_room без факела)
        if current_room == 'trap_room' and 'torch' not in inventory:
            print("Вы оступились... что-то щёлкнуло под ногой!")
            trigger_trap(game_state)