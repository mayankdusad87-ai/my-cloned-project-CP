"""
=========================================================
ChannelIQ AI

Business Object Factory

Converts Business Signals into Business Objects
consumable by the AI Consulting Layer.

=========================================================
"""

from __future__ import annotations

from core.business_objects import CommercialObject


class BusinessObjectFactory:

    def commercial(
        self,
        signal,
    ) -> CommercialObject:

        return CommercialObject(

            title=signal.title,

            category=signal.category,

            severity=signal.severity,

            status=signal.status,

            observation=signal.summary,

            management_question=signal.management_question,

            evidence=[

                {
                    "metric": "Overall Fresh Walk-ins",
                    "value": signal.evidence.get(
                        "overall_fresh_walkins",
                        0,
                    ),
                },

                {
                    "metric": "Overall Bookings",
                    "value": signal.evidence.get(
                        "overall_bookings",
                        0,
                    ),
                },

                {
                    "metric": "Overall Conversion",
                    "value": f"{signal.evidence.get('overall_conversion',0)}%",
                },

                {
                    "metric": "CP Fresh Walk-ins",
                    "value": signal.evidence.get(
                        "cp_fresh_walkins",
                        0,
                    ),
                },

                {
                    "metric": "CP Conversion",
                    "value": f"{signal.evidence.get('cp_conversion',0)}%",
                },

                {
                    "metric": "Conversion Gap",
                    "value": f"{signal.evidence.get('conversion_gap',0)}%",
                },

            ],

        )



