# BCI Competition III Project

---

## Overview

---

This project utilizes the [BCI Competition
III Dataset IVa](https://www.bbci.de/competition/iii/desc_IVa.html)
to classify 2 motor imageries:
- Right hand movements
- Right foot movements


Data set provided by Fraunhofer FIRST, Intelligent Data Analysis Group
(Klaus-Robert Müller, Benjamin Blankertz), and Campus Benjamin Franklin
of the Charité - University Medicine Berlin, Department of Neurology,
Neurophysics Group (Gabriel Curio).
 ### What is a BCI?
A brain-computer interface (BCI) is a system that allows for direct
communication between the brain and an external device using brain signals.
## Features

---

### Loading Data
A continuous raw electroencephalography (EEG) signal, sampling frequency,
and channel names are loaded from the dataset. This data is used to
create an MNE Raw object.

### Preprocessing 
A bandpass filter with a range of 8-30 Hz is applied to the Raw object
to reduce noisy signals.

### Epoching
3.5 second trials are extracted starting at each motor imagegry cue. 

### Feature Extraction
Common Spatial Patterns (CSP) extracts spatial patterns that maximize
variance differences between two classes, such as right hand vs. foot
motor imagery. 


