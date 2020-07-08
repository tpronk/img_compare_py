# Reproduces PychoPy's RMS method for comparing the similary of two pictures
# https://github.com/psychopy/psychopy/blob/810ac6bfa8945bb62d9142abd592a2267d3fc936/psychopy/tests/utils.py#L31
# Requires two PNG files of the same height and width: left.png and right.png

# Thomas Pronk, pronkthomas@gmail.com, 2020-07-08

# Dependencies
from PIL import Image
import numpy as np

# *** Read images
expected = Image.open('left.png')
expDat = np.array(expected.getdata())
frame = Image.open('right.png')
imgDat = np.array(frame.getdata())

# *** Output of tests
# Expected output based on:
# https://thomaspronk.com/resources/img_compare/left.png
# https://thomaspronk.com/resources/img_compare/right.png

# Should output: [88 81 71 87] <- RGB of first pixel, R of second pixel
print("RGB values of first four elements: " + str(expDat.flatten()[0 : 4]))
# Should output: 7372800 <- 3 * 2457600 pixels
print("Length of expDat: " + str(len(expDat.flatten())))
# Should output: 18.013210727944
print("SD of differences: " + str(np.std(imgDat-expDat)))