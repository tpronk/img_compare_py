from img_compare import calculate_rms
import pytest

def  test_kitten():
   rms = calculate_rms('left.png', 'right.png')  
   assert rms == pytest.approx(18.013210727944)

