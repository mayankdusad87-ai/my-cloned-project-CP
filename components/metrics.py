"""
Metric Cards
"""

import streamlit as st


def metric_card(
    title,
    value,
    delta=None,
    delta_color="normal",
):
    """
    Standard KPI card.
    """

    st.metric(
        label=title,
        value=value,
        delta=delta,
        delta_color=delta_color,
        border=True,
    )
