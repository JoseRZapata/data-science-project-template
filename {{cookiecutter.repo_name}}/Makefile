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

####----Install Libraries----####

install_data_libs: ## Install pandas and numpy
	@echo "🚀 Installing data science libraries..."
	poetry add pandas numpy

install_viz_libs: ## Install matplotlib seaborn plotly dev group
	@echo "🚀 Installing visualization libraries..."
	poetry add matplotlib plotly seaborn -G dev

install_ml_libs: ## Install scikit-learn
	@echo "🚀 Installing machine learning libraries..."
	poetry add scikit-learn

install_all_libs: ## Install libraries for data science and ML
	$(MAKE) install_data_libs
	$(MAKE) install_viz_libs
	$(MAKE) install_ml_libs

####----Tests----####
tests: ## Run tests with coverage
	coverage run -m pytest;coverage report

####----Project----####
help:
	@printf "%-30s %s\n" "Target" "Description"
	@printf "%-30s %s\n" "-----------------------" "----------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
