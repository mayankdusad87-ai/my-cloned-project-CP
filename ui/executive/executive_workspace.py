"""
=========================================================
ChannelIQ AI

Executive Workspace

=========================================================
"""

import streamlit as st
import pandas as pd


class ExecutiveWorkspace:

    def render(self, result, ai):

        health = ai.get("health_snapshot", {})

        reporting_period = result.metadata.get("reporting_period", "-")
        analysis_id = result.analysis_id

        sentiment = health.get("status", "-")
        score = health.get("score", "-")
        confidence = health.get("confidence", 0)
        priority = health.get("management_priority", "Medium")

        # ------------------------------------------------
        # HEADER
        # ------------------------------------------------

        st.markdown(
            """
# 📊 Executive Intelligence Report

AI Powered Business Intelligence
"""
        )

        st.divider()

        left, right = st.columns([3, 1])

        with left:
            st.markdown(
                """
### Executive Intelligence Brief

Official Executive Intelligence Briefing
"""
            )

        with right:
            st.info(
                f"""
**Reporting Period**

{reporting_period}

---

**Analysis ID**

{analysis_id}
"""
            )

        st.write("")

        c1, c2, c3 = st.columns(3)

        metrics = [
            ("Sentiment", sentiment),
            ("Health Score", score),
            ("AI Confidence", f"{confidence}%"),
        ]

        for col, (title, value) in zip([c1, c2, c3], metrics):
            with col:
                st.markdown(
                    f"""
<div class="metric-card">
<div class="metric-title">{title}</div>
<div class="metric-value">{value}</div>
</div>
""",
                    unsafe_allow_html=True,
                )

        st.write("")
        st.success(f"Priority Status : {priority}")
        st.divider()

        # ------------------------------------------------
        # Executive Intelligence Highlights
        # ------------------------------------------------

        st.subheader("Executive Intelligence Highlights")

        highlights = ai.get("executive_highlights", [])

        if highlights:

            for item in highlights:

                with st.container(border=True):

                    st.markdown(f"## {item.get('title', 'Executive Insight')}")
                   

                    st.markdown("### 💡 Key Insight")
                    st.write(
                        item.get(
                            "key_insight",
                            item.get("observation", "Not Available"),
                        )
                    )

                    st.markdown("### 📊 Supporting Evidence")
                    evidence = item.get(
                        "supporting_evidence",
                        item.get("evidence", {}),
                    )
                   

                    
                    # ------------------------------------------------
                    # Evidence as List
                    # ------------------------------------------------
                    
                    if isinstance(evidence, list):
                    
                        table_data = []
                    
                        for row in evidence:
                    
                            table_data.append(
                                {
                                    "Metric": row.get("metric", ""),
                                    "Value": row.get("value", ""),
                                }
                            )
                    
                        df = pd.DataFrame(table_data)

                        st.dataframe(
                            df,
                            hide_index=True,
                            use_container_width=True,
                        )
                    
                    # ------------------------------------------------
                    # Evidence as Dictionary
                    # ------------------------------------------------
                    
                    elif isinstance(evidence, dict):
                    
                        table_data = []
                    
                        for key, value in evidence.items():
                    
                            table_data.append(
                                {
                                    "Metric": key.replace("_", " ").title(),
                                    "Value": value,
                                }
                            )
                    
                        df = pd.DataFrame(table_data)
                        st.dataframe(
                            df,
                            hide_index=True,
                            use_container_width=True,
                        )
                    
                    # ------------------------------------------------
                    # Anything Else
                    # ------------------------------------------------
                    
                    else:
                    
                        st.write(evidence)

                    

                    st.markdown("### 💼 Business Implication")
                    st.write(
                        item.get(
                            "business_implication",
                            "Not Available",
                        )
                    )

                    st.markdown("### 🎯 Recommended Management Action")
                    st.write(
                        item.get(
                            "management_action",
                             item.get(
                                "recommended_management_action",
                                item.get(
                                    "recommended_action",
                                    "Not Available",
                                ),
                             ),     
                        )
                    )

                    st.write("")

        else:
            st.info("No Executive Highlights Available.")

        st.divider()
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
            [
                "📑 Executive Summary",
                "🏢 Commercial Intelligence",
                "🔍 Key Findings",
                "🧩 Root Causes",
                "⚠ Business Risks",
                "🚀 Opportunities",
                "🎯 Recommendations",
                "📅 Monday Plan",
            ]
        )
        
        # ---------------------------------------------------
        # Executive Summary
        # ---------------------------------------------------
        
        with tab1:
        
            st.subheader("Executive Summary")
        
            st.write(
                ai.get(
                    "executive_summary",
                    "Executive Summary unavailable."
                )
            )
        
            st.divider()
        
            st.subheader("Commercial Diagnosis")
        
            st.write(
                ai.get(
                    "diagnosis",
                    "Diagnosis unavailable."
                )
            )
        
        # ---------------------------------------------------
        # Commercial Intelligence
        # ---------------------------------------------------
        
        with tab2:
        
            signal = result.metadata.get("commercial_intelligence", {})
        
            if signal:
        
                st.subheader(signal.get("title", "Commercial Intelligence"))
        
                st.success(signal.get("summary", ""))
        
                evidence = signal.get("evidence", {})
        
                c1, c2, c3 = st.columns(3)
        
                c1.metric(
                    "Overall Conversion",
                    f"{evidence.get('overall_conversion',0)}%"
                )
        
                c2.metric(
                    "CP Conversion",
                    f"{evidence.get('cp_conversion',0)}%"
                )
        
                c3.metric(
                    "Gap",
                    f"{evidence.get('conversion_gap',0)}%"
                )
        
                st.info(signal.get("business_impact", ""))
        
                st.warning(signal.get("management_question", ""))
        
            else:
        
                st.info("Commercial Intelligence unavailable.")
        
        # ---------------------------------------------------
        # Key Findings
        # ---------------------------------------------------
        
        with tab3:
        
            findings = ai.get("key_findings", [])
        
            if findings:
        
                for finding in findings:
        
                    with st.container(border=True):
        
                        st.markdown(f"### {finding.get('title')}")
        
                        st.write(finding.get("insight"))
        
                        if finding.get("evidence"):
        
                            st.caption(f"Evidence : {finding.get('evidence')}")
        
            else:
        
                st.info("No findings available.")
        
        # ---------------------------------------------------
        # Root Causes
        # ---------------------------------------------------
        
        with tab4:
        
            causes = ai.get("root_causes", [])
        
            if causes:
        
                for cause in causes:
        
                    with st.container(border=True):
        
                        st.markdown(f"### {cause.get('cause')}")
        
                        st.write(cause.get("business_impact"))
        
            else:
        
                st.info("No root causes identified.")
        
        # ---------------------------------------------------
        # Risks
        # ---------------------------------------------------
        
        with tab5:
        
            risks = ai.get("risks", [])
        
            if risks:
        
                for risk in risks:
        
                    with st.container(border=True):
        
                        st.markdown(f"### {risk.get('risk')}")
        
                        st.write(risk.get("mitigation"))
        
            else:
        
                st.success("No significant risks identified.")
        
        # ---------------------------------------------------
        # Opportunities
        # ---------------------------------------------------
        
        with tab6:
        
            opportunities = ai.get("opportunities", [])
        
            if opportunities:
        
                for opportunity in opportunities:
        
                    with st.container(border=True):
        
                        st.markdown(
                            f"### {opportunity.get('opportunity')}"
                        )
        
                        st.write(
                            opportunity.get("recommended_action")
                        )
        
            else:
        
                st.info("No opportunities identified.")
        
        # ---------------------------------------------------
        # Recommendations
        # ---------------------------------------------------
        
        with tab7:
        
            recommendations = ai.get("recommendations", [])
        
            if recommendations:
        
                for rec in recommendations:
        
                    with st.container(border=True):
        
                        st.markdown(
                            f"### Priority : {rec.get('priority')}"
                        )
        
                        st.write(rec.get("action"))
        
                        col1, col2 = st.columns(2)
        
                        with col1:
        
                            st.caption(
                                f"Owner : {rec.get('owner')}"
                            )
        
                        with col2:
        
                            st.caption(
                                f"Timeline : {rec.get('timeline')}"
                            )
        
            else:
        
                st.info("No recommendations available.")
        
        # ---------------------------------------------------
        # Monday Plan
        # ---------------------------------------------------
        
        with tab8:
        
            plan = ai.get("monday_plan", [])
        
            if plan:
        
                for i, task in enumerate(plan, start=1):
        
                    st.checkbox(
                        f"Action {i} : {task}",
                        value=False,
                        disabled=True,
                    )
        
            else:
        
                st.info("No immediate action plan available.")
        
               
