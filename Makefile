# Create virtual environment
venv:
	python3 -m venv .venv

# Activate virtual environment
activate:
	. .venv/bin/activate

# Install requirements
install:
	.venv/bin/pip install --upgrade pip setuptools wheel && .venv/bin/pip install -r requirements.txt

# Run the application
run:
	.venv/bin/python src/habit_tracker/main.py

# Run all unittests
test:
	.venv/bin/python -m unittest discover -s tests

# Remove virtual environment and caches
clean:
	rm -rf .venv
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -r {} +

# Setup: create venv, install requirements, and run the app
setup: venv activate run

csetup: clean venv install run