"""Privy — policy-driven PII/secrets scrubber for LLM inputs, outputs, and logs.

Typical use::

    import privy

    guard = privy.Guard.from_policy("policies/default.yaml", audit_db="audit.db")

    @privy.redacted_call(guard, adapter=privy.ChatMessagesAdapter())
    def chat(*, messages): ...

    safe_line = guard.for_logs(f"user said: {prompt}")
"""

from privy.audit import AuditRecorder, MemoryAuditSink, Outcome, SQLiteAuditSink
from privy.detect import Detection, DetectionEngine, DetectorConfig, Source
from privy.middleware import (
    BlockedError,
    ChatMessagesAdapter,
    Guard,
    GuardSession,
    PrivyLogFilter,
    TextAdapter,
    redacted_call,
)
from privy.policy import Action, Destination, Policy, PolicyEngine, ScrubResult, load_policy

__all__ = [
    "Action",
    "AuditRecorder",
    "BlockedError",
    "ChatMessagesAdapter",
    "Destination",
    "Detection",
    "DetectionEngine",
    "DetectorConfig",
    "Guard",
    "GuardSession",
    "MemoryAuditSink",
    "Outcome",
    "Policy",
    "PolicyEngine",
    "PrivyLogFilter",
    "SQLiteAuditSink",
    "ScrubResult",
    "Source",
    "TextAdapter",
    "load_policy",
    "redacted_call",
]
__version__ = "0.1.0"
