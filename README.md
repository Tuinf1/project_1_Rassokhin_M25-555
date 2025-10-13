
sudo apt install python3-poetry
export PATH="$HOME/.local/bin:$PATH"
make install


venv\Scripts\Activate.ps1


poetry check
poetry run ruff check .
poetry build
poetry run project
