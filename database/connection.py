"""
=========================================================
ChannelIQ AI

Database Connection

Handles SQLite connection.

=========================================================
"""

from __future__ import annotations

import sqlite3
from sqlite3 import Connection

from config import DB_PATH, DB_TIMEOUT


class DatabaseConnection:
    """
    SQLite Database Connection Manager.
    """

    def __init__(self):

        self.db_path = DB_PATH

        self.timeout = DB_TIMEOUT

    # -----------------------------------------------------

    def connect(self) -> Connection:
        """
        Returns an open SQLite connection.
        """

        conn = sqlite3.connect(

            self.db_path,

            timeout=self.timeout

        )

        conn.row_factory = sqlite3.Row

        return conn

    # -----------------------------------------------------

    def execute(
        self,
        query: str,
        params: tuple = (),
    ) -> None:

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        conn.commit()

        conn.close()

    # -----------------------------------------------------

    def executemany(
        self,
        query: str,
        params: list[tuple],
    ) -> None:

        conn = self.connect()

        cursor = conn.cursor()

        cursor.executemany(query, params)

        conn.commit()

        conn.close()

    # -----------------------------------------------------

    def fetch_one(
        self,
        query: str,
        params: tuple = (),
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        row = cursor.fetchone()

        conn.close()

        return row

    # -----------------------------------------------------

    def fetch_all(
        self,
        query: str,
        params: tuple = (),
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        rows = cursor.fetchall()

        conn.close()

        return rows

    # -----------------------------------------------------

    def execute_return_id(
        self,
        query: str,
        params: tuple = (),
    ) -> int:

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        conn.commit()

        last_id = cursor.lastrowid

        conn.close()

        return last_id
