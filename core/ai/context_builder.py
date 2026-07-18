"""
=========================================================

ChannelIQ AI

Context Builder

Packages verified business facts and business signals.

NO business logic.
NO KPI calculations.
NO AI.

=========================================================
"""

from __future__ import annotations

from typing import Any

from core.analysis_result import AnalysisResult


class ContextBuilder:

    # =====================================================
    # PUBLIC
    # =====================================================

    def build(
        self,
        result: AnalysisResult,
    ) -> dict[str, Any]:

        metadata = result.metadata or {}

        # -------------------------------------------------
        # Convert Business Signals
        # -------------------------------------------------

        signals = []

        for signal in metadata.get("business_signals", []):

            if hasattr(signal, "to_dict"):

                signals.append(signal.to_dict())

            else:

                signals.append(signal)

        # -------------------------------------------------
        # Build Context
        # -------------------------------------------------

        context = {

            # ---------------------------------------------
            # Company
            # ---------------------------------------------

            "company": {

                "name": result.company_name,

                "project": result.project_name,

                "reporting_period": metadata.get(
                    "reporting_period",
                    "",
                ),

            },

            # ---------------------------------------------
            # Executive Context
            # ---------------------------------------------

            "executive_context": {

                "analysis_id": result.analysis_id,

                "generated_at": metadata.get(
                    "generated_at",
                    "",
                ),

            },

            # ---------------------------------------------
            # Verified Business Signals
            # ---------------------------------------------

            "business_signals": signals,

            # ---------------------------------------------
            # Verified Business Fact Pack
            # ---------------------------------------------

            "business_fact_pack": {

                "dashboard": {

                    "total_walkins":
                        metadata.get(
                            "total_walkins",
                            0,
                        ),

                    "fresh_walkins":
                        metadata.get(
                            "fresh_walkins",
                            0,
                        ),

                    "unique_revisits":
                        metadata.get(
                            "unique_revisits",
                            0,
                        ),

                    "bookings":
                        result.total_bookings,

                    "conversion":
                        result.conversion,

                    "participating_cp":
                        metadata.get(
                            "participating_cp",
                            0,
                        ),

                },

                "customer":

                    metadata.get(
                        "customer_journey",
                        {},
                    ),

                "booking":

                    metadata.get(
                        "booking_summary",
                        {},
                    ),

            },

        }

        return context

    # =====================================================
    # DEBUG
    # =====================================================

    def pretty_print(
        self,
        context: dict[str, Any],
    ) -> None:

        import json

        print("=" * 80)
        print("AI CONTEXT")
        print("=" * 80)

        print(

            json.dumps(

                context,

                indent=4,

                default=str,

            )

        )

        print("=" * 80)
