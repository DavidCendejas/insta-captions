# Example taken from https://github.com/ColumbiaOSS/example-project-python/blob/main/Makefile

#########
# LINTS #
#########

lint:  ## run static analysis with flake8
	python -m black --check src tests setup.py
	python -m flake8 src tests setup.py

# Alias
lints: lint

format:  ## run autoformatting with black
	python -m black src tests setup.py