-- criacao das tabelas

CREATE TABLE clientes (
    id_cliente INTEGER,
    nome_cliente VARCHAR(50),
    cidade VARCHAR(50)
);

CREATE TABLE ordens_servico (
    id_os INTEGER,
    id_cliente INTEGER,
    servico VARCHAR(50),
    valor NUMERIC,
    status VARCHAR(50),
    data_os DATE
);

-- inserindo os dados

INSERT INTO clientes (id_cliente, nome_cliente, cidade) VALUES
(1, 'João', 'São Paulo'),
(2, 'Maria', 'São Paulo'),
(3, 'Ana', 'Guarulhos'),
(4, 'Carlos', 'Suzano'),
(5, 'Pedro', 'Mogi das Cruzes'),
(6, 'Juliana', 'Guarulhos');

INSERT INTO ordens_servico (id_os, id_cliente, servico, valor, status, data_os) VALUES
(1, 1, 'Troca de Óleo', 120, 'Finalizado', '2026-01-05'),
(2, 2, 'Alinhamento', 80, 'Finalizado', '2026-01-05'),
(3, 1, 'Freio', 350, 'Finalizado', '2026-01-06'),
(4, 4, 'Troca de Óleo', 120, 'Pendente', '2026-01-06'),
(5, 2, 'Freio', 300, 'Finalizado', '2026-01-08'),
(6, 3, 'Revisão', 500, 'Finalizado', '2026-01-08'),
(7, 1, 'Revisão', 500, 'Finalizado', '2026-01-10'),
(8, 4, 'Alinhamento', 80, 'Finalizado', '2026-01-10'),
(9, 3, 'Freio', 320, 'Pendente', '2026-01-12'),
(10, 2, 'Revisão', 500, 'Finalizado', '2026-01-12'),
(11, 5, 'Bateria', 450, 'Finalizado', '2026-01-12'),
(12, 6, 'Troca de Óleo', 120, 'Finalizado', '2026-01-15'),
(13, 6, 'Freio', 380, 'Finalizado', '2026-01-15'),
(14, 5, 'Bateria', 420, 'Cancelado', '2026-01-18'),
(15, 3, 'Alinhamento', 90, 'Finalizado', '2026-01-18');

-- consultas

-- ### 1. Listar ordens finalizadas com dados do cliente

CREATE VIEW vw_ordens_finalizadas AS
SELECT
    o.id_os,
    o.id_cliente,
    c.nome_cliente,
    c.cidade,
    o.servico,
    o.valor,
    o.status,
    o.data_os
FROM ordens_servico o
INNER JOIN clientes c
    ON o.id_cliente = c.id_cliente
WHERE o.status = 'Finalizado';

-- ### 2. Calcular faturamento por cliente

SELECT 
    id_cliente,
    nome_cliente,
    cidade,
    sum(valor) as faturamento_total
FROM vw_ordens_finalizadas
GROUP BY
    id_cliente,
    nome_cliente,
    cidade
ORDER BY faturamento_total DESC;

-- ### 3. Calcular quantidade de ordens por cliente
SELECT 
    id_cliente,
    nome_cliente,
    count(*) as qtd_ordens
FROM vw_ordens_finalizadas
GROUP BY 
    id_cliente,
    nome_cliente
ORDER BY qtd_ordens DESC;

-- ### 4. Calcular ticket médio por cliente

SELECT
    id_cliente,
    nome_cliente,
    AVG(valor) as ticket_medio
FROM vw_ordens_finalizadas
GROUP BY 
    id_cliente,
    nome_cliente
ORDER BY ticket_medio DESC;

-- ### 5. Calcular faturamento por cidade

SELECT 
    cidade,
    sum(valor) as faturamento_total
FROM vw_ordens_finalizadas
GROUP BY cidade 
ORDER BY faturamento_total DESC;

-- ### 6. Identificar cliente com maior faturamento

SELECT 
    id_cliente,
    nome_cliente,
    cidade,
    sum(valor) as faturamento_total
FROM vw_ordens_finalizadas
GROUP BY
    id_cliente,
    nome_cliente,
    cidade
ORDER BY faturamento_total DESC
LIMIT 1;


-- ### 7. Identificar cidade com maior faturamento

SELECT 
    cidade,
    sum(valor) as faturamento_total
FROM vw_ordens_finalizadas
GROUP BY cidade 
ORDER BY faturamento_total DESC
LIMIT 1;
