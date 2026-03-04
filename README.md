# IDS 568 – Milestone 3: ML Pipeline with CI/CD

This project demonstrates a simple machine learning pipeline with experiment tracking and automated validation using MLflow and GitHub Actions.

---

# Architecture Overview

The pipeline consists of three main components:

**Training**
- `train.py` trains a Logistic Regression model on a synthetic dataset.
- The model is evaluated using accuracy.

**Experiment Tracking**
- MLflow logs experiment runs including metrics and artifacts.
- Each run records the model and accuracy score.

**Validation / Quality Gate**
- `model_validation.py` ensures the trained model meets a minimum accuracy threshold.
- If the threshold is not met, the pipeline fails.

**CI/CD Automation**
- GitHub Actions automatically runs training and validation on every push.

---

# Repository Structure

```
.github/workflows/train_and_validate.yml   CI/CD pipeline
dags/train_pipeline.py                     Airflow DAG definition
train.py                                   Model training script
model_validation.py                        Validation / quality gate
compare_runs.py                            Experiment comparison
run_comparison.csv                         Table of MLflow runs
requirements.txt                           Project dependencies
lineage_report.md                          Experiment lineage report
README.md                                  Project documentation
```

---

# Setup Instructions

Clone the repository:

```
git clone https://github.com/pujan910/ids568-milestone3-pagarw2
cd ids568-milestone3-pagarw2
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running the Pipeline Locally

Run model training:

```
python train.py
```

Run validation:

```
python model_validation.py
```

MLflow will log experiment runs automatically.

---

# CI/CD Pipeline

The repository includes a GitHub Actions workflow:

```
.github/workflows/train_and_validate.yml
```

On every push:

1. Dependencies are installed
2. Training script runs
3. MLflow logs experiment metrics
4. Validation script checks model performance
5. The pipeline succeeds or fails based on the quality gate

---

# Experiment Tracking

MLflow tracks:

- model parameters
- accuracy metrics
- trained model artifacts

Multiple experiment runs can be compared using:

```
compare_runs.py
```

Results are stored in:

```
run_comparison.csv
```

---

# Experiment Lineage

`lineage_report.md` documents:

- experiment comparisons
- model selection reasoning
- artifact lineage

This ensures reproducibility and traceability of the final model.

---

# Operational Notes

**Retry Strategy**
- CI pipeline automatically retries failed steps.

**Monitoring**
- Model accuracy is validated through the quality gate.

**Rollback**
- If validation fails, the pipeline stops and prevents deployment of the model.

---

# Technologies Used

- Python
- Scikit-Learn
- MLflow
- GitHub Actions
- Apache Airflow (DAG definition)
