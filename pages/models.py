from django.db import models

class Curso(models.Model):
    cursoid = models.IntegerField(db_column='CursoID', primary_key=True)  # Field name made lowercase.
    profesorid = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='ProfesorID')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso'


class Departamento(models.Model):
    deptoid = models.IntegerField(db_column='DeptoID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


class Profesor(models.Model):
    profesorid = models.IntegerField(db_column='ProfesorID', primary_key=True)  # Field name made lowercase.
    deptoid = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='DeptoID')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profesor'
