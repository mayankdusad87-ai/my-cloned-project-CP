"""
=========================================================
ChannelIQ AI

Data Processor

Converts raw Excel data into business metrics.

This class DOES NOT calculate scores.
It only extracts business facts.

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

    def process(self, df: pd.DataFrame) -> dict:
        """
        Process dataframe and return all business metrics.
        """

        metrics = {}

        metrics["total_records"] = len(df)

        metrics["fresh_walkins"] = self.total_fresh_walkins(df)

        metrics["unique_revisits"] = self.unique_revisits(df)

        metrics["booking_count"] = self.booking_count(df)

        metrics["booking_percentage"] = self.booking_percentage(metrics)

        metrics["active_channel_partners"] = self.active_channel_partners(df)

        metrics["top_channel_partners"] = self.top_channel_partners(df)

        metrics["top_closing_managers"] = self.top_closing_managers(df)

        return metrics

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

    # =====================================================

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

    # =====================================================

    def booking_count(
        self,
        df: pd.DataFrame,
    ) -> int:

        return df[BOOKING_DATE].notna().sum()

    # =====================================================

    def booking_percentage(
        self,
        metrics: dict,
    ) -> float:

        fresh = metrics["fresh_walkins"]

        bookings = metrics["booking_count"]

        if fresh == 0:

            return 0

        return round(

            (bookings / fresh) * 100,

            2

        )

    # =====================================================

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

        last_30_days = datetime.today() - timedelta(days=30)

        temp = temp[
            temp[VISIT_DATE] >= last_30_days
        ]

        return temp[
            CHANNEL_PARTNER
        ].dropna().nunique()

    # =====================================================

    def top_channel_partners(
        self,
        df: pd.DataFrame,
        top: int = 10,
    ) -> pd.DataFrame:

        result = (

            df.groupby(CHANNEL_PARTNER)

            .size()

            .reset_index(name="walkins")

            .sort_values(
                "walkins",
                ascending=False
            )

            .head(top)

        )

        return result

    # =====================================================

    def top_closing_managers(
        self,
        df: pd.DataFrame,
        top: int = 10,
    ) -> pd.DataFrame:

        result = (

            df.groupby(CLOSING_MANAGER)

            .size()

            .reset_index(name="walkins")

            .sort_values(
                "walkins",
                ascending=False
            )

            .head(top)

        )

        return result
