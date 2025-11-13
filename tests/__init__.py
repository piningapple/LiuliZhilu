## Define package-level variables
PACKAGE_VERSION = "1.0.0"

## __init__.py in my_package
from pinyin import get_pinyin, get_seg_and_pin_text, get_segmentation, get_segmentation_with_pinyin
from database_dict import get_translation_with_examples

## Allows direct import from package
__all__ = ['get_pinyin', 'get_seg_and_pin_text', 'get_segmentation', 'get_segmentation_with_pinyin', 'get_translation_with_examples']
