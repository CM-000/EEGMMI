from pathlib import Path
import csv

def save_experiment_result(
    experiment_name,
    num_subjects,
    num_epochs,
    test_accuracy,
    cv_mean
):
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    csv_file = results_dir / "experiment_log.csv"

    file_exists = csv_file.exists()

    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "experiment",
                "subjects",
                "epochs",
                "test_accuracy",
                "cv_mean"
            ])

        writer.writerow([
            experiment_name,
            num_subjects,
            num_epochs,
            round(test_accuracy, 3),
            round(cv_mean, 3)
        ])