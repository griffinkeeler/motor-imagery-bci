import mne


def create_epoch(raw,
                 events,
                 event_id,
                 tmin,
                 tmax
                 ):
    """
    Creates epochs from a raw EEG signal and the event markers.
    Args:
        raw (mne.io.Raw): The continuos EEG data as an MNE Raw object.
        events (ndarray): A NumPy array of shape (n_events, 3).
        event_id (dict): A dictionary mapping class names (str)
        to event IDs (int).
        tmin (float): Start time before the event in seconds.
        tmax (float): End time after the event in seconds.

    Returns:
        mne.Epochs: An epochs object containing segmented trials
        aligned to the specified events window.
    """
    epochs = mne.Epochs(
        raw=raw,
        events=events,
        event_id=event_id,
        tmin=tmin,
        tmax=tmax,
        baseline=None,
        preload=True
    )

    return epochs

