"""
All settings are imported here and assimilated. This file acts as a factory module for settings.
Settings from base.py, staging.py, production.py and local.py are import in that order (depending on set ENV VARS)
"""

# Set base settings
from .base import *

import sys

# # Decide whether to use staging settings or production settings based on environment variables
deployment_type = os.environ.get("PAYMENTS_DEPLOYMENT_TYPE", None)
if deployment_type == "STAGING":
    from .staging import *
elif deployment_type == "PRODUCTION":
    from .production import *
elif deployment_type == "DEV":
    from .dev import *
else:
    # Import local settings which has the highest precedence
    try:
        from .local import *
    except ImportError:
        pass

if 'test' in sys.argv:
    from .testing import *
