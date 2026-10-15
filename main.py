from src.data_loader import load_eeg_runs
from src.preprocessing import preprocess_raw
from src.feature_extraction import extract_csp_features
from src.model_training import train_svm

raw = load_eeg_runs(
    subject_path="physionet.org/files/eegmmidb/1.0.0/S001",
    runs=["S001R03.edf", "S001R04.edf"],
    pick_channels=["C3", "CZ", "C4"]
)

epochs = preprocess_raw(raw)

X, y, csp = extract_csp_features(
    epochs,
    n_components=3
)

model = train_svm(X, y)

print(f"Epochs loaded: {len(epochs)}")
print(f"Feature shape: {X.shape}")
print(f"Label shape: {y.shape}")

# TEMP
print(f"Classes learned: {model.classes_}")

train_accuracy = model.score(X, y)
print(f"Training accuracy: {train_accuracy:.3f}")