import numpy as np

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
    events = np.column_stack((
        labeled_positions,  # When each trial starts

        # Creates an array of zeros the length of
        # class labels used as a placeholder for
        # MNE's "previous event ID" column
        np.zeros(len(class_labels), dtype=int),
        class_labels        # Type of imagery
    ))

    return events