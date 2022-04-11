import sqlite3

datas = [
]
print(datas)

conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()
cur.executemany("INSERT INTO PRODUITS(path, nom ,description, prix, note) VALUES(?, ?, ?, ?, ?)", datas)
conn.commit()