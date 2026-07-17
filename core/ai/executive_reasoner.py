from __future__ import annotations


class ExecutiveReasoner:

    def build(
        self,
        context: dict,
        executive_highlights: list,
        findings: dict,
    ) -> dict:

        insights = []

        for highlight in executive_highlights:

            insights.append(
                self._reason_highlight(highlight)
            )

        return {

            "executive_insights": insights

        }

    def _reason_highlight(
        self,
        highlight: dict,
    ) -> dict:

        return {

            "title": highlight.get("title"),

            "priority": highlight.get("priority"),

            "observation": highlight.get("observation"),

            "evidence": self._format_evidence(
                highlight.get("evidence", {})
            ),

            "business_implication": "",

            "management_action": "",

        }

    def _format_evidence(
        self,
        evidence: dict,
    ):

        formatted = []

        for key, value in evidence.items():

            formatted.append({

                "label": key.replace("_", " ").title(),

                "value": value,

            })

        return formatted
