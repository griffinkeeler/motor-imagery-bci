import numpy as np
from scipy.io import loadmat


def load_raw_data(file_path: str):
    """
    Loads the raw data from MATLAB file path.

    Args:
        file_path: The path to the file.

    Returns:
         A dict with variable names as keys, and
         loaded matrices as values.
    """

    return loadmat(file_path)


def extract_eeg_data(raw_data: dict):
    """
    Extracts continuous EEG signals from raw data.

    Args:
        raw_data: A dict containing raw data from a MATLAB
        file.

    Returns:
        An array of continuous EEG signals with the shape
        (n_channels, n_samples).
    """

    # Converts the datatype from INT16 to a float,
    # as well as into microvolts for MNE
    eeg_data = raw_data["cnt"].astype("float32") * 0.1

    # Transposes array to (n_channels, n_samples) for MNE
    eeg_data = eeg_data.T

    return eeg_data


def extract_info(raw_data: dict):
    """
    Steps into the nested info structure
    containing info about the EEG session.

    Args:
        raw_data: A dict containing raw data from
        a MATLAB file.

    Returns:
        A MATLAB struct providing additional information:
            name: name of the data set,
            fs: sampling rate,
            clab: cell array of channel labels,
            xpos: x-position of electrodes in a 2d-projection,
            ypos: y-position of electrodes in a 2d-projection.
    """

    return raw_data["nfo"][0, 0]


def extract_sampling_rate(info):
    """
    Extracts the sampling rate from the info
    structure.

    Args:
        info: A MATLAB struct providing additional information.

    Returns:
        A floating variable of the sampling rate in Hz.
    """

    return float(info["fs"][0, 0])


def extract_channel_labels(info):
    """
    Extracts the raw channel label array from
    the info structure.

    Args:
        info: A MATLAB struct providing additional information.

    Returns:
        A MATLAB cell array of channel labels.
    """

    return info["clab"][0]


def convert_channel_labels(raw_channels):
    """
    Converts raw channels names from a MATLAB
    cell format to a list of strings.

    Args:
        raw_channels: A MATLAB cell array of channel labels.

    Returns:
        A list of strings of the channel names.
    """

    return [str(ch[0]) for ch in raw_channels]


def load_raw_eeg(filepath: str):
    """
    Loads the continuous EEG data, sampling frequency, and
    channel names from a subject.

    Args:
        filepath: The path to the MATLAB file.

    Returns:
        eeg_data: An array of continuous EEG signals with the shape
        (n_channels, n_samples).

        sfreq: A floating variable of the sampling rate in Hz.

        channel_names: A list of strings of the channels names.
    """

    mat_aa_data = load_raw_data(filepath)

    # Extract and scale EEG data
    eeg_data = extract_eeg_data(mat_aa_data)

    # Step into the info structure
    nfo = extract_info(mat_aa_data)

    # Extract the sampling rate (100 Hz)
    sfreq = extract_sampling_rate(nfo)

    # Extract the raw channel label array
    raw_ch_names = extract_channel_labels(nfo)

    # Convert from MATLAB cell format to a Python list of strings
    channel_names = convert_channel_labels(raw_ch_names)

    return eeg_data, sfreq, channel_names


def create_events_array(labeled_positions, class_labels):
    """
    Takes multiple 1D NumPy arrays and stacks them as
    columns into a 2D NumPy array.

    Args:
        labeled_positions: A 1D NumPy array of sample indices.

        class_labels: A 1D NumPy array of class labels
        as type: int.

    Returns:
        A 2D NumPy array with the shape
        (labeled_positions, zeros, class_labels)
    """

    # Takes multiple 1D arrays and stacks them as
    # columns into a 2D array
    events = np.column_stack(
        (
            labeled_positions,  # When each trial starts
            # Creates an array of zeros the length of
            # class labels used as a placeholder for
            # MNE's "previous event ID" column
            np.zeros(len(class_labels), dtype=int),
            class_labels,  # Type of imagery
        )
    )

    return events


def load_events(filepath: str):
    """
    Loads the labeled cues where each event occurred
    and the class label for the event from the raw
    subject data.

    Args:
        filepath: The path to the MATLAB file.

    Returns:
        labeled_positions: The sample indices of only labeled trials.

        class_labels: A 1D array of class labels as type: int.
    """

    # Loads raw data from the subject
    mat_data = load_raw_data(filepath)

    # Extracts the 'mrk' structure by unwrapping
    # the MATLAB structure from the NumPy array
    mrk = mat_data["mrk"][0, 0]

    # The positions of the motor imagery cues flattened
    # to a 1D NumPy array of shape (280,)
    positions = mrk["pos"][0]

    # The class labels of the motor imagery cues flattened
    # to a 1D NumPy array of shape (280,)
    labels = mrk["y"][0]

    # Creates a boolean array where labeled classes (1 or 2) are
    # True and NaN classes are False
    labeled_mask = ~np.isnan(labels)

    # Extracts the sample indices of only labeled trials
    labeled_positions = positions[labeled_mask]

    # Creates a 1D array of class labels as type: int
    class_labels = labels[labeled_mask].astype(int)

    return create_events_array(labeled_positions=labeled_positions,
                               class_labels=class_labels)



