install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install dist/*.whl
publish:
	poetry publish --dry-run
run:
	poetry run project
test-run:
	project