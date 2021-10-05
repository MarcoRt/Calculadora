// Botones de Operaciones
const botonSeleccion    = document.querySelector("#seleccion");
const botonProyeccion   = document.querySelector("#proyeccion");
const botonReunion      = document.querySelector("#reunion");
const botonProducto     = document.querySelector("#producto");
const botonUnion        = document.querySelector("#union");
const botonInterseccion = document.querySelector("#interseccion");
const botonDiferencia   = document.querySelector("#diferencia");
const enviarConsulta    = document.querySelector(".enviar-consulta")

// Textarea de la expresion
const expresion = document.querySelector(".herramienta-expresion__input");

// Expresiones de Operaciones
const expresionSeleccion    = 'σ()';
const expresionProyeccion   = 'π()';
const expresionReunion      = '⋈()';
const expresionProducto     = 'X';
const expresionUnion        = '∪';
const expresionInterseccion = '∩';
const expresionDiferencia   = '-';

// Funciones de botones de operaciones
$(botonSeleccion).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionSeleccion + textAfter);
});

$(botonProyeccion).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionProyeccion + textAfter);
});

$(botonReunion).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionReunion + textAfter);
});

$(botonProducto).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionProducto + textAfter);
});

$(botonUnion).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionUnion + textAfter);
});

$(botonInterseccion).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionInterseccion + textAfter);
});

$(botonDiferencia).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionDiferencia + textAfter);
});