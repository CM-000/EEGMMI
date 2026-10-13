from src.data_loader import load_eeg_runs
from src.preprocessing import preprocess_raw

raw = load_eeg_runs(
    subject_path="physionet.org/files/eegmmidb/1.0.0/S001",
    runs=["S001R03.edf", "S001R04.edf"],
    pick_channels=["C3", "CZ", "C4"]
)

epochs = preprocess_raw(raw)

print(f"Epochs loaded: {len(epochs)}")