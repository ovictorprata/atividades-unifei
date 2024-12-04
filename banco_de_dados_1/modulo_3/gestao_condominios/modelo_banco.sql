CREATE TABLE Morador (
    morador_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE Unidade (
    unidade_id INT PRIMARY KEY AUTO_INCREMENT,
    numero VARCHAR(20) NOT NULL,
    bloco VARCHAR(20),
    morador_id INT,
    FOREIGN KEY (morador_id) REFERENCES Morador(morador_id)
);

CREATE TABLE Boleto (
    boleto_id INT PRIMARY KEY AUTO_INCREMENT,
    unidade_id INT,
    valor DECIMAL(10, 2) NOT NULL,
    data_vencimento DATE,
    status VARCHAR(20),
    FOREIGN KEY (unidade_id) REFERENCES Unidade(unidade_id)
);


CREATE TABLE Reserva (
    reserva_id INT PRIMARY KEY AUTO_INCREMENT,
    unidade_id INT,
    data_reserva DATETIME,
    area_comum VARCHAR(50),
    status VARCHAR(20),
    FOREIGN KEY (unidade_id) REFERENCES Unidade(unidade_id)
);