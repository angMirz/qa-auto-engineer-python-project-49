install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force $(wildcard dist/*.whl)
# 	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games --fix

activate:
	source .venv/bin/activate
