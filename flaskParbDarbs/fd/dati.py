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

def iegut_lietotajvardus():
    cur = conn.cursor()
    cur.execute(
        """
        SELECT lietotajvards, vards, uzvards FROM lietotaji
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def zinojumu_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS zinojumi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lietotaja_id INTEGER NOT NULL,
        zinojums TEXT NOT NULL,
        datums DATETIME DEFAULT CURRENT_TIMESTAMP, 
        FOREIGN KEY (lietotaja_id) REFERENCES lietotaji(id)
        )
        """
    )
    conn.commit()

# def iegut_lietotajvarda_id(lietotajvards):
#     cur = conn.cursor()
#     cur.execute(
#         f"""
#         SELECT id FROM lietotaji
#         WHERE lietotajvards = {lietotajvards}
#         """
#     )
#     conn.commit()
#     dati = cur.fetchone()
#     return dati

# def pievienot_zinojumu(lietotajvards, zinojums):
#     id = iegut_lietotajvarda_id(lietotajvards)
#     cur = conn.cursor()
#     cur.execute(
#         f"""
#         INSERT INTO zinojumi(lietotaja_id, zinojums)
#         VALUES("{id}","{zinojums}")
#         """
#     )
#     conn.commit()
def pievienot_zinojumu(lietotajvards,zinojums):
    cur = conn.cursor()
    cur.execute(
    f"""
    SELECT id FROM lietotaji WHERE lietotajvards = {lietotajvards}
    """)
    lietotaja_id = cur.fetchone()
    cur.execute(
        f"""
        INSERT INTO zinojumi(lietotaja_id, zinojums)
        VALUES({lietotaja_id}, {zinojums})
        """
    )
    

def iegut_zinojumus():
    cur = conn.cursor()
    cur.execute(
        """
        SELECT 
            zinojumi.id,
            lietotaji.vards,
            lietotaji.uzvards,
            lietotaji.lietotajvards,
            zinojumi.zinojums,
            zinojumi.datums
        FROM zinojumi
        JOIN lietotaji ON zinojumi.lietotaja_id = lietotaji.id
        ORDER BY zinojumi.datums DESC
        """
    )
    dati = cur.fetchall()
    print(dati)
    return dati




