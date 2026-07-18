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

            group_column="channel_partner_company"

        )

        # --------------------------------------------------
        # Facts
        # --------------------------------------------------

        facts = {}

        # --------------------------------------------------
        # Diagnosis
        # --------------------------------------------------

      

        share = pareto["pareto_share"]
        
        if share >= 80:
        
            diagnosis = "HIGH_NETWORK_CONCENTRATION"
        
            severity = "High"
        
            status = "Negative"
        
        elif share >= 65:
        
            diagnosis = "MODERATE_NETWORK_CONCENTRATION"
        
            severity = "Medium"
        
            status = "Neutral"
        
        else:
        
            diagnosis = "DIVERSIFIED_NETWORK"
        
            severity = "Low"
        
            status = "Positive"

        # --------------------------------------------------
        # Return Signal
        # --------------------------------------------------

        return Signal(

            id="partner_performance",

            title="Partner Performance",

            category="Channel Partner",

            severity=severity,

            status=status,

            diagnosis=diagnosis,

            facts={

                "active_cp": cp_df["channel_partner_company"].nunique(),
            
                "pareto_cp_count": pareto["pareto_count"],
            
                "pareto_walkin_share": pareto["pareto_share"],
            
                "pareto_cp_names": pareto["pareto_names"]
            
            },

            summary="",

            business_impact="",

            management_question="",

            evidence=facts

        )
