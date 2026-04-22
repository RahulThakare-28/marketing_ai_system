"""
Behavior Module
===============

Handles user behavior analysis including interaction scoring
and product similarity computation.
"""

from .interaction import InteractionEngine
from .similarity import ProductSimilarity

__all__ = ["InteractionEngine", "ProductSimilarity"]
