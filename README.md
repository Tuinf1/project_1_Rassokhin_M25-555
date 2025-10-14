# 🏰 Лабиринт сокровищ

Текстовое приключение на Python, где игрок исследует комнаты, решает загадки, собирает предметы и избегает ловушек, чтобы добраться до сокровищницы.

---

## 🚀 Запуск игры

sudo apt install python3-poetry
export PATH="$HOME/.local/bin:$PATH"
make install


venv\Scripts\Activate.ps1


poetry check 
poetry run ruff check .
poetry build
poetry run project


## 🎥 Demo (asciinema)

https://asciinema.org/a/mUN2EREErTFOdnjEab2qXtxEy

poetry run project


- help - команда покажет список команд в игре. 

⚙️ Основные модули
Файл	Назначение
main.py	Главный игровой цикл и обработка команд
player_actions.py	Действия игрока (движение, сбор предметов)
rooms.py	Описание комнат и их содержимого
events.py	Ловушки, случайные события
config.py	Константы и настройки вероятностей





