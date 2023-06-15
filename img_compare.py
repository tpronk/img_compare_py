# Reproduces PychoPy's RMS method for comparing the similary of two pictures
# https://github.com/psychopy/psychopy/blob/810ac6bfa8945bb62d9142abd592a2267d3fc936/psychopy/tests/utils.py#L31
# Requires two PNG files of the same height and width: left.png and right.png

# Thomas Pronk, pronkthomas@gmail.com, 2020-07-08

# Dependencies
from PIL import Image
import numpy as np

def calculate_rms(file_left, file_right):
    # *** Read images
    expected = Image.open(file_left)
    expDat = np.array(expected.getdata())
    frame = Image.open(file_right)
    imgDat = np.array(frame.getdata())
    # Calculate RMS
    return np.std(imgDat-expDat)

