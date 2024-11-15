import sqlite3

conn = sqlite3.connect("dati.db", check_same_thread=False)

def lietotaju_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS lietotaji(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        lietotajvards TEXT NOT NULL 
        )
        """
    )
    conn.commit()

def pievienot_lietotaju(vards, uzvards, lietotajvards):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO lietotaji(vards, uzvards, lietotajvards)
        VALUES("{vards}","{uzvards}","{lietotajvards}")
        """
    )
    conn.commit()

