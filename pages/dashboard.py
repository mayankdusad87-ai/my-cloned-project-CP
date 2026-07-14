import streamlit as st


def show_dashboard(result):

    st.header("📊 Executive Dashboard")

    st.caption(
        f"Reporting Period : {result.metadata['reporting_period']}"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Fresh Walk-ins",
            result.metadata["fresh_walkins"],
        )

    with c2:
        st.metric(
            "Repeat Walk-ins",
            result.metadata["unique_revisits"],
        )

    with c3:
        st.metric(
            "Bookings",
            result.total_bookings,
        )

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "Conversion %",
            f"{result.conversion:.2f}%"
        )

    with c5:
        st.metric(
            "Participating CP",
            result.metadata["participating_cp"],
        )

    with c6:
        st.metric(
            "Total Walk-ins",
            result.metadata["total_walkins"],
        )
