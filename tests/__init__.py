## Define package-level variables
PACKAGE_VERSION = "1.0.0"

## __init__.py in my_package
from pinyin import getPinyin, getSegAndPinText, getSegmentation, getSegmentationWithPinyin

## Allows direct import from package
__all__ = ['getPinyin', 'getSegAndPinText', 'getSegmentation', 'getSegmentationWithPinyin']