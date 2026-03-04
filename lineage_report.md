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

## Experiment Comparison

Multiple MLflow runs were executed with different random seeds.  
The results were exported using `compare_runs.py` into `run_comparison.csv`.

The comparison table contains:

- run start time
- random seed parameter
- accuracy metric

These runs allow comparison of model performance across different training seeds.

## Model Selection

The production model is selected based on the highest validation accuracy among the experiment runs recorded in MLflow.

The run with the best accuracy is considered the candidate production model.

## Monitoring and Risks

Potential risks include:

- model accuracy degradation over time
- data distribution changes

Monitoring strategy:

- continue logging metrics in MLflow
- trigger alerts if accuracy drops below the validation threshold
- retrain the model periodically if performance decreases.

## Reproducibility

The pipeline is designed to be reproducible across environments. All dependencies are pinned in `requirements.txt` and automatically installed during CI execution. The training process accepts a seed parameter which ensures deterministic dataset generation and model training. Each experiment run is tracked by MLflow with recorded parameters, metrics, and artifacts, allowing experiments to be reproduced exactly.

## Operational Reliability

The pipeline incorporates several mechanisms to ensure operational reliability. The Airflow DAG defines clear task dependencies between preprocessing, training, and registration steps. Retry logic and failure callbacks are configured to handle transient execution failures. The CI/CD workflow automatically executes the pipeline on each commit, ensuring that any changes to the codebase are validated immediately. The validation script acts as a quality gate, preventing pipelines from passing if the model does not produce the expected performance metric.
