# Feature/Training/Inference Pipelines

File Structure based on:

<https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines>

- data: data extraction, data validation, data processing, data transformation, data save and export, etc.
- model: model training, model evaluation, model validation, model save and export, etc.
- inference: model prediction, model serving, model monitoring, etc.

- pipelines:
    - feature_pipeline: takes as input raw data that it transforms into features (and labels)
    - training_pipeline: takes as input features and labels that it transforms into a model
    - inference_pipeline: takes new feature data and a trained model and makes predictions.
