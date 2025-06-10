from build_mne_raw import create_raw_object
from load_events_data import load_events
from build_mne_events import create_events_array
from epoch_data import create_epoch


def main():
    """
    Main script for loading, preprocessing, and epoching motor imagery
    EEG data for BCI Competition III data set IVa (subject 'aa').
    """
    # Creates the raw MNE object for subject AA
    aa_raw = create_raw_object('data/raw/aa.mat')

    # Loads the labeled cues where each event occurred
    # and class labels for subject AA
    aa_labeled_positions, aa_class_labels = load_events('data/raw/aa.mat')

    # Creates an 2D NumPy array with shape (labeled_positions, zeros, class_labels)
    # for subject AA
    aa_events = create_events_array(aa_labeled_positions, aa_class_labels)

    # A dictionary containing class names as keys and integers
    # as values
    aa_event_id = {
        'right': 1,
        'foot': 2
    }

    # Creates epochs with a length of 3.5 seconds
    # at each event for subject AA
    aa_epochs = create_epoch(raw=aa_raw,
                            events=aa_events,
                            event_id=aa_event_id,
                            tmin=0.0,
                            tmax=3.5)


if __name__ == 'main':
    main()









