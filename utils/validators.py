"""
=========================================================
ChannelIQ AI

Validation Utilities
=========================================================
"""

from __future__ import annotations

import pandas as pd


class TemplateValidationError(Exception):
    """Raised when uploaded template is invalid."""


class TemplateValidator:

    def __init__(self):

        self.required_columns = [

            "Form No",

            "Date of Visit",

            "Channel Partner",

            "Sales Person",

            "Customer Name",

            "Mobile No",

        ]

    # ----------------------------------------------------

    def validate(
        self,
        df: pd.DataFrame
    ) -> None:

        missing = [

            column

            for column in self.required_columns

            if column not in df.columns

        ]

        if missing:

            raise TemplateValidationError(

                "Missing required columns:\n\n"

                + "\n".join(missing)

            )
