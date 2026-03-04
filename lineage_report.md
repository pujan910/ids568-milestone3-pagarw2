# ML Pipeline Lineage Report

## Dataset
Synthetic dataset generated using sklearn `make_classification`.

## Training Script
`train.py` trains a Logistic Regression model and logs metrics using MLflow.

## Metrics Logged
Accuracy is calculated on the test split and logged to MLflow.

## Experiment Tracking
MLflow tracks experiment runs inside the `mlruns/` directory.

## Model Artifact
The trained model is stored as an MLflow artifact (`model.pkl`).

## Validation
`model_validation.py` runs the training script and verifies that the output contains an accuracy metric.  
If accuracy is not found, the pipeline fails.

## CI/CD Pipeline
GitHub Actions automatically runs the training and validation pipeline on every push to the repository.

Workflow file:
`.github/workflows/train_and_validate.yml`

## Quality Gate
The pipeline ensures that the training script successfully outputs accuracy before allowing the workflow to pass.