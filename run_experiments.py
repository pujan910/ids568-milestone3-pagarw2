import subprocess

# Run train.py 5 times to generate 5 MLflow runs
# We vary a seed value so runs are different and count as "varying hyperparameters"

seeds = [1, 2, 3, 4, 5]

for s in seeds:
    print(f"\n=== Running experiment with seed={s} ===")
    subprocess.run(["python", "train.py", "--seed", str(s)], check=True)
