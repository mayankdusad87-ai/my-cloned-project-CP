"""
=========================================================
ChannelIQ AI

Reporting Period Engine

Uses the Excel column:

Month name

Example values

Jan 25
Feb 25
Sep 25

=========================================================
"""

from __future__ import annotations

import pandas as pd


class ReportingPeriod:

    """
    Handles reporting period discovery,
    sorting and filtering.
    """

    def __init__(self):

        self.column = "reporting_period"

    # ----------------------------------------------------

    def prepare(self, df: pd.DataFrame) -> pd.DataFrame:

        """
        Creates an internal datetime column
        for sorting.

        Excel value:
            Sep 25

        Internal:
            2025-09-01
        """

        df = df.copy()

        df["_period"] = pd.to_datetime(

            df[self.column],

            format="%b %y",

            errors="coerce",

        )

        return df

    # ----------------------------------------------------

    def available_periods(

        self,

        df: pd.DataFrame,

    ) -> list[str]:

        """
        Returns

        January 2025
        February 2025
        ...
        """

        df = self.prepare(df)

        periods = (

            df["_period"]

            .dropna()

            .drop_duplicates()

            .sort_values()

        )

        return [

            p.strftime("%B %Y")

            for p in periods

        ]

    # ----------------------------------------------------

    def latest_period(

        self,

        df: pd.DataFrame,

    ) -> str | None:

        periods = self.available_periods(df)

        if len(periods) == 0:

            return None

        return periods[-1]

    # ----------------------------------------------------

    def filter(

        self,

        df: pd.DataFrame,

        period: str,

    ) -> pd.DataFrame:

        """
        period example

        September 2025
        """

        df = self.prepare(df)

        selected = pd.to_datetime(

            period,

            format="%B %Y",

        )

        filtered = df[

            (df["_period"].dt.month == selected.month)

            &

            (df["_period"].dt.year == selected.year)

        ]

        return filtered.drop(

            columns="_period",

            errors="ignore",

        ).reset_index(drop=True)

    # ----------------------------------------------------

    def latest_dataframe(

        self,

        df: pd.DataFrame,

    ) -> pd.DataFrame:

        """
        Returns dataframe for latest month.
        """

        latest = self.latest_period(df)

        if latest is None:

            return df

        return self.filter(df, latest)

    # ----------------------------------------------------

    def summary(

        self,

        df: pd.DataFrame,

    ) -> dict:

        return {

            "available_periods":

                self.available_periods(df),

            "latest_period":

                self.latest_period(df),

            "records":

                len(df),

        }
