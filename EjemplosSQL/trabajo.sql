CREATE DATABASE trabajo;

CREATE TABLE departamento (
    DepartamentoID int NOT NULL PRIMARY KEY,
    Nombre varchar(40) NOT NULL UNIQUE KEY
);

CREATE TABLE empleado (
    EmpleadoID int NOT NULL,
    DepartamentoID int NOT NULL,
    FechaNacimiento date NOT NULL,
    Nombre  varchar(50) NOT NULL,
    FechaContratacion date NOT NULL,
    Salario int NOT NULL,
    CONSTRAINT empleado_departamento FOREIGN KEY (DepartamentoID) REFERENCES departamento(DepartamentoID),
    PRIMARY KEY (EmpleadoID)
);

INSERT INTO departamento(DepartamentoID,Nombre) VALUES
    (1,"Administracion"),
    (2,"Recursos Humanos"),
    (3,"Ventas"),
    (4,"Sistemas");

INSERT INTO empleado(EmpleadoID,DepartamentoID,FechaNacimiento,Nombre,FechaContratacion,Salario) VALUES
    (1,1,"1985-05-25","Rodrigo López Castro","2020-01-07",4500),
    (2,1,"1986-05-23","Mario Alberto Martínez Sánchez","2019-05-05",8000),
    (3,1,"1984-03-14","Alejandro Santiago Mendoza","2020-07-15",7000),
    (4,2,"1985-11-12","Paulina Sánchez Valadez","2017-05-01",7500),
    (5,2,"1990-06-05","Lorena Castro Gutierrez","2018-11-22",10500),
    (6,3,"1992-02-09","Karen Bustos Brisuela","2020-01-07",21000),
    (7,3,"1988-10-15","Daniela Rivera Fuentes","2015-12-06",13500),
    (8,3,"1991-11-17","Eduardo Pérez Zambrano","2019-01-25",5500),
    (9,3,"1994-08-22","Ana Alcantara Solano","2020-01-07",5500),
    (10,4,"1990-06-08","Maria Rojas Vargas","2019-06-22",13000);