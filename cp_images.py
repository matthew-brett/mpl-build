""" Copy matplotlib test images to installed directory
"""

import sys
from os.path import dirname, join as pjoin
from shutil import copytree
import matplotlib

MPL_SRC_DIR = sys.argv[1]
MPL_INSTALL_DIR = dirname(matplotlib.__file__)

copytree(pjoin(MPL_SRC_DIR, 'lib', 'matplotlib', 'tests', 'baseline_images'),
         pjoin(MPL_INSTALL_DIR, 'tests', 'baseline_images'))
