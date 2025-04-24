.PHONY: tests help init_env init_git pre-commit_update docs docs_test docs_view test actionlint check

####----Basic configurations----####

install: ## Install libs with poetry and pre-commit
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	uv sync --all-groups
	@echo "🚀 Installing pre-commit..."
	uv run pre-commit install
	@echo "💻 Activate virtual environment..."
	source .venv/bin/activate

init_git: ## Initialize git repository
	@echo "🚀 Initializing local git repository..."
	git init -b main
	git add .
	git commit -m "🎉 Initial commit"
	@echo "🚀 Local Git already set!"

####----Pre-commit----####
pre-commit_update: ## Update pre-commit hooks
	@echo "🚀 Updating pre-commit hooks..."
	uv run pre-commit clean
	uv run pre-commit autoupdate

####----Clean----####
clean_env: ## Clean the environment
	@echo "🚀 Cleaning the environment..."
	@[ -d .venv ] && rm -rf .venv || echo ".venv directory does not exist"

####----Git----####
switch_main: ## Switch to main branch and pull
	@echo "🚀 Switching to main branch..."
	@git switch main
	@git pull

clean_branchs: ## Clean local branches already merged on the remote
	@echo "🚀 Cleaning up merged branches..."
	@git fetch -p
	@for branch in $$(git for-each-ref --format '%(refname:short)' refs/heads/ | grep -v '^\*' | grep -v ' main$$'); do \
		if ! git show-ref --quiet refs/remotes/origin/$$branch; then \
			echo "Deleting local branch $$branch"; \
			git branch -D $$branch; \
		fi \
	done

####----Docs----####
docs: ## Build and serve the documentation
	@echo "🚀 Viewing documentation..."
	uv run mkdocs serve

docs_test: ## Test if documentation can be built without warnings or errors
	@uv run mkdocs build -s

view_tree: ## View the project tree
	@echo "🚀 Viewing project tree..."
	@tree -a {{cookiecutter.repo_name}} -I '__init__.py|.gitkeep'

####----Tests----####

test: ## Test the code with pytest and coverage
	@echo "🚀 Testing code: Running pytest"
	@uv run pytest --cov

test_coverage: ## Test the code with pytest and coverage
	@echo "🚀 Testing code: coverage.xml"
	@uv run pytest --cov --cov-report xml:coverage.xml

####----Checks----####
actionlint: ## Check GitHub Actions
	@echo "🚀 Checking GitHub Actions..."
	actionlint -color -verbose

check: ## Run code quality tools with pre-commit hooks.
	@echo "🚀 Linting, formating and Static type checking code: Running pre-commit"
	@uv run pre-commit run -a

lint: ## Run code quality tools with pre-commit hooks.
	@echo "🚀 Linting, formating and Static type checking code: Running pre-commit"
	@uv run pre-commit run ruff

####----Project----####
help:
	@printf "%-30s %s\n" "Target" "Description"
	@printf "%-30s %s\n" "-----------------------" "----------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
