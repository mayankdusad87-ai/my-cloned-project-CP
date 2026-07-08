
"""
=========================================================
ChannelIQ AI

Database Models

Creates all database tables.

=========================================================
"""

from __future__ import annotations

from database.connection import DatabaseConnection


def create_tables() -> None:
    """
    Creates all database tables.
    Safe to call multiple times.
    """

    db = DatabaseConnection()

    db.execute(
        """
        CREATE TABLE IF NOT EXISTS analysis_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            analysis_id TEXT UNIQUE,

            company_name TEXT,

            project_name TEXT,

            month TEXT,

            year INTEGER,

            fresh_walkins INTEGER,

            unique_revisits INTEGER,

            bookings INTEGER,

            booking_percentage REAL,

            active_channel_partners INTEGER,

            health_score REAL,

            revenue_opportunity REAL,

            growth_rate REAL,

            ai_summary TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_analysis_id
        ON analysis_history(analysis_id)
        """
    )

    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_company
        ON analysis_history(company_name)
        """
    )

    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_project
        ON analysis_history(project_name)
        """
    )

    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_created_at
        ON analysis_history(created_at)
        """
    )
