%{
#include "gramatica.tab.h"
#include <string.h>
%}
DIGITO [0-9]+
IDENTIFICADOR [P][I][_][1]|[S][E][_][1]
SIGNO [=]|[<]|[>]|[<][=]|[>][=]|[!][=]|[/]|[-]|[+]|[U][N][I][O][N]|[E][Q][U][I][S]|[D][I][F][E][R][E][N][T][E]|[I][N][T][E][R]
VARIABLE [']*["]*[a-zA-Z]+[0-9_]*[a-zA-Z]*["]*[']*
VARIABLES ["]+([a-zA-Z]+[0-9_]*[" "][a-zA-Z]+[0-9_]*)*["]+|[']+([a-zA-Z]+[0-9_]*[" "][a-zA-Z]+[0-9_]*)*[']+
ESPACIO [" "]
%%
{DIGITO} {//printf("Digito %s\n",yytext);
yylval.texto = (char *) strdup(yytext);
return ENTERO;
}

{IDENTIFICADOR} {printf("Identificador\n");
yylval.texto = (char *) strdup(yytext);
  return (IDENTIFICADOR);}

{SIGNO} {//printf("Signo\n");
yylval.texto = (char *) strdup(yytext);
  return (SIGNO);
}


"(" {//printf("Paréntesis izquierdo\n");
yylval.texto = (char *) strdup(yytext);
  return (PAR_IZQ);
}


")" {//printf("a\n");
yylval.texto = (char *) strdup(yytext);
  return (PAR_DER);
}


"," {//printf("Coma\n");
yylval.texto = (char *) strdup(yytext);
  return (COMA);}

  "." {//printf("Punto\n");
  yylval.texto = (char *) strdup(yytext);
    return (PUNTO);}
  "^" {//printf("Y\n");
  yylval.texto = (char *) strdup(yytext);
    return (CONJUNCION);}

    "^^" {//printf("O\n");
    yylval.texto = (char *) strdup(yytext);
      return (DISYUNCION);}

{VARIABLE}|{VARIABLE}"_"{VARIABLE} {//printf("Cadena\n");
yylval.texto = (char *) strdup(yytext);
return CADENA;
}

{VARIABLES} {//printf("Cadena\n");
yylval.texto = (char *) strdup(yytext);
return CADENAS;
}

"\n"            {
		//printf("Salto de linea\n");
                return (yytext[0]);
                }
