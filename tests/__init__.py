## Define package-level variables
PACKAGE_VERSION = "1.0.0"

## __init__.py in my_package
from database_dict import get_translation_with_examples

## Allows direct import from package
__all__ = ['get_translation_with_examples']
