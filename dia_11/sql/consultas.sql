-- Criacao da tabela

CREATE TABLE ordens_servico(
	id_os INTEGER, 
	cliente VARCHAR(50), 
	servico VARCHAR(50), 
	valor NUMERIC, 
	status VARCHAR(50), 
	data_os DATE
);


-- Adicionando os dados

INSERT INTO ordens_servico(id_os, cliente, servico, valor, status, data_os) VALUES
(1, 'João', 'Troca de Óleo', 120, 'Finalizado', '2026-01-05'),
(2, 'Maria', 'Alinhamento', 80, 'Finalizado', '2026-01-05'),
(3, 'João', 'Freio', 350, 'Finalizado', '2026-01-06'),
(4, 'Carlos', 'Troca de Óleo', 120, 'Pendente', '2026-01-06'),
(5, 'Maria', 'Freio', 300, 'Finalizado', '2026-01-08'),
(6, 'Ana', 'Revisão', 500, 'Finalizado', '2026-01-08'),
(7, 'João', 'Revisão', 500, 'Finalizado', '2026-01-10'),
(8, 'Carlos', 'Alinhamento', 80, 'Finalizado', '2026-01-10'),
(9, 'Ana', 'Freio', 320, 'Pendente', '2026-01-12'),
(10, 'Maria', 'Revisão', 500, 'Finalizado', '2026-01-12'),
(11, 'Pedro', 'Bateria', 450, 'Finalizado', '2026-01-12'),
(12, 'Ana', 'Troca de Óleo', 120, 'Finalizado', '2026-01-15'),
(13, 'João', 'Freio', 380, 'Finalizado', '2026-01-15'),
(14, 'Carlos', 'Bateria', 420, 'Cancelado', '2026-01-18'),
(15, 'Maria', 'Alinhamento', 90, 'Finalizado', '2026-01-18');


-- Consultas

-- ### 1. Listar todas as ordens de serviço

SELECT *
FROM ordens_servico;

-- ### 2. Listar apenas ordens finalizadas

SELECT *
FROM ordens_servico
WHERE status = 'Finalizado';

-- ### 3. Calcular o faturamento total

SELECT sum(valor) as faturamento_total
FROM ordens_servico
WHERE status = 'Finalizado';

-- ### 4. Calcular a quantidade de ordens finalizadas

SELECT count(id_os) as ordens_finalizadas
FROM ordens_servico
WHERE status = 'Finalizado';

-- ### 5. Calcular o faturamento por cliente

SELECT cliente, sum(valor) as faturamento_cliente
FROM ordens_servico
WHERE status = 'Finalizado'
GROUP BY cliente
ORDER BY faturamento_cliente DESC;

-- ### 6. Calcular o faturamento por serviço

SELECT servico, sum(valor) as faturamento_servico
FROM ordens_servico
WHERE status = 'Finalizado'
GROUP BY servico
ORDER BY faturamento_servico DESC;

-- ### 7. Identificar o cliente com maior faturamento

SELECT cliente, sum(valor) as faturamento_cliente
FROM ordens_servico
WHERE status = 'Finalizado'
GROUP BY cliente
ORDER BY faturamento_cliente DESC
LIMIT 1;

-- ### 8. Identificar o serviço com maior ticket médio

SELECT servico, avg(valor) as ticket_medio
FROM ordens_servico
WHERE status = 'Finalizado'
GROUP BY servico
ORDER BY ticket_medio DESC
LIMIT 1;
