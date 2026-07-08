"""
=========================================================
ChannelIQ AI

Column Mapping

This file maps business fields to the
standard ChannelIQ Excel template.

If the Excel template changes,
only this file should be updated.
=========================================================
"""

# =========================================================
# EXCEL COLUMN MAPPING
# =========================================================

COLUMN_MAPPING = {

    # -----------------------------------------------------
    # Customer
    # -----------------------------------------------------

    "form_no": "Form No",

    "visit_date": "Date of Visit",

    "customer_name": "Customer Name",

    "mobile": "Mobile Number",

    "visit_type": "Visit Type",

    "customer_stage": "Customer Fresh/Revisit",

    # -----------------------------------------------------
    # Sales
    # -----------------------------------------------------

    "closing_manager": "Closing Manager*",

    "booking_date": "Booking Date",

    # -----------------------------------------------------
    # Channel Partner
    # -----------------------------------------------------

    "channel_partner": "Channel Partner Company*",

    # -----------------------------------------------------
    # Project
    # -----------------------------------------------------

    "project_name": "Project Name",

    "source": "Source*",

    "budget": "Budget*",

    "configuration": "Preferred Configuration*"

}

# =========================================================
# BUSINESS VALUES
# =========================================================

BUSINESS_VALUES = {

    "fresh": "Fresh",

    "unique_revisit": "Unique Revisit",

    "second_revisit": "Second Revisit",

    "third_revisit": "Third Revisit",

    "fourth_revisit": "Fourth Revisit",

    "revisit": "Revisit"

}
