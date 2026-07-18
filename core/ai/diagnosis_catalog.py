"""
=========================================================

ChannelIQ AI

Diagnosis Catalog

Maps Business Engine diagnosis codes into
business implications and management actions.

This file contains NO business calculations.
It only translates diagnosis codes into
consistent business language.

=========================================================
"""

from __future__ import annotations


class DiagnosisCatalog:

    def __init__(self):

        self._catalog = {

            # -------------------------------------------------
            # Commercial
            # -------------------------------------------------

            "NO_BOOKINGS": {

                "business_implication":
                    "No revenue was generated during the reporting period.",

                "management_action":
                    "Review the complete sales funnel immediately.",

            },

            "CP_OUTPERFORMING_PROJECT": {

                "business_implication":
                    "The channel partner ecosystem is outperforming the overall project benchmark.",

                "management_action":
                    "Scale relationships with top-performing channel partners.",

            },

            "CP_NEAR_PROJECT_AVERAGE": {

                "business_implication":
                    "Channel partner performance is aligned with the overall project benchmark.",

                "management_action":
                    "Continue monitoring partner performance.",

            },

            "CP_UNDERPERFORMING_PROJECT": {

                "business_implication":
                    "Channel partner conversion is reducing overall commercial effectiveness.",

                "management_action":
                    "Review partner conversion quality and sales follow-up.",

            },

            "CP_SIGNIFICANTLY_UNDERPERFORMING": {

                "business_implication":
                    "Commercial performance is materially impacted by weak partner conversion.",

                "management_action":
                    "Launch a focused commercial improvement plan for channel partners.",

            },

            # -------------------------------------------------
            # Partner Network
            # -------------------------------------------------

            "HIGH_NETWORK_CONCENTRATION": {

                "business_implication":
                    "The business is dependent on a small number of channel partners.",

                "management_action":
                    "Recruit additional active channel partners to diversify demand.",

            },

            "MODERATE_NETWORK_CONCENTRATION": {

                "business_implication":
                    "Partner acquisition risk is beginning to increase.",

                "management_action":
                    "Increase engagement with mid-performing partners.",

            },

            "DIVERSIFIED_NETWORK": {

                "business_implication":
                    "The partner ecosystem is well diversified.",

                "management_action":
                    "Maintain the current acquisition strategy.",

            },

        }

    # =====================================================

    def business_implication(
        self,
        diagnosis: str,
    ) -> str:

        return self._catalog.get(
            diagnosis,
            {},
        ).get(
            "business_implication",
            "No business implication available.",
        )

    # =====================================================

    def management_action(
        self,
        diagnosis: str,
    ) -> str:

        return self._catalog.get(
            diagnosis,
            {},
        ).get(
            "management_action",
            "No management action available.",
        )
