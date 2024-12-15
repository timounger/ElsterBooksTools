"""!
********************************************************************************
@file   version.py
@brief  Version and general information
********************************************************************************
"""

# Version
VERSION_MAJOR = 0  # major changes/breaks at API (e.g incompatibility)
VERSION_MINOR = 1  # minor changes/does not break the API (e.g new feature)
VERSION_PATCH = 0  # Bug fixes
VERSION_BUILD = 0  # build number (if available)

__title__ = "ElsterBooksTools"
__description__ = "Create external Tools for ElsterBooks"
__author__ = "Timo Unger"
__owner__ = "timounger"
__repo__ = "ElsterBooksTools"
__copyright__ = f"Copyright © 2024 {__author__}"
__license__ = "GNU General Public License"
__home__ = f"https://{__owner__}.github.io/{__repo__}"


if VERSION_BUILD == 0:
    PRERELEASE_BUILD = False
    __version__ = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
else:
    PRERELEASE_BUILD = True
    __version__ = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}.{VERSION_BUILD}"


B_DEBUG = False  # debug/test code
