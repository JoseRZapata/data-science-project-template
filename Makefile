.PHONY: tests help init_env init_git pre-commit_update docs_view docs-test test actionlint check

####----Basic configurations----####

init_env: ## Install libs with poetry and pre-commit
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	poetry install
	@echo "🚀 Installing pre-commit..."
	poetry run pre-commit install
	@echo "💻 Activate virtual environment..."
	@poetry shell

init_git: ## Initialize git repository
	@echo "🚀 Initializing local git repository..."
	git init -b main
	git add .
	git commit -m "🎉 Initial commit"
	@echo "🚀 Local Git already set!"

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

####----Tests----####

test: ## Test the code with pytest and coverage
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov

####----Checks----####
actionlint: ## Check GitHub Actions
	@echo "🚀 Checking GitHub Actions..."
	actionlint -color -verbose

check: ## Run code quality tools with pre-commit hooks.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry check --lock
	@echo "🚀 Linting, formating and Static type checking code: Running pre-commit"
	@poetry run pre-commit run -a

####----Project----####
help:
	@printf "%-30s %s\n" "Target" "Description"
	@printf "%-30s %s\n" "-----------------------" "----------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
