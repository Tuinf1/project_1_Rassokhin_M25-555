#  для функций, связанных с действиями игрока.
from labyrinth_game.main import game_state

def show_inventory(game_state):
    player_inventory = game_state['player_inventory']

    if not player_inventory:
        print('Инвентарь игрока пуст')
    else:
        print('В инвентаре:', ', '.join(player_inventory))