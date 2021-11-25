// Botones de Operaciones
const botonSeleccion    = document.querySelector("#seleccion");
const botonProyeccion   = document.querySelector("#proyeccion");
//const botonReunion      = document.querySelector("#reunion");
const botonProducto     = document.querySelector("#producto");
const botonUnion        = document.querySelector("#union");
// const botonInterseccion = document.querySelector("#interseccion");
const botonDiferencia   = document.querySelector("#diferencia");
const botonConjuncion   = document.querySelector("#conjuncion");
const botonDisyuncion   = document.querySelector("#disyuncion");
const enviarConsulta    = document.querySelector(".enviar-consulta")
const borrarConsulta    = document.querySelector("#borrar-consulta");

// Textarea de la expresion
const expresion = document.querySelector(".herramienta-expresion__input");

// Expresiones de Operaciones
const expresionSeleccion    = 'σ';
const expresionProyeccion   = 'π';
//const expresionReunion      = '(Relacion1)⋈(condicion)(Relacion2)';
const expresionProducto     = 'X';
const expresionUnion        = '∪';
// const expresionInterseccion = '∩';
const expresionDiferencia   = '-';
const expresionConjuncion   = '∧';
const expresionDisyuncion   = '∨';

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

// $(botonReunion).on('click', function () {
//     var cursorPos = $(expresion).prop('selectionStart');
//     var v = $(expresion).val();
//     var textBefore = v.substring(0,  cursorPos);
//     var textAfter  = v.substring(cursorPos, v.length);
//     $(expresion).val(textBefore + expresionReunion + textAfter);
// });

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

// $(botonInterseccion).on('click', function () {
//     var cursorPos = $(expresion).prop('selectionStart');
//     var v = $(expresion).val();
//     var textBefore = v.substring(0,  cursorPos);
//     var textAfter  = v.substring(cursorPos, v.length);
//     $(expresion).val(textBefore + expresionInterseccion + textAfter);
// });

$(botonDiferencia).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionDiferencia + textAfter);
});

$(botonConjuncion).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionConjuncion + textAfter);
});

$(botonDisyuncion).on('click', function () {
    var cursorPos = $(expresion).prop('selectionStart');
    var v = $(expresion).val();
    var textBefore = v.substring(0,  cursorPos);
    var textAfter  = v.substring(cursorPos, v.length);
    $(expresion).val(textBefore + expresionDisyuncion + textAfter);
});

$(borrarConsulta).on('click', function () {
    $(expresion).val('');
});
