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
	@poetry shell

####----Pre-commit----####
pre-commit_update: ## Update pre-commit hooks
	@echo "🚀 Updating pre-commit hooks..."
	poetry run pre-commit clean
	poetry run pre-commit autoupdate

####----Docs----####
docs_view: ## Build and serve the documentation
	@echo "🚀 Viewing documentation..."
	@poetry run mkdocs serve

docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

####----Checks----####
actionlint: ## Check GitHub Actions
	@echo "🚀 Checking GitHub Actions..."
	actionlint -color -verbose

check: ## Run code quality tools with pre-commit hooks.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry check --lock
	@echo "🚀 Linting, formating and Static type checking code: Running pre-commit"
	@poetry run pre-commit run -a

docs_test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

####----Project----####
help:
	@printf "%-30s %s\n" "Target" "Description"
	@printf "%-30s %s\n" "-----------------------" "----------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
