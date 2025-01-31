# {{ cookiecutter.project_name }} - Notebooks

Project the notebooks. The naming convention is:
`[##.#]-[creator initials]-[short_description]-[yyyy_mm_dd].ipynb`

- `##.#` is the notebook number and version.
- `creator initials` are the initials of the person who created the notebook.
- `short_description` is a short `_` delimited description of the notebook,  .
- `yyyy_mm_dd` is the date the notebook was created.

Examples:
01-jrz-data_exploration-2024_10_02.ipynb
02.1-jrz_data_raw_analysis-2024_10_08.ipynb
02.2-jrz_data_raw_analysis-2024_11_21.ipynb

## folder structure

```bash
├── notebooks
│   ├── 1-data                   # data extraction and cleaning
│   ├── 2-exploration            # exploratory data analysis (EDA)
│   ├── 3-analysis               # Statistical analysis, hypothesis testing.
│   ├── 4-feat_eng               # feature engineering (creation, selection, and transformation.)
│   ├── 5-models                 # model training, evaluation, and hyperparameter tuning.
│   ├── 6-interpretation         # model interpretation
│   ├── 7-deploy                 # model packaging, deployment strategies.
│   ├── 8-reports                # story telling, summaries and analysis conclusions.
│   ├── notebook_template.ipynb
```
