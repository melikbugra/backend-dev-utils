poetry run coverage run -m pytest -v tests
poetry run coverage report -m --skip-empty --fail-under=95