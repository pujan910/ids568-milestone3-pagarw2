# ids568-milestone3-pagarw2
# IDS 568 – Milestone 3: ML Pipeline with CI/CD

This project demonstrates a simple machine learning pipeline with experiment tracking and automated validation.

## Components

**Training Script**

* `train.py` trains a Logistic Regression model on synthetic data.
* Accuracy is logged using MLflow.

**Experiment Tracking**

* MLflow tracks experiment runs in the `mlruns/` directory.

**Quality Gate**

* `model_validation.py` ensures the training script outputs a valid accuracy metric.

**CI/CD Pipeline**

* GitHub Actions automatically runs training and validation on every push.

**Documentation**

* `lineage_report.md` describes the pipeline lineage and artifacts.

## Workflow

1. Push code to GitHub
2. GitHub Actions runs the pipeline
3. Model trains and logs metrics
4. Validation script checks accuracy
5. Pipeline passes or fails automatically
