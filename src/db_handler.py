import sqlite3
import pandas as pd
from typing import Dict, Any

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.create_tables()
    
    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS processed_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ata TEXT,
                task_number TEXT,
                description TEXT,
                mpn TEXT,
                pn TEXT,
                limit_value TEXT,
                margin TEXT,
                documentation TEXT,
                reference TEXT
            )
        ''')
        self.conn.commit()
    
    def save_processed_data(self, df: pd.DataFrame):
        # Rename 'Limit' column to 'limit_value' if it exists
        if 'Limit' in df.columns:
            df = df.rename(columns={'Limit': 'limit_value'})
        df.to_sql('processed_data', self.conn, if_exists='append', index=False)
        self.conn.commit()
    
    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()
