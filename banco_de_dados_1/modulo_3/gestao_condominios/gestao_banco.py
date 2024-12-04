import sqlite3
import os

# Obtém o diretório onde o script está sendo executado
current_directory = os.path.dirname(os.path.abspath(__file__))

# Cria o caminho para o banco de dados na mesma pasta onde o script está
db_path = os.path.join(current_directory, 'gestao_condominio.db')

# Conexão com o banco de dados SQLite na mesma pasta onde o script está
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Criar as tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS morador (
    id_morador INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    telefone TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS apartamento (
    id_apartamento INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_apartamento INTEGER NOT NULL,
    andar INTEGER NOT NULL,
    id_morador INTEGER,
    FOREIGN KEY (id_morador) REFERENCES morador(id_morador)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS taxa (
    id_taxa INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL NOT NULL,
    tipo TEXT CHECK(tipo IN ('fixa', 'extra')) NOT NULL,
    data_vencimento TEXT NOT NULL,
    id_apartamento INTEGER,
    FOREIGN KEY (id_apartamento) REFERENCES apartamento(id_apartamento)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pagamento (
    id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
    data_pagamento TEXT NOT NULL,
    valor_pago REAL NOT NULL,
    id_taxa INTEGER,
    FOREIGN KEY (id_taxa) REFERENCES taxa(id_taxa)
);
''')

# 2. Inserir dados nas tabelas
# Inserir moradores
cursor.execute("INSERT INTO morador (nome, cpf, telefone) VALUES ('Carlos Silva', '12345678901', '999999999')")
cursor.execute("INSERT INTO morador (nome, cpf, telefone) VALUES ('Ana Souza', '98765432100', '888888888')")
cursor.execute("INSERT INTO morador (nome, cpf, telefone) VALUES ('José Almeida', '11223344556', '777777777')")

# Inserir apartamentos
cursor.execute("INSERT INTO apartamento (numero_apartamento, andar, id_morador) VALUES (101, 1, 1)")
cursor.execute("INSERT INTO apartamento (numero_apartamento, andar, id_morador) VALUES (102, 1, 2)")
cursor.execute("INSERT INTO apartamento (numero_apartamento, andar, id_morador) VALUES (201, 2, 3)")

# Inserir taxas
cursor.execute("INSERT INTO taxa (valor, tipo, data_vencimento, id_apartamento) VALUES (500.0, 'fixa', '2024-12-05', 1)")
cursor.execute("INSERT INTO taxa (valor, tipo, data_vencimento, id_apartamento) VALUES (400.0, 'fixa', '2024-12-10', 2)")
cursor.execute("INSERT INTO taxa (valor, tipo, data_vencimento, id_apartamento) VALUES (600.0, 'extra', '2024-12-15', 3)")

# Inserir pagamentos
cursor.execute("INSERT INTO pagamento (data_pagamento, valor_pago, id_taxa) VALUES ('2024-12-03', 500.0, 1)")
cursor.execute("INSERT INTO pagamento (data_pagamento, valor_pago, id_taxa) VALUES ('2024-12-05', 400.0, 2)")
cursor.execute("INSERT INTO pagamento (data_pagamento, valor_pago, id_taxa) VALUES ('2024-12-06', 600.0, 3)")

# Commit para garantir que as alterações sejam salvas no banco de dados
conn.commit()

# 3. Consultar dados (com filtro WHERE)
cursor.execute("SELECT * FROM morador WHERE id_morador = 1")
moradores = cursor.fetchall()
print("Consulta: Morador com ID 1")
for morador in moradores:
    print(morador)

# 4. Atualizar um registro existente (alterar o telefone de um morador)
cursor.execute("UPDATE morador SET telefone = '955555555' WHERE id_morador = 1")
conn.commit()

# Consultar após atualização
cursor.execute("SELECT * FROM morador WHERE id_morador = 1")
moradores = cursor.fetchall()
print("\nApós Atualização: Morador com ID 1")
for morador in moradores:
    print(morador)

# 5. Excluir um registro (remover um pagamento)
cursor.execute("DELETE FROM pagamento WHERE id_pagamento = 1")
conn.commit()

# Consultar após exclusão
cursor.execute("SELECT * FROM pagamento")
pagamentos = cursor.fetchall()
print("\nApós Exclusão: Todos os pagamentos")
for pagamento in pagamentos:
    print(pagamento)

# 6. Inserir novos registros em duas tabelas relacionadas
# Inserir nova taxa vinculada ao apartamento
cursor.execute("INSERT INTO taxa (valor, tipo, data_vencimento, id_apartamento) VALUES (550.0, 'fixa', '2024-12-20', 1)")
conn.commit()

# Consultar todas as taxas após inserção
cursor.execute("SELECT * FROM taxa")
taxas = cursor.fetchall()
print("\nApós Inserção em Tabelas Relacionadas: Todas as taxas")
for taxa in taxas:
    print(taxa)

# Fechar a conexão
conn.close()
