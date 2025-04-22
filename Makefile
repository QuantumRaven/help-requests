PYTHON := python3
PIP := $(PYTHON) -m pip
VENV_DIR := .venv
ACTIVATE := source $(VENV_DIR)/bin/activate

.PHONY: help create_venv install test clean

help: # Display help message
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*? # / {printf "  %-20s %s\n", $$1, $$2}' Makefile

create_venv: # Create virtual environment
	@echo "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

requirements: # Create requirements.txt
	@echo "Creating requirements.txt..."
	@$(PYTHON) -m pip freeze > requirements.txt
	@echo "requirements.txt created"

install: # Install dependencies
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

test: # Run tests
	@echo "Running tests..."
	$(ACTIVATE) && pytest
	@echo "Tests finished."

clean: ## Clean up build files
	@echo "Cleaning build files..."
	rm -rf $(VENV_DIR) __pycache__ .pytest_cache dist *.egg-info
	@echo "Clean complete."
