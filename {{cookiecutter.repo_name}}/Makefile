.PHONY: tests help

dependencies: ## Install dependencies
	@echo "Initialize Git..."
	git init
	@echo "Installing dependencies..."
	poetry install
	@echo "Installing pre-commit..."
	poetry run pre-commit install

env: dependencies
	@echo "Activate virtual environment..."
	poetry shell

tests: ## Run tests
	pytest


help:
	@printf "%-30s %s\n" "Target" "Description"
	@printf "%-30s %s\n" "-----------------------" "-------------------------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
