from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Signal:
    """
    Standard Business Signal produced by the Business Engine.

    The Business Engine is responsible ONLY for:
    - Computing verified business facts
    - Assigning a diagnosis
    - Setting severity/status

    Any English narrative (executive summaries, recommendations,
    business impact, management questions, etc.) belongs to the AI layer.
    """

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------
    id: str
    title: str
    category: str

    # ------------------------------------------------------------------
    # Business Classification
    # ------------------------------------------------------------------
    severity: str
    status: str
    diagnosis: str = ""

    # ------------------------------------------------------------------
    # Structured Business Facts (Primary Output)
    # ------------------------------------------------------------------
    facts: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Legacy Fields
    # Keep temporarily for backward compatibility.
    # These will be removed after the AI layer is migrated.
    # ------------------------------------------------------------------
    summary: str = ""
    business_impact: str = ""
    management_question: str = ""
    evidence: Dict[str, Any] = field(default_factory=dict)
