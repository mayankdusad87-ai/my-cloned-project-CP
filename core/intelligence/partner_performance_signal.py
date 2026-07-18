"""
=========================================================
ChannelIQ AI

Partner Performance Signal

Sprint 5.2.0
=========================================================
"""

from __future__ import annotations

from core.intelligence.signal import Signal


class PartnerPerformanceSignal:

    def analyse(self, df):

        # TODO
        # Active CP
        # Pareto Analysis
        # Micro Market Analysis
        # Revisit Analysis

        signal = Signal(

            id="partner_performance",

            title="Partner Performance",

            category="Channel Partner",

            severity="Low",

            status="Neutral",

            diagnosis="NOT_ANALYSED",

            facts={},

            summary="",

            business_impact="",

            management_question="",

            evidence={}

        )

        return signal
