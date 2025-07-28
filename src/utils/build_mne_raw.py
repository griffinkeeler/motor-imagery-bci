import mne
from src.utils.load_eeg_data import load_raw_eeg, load_events


def create_info_object(ch_names: list, fs: float, ch_types: str):
    """
    Creates the MNE info object holding metadata
    for the EEG recording.

    Args:
        ch_names: A list of the channel names.
        fs: The sampling rate in Hz.
        ch_types: The type of recording technique.

    Returns:
        An MNE data structure which keeps track of
        various recording details.
    """
    return mne.create_info(ch_names=ch_names, sfreq=fs, ch_types=ch_types)


def create_raw_array(eeg_data, info):
    """
    Creates the MNE RawArray for plotting, filtering, and epoching.

    Args:
        eeg_data: An array of continuous EEG signals with
        the shape (n_channels, n_samples).
        info: An MNE data structure which keeps track of
        various recording details.

    Returns:
        A Raw object from a numpy array.
    """

    return mne.io.RawArray(data=eeg_data, info=info)


def create_raw_object(filepath: str, ch_type: str):
    """
    Creates the raw MNE object holding continuous EEG data.

    Args:
        filepath: The path to the MATLAB file.
        ch_type: The type of recording channel (e.g. EEG).

    Returns:
        Raw object from a numpy array.
    """
    # Load the subject's data to create the raw MNE object
    eeg_data, sfreq, channel_names = load_raw_eeg(filepath)

    # Create the MNE info object containing the subject's EEG recording
    # metadata
    info = create_info_object(ch_names=channel_names, fs=sfreq, ch_types=ch_type)

    # Creates a 2D NumPy array with shape
    # (labeled positions, zeros, class_labels)
    events = load_events(filepath=filepath)

    # Create the MNE RawArray for plotting, filtering, and epoching
    raw = create_raw_array(eeg_data=eeg_data, info=info)

    return raw, events
