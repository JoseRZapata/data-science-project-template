.PHONY: tests help init_env init_git pre-commit_update docs_view docs_test test check

####----Basic configurations----####

init_env: ## Install dependencies with poetry and activate env
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

####----Install Libraries----####

install_data_libs: ## Install pandas, scikit-learn, Jupyter, seaborn
	@echo "🚀 Installing data science libraries..."
	poetry add "pandas[parquet]" numpy scipy scikit-learn
	@echo "🚀 Installing Jupyter, matplotlib and seaborn in dev..."
	poetry add jupyter matplotlib seaborn -G dev

install_mlops_libs: ## Install dvc, mlflow
	@echo "🚀 Installing MLOps libraries ..."
	poetry add dvc great-expectations
	poetry add mlflow deepchecks -G dev

####----Tests----####
test: ## Test the code with pytest and coverage
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov

####----Pre-commit----####
pre-commit_update: ## Update pre-commit hooks
	@echo "🚀 Updating pre-commit hooks..."
	poetry run pre-commit clean
	poetry run pre-commit autoupdate

####----Docs----####
docs_view: ## Build and serve the documentation
	@echo "🚀 Viewing documentation..."
	@poetry run mkdocs serve

docs_test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

####----Checks----####
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
