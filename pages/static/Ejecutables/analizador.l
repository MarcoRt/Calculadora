%{
#include "gramatica.tab.h"
#include <string.h>
%}
DIGITO [0-9]+
IDENTIFICADOR [P][I]|[S][E]
SIGNO [=]|[<]|[>]|[<][=]|[>][=]|[!][=]|[/]|[-]|[+]|[U][N][I][O][N]|[E][Q][U][I][S]|[D][I][F][E][R][E][N][T][E]
VARIABLE ["]*[a-zA-Z]+[0-9_]*["]*
%%
{DIGITO} {//printf("Digito %s\n",yytext);
yylval.texto = (char *) strdup(yytext);
return ENTERO;
}

{IDENTIFICADOR} {//printf("Identificador\n");
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


  "^" {//printf("Y\n");
  yylval.texto = (char *) strdup(yytext);
    return (CONJUNCION);}

    "^^" {//printf("O\n");
    yylval.texto = (char *) strdup(yytext);
      return (DISYUNCION);}

{VARIABLE} {//printf("Cadena\n");
yylval.texto = (char *) strdup(yytext);
return CADENA;
}


"\n"            {
		//printf("Salto de linea\n");
                return (yytext[0]);
                }
