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