"""Initialize tcor package.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import os

# Home PATH
HOME = os.environ["HOME"]

# tcor Root path
try:
    TCOR_ROOT = os.environ["TCOR_ROOT_PATH"]
except KeyError:
    TCOR_ROOT = "tcor_root"

# tcor related paths
TCOR_DATA_PATH = os.path.join(TCOR_ROOT, "data")
TCOR_RES_PATH = os.path.join(TCOR_ROOT, "res")


def set_root(tcor_root_path):
    """Set tcor root path.

    Parameters
    ----------
    tcor_root_path : str
        the absolute path of root path

    Returns
    -------
    set_root_flag : bool
        indicates if path sets successful. (True: success, False: failed)
    """
    global TCOR_ROOT, TCOR_DATA_PATH, TCOR_RES_PATH
    if not os.access(tcor_root_path, os.W_OK):
        return False

    # set root path
    if not os.path.isdir(tcor_root_path):
        os.makedirs(tcor_root_path)
        TCOR_ROOT = tcor_root_path
    else:
        TCOR_ROOT = tcor_root_path

    # set sub folders
    TCOR_DATA_PATH = os.path.join(TCOR_DATA_PATH, "data")
    TCOR_RES_PATH = os.path.join(TCOR_RES_PATH, "res")

    if not os.path.isdir(TCOR_DATA_PATH):
        os.makedirs(TCOR_DATA_PATH)

    if not os.path.isdir(TCOR_RES_PATH):
        os.makedirs(TCOR_RES_PATH)
    
    return True
