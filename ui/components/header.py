"""
=========================================================
ChannelIQ

Header Component

=========================================================
"""

import streamlit as st


class Header:

    @staticmethod
    def render(

        title,

        subtitle="",

    ):

        st.markdown(

            f"""

<div class="channel-title">

{title}

</div>

<div class="channel-subtitle">

{subtitle}

</div>

""",

            unsafe_allow_html=True,

        )
