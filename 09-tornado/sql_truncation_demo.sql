-- Crear base de datos de prueba
DROP DATABASE IF EXISTS truncation_test;
CREATE DATABASE truncation_test;
USE truncation_test;

-- Desactivar modo estricto para simular el ataque
SET SESSION sql_mode = '';

-- Crear tabla vulnerable
CREATE TABLE users (
    username VARCHAR(13),
    password VARCHAR(100)
);

-- Insertar usuario legítimo
INSERT INTO users (username, password) VALUES ('jacob@tornado', 'originalpass');

-- Simular intento de registro malicioso (truncado silenciosamente)
INSERT INTO users (username, password) VALUES ('jacob@tornadoX', 'attackerpass');

-- Mostrar resultados
SELECT 'Contenido actual de la tabla:' AS info;
SELECT username, password FROM users;

-- Simular login inseguro
SELECT 'Simulando login inseguro con username truncado:' AS info;
SELECT * FROM users WHERE username = 'jacob@tornado' AND password = 'attackerpass' LIMIT 1;

-- ============================
-- Prevención
-- ============================

-- Activar modo estricto global (requiere privilegios de superusuario)
-- SET GLOBAL sql_mode = 'STRICT_ALL_TABLES';

-- Agregar restricción de unicidad
ALTER TABLE users ADD UNIQUE (username);

-- Intento de inserción con truncamiento (debería fallar si modo estricto + UNIQUE están activos)
-- Comentado para evitar error en ejecución inicial
-- INSERT INTO users (username, password) VALUES ('jacob@tornadoZZ', 'blockme');

-- Verificación final
SELECT 'Después de aplicar medidas de prevención:' AS info;
SELECT username, password FROM users;

