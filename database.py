"""
database.py
Database layer for ChannelIQ AI

Handles:
- Database creation
- Table creation
- Insert operations
- Read operations
- History
"""

import sqlite3
from pathlib import Path
from datetime import datetime

from config import DB_FILE


class Database:

    def __init__(self):

        self.db_path = Path(DB_FILE)

        self.connection = sqlite3.connect(
            self.db_path,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    # ----------------------------------------------------

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS companies(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company_name TEXT UNIQUE,

            created_at TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS projects(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company_id INTEGER,

            project_name TEXT,

            created_at TEXT,

            FOREIGN KEY(company_id)
            REFERENCES companies(id)

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS uploads(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_id INTEGER,

            upload_month TEXT,

            upload_year INTEGER,

            uploaded_at TEXT,

            original_file TEXT,

            health_score REAL,

            total_bookings REAL,

            conversion REAL,

            total_fresh REAL,

            total_hot REAL,

            total_warm REAL,

            total_cold REAL,

            FOREIGN KEY(project_id)
            REFERENCES projects(id)

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS partners(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            upload_id INTEGER,

            partner_name TEXT,

            fresh REAL,

            hot REAL,

            warm REAL,

            cold REAL,

            bookings REAL,

            conversion REAL,

            partner_score REAL,

            risk_score REAL,

            opportunity_value REAL,

            category TEXT,

            FOREIGN KEY(upload_id)
            REFERENCES uploads(id)

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS ai_reports(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            upload_id INTEGER,

            executive_summary TEXT,

            risks TEXT,

            opportunities TEXT,

            recommendations TEXT,

            prediction TEXT,

            created_at TEXT,

            FOREIGN KEY(upload_id)
            REFERENCES uploads(id)

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS settings(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company_name TEXT,

            logo TEXT,

            average_booking_value REAL,

            currency TEXT

        )

        """)

        self.connection.commit()

    # ----------------------------------------------------

    def create_company(self, company_name):

        self.cursor.execute("""

        INSERT OR IGNORE INTO companies(

            company_name,

            created_at

        )

        VALUES(

            ?,?

        )

        """,

        (

            company_name,

            datetime.now().isoformat()

        ))

        self.connection.commit()

    # ----------------------------------------------------

    def get_company_id(self, company_name):

        row = self.cursor.execute("""

        SELECT id

        FROM companies

        WHERE company_name=?

        """,

        (company_name,)

        ).fetchone()

        if row:

            return row["id"]

        return None

    # ----------------------------------------------------

    def create_project(

        self,

        company_id,

        project_name

    ):

        self.cursor.execute("""

        INSERT INTO projects(

            company_id,

            project_name,

            created_at

        )

        VALUES(

            ?,?,?

        )

        """,

        (

            company_id,

            project_name,

            datetime.now().isoformat()

        ))

        self.connection.commit()

    # ----------------------------------------------------

    def get_projects(self):

        return self.cursor.execute("""

        SELECT *

        FROM projects

        ORDER BY project_name

        """

        ).fetchall()

    # ----------------------------------------------------

    def save_upload(

        self,

        project_id,

        month,

        year,

        filename,

        summary

    ):

        self.cursor.execute("""

        INSERT INTO uploads(

            project_id,

            upload_month,

            upload_year,

            uploaded_at,

            original_file,

            health_score,

            total_bookings,

            conversion,

            total_fresh,

            total_hot,

            total_warm,

            total_cold

        )

        VALUES(

            ?,?,?,?,?,?,?,?,?,?,?,?

        )

        """,

        (

            project_id,

            month,

            year,

            datetime.now().isoformat(),

            filename,

            summary["health_score"],

            summary["bookings"],

            summary["conversion"],

            summary["fresh"],

            summary["hot"],

            summary["warm"],

            summary["cold"]

        ))

        self.connection.commit()

        return self.cursor.lastrowid

    # ----------------------------------------------------

    def save_ai_report(

        self,

        upload_id,

        report

    ):

        self.cursor.execute("""

        INSERT INTO ai_reports(

            upload_id,

            executive_summary,

            risks,

            opportunities,

            recommendations,

            prediction,

            created_at

        )

        VALUES(

            ?,?,?,?,?,?,?

        )

        """,

        (

            upload_id,

            report["summary"],

            report["risks"],

            report["opportunities"],

            report["recommendations"],

            report["prediction"],

            datetime.now().isoformat()

        ))

        self.connection.commit()

    # ----------------------------------------------------

    def get_history(self):

        return self.cursor.execute("""

        SELECT

            uploads.id,

            companies.company_name,

            projects.project_name,

            uploads.upload_month,

            uploads.upload_year,

            uploads.health_score,

            uploads.total_bookings,

            uploads.conversion

        FROM uploads

        JOIN projects

        ON uploads.project_id=projects.id

        JOIN companies

        ON projects.company_id=companies.id

        ORDER BY uploads.id DESC

        """

        ).fetchall()
