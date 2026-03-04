import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# create fake dataset
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# start mlflow run
with mlflow.start_run():

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)

    mlflow.log_metric("accuracy", acc)

    mlflow.sklearn.log_model(model, "model")

    print("Accuracy:", acc)