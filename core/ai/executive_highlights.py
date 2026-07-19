
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

    business_signals = context.get(
        "business_signals",
        []
    )

    for signal in business_signals:

        highlights.append({

            "priority": signal.severity,

            "title": signal.title,

            "observation": signal.summary,

            "evidence": signal.evidence,

        })

    return highlights

    
