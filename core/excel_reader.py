"""
=========================================================
ChannelIQ AI

Excel Reader

Reads the standard ChannelIQ Excel template.

Header  : Row 4
Data    : Row 5 onwards
=========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

import pandas as pd

from config import (
    EXCEL_HEADER_ROW,
    EXCEL_DATA_START_ROW,
)


class ExcelReader:
    """
    Reads the standard ChannelIQ template.
    """

    def read(
        self,
        file: Union[str, Path, bytes]
    ) -> pd.DataFrame:

        df = pd.read_excel(
            file,
            header=EXCEL_HEADER_ROW - 1,
            engine="openpyxl"
        )

        # --------------------------------------------------
        # Remove completely empty rows
        # --------------------------------------------------

        df = df.dropna(how="all")

        # --------------------------------------------------
        # Actual data starts from Row 5
        # --------------------------------------------------

        df = df.iloc[
            EXCEL_DATA_START_ROW - EXCEL_HEADER_ROW:
        ]

        # --------------------------------------------------
        # Reset Index
        # --------------------------------------------------

        df.reset_index(
            drop=True,
            inplace=True
        )

        # --------------------------------------------------
        # Clean Column Names
        # --------------------------------------------------

        df.columns = [
            str(col).strip()
            for col in df.columns
        ]

        return df
