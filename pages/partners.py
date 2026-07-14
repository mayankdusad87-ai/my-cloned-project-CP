 st.subheader("🏆 Partner Performance")

    partner_table = result.metadata["partner_table"]

    st.dataframe(
        partner_table,
        use_container_width=True,
        hide_index=True,
      )

