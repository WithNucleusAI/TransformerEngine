# Copyright (c) 2022-2025, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# See LICENSE for license information.

"""Top level package"""

# pylint: disable=unused-import

from importlib import metadata
import transformer_engine.common

try:
    from . import pytorch
except (ImportError, FileNotFoundError):
    pass

try:
    from . import jax
except (ImportError, FileNotFoundError):
    pass

__version__ = str(metadata.version("transformer_engine"))
