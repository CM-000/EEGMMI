from mne.decoding import CSP

# Think of CSP as building weighted "teams" of electrodes
# that make left- and right-hand motor imagery easier to
# distinguish.

def extract_csp_features(
    epochs,
    n_components=8
):
    """
    Convert EEG epochs into machine-learning features using
    Common Spatial Patterns (CSP).

    CSP learns weighted combinations of EEG channels that
    best separate the two motor imagery classes. The output
    is a feature matrix suitable for traditional ML models
    such as SVMs or Logistic Regression.
    """

    # Labels associated with each epoch (e.g. T1 vs T2)
    labels = epochs.events[:, -1]

    # Learn spatial filters that maximize the difference
    # between the two classes.
    csp = CSP(
        n_components=n_components,
        log=True
    )

    # Transform EEG data from:
    # (trials, channels, samples)
    # into:
    # (trials, features)
    X = csp.fit_transform(
        epochs.get_data(),
        labels
    )

    return X, labels, csp