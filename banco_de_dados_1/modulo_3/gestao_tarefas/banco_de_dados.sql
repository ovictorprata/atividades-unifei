-- Criar tabela de Usuários
CREATE TABLE IF NOT EXISTS Usuario (
    usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

-- Criar tabela de Categorias
CREATE TABLE IF NOT EXISTS Categoria (
    categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

-- Criar tabela de Tarefas
CREATE TABLE IF NOT EXISTS Tarefa (
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
);
