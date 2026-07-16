"""
=========================================================
ChannelIQ

Workspace Tabs

=========================================================
"""

import streamlit as st


class WorkspaceTabs:

    @staticmethod
    def render():

        return st.tabs(

            [

                "📊 Executive",

                "🏢 Commercial",

                "💡 Insights",

                "🎯 Recommendations",

                "🗓️ Action Plan",

            ]

        )
