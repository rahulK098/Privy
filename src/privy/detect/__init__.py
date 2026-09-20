"""Detection layer: wraps Presidio and detect-secrets behind one schema (ADR-0001, ADR-0003)."""

from privy.detect.base import Detector
from privy.detect.custom import PatternSpec
from privy.detect.engine import DetectionEngine, DetectorConfig
from privy.detect.merge import resolve_overlaps
from privy.detect.schema import Detection, Source

__all__ = [
    "Detection",
    "DetectionEngine",
    "Detector",
    "DetectorConfig",
    "PatternSpec",
    "Source",
    "resolve_overlaps",
]
