.PHONY: tests help

init_env: ## Install dependencies
	@echo "Initialize Git..."
	git init
	@echo "Installing dependencies..."
	poetry install
	@echo "Installing pre-commit..."
	poetry run pre-commit install

env: dependencies
	@echo "Activate virtual environment..."
	poetry shell

install_data_libs: ## Install Data Science libraries
	poetry add pandas numpy matplotlib

# install visualization libraries in dev group
install_viz_libs: ## Install Visualization libraries
	poetry add plotly seaborn -G dev

# install machine learning libraries
install_ml_libs: ## Install Machine Learning libraries
	poetry add scikit-learn

# install all libraries
install_all_libs: ## Install all libraries for data science and ML
	install_data_libs
	install_viz_libs
	install_ml_libs

tests: ## Run tests
	pytest

help:
	@printf "%-30s %s\n" "Target" "Description"
	@printf "%-30s %s\n" "-----------------------" "-------------------------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
