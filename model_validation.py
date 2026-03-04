import sys
import re
import subprocess

MIN_ACCURACY = 0.80  # quality gate threshold

def main():
    # run train.py and capture its output
    result = subprocess.run(
        ["python", "train.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    # find "Accuracy: 0.xxx" in output
    match = re.search(r"Accuracy:\s*([0-9]*\.?[0-9]+)", result.stdout)
    if not match:
        print("FAILED: Could not find Accuracy in output")
        sys.exit(1)

    acc = float(match.group(1))
    print(f"Parsed accuracy = {acc}")

    if acc < MIN_ACCURACY:
        print(f"FAILED: Accuracy {acc} is below threshold {MIN_ACCURACY}")
        sys.exit(1)

    print("PASSED: Quality gate satisfied")
    sys.exit(0)

if __name__ == "__main__":
    main()