import sys
import unittest

# �ʂ̃e�X�g
#from test import test_sun_position

def get_suite():

    return unittest.defaultTestLoader.discover("test", pattern="test_*.py")

if __name__ == "__main__":
    suite = get_suite()
    unittest.TextTestRunner().run(suite)