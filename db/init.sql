CREATE TABLE fila_cirurgica (
    id SERIAL PRIMARY KEY,
    paciente TEXT,
    prontuario VARCHAR(20),
    especialidade TEXT,
    procedimento TEXT,
    prioridade TEXT,
    data_inclusao DATE,
    status TEXT
);

INSERT INTO fila_cirurgica
(paciente, prontuario, especialidade, procedimento, prioridade, data_inclusao, status)
VALUES
('João da Silva','12345','cardiologia','revascularização','alta','2025-11-02','aguardando'),
('Maria Souza','54321','ortopedia','prótese de joelho','media','2025-12-10','aguardando'),
('Pedro Santos','22222','cardiologia','cateterismo','alta','2025-12-22','aguardando');

CREATE VIEW vw_fila_cirurgica AS
SELECT
    paciente,
    especialidade,
    procedimento,
    prioridade,
    data_inclusao
FROM fila_cirurgica
WHERE status='aguardando';
