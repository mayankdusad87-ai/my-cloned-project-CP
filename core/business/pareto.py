
"""
=========================================================
Pareto Analysis Utility
=========================================================
"""

from __future__ import annotations

import pandas as pd


class ParetoAnalyzer:

    @staticmethod
    def analyse(df, group_column, value_column=None):

        if value_column is None:

            summary = (
                df
                .groupby(group_column)
                .size()
                .reset_index(name="value")
            )

        else:

            summary = (
                df
                .groupby(group_column)[value_column]
                .sum()
                .reset_index(name="value")
            )

        summary = summary.sort_values(
            "value",
            ascending=False
        )

        total = summary["value"].sum()

        summary["share"] = (
            summary["value"] / total * 100
        )

        summary["cumulative_share"] = (
            summary["share"].cumsum()
        )

        pareto = summary[
            summary["cumulative_share"] <= 80
        ].copy()

        # Always include the CP that crosses the threshold
        if len(pareto) < len(summary):
            pareto = summary.iloc[:len(pareto) + 1]

        return {

            "summary": summary,

            "pareto": pareto,

            "pareto_count": len(pareto),

            "pareto_share": round(
                pareto["share"].sum(),
                2
            ),

            "pareto_names": pareto[group_column].tolist()

        }
