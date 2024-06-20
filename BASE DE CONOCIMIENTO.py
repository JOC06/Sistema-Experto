# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:55:47 2024

@author: Dell
"""

import sqlite3


conn = sqlite3.connect('vehiculos.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS vehiculos (
    modelo TEXT PRIMARY KEY,
    tipo TEXT,
    kilometraje_maximo REAL,
    consumo_gasolina_maximo REAL,
    mantenimiento TEXT
)
''')


vehiculos = [
    ('2020', 'sedan', 100000, 10.5, 'preventivo'),
    ('2010', 'camioneta', 120000, 12.0, 'correctivo'),
    ('2015', 'hatchback', 90000, 11.0, 'preventivo'),
    ('2008', 'sedan', 130000, 9.5, 'correctivo'),
    ('2018', 'camioneta', 110000, 11.5, 'preventivo'),
    ('2012', 'sedan', 105000, 10.0, 'correctivo'),
    ('2016', 'hatchback', 95000, 10.8, 'preventivo'),
    ('2005', 'camioneta', 150000, 8.0, 'correctivo'),
    ('2019', 'sedan', 95000, 12.5, 'preventivo'),
    ('2013', 'camioneta', 100000, 9.0, 'correctivo')
]

cursor.executemany('INSERT OR IGNORE INTO vehiculos (modelo, tipo, kilometraje_maximo, consumo_gasolina_maximo, mantenimiento) VALUES (?, ?, ?, ?, ?)', vehiculos)

conn.commit()  
conn.close()   