install:
	poetry install
project:
	poetry run project
build:
	poetry build
package-install:
	python3 -m pip install dist/*.whl
lint:
	poetry run ruff check .