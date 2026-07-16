
"""
=========================================================
ChannelIQ AI

Executive Intelligence Highlights

Creates the Executive Intelligence section
shown at the top of the report.

=========================================================
"""

from __future__ import annotations

from typing import Any


class ExecutiveHighlights:

    def build(
        self,
        context: dict[str, Any],
    ) -> list[dict]:

        highlights = []

        commercial = context.get(
            "commercial_intelligence",
            {},
        )

        # -------------------------------------------------
        # Commercial Intelligence
        # -------------------------------------------------

        if commercial:

            highlights.append(

                {

                    "priority": commercial.get(
                        "severity",
                        "Medium",
                    ),

                    "title": commercial.get(
                        "title",
                        "",
                    ),

                    "observation": commercial.get(
                        "summary",
                        "",
                    ),

                    "evidence": commercial.get(
                        "evidence",
                        {},
                    ),

                }

            )

        return highlights
