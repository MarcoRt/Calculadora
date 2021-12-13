CREATE DATABASE escuela;

CREATE TABLE departamento (
	DeptoID int NOT NULL,
	Nombre varchar(50) NOT NULL,
	Director varchar(50) NOT NULL,
	Descripcion varchar(100) NOT NULL,
	PRIMARY KEY(DeptoID)
);

CREATE TABLE profesor (
	ProfesorID int NOT NULL,
	DeptoID int NOT NULL,
	Nombre varchar(50) NOT NULL,
	Direccion varchar(100) NOT NULL,
	Telefono int NOT NULL,
	PRIMARY KEY (ProfesorID),
	CONSTRAINT profesor_departamento FOREIGN KEY (DeptoID) REFERENCES departamento(DeptoID)
);

CREATE TABLE curso(
	CursoID int NOT NULL,
	Nombre varchar(50) NOT NULL,
	PRIMARY KEY (CursoID)
);

CREATE TABLE profesor_curso (
	ProfesorID int NOT NULL,
	CursoID int NOT NULL,
	CONSTRAINT profesor_curso_profesor FOREIGN KEY (ProfesorID) REFERENCES profesor(ProfesorID),
	CONSTRAINT profesor_curso_curso FOREIGN KEY (CursoID) REFERENCES curso(CursoID),
	CONSTRAINT profesor_curso_unique UNIQUE (ProfesorID,CursoID)
);

INSERT INTO departamento(DeptoID,Nombre,Director,Descripcion) VALUES
	(1,"Ingenieria","Miguel Velazquez","Departamento encargado del area de ingenieria"),
	(2,"Ciencias Sociales","Mateo Sousa","Departamento encargado del area de ciencias sociales"),
	(3,"Ciencias de la Salud","Mercedes Romero","Departamento encargado del area de ciencias de la salud");

INSERT INTO profesor(ProfesorID,DeptoID,Nombre,Direccion,Telefono) VALUES
	(1,1,"Ildefonso Castillo","LEANDRO VALLE NO. 370 S/N, IRAPUATO CENTRO, 36500",55849615),
	(2,1,"Rafael Donoso","AV SAN PEDRO NO. 100 Int. F, SAN LUIS POTOSI CENTRO, 78000",55742653),
	(3,1,"Toribio Pizarro","BRAVO NO. 726, CENTRO, 91700",55423618),
	(4,2,"Efraín Costa","PARQUE NOROESTE NO. 718, EJIDAL, 81283",55684832),
	(5,2,"Ariadna Lerma","ORTIZ RUBIO NO. 300 NO. F, TECATE CENTRO, 21400",55421463),
	(6,3,"Esmeralda Chaparro","REPUBLICA NO 40 LOCAL 507, PLAZA TAPATIA, 443107",55854523),
	(7,3,"Priscila Bayón","CALLE 56 508 ALTOS, MERIDA CENTRO, 97000",55874569);

INSERT INTO curso(CursoID,Nombre) VALUES
	(101,"Calculo"),
	(102,"Algebra Lineal"),
	(103,"Calculo Avanzado"),
	(201,"Historia de Mexico"),
	(202,"Filosofia y Logica"),
	(301,"Introduccion a la Psicologia"),
	(302,"Nutricion");

INSERT INTO profesor_curso(ProfesorID,CursoID) VALUES
	(1,101),
	(2,102),
	(3,103),
	(4,201),
	(5,202),
	(6,301),
	(7,302);