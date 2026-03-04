import argparse
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import os

parser = argparse.ArgumentParser()
parser.add_argument("--seed", type=int, default=42)
args = parser.parse_args()

seed = args.seed

# create fake dataset
X, y = make_classification(n_samples=1000, n_features=10, random_state=seed)

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

# Force MLflow to use a local folder inside the repo (works on Mac + GitHub Actions)
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("milestone3")
os.makedirs("mlruns", exist_ok=True)

# start mlflow run
with mlflow.start_run():
    mlflow.log_param("seed", seed)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)

    mlflow.log_metric("accuracy", acc)

    mlflow.sklearn.log_model(model, "model")

    print("Accuracy:", acc)
