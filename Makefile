.PHONY: serve freeze deploy build test

serve:
	uv run python -m pyvecorg serve

freeze:
	uv run python -m pyvecorg freeze

deploy:
	uv run python -m pyvecorg deploy --push

build:
	uv run python -m pyvecorg.build

test:
	uv run pytest -v
