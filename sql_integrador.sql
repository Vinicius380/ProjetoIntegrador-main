USE bd_medidor;

CREATE TABLE tb_memoria(
    id INT AUTO_INCREMENT PRIMARY KEY,
    prompt LONGTEXT,
    resposta_gemini LONGTEXT
);

CREATE TABLE `tb_registro` (
  `id` int NOT NULL AUTO_INCREMENT,
  `temperatura` decimal(10,2) DEFAULT NULL,
  `pressao` decimal(10,2) DEFAULT NULL,
  `altitude` decimal(10,2) DEFAULT NULL,
  `umidade` decimal(10,2) DEFAULT NULL,
  `co2` decimal(10,2) DEFAULT NULL,
  `poeira` decimal(10,2) DEFAULT NULL,
  `tempo_registro` datetime DEFAULT NULL,
  `regiao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);


DROP TABLE tb_registro;

SELECT * FROM tb_registro;