"""
ChannelIQ Validators
"""

import pandas as pd


REQUIRED_COLUMNS = [

    "Form No",

    "Date of Visit",

    "Channel Partner",

    "Sales Person",

    "Customer Name",

    "Mobile No"

]


class ValidationError(Exception):
    pass


def validate_template(
    df: pd.DataFrame
):

    missing = []

    for column in REQUIRED_COLUMNS:

        if column not in df.columns:

            missing.append(column)

    if missing:

        raise ValidationError(

            "Missing required columns:\n\n"

            + "\n".join(missing)

        )

    return True
