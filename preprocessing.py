

def bandpass_filter(raw, l_freq=8.0, h_freq=30.0):
    """
    Returns a band-pass filtered copy of the raw EEG signal.

    Args:
        raw: The MNE Raw object to filter.
        l_freq: Low cutoff frequency in hertz.
        h_freq: High cutoff frequency in hertz.

    Returns:
        A filtered Raw object.

    """
    return raw.copy().filter(
        l_freq=l_freq,
        h_freq=h_freq,
        fir_design='firwin',
        skip_by_annotation='edge'
    )




