"""
=========================================================
ChannelIQ

Reusable Cards

=========================================================
"""

import streamlit as st


def begin_card():

    st.markdown(

        '<div class="channel-card">',

        unsafe_allow_html=True,

    )


def end_card():

    st.markdown(

        "</div>",

        unsafe_allow_html=True,

    )


def section_title(title):

    st.markdown(

        f'<div class="section-title">{title}</div>',

        unsafe_allow_html=True,

    )
