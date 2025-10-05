#  для функций, связанных с действиями игрока.
from labyrinth_game.player_actions import show_inventory

def show_inventory(game_state):
    player_inventory = game_state['player_inventory']

    if not player_inventory:
        print('Инвентарь игрока пуст')
    else:
        print('В инвентаре:', ', '.join(player_inventory))

def get_input(prompt="> "):
    try:
        # тут ваш код
        z = None
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 