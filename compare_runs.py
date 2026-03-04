import mlflow
import pandas as pd

# set tracking location
mlflow.set_tracking_uri("file:./mlruns")

# get experiment
experiment = mlflow.get_experiment_by_name("milestone3")

# fetch runs
runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id])

# keep useful columns
df = runs[["params.seed", "metrics.accuracy", "start_time"]]

# sort by accuracy
df = df.sort_values(by="metrics.accuracy", ascending=False)

# save comparison
df.to_csv("run_comparison.csv", index=False)

print(df)
print("\nSaved comparison table to run_comparison.csv")
