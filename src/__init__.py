
"""
Marketing AI System - Source Package
=====================================

Core modules for data processing, feature engineering,
model training, and customer targeting.
"""

from .behavior.interaction import InteractionEngine
from .behavior.similarity import ProductSimilarity 

from .data.loader import DataLoader
from .data.merger import DataMerger

from .features.builder import FeatureBuilder

from .models.train import ModelTrainer
from .models.predict import Predictor

from .pipeline.main_pipeline import Pipeline

from .targeting.filter import TargetSelector

from .utils.logger import get_logger

__all__ = [
    "InteractionEngine",
    "ProductSimilarity",
    "DataLoader",
    "DataMerger",
    "FeatureBuilder",
    "ModelTrainer",
    "Predictor",
    "Pipeline",
    "TargetSelector",
    "get_logger"
]