"""
=========================================================
ChannelIQ AI

Executive Reasoner

Sprint 6.0
=========================================================
"""

from __future__ import annotations
from core.ai.diagnosis_catalog import DiagnosisCatalog


class ExecutiveReasoner:
    def __init__(self):

        self.catalog = DiagnosisCatalog()
    """
    Converts Business Signals into Executive Insights.

    Input:
        List[Signal]

    Output:
        {
            "executive_insights": [...]
        }

    No AI is used here.
    This is deterministic business reasoning.
    """

    def build(self, business_signals: list) -> dict:

        executive_insights = []

        for signal in business_signals:

            executive_insights.append(

                self._build_insight(signal)

            )

        return {

            "executive_insights": executive_insights

        }

    # ======================================================
    # PRIVATE
    # ======================================================

    def _build_insight(self, signal):

        return {

            "id": signal.id,

            "title": signal.title,

            "category": signal.category,

            "priority": signal.severity,

            "status": signal.status,

            "diagnosis": signal.diagnosis,

            # Temporary
            "observation": signal.summary,

            "business_implication": self._business_implication(signal),

            "management_action": self._management_action(signal),

            "evidence": self._format_facts(signal.facts)

        }

    # ======================================================

    def _business_implication(self, signal):


        return self.catalog.business_implication(
            signal.diagnosis
    )

    # ======================================================

    def _management_action(self, signal):

        return self.catalog.management_action(
            signal.diagnosis
    )

    # ======================================================

    def _format_facts(self, facts):

        formatted = []

        for key, value in facts.items():

            formatted.append({

                "label": key.replace("_", " ").title(),

                "value": value

            })

        return formatted
