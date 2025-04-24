# Feature/Training/Inference Pipelines

File Structure based on:

<https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines>

## Folder Structure

- src: source code
    - data: data extraction, data validation, data processing, data transformation, data save and export, etc.
    - model: model training, model evaluation, model validation, model save and export, etc.
    - inference: model prediction, model serving, model monitoring, etc.
    - pipelines:
        - feature_pipeline: takes as input raw data that it transforms into features (and labels)
        - training_pipeline: takes as input features and labels that it transforms into a model
        - inference_pipeline: takes new feature data and a trained model and makes predictions.

you could have multiple pipelines, for example:

- 3 feature pipelines that extract raw data from different sources and transform them into features and save it into a feature store.
- 2 training pipelines that take the features from the feature store and train different models.
- 3 inference pipeline that creates a model serving endpoint for each of the trained models and 1 batch
  inference pipeline that takes the features from the feature store and makes predictions in batch mode.

Finally is recommended to have a script that orchestrates the execution of the pipelines. This script should could be run in a cron job or a workflow orchestrator like Airflow, Prefect, Dagster, etc.
