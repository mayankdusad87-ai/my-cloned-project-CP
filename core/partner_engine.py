"""
=========================================================
ChannelIQ AI

Partner Engine

Version : 1.0

Calculates partner-wise business KPIs for the
selected reporting period.

=========================================================
"""

from __future__ import annotations

import pandas as pd

from core.column_mapping import (
    CHANNEL_PARTNER,
    CUSTOMER_FRESH_REVISIT,
    BOOKING_DONE,
    BUSINESS_VALUES,
)


class PartnerEngine:

    def __init__(self):
        pass

    # ----------------------------------------------------

    def analyse(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        if df.empty:
            return pd.DataFrame()

        partners = []

        grouped = df.groupby(CHANNEL_PARTNER)

        for partner, data in grouped:

            if pd.isna(partner):
                continue

            total_walkins = len(data)

            fresh_walkins = len(
                data[
                    data[CUSTOMER_FRESH_REVISIT]
                    .fillna("")
                    .astype(str)
                    .str.upper()
                    ==
                    BUSINESS_VALUES["fresh"].upper()
                ]
            )

            unique_revisits = len(
                data[
                    data[CUSTOMER_FRESH_REVISIT]
                    .fillna("")
                    .astype(str)
                    .str.upper()
                    ==
                    BUSINESS_VALUES["unique_revisit"].upper()
                ]
            )

            bookings = len(
                data[
                    data[BOOKING_DONE]
                    .fillna("")
                    .astype(str)
                    .str.upper()
                    == "Y"
                ]
            )

            conversion = 0

            if fresh_walkins > 0:
                conversion = round(
                    bookings / fresh_walkins * 100,
                    2,
                )

            partners.append({

                "partner": partner,

                "total_walkins": total_walkins,

                "fresh_walkins": fresh_walkins,

                "unique_revisits": unique_revisits,

                "bookings": bookings,

                "conversion": conversion,

            })

        partner_df = pd.DataFrame(partners)

        if partner_df.empty:
            return partner_df

        partner_df = partner_df.sort_values(

            by=[
                "bookings",
                "fresh_walkins",
                "total_walkins",
            ],

            ascending=False,

        ).reset_index(drop=True)

        partner_df.insert(

            0,

            "rank",

            range(1, len(partner_df) + 1),

        )

        return partner_df
