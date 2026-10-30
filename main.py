import numpy as np

# from src.data_loader import load_eeg_runs
from src.data_loader import load_eeg_dataset
from src.preprocessing import preprocess_raw
from src.feature_extraction import extract_csp_features
from src.model_training import train_svm
from src.evaluation import evaluate_model

from src.experiments import EXPERIMENTS

experiment = EXPERIMENTS["imagery_lr"]

subject = experiment["subjects"][0]

runs = [
    f"{subject}{run}.edf"
    for run in experiment["runs"]
]

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

epochs = preprocess_raw(raw)

X, y, csp = extract_csp_features(
    epochs,
    n_components=3
)

model = train_svm(X, y)

results = evaluate_model(
    model,
    X,
    y
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