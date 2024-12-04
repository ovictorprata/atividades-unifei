-- Criar a tabela de Usuários
CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);

-- Criar a tabela de Contas
CREATE TABLE conta (
    id_conta INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_conta TEXT NOT NULL,
    saldo REAL DEFAULT 0,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- Criar a tabela de Categorias
CREATE TABLE categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

-- Criar a tabela de Transações
CREATE TABLE transacao (
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
