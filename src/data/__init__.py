"""
Data Module
===========

Provides data loading and merging capabilities for multiple
data sources including users, products, orders, and events.
"""

from .loader import DataLoader
from .merger import DataMerger

__all__ = ["DataLoader", "DataMerger"]
