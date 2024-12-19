import sqlite3
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_directory, 'gestao_tarefas.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# Criar as tabelas
cursor.execute('''CREATE TABLE IF NOT EXISTS Usuario (
    usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Categoria (
    categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Tarefa (
    tarefa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    data_criacao TEXT NOT NULL,
    data_vencimento TEXT,
    status TEXT,
    prioridade TEXT,
    usuario_id INTEGER,
    categoria_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (categoria_id) REFERENCES Categoria(categoria_id)
)''')

# Inserir dados nas tabelas com parâmetros
cursor.execute("INSERT INTO Usuario (nome, email, senha) VALUES (?, ?, ?)", ('João', 'joao@email.com', 'senha123'))
cursor.execute("INSERT INTO Usuario (nome, email, senha) VALUES (?, ?, ?)", ('Maria', 'maria@email.com', 'senha456'))
cursor.execute("INSERT INTO Usuario (nome, email, senha) VALUES (?, ?, ?)", ('Carlos', 'carlos@email.com', 'senha789'))

# Inserir categorias
cursor.execute("INSERT INTO Categoria (nome) VALUES (?)", ('Pessoal',))
cursor.execute("INSERT INTO Categoria (nome) VALUES (?)", ('Trabalho',))
cursor.execute("INSERT INTO Categoria (nome) VALUES (?)", ('Urgente',))

# Inserir tarefas
cursor.execute("INSERT INTO Tarefa (titulo, descricao, data_criacao, data_vencimento, status, prioridade, usuario_id, categoria_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
               ('Comprar leite', 'Comprar leite no supermercado', '2024-12-03 08:00:00', '2024-12-03 18:00:00', 'pendente', 'baixa', 1, 1))
cursor.execute("INSERT INTO Tarefa (titulo, descricao, data_criacao, data_vencimento, status, prioridade, usuario_id, categoria_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
               ('Reunião de equipe', 'Reunião com a equipe de desenvolvimento', '2024-12-03 09:00:00', '2024-12-03 11:00:00', 'concluída', 'alta', 2, 2))
cursor.execute("INSERT INTO Tarefa (titulo, descricao, data_criacao, data_vencimento, status, prioridade, usuario_id, categoria_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
               ('Revisar contrato', 'Revisar contrato com fornecedor', '2024-12-03 10:00:00', '2024-12-03 14:00:00', 'pendente', 'média', 3, 3))

# Consultar tarefas com status 'pendente'
cursor.execute("SELECT * FROM Tarefa WHERE status = ?", ('pendente',))
tasks = cursor.fetchall()
for task in tasks:
    print(task)

# Atualizar status de uma tarefa
cursor.execute("UPDATE Tarefa SET status = ? WHERE tarefa_id = ?", ('concluída', 1))

# Excluir uma tarefa
cursor.execute("DELETE FROM Tarefa WHERE tarefa_id = ?", (2,))
conn.commit()
conn.close()
