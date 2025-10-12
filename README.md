
poetry install
.venv\Scripts\Activate.ps1


poetry check
poetry run ruff check .
poetry build
poetry run project

