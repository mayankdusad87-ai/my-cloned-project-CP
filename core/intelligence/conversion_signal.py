"""
=========================================================
ChannelIQ AI

Commercial Conversion Signal

Sprint 5.1.1

=========================================================
"""

from __future__ import annotations

from config import AVERAGE_BOOKING_VALUE
from core.intelligence.signal import Signal


class ConversionSignal:
    """
    Commercial Conversion Intelligence

    Business Dictionary

    Overall Fresh Walk-ins
        Customer Fresh/Revisit = Fresh

    Overall Bookings
        Booking Done = Y

    CP Fresh Walk-ins
        Source = Channel Partner
        AND Fresh

    CP Bookings
        Source = Channel Partner
        AND Booking Done = Y
    """

    def analyse(self, df):

        # ==================================================
        # Overall Fresh Walk-ins
        # ==================================================

        overall_fresh_walkins = len(

            df[
                df["customer_fresh_revisit"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "FRESH"
            ]

        )

        # ==================================================
        # Overall Bookings
        # ==================================================

        overall_bookings = len(

            df[
                df["booking_done"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "Y"
            ]

        )

        # ==================================================
        # CP Fresh Walk-ins
        # ==================================================

        cp_fresh_walkins = len(

            df[

                (df["source"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "CHANNEL PARTNER")

                &

                (df["customer_fresh_revisit"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "FRESH")

            ]

        )

        # ==================================================
        # CP Bookings
        # ==================================================

        cp_bookings = len(

            df[

                (df["source"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "CHANNEL PARTNER")

                &

                (df["booking_done"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "Y")

            ]

        )

        # ==================================================
        # Conversion
        # ==================================================

        overall_conversion = (

            overall_bookings / overall_fresh_walkins * 100

            if overall_fresh_walkins

            else 0

        )

        cp_conversion = (

            cp_bookings / cp_fresh_walkins * 100

            if cp_fresh_walkins

            else 0

        )

        conversion_gap = (

            cp_conversion - overall_conversion

        )

        # ==================================================
        # Channel Partner Intelligence
        # ==================================================

        cp_df = df[

            (df["source"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "CHANNEL PARTNER")

            &

            (df["customer_fresh_revisit"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "FRESH")

        ].copy()

        cp_summary = (

            cp_df

            .groupby("channel_partner")

            .agg(

                fresh_walkins=("channel_partner", "count"),

                bookings=(

                    "booking_done",

                    lambda x: (

                        x.astype(str)

                        .str.strip()

                        .str.upper()

                        == "Y"

                    ).sum()

                )

            )

            .reset_index()

        )

        if not cp_summary.empty:

            cp_summary["conversion"] = (

                cp_summary["bookings"]

                / cp_summary["fresh_walkins"]

                * 100

            ).round(2)

        else:

            cp_summary["conversion"] = []



        # ----------------------------------------------
        # Top Conversion Partners
        # ----------------------------------------------

        top_conversion_partners = (

            cp_summary

            .sort_values(

                ["conversion", "bookings"],

                ascending=[False, False]

            )

            .head(5)

            .to_dict("records")

        )



        # ----------------------------------------------
        # Top Booking Partners
        # ----------------------------------------------

        top_booking_partners = (

            cp_summary

            .sort_values(

                "bookings",

                ascending=False

            )

            .head(5)

            .to_dict("records")

        )



        # ----------------------------------------------
        # High Walk-in / Low Conversion Partners
        # ----------------------------------------------

        low_conversion_high_volume = (

            cp_summary[

                cp_summary["fresh_walkins"] >= 5

            ]

            .sort_values(

                ["conversion", "fresh_walkins"],

                ascending=[True, False]

            )

            .head(5)

            .to_dict("records")

        )



        # ----------------------------------------------
        # Partner Dependency
        # ----------------------------------------------

        if cp_summary["fresh_walkins"].sum() > 0:

            partner_dependency = round(

                cp_summary["fresh_walkins"].max()

                /

                cp_summary["fresh_walkins"].sum()

                * 100,

                2

            )

        else:

            partner_dependency = 0
        # ==================================================
        # Expected Bookings
        # ==================================================

        

        # ==================================================
        # Expected Bookings
        # ==================================================

        expected_cp_bookings = (

            cp_fresh_walkins

            * overall_conversion

            / 100

        )

        lost_bookings = max(

            0,

            round(expected_cp_bookings - cp_bookings)

        )

        revenue_opportunity = (

            lost_bookings

            * AVERAGE_BOOKING_VALUE

        )

        # ==================================================
        # Severity
        # ==================================================

        if overall_bookings == 0:

            severity = "Critical"

            status = "Negative"

            summary = (

                "No bookings were recorded during the reporting period."

            )

        else:

            if conversion_gap >= 0:

                severity = "Excellent"

                status = "Positive"

                summary = (

                     f"Channel Partner conversion ({cp_conversion:.2f}%) "
                     f"exceeded the overall project conversion "
                     f"({overall_conversion:.2f}%) during the reporting period."
                )

            elif conversion_gap >= -1:

                severity = "Low"

                status = "Neutral"

                summary = (

                    f"Channel Partner conversion ({cp_conversion:.2f}%) "
                    f"was marginally below the overall project conversion "
                    f"({overall_conversion:.2f}%)."


                )

            elif conversion_gap >= -3:

                severity = "Medium"

                status = "Negative"

                summary = (

                    f"Channel Partner conversion ({cp_conversion:.2f}%) "
                    f"was below the overall project conversion "
                    f"({overall_conversion:.2f}%), indicating reduced commercial effectiveness." 
                )
            else:

                severity = "Critical"

                status = "Negative"

                summary = (

                    "Channel Partner conversion is significantly below the project benchmark."

                )
        # ==================================================
        # Diagnosis
        # ==================================================
        if overall_bookings == 0:
            
                diagnosis = "NO_BOOKINGS"
            
        elif conversion_gap >= 0:
            
                diagnosis = "CP_OUTPERFORMING_PROJECT"
            
        elif conversion_gap >= -1:
            
                diagnosis = "CP_NEAR_PROJECT_AVERAGE"
            
        elif conversion_gap >= -3:
            
                diagnosis = "CP_UNDERPERFORMING_PROJECT"
            
        else:
            
                diagnosis = "CP_SIGNIFICANTLY_UNDERPERFORMING"   

        facts = {

            "overall_fresh_walkins": overall_fresh_walkins,
        
            "overall_bookings": overall_bookings,
        
            "overall_conversion": round(overall_conversion, 2),
        
            "cp_fresh_walkins": cp_fresh_walkins,
        
            "cp_bookings": cp_bookings,
        
            "cp_conversion": round(cp_conversion, 2),
        
            "conversion_gap": round(conversion_gap, 2),
        
            "expected_cp_bookings": round(expected_cp_bookings),
        
            "lost_bookings": lost_bookings,
        
            "revenue_opportunity": revenue_opportunity,
        
            "top_conversion_partners": top_conversion_partners,
        
            "top_booking_partners": top_booking_partners,
        
            "low_conversion_high_volume": low_conversion_high_volume,
        
            "partner_dependency_percent": partner_dependency,
        
        }
                            

        # ==================================================
        # Signal
        # ==================================================

        signal = Signal(

            id="commercial_conversion",

            title="Commercial Conversion",

            category="Commercial",

            severity=severity,

            status=status,
            
            diagnosis=diagnosis,

            facts=facts,

            summary=summary,

            business_impact=(

                f"Estimated opportunity of "

                f"{lost_bookings} additional bookings "

                f"worth approximately ₹{revenue_opportunity:,.0f}."

            ),

            management_question=(

                "Is the Channel Partner network helping or hurting overall project conversion?"

            ),

            evidence= facts,

               

        )

        return signal
