import sys
import numpy as np

# from src.data_loader import load_eeg_runs
from src.data_loader import load_eeg_dataset
from src.preprocessing import preprocess_raw
from src.feature_extraction import extract_csp_features
from src.model_training import train_svm
from src.evaluation import evaluate_model

from src.experiments import EXPERIMENTS
from src.results_manager import save_results

# Program start expects argument (experiment name from experiments.py)
if len(sys.argv) < 2:
    print("Usage:")
    print("    python main.py <experiment_name>")
    print()

    print("Available experiments:")

    for name in EXPERIMENTS:
        print(f"    {name}")

    sys.exit(1)

experiment_name = sys.argv[1]

if experiment_name not in EXPERIMENTS:
    print(f"Unknown experiment: {experiment_name}")
    sys.exit(1)

experiment = EXPERIMENTS[experiment_name]

print()
print(f"Running Experiment: {experiment_name}")
print(experiment["description"])
print()

"""
raw = load_eeg_runs(
    subject_path=f"physionet.org/files/eegmmidb/1.0.0/{subject}",
    runs=runs,
    pick_channels=experiment["channels"]
)
"""

raw = load_eeg_dataset(
    root_path="physionet.org/files/eegmmidb/1.0.0",
    subjects=experiment["subjects"],
    runs=experiment["runs"],
    pick_channels=experiment["channels"]
)

epochs = preprocess_raw(
    raw,

    l_freq=experiment["preprocessing"]["l_freq"],
    h_freq=experiment["preprocessing"]["h_freq"],

    tmin=experiment["preprocessing"]["tmin"],
    tmax=experiment["preprocessing"]["tmax"],

    event_id=experiment["preprocessing"]["event_id"],

    reject_bad_epochs=experiment["preprocessing"]["reject_bad_epochs"]
)

X, y, csp = extract_csp_features(
    epochs,

    n_components=experiment["feature_extraction"]["n_components"]
)

model = train_svm(X, y)

results = evaluate_model(
    model,
    X,
    y,

    test_size=experiment["evaluation"]["test_size"],
    random_state=experiment["evaluation"]["random_state"],
    cv=experiment["evaluation"]["cv"]
)

print(f"Epochs loaded: {len(epochs)}")
print(f"Feature shape: {X.shape}")
print(f"Label shape: {y.shape}")
print(f"Classes learned: {model.classes_}")

print(f"Test Accuracy: {results['test_accuracy']:.3f}")
print(f"CV Scores: {results['cv_scores']}")
print(f"CV Mean: {results['cv_mean']:.3f}")

print("Class counts:")
print(np.unique(y, return_counts=True))

# Saving results

save_results({

    "experiment": experiment_name,

    "description":
    experiment["description"],

    "subjects":
    len(experiment["subjects"]),

    "runs":
    ",".join(experiment["runs"]),

    "channels":
    ",".join(experiment["channels"]),

    "epochs":
    len(epochs),

    "test_accuracy":
    results["test_accuracy"],

    "cv_mean":
    results["cv_mean"]

})

print()
print("Results saved.")