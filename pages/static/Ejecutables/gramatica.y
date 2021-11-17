%{
#include <string.h>
#include "funciones.h"
%}
/* Declaraciones de BISON */
%union{
	int entero;
	float deci;
  char *texto;
}
%token <texto> CADENA
%token <deci> DECIMAL
%token <texto> ENTERO
%token <texto> SIGNO
%token <texto> COMA
%token <texto> PUNTO
%token <texto> PAR_IZQ
%token <texto> PAR_DER
%token <texto> IDENTIFICADOR
%token <texto> CONJUNCION
%token <texto> DISYUNCION

%type <texto> consulta
%type <texto> exp
%type <texto> tabla

%%
input: /* cadena vacía */
  | input line;

line: '\n'
  | consulta '\n' {Recibir_cadena_analizador($1);}
  | consulta { Recibir_cadena_analizador($1);}
;
consulta:     exp	{$$ = $1;}
	| IDENTIFICADOR PAR_IZQ exp tabla PAR_DER { $$ = strcat($1,strcat($3,$4));}
	| IDENTIFICADOR exp tabla { $$ = strcat($1,strcat($2,$3));}
	| IDENTIFICADOR PAR_IZQ exp PAR_IZQ consulta PAR_DER PAR_DER {$$ = strcat($1,strcat($3,strcat($4,strcat($5,$6))));}
	| IDENTIFICADOR PAR_IZQ exp PAR_DER PAR_IZQ consulta PAR_DER {$$ = strcat($1,strcat($3,strcat($5,strcat($6,$7))));}
	| IDENTIFICADOR exp PAR_IZQ consulta PAR_DER { $$ = strcat($1,strcat($2,strcat($3,strcat($4,$5))));}
	| PAR_IZQ consulta SIGNO consulta PAR_DER { $$ = strcat($2,strcat($3,$4));}
	| consulta SIGNO consulta {$$ = strcat($1,strcat($2,$3));}
	| PAR_IZQ IDENTIFICADOR exp consulta PAR_DER {$$ = strcat($2,strcat($3,$4));}
	| IDENTIFICADOR exp consulta {$$ = strcat($1,strcat($2,$3));}
	| PAR_IZQ consulta PAR_DER {$$ = strcat($1,strcat($2,$3));}
;
exp: CADENA { $$ = $1;}
	| ENTERO {$$ = $1;}
	| SIGNO {$$ = $1;}
	| exp COMA exp {$$ = strcat($1,strcat($2,$3));}
	| exp PUNTO exp {$$ = strcat($1,strcat($2,$3));}
	| exp IDENTIFICADOR exp {$$ = strcat($1,strcat($2,$3));}
	| exp SIGNO exp {$$ = strcat($1,strcat($2,$3));;}
	| exp CONJUNCION exp {$$ = strcat($1,strcat($2,$3));}
	| exp DISYUNCION exp {$$ = strcat($1,strcat($2,$3));}
	| SIGNO exp {$$ = strcat($1,$2);;}
	;
tabla: PAR_IZQ exp PAR_DER {$$ = strcat($1,strcat($2,$3));}
	;
%%
  int main() {
    yyparse();
  }

  yyerror (char *s)
  {
    printf ("--%s--\n", s);
  }

  int yywrap()
  {
    return 1;
  }
