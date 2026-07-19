"""
=========================================================
ChannelIQ AI

Findings Engine

Converts Business Signals into Findings.

No AI.
No business calculations.
Only transforms verified Business Signals into
findings for downstream AI and UI consumption.

=========================================================
"""

from __future__ import annotations

from typing import Any


class FindingsEngine:
    """
    Converts Business Signals into standardized findings.
    """

    # =====================================================
    # PUBLIC
    # =====================================================

    def analyse(
        self,
        context: dict[str, Any],
    ) -> dict[str, list]:

        findings = []
        risks = []
        opportunities = []

        business_signals = context.get(
            "business_signals",
            [],
        )

        for signal in business_signals:

            finding = {

                "id": signal.id,

                "title": signal.title,

                "category": signal.category,

                "priority": signal.severity,

                "status": signal.status,

                "diagnosis": signal.diagnosis,

                "insight": signal.summary,

                "business_impact": signal.business_impact,

                "management_question": signal.management_question,

                "evidence": signal.evidence,

            }

            findings.append(finding)

            if signal.status.lower() == "negative":

                risks.append(finding)

            elif signal.status.lower() == "positive":

                opportunities.append(finding)

        return {

            "findings": self.prioritize(findings),

            "risks": self.prioritize(risks),

            "opportunities": self.prioritize(opportunities),

        }

    # =====================================================
    # PRIORITIZE
    # =====================================================

    def prioritize(
        self,
        findings: list,
    ) -> list:

        priority_order = {

            "Critical": 0,

            "High": 1,

            "Medium": 2,

            "Low": 3,

            "Excellent": 4,

        }

        return sorted(

            findings,

            key=lambda x: priority_order.get(

                x["priority"],

                99,

            ),

        )
