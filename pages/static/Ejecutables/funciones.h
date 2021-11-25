#include <stdio.h>
#include <time.h>
#include <stdlib.h>
//Recibe la cadena del analizador semántico y crea un archivo de texto con la sentencia
int Recibir_cadena_analizador(char *string)
{
  int n = 10000;
  char * oracion = malloc(n * sizeof(char));
  //printf("%s\n",string);
  strcpy(oracion,string);
  n = strlen(oracion);
  char nombre_archivo [100];
  time_t t = time(NULL);
  srand((unsigned) time(&t));
  struct tm tm = *localtime(&t);
  int numero = (rand() % 500000);
  numero = numero * (tm.tm_hour+tm.tm_hour+tm.tm_sec);
  sprintf(nombre_archivo, "%d", numero);
  char buf[0x1000];
  snprintf(buf, sizeof(buf), "/home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/Archivos_consulta/%s", nombre_archivo);
  FILE *consulta = fopen(buf,"wt");
  if(consulta==NULL)
  {
    printf("Error: no se ha podido acceder al fichero\n");
  }
  else{
    fwrite(oracion,n,1,consulta);
    fclose(consulta);
    printf("\n%d",numero);
  }
}
