import numpy as np
from load_eeg_data import load_raw_data


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
    mrk = mat_data['mrk'][0, 0]

    # The positions of the motor imagery cues flattened
    # to a 1D NumPy array of shape (280,)
    positions = mrk['pos'][0]

    # The class labels of the motor imagery cues flattened
    # to a 1D NumPy array of shape (280,)
    labels = mrk['y'][0]

    # Creates a boolean array where labeled classes (1 or 2) are
    # True and NaN classes are False
    labeled_mask = ~np.isnan(labels)

    # Extracts the sample indices of only labeled trials
    labeled_positions = positions[labeled_mask]

    # Creates a 1D array of class labels as type: int
    class_labels = labels[labeled_mask].astype(int)

    return labeled_positions, class_labels


