"""
=========================================================
ChannelIQ AI

Data Processor

Converts cleaned Excel data into business metrics.

Version : 1.0
=========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

import pandas as pd

from core.column_mapping import (
    VISIT_DATE,
    CUSTOMER_STAGE,
    CHANNEL_PARTNER,
    CLOSING_MANAGER,
    BOOKING_DATE,
    BUSINESS_VALUES,
)


class DataProcessor:

    """
    Extracts business metrics from the cleaned dataframe.

    This class does NOT generate AI insights.

    It only calculates facts.
    """

    def process(
        self,
        df: pd.DataFrame,
    ) -> dict:

        dashboard = self.dashboard_summary(df)

        customer = self.customer_journey(df)

        bookings = self.booking_summary(df)

        return {

            "dashboard": dashboard,

            "customer": customer,

            "bookings": bookings,

        }

    # =====================================================
    # DASHBOARD SUMMARY
    # =====================================================

    def dashboard_summary(
        self,
        df: pd.DataFrame,
    ) -> dict:

        fresh_walkins = self.total_fresh_walkins(df)

        unique_revisits = self.unique_revisits(df)

        booking_count = self.booking_count(df)

        booking_percentage = self.booking_percentage(
            booking_count,
            fresh_walkins,
        )

        active_channel_partners = self.active_channel_partners(
            df
        )

        return {

            "fresh_walkins": fresh_walkins,

            "unique_revisits": unique_revisits,

            "booking_count": booking_count,

            "booking_percentage": booking_percentage,

            "active_channel_partners":
                active_channel_partners,

        }

    # =====================================================
    # CUSTOMER JOURNEY
    # =====================================================

    def customer_journey(
        self,
        df: pd.DataFrame,
    ) -> dict:

        fresh = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fresh"]
            ]

        )

        unique = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["unique_revisit"]
            ]

        )

        second = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["second_revisit"]
            ]

        )

        third = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["third_revisit"]
            ]

        )

        fourth = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fourth_revisit"]
            ]

        )

        revisit = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["revisit"]
            ]

        )

        return {

            "fresh": fresh,

            "unique_revisit": unique,

            "second_revisit": second,

            "third_revisit": third,

            "fourth_revisit": fourth,

            "revisit": revisit,

        }

    # =====================================================
    # BOOKINGS
    # =====================================================

    def booking_summary(
        self,
        df: pd.DataFrame,
    ) -> dict:

        booking_count = self.booking_count(df)

        fresh_walkins = self.total_fresh_walkins(df)

        return {

            "booking_count": booking_count,

            "booking_percentage":

                self.booking_percentage(

                    booking_count,

                    fresh_walkins,

                )

        }

    # =====================================================
    # BASIC KPI FUNCTIONS
    # =====================================================

    def total_fresh_walkins(
        self,
        df: pd.DataFrame,
    ) -> int:

        return len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fresh"]
            ]

        )

    # -----------------------------------------------------

    def unique_revisits(
        self,
        df: pd.DataFrame,
    ) -> int:

        return len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["unique_revisit"]
            ]

        )

    # -----------------------------------------------------

    def booking_count(
        self,
        df: pd.DataFrame,
    ) -> int:

        return int(

            df[BOOKING_DATE]

            .notna()

            .sum()

        )

    # -----------------------------------------------------

    def booking_percentage(
        self,
        bookings: int,
        fresh_walkins: int,
    ) -> float:

        if fresh_walkins == 0:

            return 0.0

        return round(

            (bookings / fresh_walkins) * 100,

            2,

        )

    # -----------------------------------------------------

    def active_channel_partners(
        self,
        df: pd.DataFrame,
    ) -> int:

        temp = df.copy()

        temp[VISIT_DATE] = pd.to_datetime(

            temp[VISIT_DATE],

            errors="coerce",

            dayfirst=True,

        )

        last_30_days = (

            datetime.today()

            - timedelta(days=30)

        )

        temp = temp[
            temp[VISIT_DATE]
            >= last_30_days
        ]

        return temp[
            CHANNEL_PARTNER
        ].dropna().nunique()
