# Agent Context & Conventions (Single Source of Truth)

This document contains the mandatory rules, conventions, and security guardrails for any AI, agent, or LLM operating within this repository.

## 1. Tech Stack and Commands

* **Dependency Management:** DO NOT use `pip` or `poetry`. This project exclusively uses **`uv`**.
    * To add packages: `uv add <package>`
    * To run scripts/tools: `uv run python <script.py>` or `uv run pytest`
* **Linter and Formatter:** Use **Ruff**. Do not install or suggest Black, Isort, or Flake8. Run `uv run ruff check --fix .` before completing a task.
* **Static Typing:** All code inside the `src/` directory must be typed and pass static type checking using **Mypy**.

## 2. Workflow and Architecture

* **Experimentation:** Use the `notebooks/` folder exclusively for EDA (Exploratory Data Analysis), hypothesis testing, and visualizations.
* **Production Code:** To "move a model to production" or refactor, you must extract the logic from the notebooks into `.py` modules within the `src/` directory.
* **Testing:** Every new module in `src/` must have a corresponding test in the `tests/` directory using **Pytest**.

## 3. Code Style (Machine Learning)

* **Documentation:** Document all functions and classes using Docstrings (NumPy or Google format).
* **Pipelines:** Prefer the use of Scikit-Learn *Pipelines* over isolated transformations to prevent data leakage.
* **Reproducibility:** Always set a random seed (e.g., `random_state=42`) in data splits, algorithms, and models.

## 4. Critical Security Rules (Agentic Guardrails)

* **PII Protection:** Never read, print to the console, or process raw data in the chat if you suspect it contains Personally Identifiable Information. Use only `df.info()`, `df.describe()`, or `df.head()` with safely anonymized data.
* **Secrets Management:** Forbidden to hardcode tokens (Hugging Face, OpenAI, AWS) or database credentials in the code or Notebooks. Enforce the use of a local, untracked `.env` file and `os.getenv()`.
* **Safe Installation:** Do not invent packages or install libraries suggested by hallucinations. Install only official dependencies and verify there is no typosquatting risk before running `uv add`.
* **Notebook Outputs:** Never commit a Jupyter notebook with saved outputs (`notebooks/*.ipynb`). Ensure outputs are cleared before committing changes to prevent data leaks.
* **Raw Data Protection:** Forbidden to write, overwrite, or delete files in the `data/raw/` directory. All agent-generated data transformations must be saved exclusively in `data/processed/` or `data/interim/`.
