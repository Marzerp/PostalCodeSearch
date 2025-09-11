CREATE DATABASE IF NOT EXISTS codigos_postales;
USE codigos_postales;

CREATE TABLE IF NOT EXISTS cp (
d_codigo VARCHAR(5) NOT NULL,
d_asenta VARCHAR(120) NOT NULL,
d_tipo_asenta VARCHAR(60) NULL,
D_mnpio VARCHAR(100) NOT NULL,
d_estado VARCHAR(100) NOT NULL,
d_ciudad VARCHAR(100) NULL,
d_CP VARCHAR(5) NULL,
c_estado VARCHAR(2) NULL,
c_oficina VARCHAR(5) NULL,
c_CP VARCHAR(5) NULL,
c_tipo_asenta VARCHAR(2) NULL,
c_mnpio VARCHAR(3) NULL,
id_asenta_cpcons INT NULL,
d_zona VARCHAR(10) NULL,
c_cve_ciudad VARCHAR(4) NULL
);

--SET GLOBAL local_infile=1;

LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/CPdescarga.txt' 
INTO TABLE cp
CHARACTER SET latin1
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 2 LINES
(d_codigo, d_asenta, d_tipo_asenta, D_mnpio, d_estado, d_ciudad, d_CP, c_estado, c_oficina, c_CP, c_tipo_asenta, c_mnpio, id_asenta_cpcons, d_zona, c_cve_ciudad);

CREATE INDEX idx_asenta_prefix ON cp (d_asenta);
CREATE INDEX idx_mnpio_prefix ON cp (D_mnpio);

ALTER USER 'root'@'%' IDENTIFIED BY 'flaskpass';
FLUSH PRIVILEGES;

CREATE USER IF NOT EXISTS 'flaskuser'@'%' IDENTIFIED BY 'flaskpass';
GRANT ALL PRIVILEGES ON codigos_postales.* TO 'flaskuser'@'%';
FLUSH PRIVILEGES;
