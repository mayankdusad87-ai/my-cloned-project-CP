"""
=========================================================
Business Filters

Reusable business filters used across all signals.
=========================================================
"""

from __future__ import annotations


class BusinessFilters:

    @staticmethod
    def clean(series):
        """Standardize string values."""
        return (
            series
            .fillna("")
            .astype(str)
            .str.strip()
            .str.upper()
        )

    @staticmethod
    def fresh_walkins(df):

        return df[
            BusinessFilters.clean(df["customer_fresh_revisit"])
            == "FRESH"
        ]

    @staticmethod
    def booked(df):

        return df[
            BusinessFilters.clean(df["booking_done"])
            == "Y"
        ]

    @staticmethod
    def channel_partner(df):

        return df[
            BusinessFilters.clean(df["source"])
            == "CHANNEL PARTNER"
        ]

    @staticmethod
    def cp_fresh(df):

        return BusinessFilters.fresh_walkins(
            BusinessFilters.channel_partner(df)
        )

    @staticmethod
    def cp_bookings(df):

        return BusinessFilters.booked(
            BusinessFilters.channel_partner(df)
        )
