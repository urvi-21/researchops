import sqlite3
from datetime import datetime


class MetadataStore:

    def __init__(
        self,
        db_path="storage/metadata/research_metadata.db"
    ):

        self.db_path = db_path

        self.connection = sqlite3.connect(
            self.db_path
        )

        self.cursor = self.connection.cursor()

        self.initialize_tables()

    def initialize_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            filepath TEXT,
            topic TEXT,
            pages INTEGER,
            created_at TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS workflows (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workflow_name TEXT,
            status TEXT,
            created_at TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_name TEXT,
            topic TEXT,
            created_at TEXT
        )
        """)

        self.connection.commit()

    def add_document(
        self,
        filename,
        filepath,
        topic,
        pages
    ):

        self.cursor.execute("""
        INSERT INTO documents (
            filename,
            filepath,
            topic,
            pages,
            created_at
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            filename,
            filepath,
            topic,
            pages,
            datetime.now().isoformat()
        ))

        self.connection.commit()

    def add_workflow(
        self,
        workflow_name,
        status
    ):

        self.cursor.execute("""
        INSERT INTO workflows (
            workflow_name,
            status,
            created_at
        )
        VALUES (?, ?, ?)
        """, (
            workflow_name,
            status,
            datetime.now().isoformat()
        ))

        self.connection.commit()

    def add_report(
        self,
        report_name,
        topic
    ):

        self.cursor.execute("""
        INSERT INTO reports (
            report_name,
            topic,
            created_at
        )
        VALUES (?, ?, ?)
        """, (
            report_name,
            topic,
            datetime.now().isoformat()
        ))

        self.connection.commit()

    def fetch_documents(self):

        self.cursor.execute(
            "SELECT * FROM documents"
        )

        return self.cursor.fetchall()

    def fetch_workflows(self):

        self.cursor.execute(
            "SELECT * FROM workflows"
        )

        return self.cursor.fetchall()

    def fetch_reports(self):

        self.cursor.execute(
            "SELECT * FROM reports"
        )

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()