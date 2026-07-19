"""
=========================================================
ChannelIQ AI

Partner Performance Signal

Sprint 5.2.0
=========================================================
"""

from __future__ import annotations

from core.intelligence.signal import Signal
from core.business.filters import BusinessFilters
from core.business.pareto import ParetoAnalyzer


class PartnerPerformanceSignal:

    def analyse(self, df):

        # --------------------------------------------------
        # Channel Partner Fresh Walk-ins
        # --------------------------------------------------

        cp_df = BusinessFilters.cp_fresh(df)

        # --------------------------------------------------
        # Pareto Analysis
        # --------------------------------------------------

        pareto = ParetoAnalyzer.analyse(

            cp_df,

            group_column="channel_partner"

        )

        # --------------------------------------------------
        # Facts (Primary Business Output)
        # --------------------------------------------------

        facts = {

            "active_cp": cp_df["channel_partner"].nunique(),

            "pareto_cp_count": pareto["pareto_count"],

            "pareto_walkin_share": pareto["pareto_share"],

            "pareto_cp_names": pareto["pareto_names"]

        }

        # --------------------------------------------------
        # Diagnosis
        # --------------------------------------------------

        share = pareto["pareto_share"]

        if share >= 80:

            diagnosis = "HIGH_NETWORK_CONCENTRATION"

            severity = "High"

            status = "Negative"

            summary = (
                f"{pareto['pareto_count']} channel partners generate "
                f"{share:.1f}% of fresh walk-ins."
            )

            business_impact = (
                "The business is heavily dependent on a small group of channel partners."
            )

        elif share >= 65:

            diagnosis = "MODERATE_NETWORK_CONCENTRATION"

            severity = "Medium"

            status = "Neutral"

            summary = (
                "Fresh walk-ins are moderately concentrated among top-performing partners."
            )

            business_impact = (
                "Increasing contribution from the remaining partner network can reduce dependency risk."
            )

        else:

            diagnosis = "DIVERSIFIED_NETWORK"

            severity = "Low"

            status = "Positive"

            summary = (
                "Fresh walk-ins are well distributed across the partner network."
            )

            business_impact = (
                "The partner ecosystem appears healthy and diversified."
            )

        management_question = (
            "Is the partner acquisition network sufficiently diversified?"
        )

        # --------------------------------------------------
        # Return Signal
        # --------------------------------------------------

        return Signal(

            id="partner_performance",

            title="Partner Performance",

            category="Partner",

            severity=severity,

            status=status,

            diagnosis=diagnosis,

            facts=facts,

            # --------------------------------------------------
            # Legacy fields (temporary)
            # --------------------------------------------------

            summary=summary,

            business_impact=business_impact,

            management_question=management_question,

            evidence=facts.copy()

        )
