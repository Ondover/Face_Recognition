import FaceManipulation as fm
import sqlite3
import pandas as pd

banco = sqlite3.connect('Banco4')
cursor = banco.cursor()

df1 = pd.read_sql_query("SELECT * FROM ALUNO", banco)
results = cursor.execute("SELECT nome FROM ALUNO LIMIT 5").fetchall()
df2 = pd.DataFrame(results)

if 'Rafael Nascimento de Sousa' in df2:
    print('true')