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
    Calculates Commercial Conversion Intelligence.
    """

    def analyse(self, df):

        # ------------------------------------------
        # Overall Walk-ins (Fresh only)
        # ------------------------------------------

        overall_walkins = len(

            df[
                df["Customer Fresh/Revisit"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "FRESH"
            ]

        )

        # ------------------------------------------
        # Overall Bookings
        # ------------------------------------------

        overall_bookings = len(

            df[
                df["Booking Done"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "Y"
            ]

        )

        # ------------------------------------------
        # CP Walk-ins
        # ------------------------------------------

        cp_walkins_df = df[

            (df["Source"].astype(str).str.strip().str.upper() == "CHANNEL PARTNER")

            &

            (
                df["Customer Fresh/Revisit"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "FRESH"
            )

        ]

        cp_walkins = len(cp_walkins_df)

        # ------------------------------------------
        # CP Bookings
        # ------------------------------------------

        cp_bookings = len(

            df[

                (df["Source"].astype(str).str.strip().str.upper() == "CHANNEL PARTNER")

                &

                (
                    df["Booking Done"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "Y"
                )

            ]

        )

        # ------------------------------------------
        # Conversion
        # ------------------------------------------

        overall_conversion = (

            overall_bookings / overall_walkins * 100

            if overall_walkins else 0

        )

        cp_conversion = (

            cp_bookings / cp_walkins * 100

            if cp_walkins else 0

        )

        gap = cp_conversion - overall_conversion

        # ------------------------------------------
        # Expected Bookings
        # ------------------------------------------

        expected_cp_bookings = (

            cp_walkins * overall_conversion / 100

        )

        lost_bookings = max(

            0,

            round(expected_cp_bookings - cp_bookings)

        )

        revenue_opportunity = (

            lost_bookings

            * AVERAGE_BOOKING_VALUE

        )

        # ------------------------------------------
        # Severity
        # ------------------------------------------

        if gap >= 0:

            severity = "Excellent"

            status = "Positive"

        elif gap >= -1:

            severity = "Low"

            status = "Neutral"

        elif gap >= -3:

            severity = "Medium"

            status = "Negative"

        else:

            severity = "Critical"

            status = "Negative"

        # ------------------------------------------
        # Business Summary
        # ------------------------------------------

        if gap >= 0:

            summary = (

                "Channel Partner conversion is meeting or exceeding "

                "overall project conversion."

            )

        else:

            summary = (

                "Channel Partner conversion is below "

                "overall project conversion."

            )

        # ------------------------------------------
        # Signal
        # ------------------------------------------

        signal = Signal(

            id="commercial_conversion",

            title="Commercial Conversion",

            category="Commercial",

            severity=severity,

            status=status,

            summary=summary,

            business_impact=(

                f"Estimated opportunity of "

                f"{lost_bookings} additional bookings."

            ),

            management_question=(

                "Is the Channel Partner network "

                "helping or hurting project conversion?"

            ),

            evidence={

                "overall_walkins": overall_walkins,

                "overall_bookings": overall_bookings,

                "overall_conversion": round(overall_conversion,2),

                "cp_walkins": cp_walkins,

                "cp_bookings": cp_bookings,

                "cp_conversion": round(cp_conversion,2),

                "gap": round(gap,2),

                "expected_cp_bookings": round(expected_cp_bookings),

                "lost_bookings": lost_bookings,

                "revenue_opportunity": revenue_opportunity,

            },

        )

        return signal
