"""
=========================================================
ChannelIQ

Card Component

Reusable white card container

=========================================================
"""

import streamlit as st


class Card:

    @staticmethod
    def begin():

        st.markdown(
            """
            <div class="channel-card">
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def end():

        st.markdown(
            """
            </div>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def title(text: str):

        st.markdown(
            f"""
            <div class="section-title">
                {text}
            </div>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def divider():

        st.markdown(
            "<hr style='border:1px solid #ECECEC;'>",
            unsafe_allow_html=True,
        )
