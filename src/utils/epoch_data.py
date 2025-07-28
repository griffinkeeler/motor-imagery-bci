import mne


def create_epoch(filtered_raw, events, event_id, tmin, tmax):
    """
    Creates epochs from a raw EEG signal and the event markers.

    Args:
        filtered_raw (mne.io.Raw): The continuos EEG data as an MNE Raw object.
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
        raw=filtered_raw,
        events=events,
        event_id=event_id,
        tmin=tmin,
        tmax=tmax,
        baseline=None,
        preload=True,
    )

    return epochs


def create_subject_epochs(raw, events):
    """
    Loads, preprocesses, and epochs motor imagery EEG data from
    subjects in the BCI Competition III data set IVa.

    Args:
        raw:
        events:

    Returns:
        An MNE epoch object containing raw EEG data, events,
        event IDs, and epoch length.
    """
    # A dictionary containing class names as keys and
    # integers as values
    event_id = {"right": 1, "foot": 2}

    # Creates epoch with a length of 3.5 seconds at each event
    epochs = create_epoch(
        filtered_raw=raw, events=events, event_id=event_id, tmin=0.0, tmax=3.5
    )

    return epochs
