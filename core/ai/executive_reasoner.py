"""
=========================================================
ChannelIQ AI

Executive Reasoner

Sprint 6.0
=========================================================
"""

from __future__ import annotations


class ExecutiveReasoner:
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

        diagnosis = signal.diagnosis

        implications = {

            "NO_BOOKINGS":
                "No revenue was generated during the reporting period.",

            "CP_OUTPERFORMING_PROJECT":
                "The channel partner ecosystem is outperforming the project benchmark.",

            "CP_NEAR_PROJECT_AVERAGE":
                "Channel partner performance is aligned with the overall project benchmark.",

            "CP_UNDERPERFORMING_PROJECT":
                "Channel partner conversion is reducing overall commercial effectiveness.",

            "CP_SIGNIFICANTLY_UNDERPERFORMING":
                "Commercial performance is materially impacted by weak partner conversion.",

            "HIGH_NETWORK_CONCENTRATION":
                "The business is dependent on a small number of channel partners.",

            "MODERATE_NETWORK_CONCENTRATION":
                "Partner acquisition risk is beginning to increase.",

            "DIVERSIFIED_NETWORK":
                "The partner ecosystem is well diversified."

        }

        return implications.get(

            diagnosis,

            "No business implication available."

        )

    # ======================================================

    def _management_action(self, signal):

        diagnosis = signal.diagnosis

        actions = {

            "NO_BOOKINGS":
                "Review the complete sales funnel immediately.",

            "CP_OUTPERFORMING_PROJECT":
                "Scale relationships with top-performing channel partners.",

            "CP_NEAR_PROJECT_AVERAGE":
                "Continue monitoring partner performance.",

            "CP_UNDERPERFORMING_PROJECT":
                "Review partner conversion quality and sales follow-up.",

            "CP_SIGNIFICANTLY_UNDERPERFORMING":
                "Launch a focused commercial improvement plan for channel partners.",

            "HIGH_NETWORK_CONCENTRATION":
                "Recruit additional active channel partners to diversify demand.",

            "MODERATE_NETWORK_CONCENTRATION":
                "Increase engagement with mid-performing partners.",

            "DIVERSIFIED_NETWORK":
                "Maintain the current acquisition strategy."

        }

        return actions.get(

            diagnosis,

            "No management action available."

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
