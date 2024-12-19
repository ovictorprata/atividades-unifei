import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS local(
id INTEGER primary key AUTOINCREMENT, 
latitude INTEGER NOT NULL,
longitude INTEGER NOT NULL,
descricao_local varchar(255) NOT NULL
);

              ''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS amostra (
codigo INTEGER PRIMARY KEY AUTOINCREMENT,
data INTEGER NOT NULL,
descricao VARCHAR(250) NOT NULL,
temperatura INTEGER,
ph REAL,
condutividade REAL,
turbidez REAL,
acidez REAL,
alcalinidade_parcial REAL,
alcalinidade_total REAL,
alcalinidade_bicarbonato REAL,
alcalinidade_cabonato REAL,
alcalinidade_hidroxila REAL,
local_id INTEGER NO NULL,
FOREIGN KEY(local_id) REFERENCES local(id)
);

''')
conn.commit()

latitudes = [-19673.864, -19673.847, -19673.791, -19673.801, -19673.738, -19673.738, -19673.732, -19673.668, -19673.724, -19673.788, -19674.164]
longitudes = [-43212.684, -43212.642, -43212.665, -43212.643, -43212.656, -43212.656, -43212.638, -43212.605, -43212.655, -43212.584, -43212.591]
locais = ['2º andar, prédio 1', '2º andar, prédio 1', '2º andar, prédio 1', '2º andar, prédio 1', '1º andar, prédio 1', '1º andar, prédio 1', '1º andar, prédio 1', '2º andar, prédio 1', '1º andar, prédio 1', '2º andar, prédio 1', 'rua Unifei']
datas = ['11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024', '11/12/2024' ]
descricoes = ['Balde com água ', 'Bebedouro ', 'Torneira banheiro ', 'Banheiro deficientes', 'Torneira banheiro feminino', 'Bebedouro prédio 1', 'Torneira banheiro masculino', 'Torneira laboratório polímeros ', 'Banheiro PCD', 'Banheiro masculino', 'Poço de água']
temperaturas = [22, 23, 23, 23, 23, 22, 23, 23, 22.5, 23.5, 23]
phs = [3.3,7.63,7.56,7.56,7.78,7.72,7.88,7.57,7.75,7.76,8.08]
condutividades = [388, 135.3, 130.9, 129.1, 127.9, 124.8, 122, 120, 117.6, 109.9, 81.2]
turbidez = [1.52, 0.04, 0.22, 0.19, 0.08, 0.07, 0.09, 0.05, 0.07, 0.08, 374]
alcalidades = ['NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL', 'NENHUMA TEVE ALCALINIDADE PARCIAL']
acidezes = [7.5, 5.0, 5.0, 8.1, 12.5, 7.5, 7.5, 5.0, 5.0, 5.0, 7.5]
alcalinidade_total = [27.5, 425.0, 25.0, 40.3, 20.0, 17.5, 32.5, 40.0, 42.5, 75.0, 52.5]
locais_id = [1,2,3,4,5,6,7,8,9,10,11]



cursor = conn.cursor()
for i in range (len(latitudes)):
    cursor.execute(f'''
    INSERT INTO local (latitude, longitude, descricao_local) VALUES
    ({latitudes[i]}, {longitudes[i]}, '{locais[i]}')''')
conn.commit()


for i in range (len(latitudes)):
    cursor.execute(f'''
    INSERT INTO amostra(data, descricao, temperatura, ph, condutividade,turbidez,alcalinidade_parcial, acidez, alcalinidade_total, local_id) values
    ('{datas[i]}', '{descricoes[i]}', {temperaturas[i]}, {phs[i]}, {condutividades[i]},{turbidez[i]},'{alcalidades[i]}',{acidezes[i]},{alcalinidade_total[i]}, {locais_id[i]})''')
conn.commit()

conn.close()



