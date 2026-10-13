import mne
from pathlib import Path

def load_eeg_runs(
    subject_path: str,
    runs: list,
    montage_name: str = "standard_1005",
    pick_channels: list | None = None
):
    """
    Load and concatenate multiple EEG runs for a subject.

    Parameters
    ----------
    subject_path : str
        Path to the subject folder containing EDF files.
    runs : list
        List of run filenames (e.g., ["S001R03.edf", "S001R04.edf"]).
    montage_name : str
        Name of the MNE montage to apply.
    pick_channels : list or None
        If provided, keep only these channels (e.g., ["C3", "CZ", "C4"]).

    Returns
    -------
    raw : mne.io.Raw
        Concatenated and cleaned raw EEG object.
    """

    subject_path = Path(subject_path)
    raws = []

    for run in runs:
        file_path = subject_path / run
        raw = mne.io.read_raw_edf(file_path, preload=True)

        # Clean channel names
        raw.rename_channels(lambda name: name.replace(".", "").upper())

        raws.append(raw)

    # Concatenate runs
    raw = mne.concatenate_raws(raws)

    # Apply montage
    montage = mne.channels.make_standard_montage(montage_name)
    raw.set_montage(montage, on_missing="ignore")

    # Optional channel selection
    if pick_channels is not None:
        raw.pick([ch.upper() for ch in pick_channels])

    return raw