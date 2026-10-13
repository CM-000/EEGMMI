import mne

def preprocess_raw(
    raw,
    l_freq: float = 8.0,
    h_freq: float = 30.0,
    tmin: float = 0.0,
    tmax: float = 1.0,
    event_id: dict = {"T1": 2, "T2": 3},
    reject_bad_epochs: bool = True
):
    """
    Preprocess a Raw EEG object:
    - bandpass filter
    - extract events
    - epoch the data
    - drop bad epochs (optional)

    Parameters
    ----------
    raw : mne.io.Raw
        The loaded EEG data.
    l_freq : float
        Low cutoff frequency for bandpass filter.
    h_freq : float
        High cutoff frequency for bandpass filter.
    tmin : float
        Start time of each epoch relative to event.
    tmax : float
        End time of each epoch relative to event.
    event_id : dict
        Mapping of event labels to integers.
    reject_bad_epochs : bool
        Whether to drop epochs with extreme amplitudes.

    Returns
    -------
    epochs : mne.Epochs
        Preprocessed and epoched EEG data.
    labels : ndarray
        Array of integer class labels.
    """

    # 1. Bandpass filter
    raw_filt = raw.copy().filter(l_freq, h_freq)

    # 2. Extract events
    events, _ = mne.events_from_annotations(raw_filt)

    # 3. Epoching
    epochs = mne.Epochs(
        raw_filt,
        events,
        event_id=event_id,
        tmin=tmin,
        tmax=tmax,
        baseline=None,
        preload=True
    )

    # 4. Drop bad epochs (optional)
    if reject_bad_epochs:
        epochs.drop_bad()

    return epochs