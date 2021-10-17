echo Compilando archivos

flex /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/analizador.l

bison /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/gramatica.y -d

mv /home/marco/Documentos/GitHub/Calculadora/*.c /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables

mv /home/marco/Documentos/GitHub/Calculadora/*.h /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables

gcc /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/lex.yy.c /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/gramatica.tab.c -w

mv /home/marco/Documentos/GitHub/Calculadora/a.out /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables
