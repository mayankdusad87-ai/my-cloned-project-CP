"""
=========================================================

ChannelIQ AI

Context Builder

Builds the verified AI context.

This class does NOT perform any business analysis.
It only packages verified facts and business signals.

=========================================================
"""

from __future__ import annotations

from typing import Any

from core.analysis_result import AnalysisResult


class ContextBuilder:

    def build(
        self,
        result: AnalysisResult,
    ) -> dict[str, Any]:

        metadata = result.metadata or {}

        context = {

            # -------------------------------------------------
            # COMPANY
            # -------------------------------------------------

            "company": {

                "name": result.company_name,
                "project": result.project_name,
                "reporting_period": metadata.get(
                    "reporting_period",
                    "",
                ),

            },

            # -------------------------------------------------
            # EXECUTIVE CONTEXT
            # -------------------------------------------------

            "executive_context": {

                "analysis_id": result.analysis_id,

                "generated_at": metadata.get(
                    "generated_at",
                    "",
                ),

            },

            # -------------------------------------------------
            # VERIFIED BUSINESS SIGNALS
            # -------------------------------------------------

            "business_signals": metadata.get(
                "business_signals",
                [],
            ),

            # -------------------------------------------------
            # VERIFIED FACT PACK
            # -------------------------------------------------

            "business_fact_pack": {

                "dashboard": {

                    "total_walkins": metadata.get(
                        "total_walkins",
                        0,
                    ),

                    "fresh_walkins": metadata.get(
                        "fresh_walkins",
                        0,
                    ),

                    "unique_revisits": metadata.get(
                        "unique_revisits",
                        0,
                    ),

                    "bookings": result.total_bookings,

                    "conversion": result.conversion,

                    "participating_cp": metadata.get(
                        "participating_cp",
                        0,
                    ),

                },

                "customer": metadata.get(
                    "customer_journey",
                    {},
                ),

                "booking": metadata.get(
                    "booking_summary",
                    {},
                ),

            },

        }

        return context
