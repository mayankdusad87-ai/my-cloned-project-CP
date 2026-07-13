"""
=========================================================
ChannelIQ AI

Context Builder

Creates a structured business context
for the AI Consulting Layer.

Version : 1.0
=========================================================
"""

from __future__ import annotations

from core.analysis_result import AnalysisResult


class ContextBuilder:
    """
    Converts AnalysisResult into a structured
    AI-ready business context.
    """

    def build(
        self,
        result: AnalysisResult,
    ) -> dict:

        context = {

            # -----------------------------------------
            # Company Information
            # -----------------------------------------

            "company": result.company_name,

            "project": result.project_name,

            "reporting_period":

                result.metadata.get(
                    "reporting_period",
                    "",
                ),

            # -----------------------------------------
            # Executive KPIs
            # -----------------------------------------

            "dashboard": {

                "total_walkins":

                    result.metadata.get(
                        "total_walkins",
                        0,
                    ),

                "fresh_walkins":

                    result.metadata.get(
                        "fresh_walkins",
                        0,
                    ),

                "unique_revisits":

                    result.metadata.get(
                        "unique_revisits",
                        0,
                    ),

                "bookings":

                    result.total_bookings,

                "conversion":

                    result.conversion,

                "participating_cp":

                    result.metadata.get(
                        "participating_cp",
                        0,
                    ),

            },

            # -----------------------------------------
            # Business Tables
            # -----------------------------------------

            "partner_table":

                result.metadata.get(
                    "partner_table",
                    None,
                ),

            "customer_journey":

                result.metadata.get(
                    "customer_journey",
                    None,
                ),

            "booking_summary":

                result.metadata.get(
                    "booking_summary",
                    None,
                ),

            # -----------------------------------------
            # Existing AI Output
            # (temporary)
            # -----------------------------------------

            "executive_summary":

                result.executive_summary,

            "recommendations":

                result.recommendations,

        }

        return context
