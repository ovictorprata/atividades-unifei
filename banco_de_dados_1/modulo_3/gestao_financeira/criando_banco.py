import sqlite3
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_directory, 'gestao_financeira.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Criar as tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS conta (
    id_conta INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_conta TEXT NOT NULL,
    saldo REAL DEFAULT 0,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transacao (
    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    valor REAL NOT NULL,
    tipo TEXT CHECK(tipo IN ('débito', 'crédito')) NOT NULL,
    descricao TEXT,
    id_conta INTEGER,
    id_categoria INTEGER,
    FOREIGN KEY (id_conta) REFERENCES conta(id_conta),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);
''')

# 2. Inserir dados nas tabelas com parâmetros
# Inserir usuários
cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)", ('Carlos Silva', 'carlos@exemplo.com', 'senha123'))
cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)", ('Ana Souza', 'ana@exemplo.com', 'senha456'))
cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)", ('José Almeida', 'jose@exemplo.com', 'senha789'))

# Inserir contas
cursor.execute("INSERT INTO conta (nome_conta, saldo, id_usuario) VALUES (?, ?, ?)", ('Conta Corrente', 1000.0, 1))
cursor.execute("INSERT INTO conta (nome_conta, saldo, id_usuario) VALUES (?, ?, ?)", ('Poupança', 5000.0, 2))
cursor.execute("INSERT INTO conta (nome_conta, saldo, id_usuario) VALUES (?, ?, ?)", ('Cartão de Crédito', -200.0, 3))

# Inserir categorias
cursor.execute("INSERT INTO categoria (nome) VALUES (?)", ('Alimentação',))
cursor.execute("INSERT INTO categoria (nome) VALUES (?)", ('Lazer',))
cursor.execute("INSERT INTO categoria (nome) VALUES (?)", ('Saúde',))

# Inserir transações
cursor.execute("INSERT INTO transacao (data, valor, tipo, descricao, id_conta, id_categoria) VALUES (?, ?, ?, ?, ?, ?)", 
               ('2024-12-01', 200.0, 'débito', 'Compra no supermercado', 1, 1))
cursor.execute("INSERT INTO transacao (data, valor, tipo, descricao, id_conta, id_categoria) VALUES (?, ?, ?, ?, ?, ?)", 
               ('2024-12-02', 50.0, 'débito', 'Cinema', 2, 2))
cursor.execute("INSERT INTO transacao (data, valor, tipo, descricao, id_conta, id_categoria) VALUES (?, ?, ?, ?, ?, ?)", 
               ('2024-12-03', 100.0, 'crédito', 'Pagamento de salário', 3, 3))

conn.commit()

# 3. Consultar dados (com filtro WHERE)
cursor.execute("SELECT * FROM usuario WHERE id_usuario = ?", (1,))
usuarios = cursor.fetchall()
print("Consulta: Usuário com ID 1")
for usuario in usuarios:
    print(usuario)

# 4. Atualizar um registro existente (alterar o nome de um usuário)
cursor.execute("UPDATE usuario SET nome = ? WHERE id_usuario = ?", ('Carlos Alberto Silva', 1))
conn.commit()

# Consultar após atualização
cursor.execute("SELECT * FROM usuario WHERE id_usuario = ?", (1,))
usuarios = cursor.fetchall()
print("\nApós Atualização: Usuário com ID 1")
for usuario in usuarios:
    print(usuario)

# 5. Excluir um registro (remover uma transação)
cursor.execute("DELETE FROM transacao WHERE id_transacao = ?", (1,))
conn.commit()

cursor.execute("SELECT * FROM transacao")
transacoes = cursor.fetchall()
print("\nApós Exclusão: Todas as transações")
for transacao in transacoes:
    print(transacao)

# 6. Inserir novos registros em duas tabelas relacionadas
# Inserir nova transação vinculada à conta e categoria
cursor.execute("INSERT INTO transacao (data, valor, tipo, descricao, id_conta, id_categoria) VALUES (?, ?, ?, ?, ?, ?)", 
               ('2024-12-04', 300.0, 'débito', 'Novo débito em Conta Corrente', 1, 1))
conn.commit()

cursor.execute("SELECT * FROM transacao")
transacoes = cursor.fetchall()
print("\nApós Inserção em Tabelas Relacionadas: Todas as transações")
for transacao in transacoes:
    print(transacao)

conn.close()
