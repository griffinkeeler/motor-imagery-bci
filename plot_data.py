import matplotlib.pyplot as plt
from build_mne_raw import create_raw_object

def plot_raw(raw_object,
             n_channels: int,
             subject: str,):
    """
    Plots the EEG data using the Raw object.

    Args:
        raw_object: The MNE Raw object.
        n_channels: The number of channels to be shown.
        subject: The name of the subject.

    Side Effects:
        Displays an interactive EEG plot window using matplotlib.
    """

    raw_object.plot(
        n_channels=n_channels,
        scalings='auto',
        title='Subject ' + subject + ' EEG Data'
    )
    plt.show()

aa_raw = create_raw_object('data/raw/aa.mat')

plot_raw(raw_object=aa_raw,
         n_channels=10,
         subject='AA')