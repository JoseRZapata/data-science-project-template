.PHONY: tests help

####----Basic configurations----####

init_env: ## Install dependencies with poetry and init git
	@echo "Initialize Git in main branch..."
	git init -b main
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	poetry install
	@echo "🚀 Installing pre-commit..."
	poetry run pre-commit install
	@echo "🎉 First commit..."
	git add .
	git commit -m "🎉 Begin a project, Initial commit"
	@echo "💻 Activate virtual environment..."
	poetry shell

####----Pre-commit----####

pre_commit-all: ## Run pre-commit hooks
	@echo "🚀 Running pre-commit hooks..."
	poetry run pre-commit run --all-files

pre_commit-update: ## Update pre-commit hooks
	@echo "🚀 Updating pre-commit hooks..."
	poetry run pre-commit clean
	poetry run pre-commit autoupdate


####----Project----####
help:
	@printf "%-30s %s\n" "Target" "Description"
	@printf "%-30s %s\n" "-----------------------" "----------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
