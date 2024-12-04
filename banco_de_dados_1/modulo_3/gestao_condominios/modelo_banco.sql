-- Criar a tabela de moradores
CREATE TABLE IF NOT EXISTS morador (
    id_morador INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    telefone TEXT
);

-- Criar a tabela de apartamentos
CREATE TABLE IF NOT EXISTS apartamento (
    id_apartamento INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_apartamento INTEGER NOT NULL,
    andar INTEGER NOT NULL,
    id_morador INTEGER,
    FOREIGN KEY (id_morador) REFERENCES morador(id_morador)
);

-- Criar a tabela de taxas
CREATE TABLE IF NOT EXISTS taxa (
    id_taxa INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL NOT NULL,
    tipo TEXT CHECK(tipo IN ('fixa', 'extra')) NOT NULL,
    data_vencimento TEXT NOT NULL,
    id_apartamento INTEGER,
    FOREIGN KEY (id_apartamento) REFERENCES apartamento(id_apartamento)
);

-- Criar a tabela de pagamentos
CREATE TABLE IF NOT EXISTS pagamento (
    id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
    data_pagamento TEXT NOT NULL,
    valor_pago REAL NOT NULL,
    id_taxa INTEGER,
    FOREIGN KEY (id_taxa) REFERENCES taxa(id_taxa)
);
