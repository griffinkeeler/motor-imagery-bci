

def extract_csp_features(epochs):
    """
    Extracts features to be used for CSP.

    Args:
        epochs: An MNE epoch object containing raw EEG data, events,
        event IDs, and epoch length.

    Returns:
         X: EEG data from the epoch object with shape (n_epochs, n_channels, n_times).
         y: class labels (event ID) (1 or 2) with shape (n_epochs,).
    """
    # Extracts EEG data from the epoch object with shape
    # (n_epochs, n_channels, n_times)
    X = epochs.get_data()

    # Extracts class labels (event ID) (1 or 2) with shape
    # (n_epochs,)
    y = epochs.events[:, -1]

    return X, y


