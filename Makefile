# Example taken from https://github.com/ColumbiaOSS/example-project-python/blob/main/Makefile

#########
# LINTS #
#########

lint:  ## run static analysis with flake8
	python -m black --check src tests setup.py
	python -m flake8 --per-file-ignores="__init__.py:F401" src tests setup.py

# Alias
lints: lint

format:  ## run autoformatting with black
	python -m black src tests setup.py

#########
# TESTS #
#########
test: ## clean and run unit tests
	python -m unittest tests.test_transcription

coverage:  ## clean and run unit tests with coverage
	python -m coverage run -m unittest tests.test_transcription && python -m coverage report