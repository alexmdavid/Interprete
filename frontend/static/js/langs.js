var atencion = "Atención:"
var txAreaVacio = "Por favor, introduzca su código en el editor antes de validar o ejecutar."
var txvalidarOk = "El código ha sido ejecutado satisfactoriamente."
var txvalidarMal = "El código no es válido."
var txEjecutar = "El código ha sido ejecutado satisfactoriamente."

var es = {
    "tituloP": "Proyecto Final - Intérprete",
    "labeltxArea": "Escriba su código aquí:",
    "btnValidar": "Validar",
    "btnEjecutar": "Ejecutar",
    "lenguaje": "Lenguaje",
    "salida": "Salida",
    "ejemplo": "Código de ejemplo:",
    "español": "Español",
    "ingles": "Inglés",
    "portugues": "Portugués",
    "atencion": "Atención:",
    "txAreaVacio": "Por favor, introduzca su código en el editor antes de validar o ejecutar.",
    "txvalidarOk": "El código ha sido ejecutado satisfactoriamente.",
    "txvalidarMal": "El código no es válido.",
    "txEjecutar": "El código ha sido ejecutado, revise la salida.",
    "lblvoz": "Voz",
    "tablas": "Tablas de multiplicar",
    "vacio": "vacío",
    "suma": "Tablas De Sumar",
    "multiplicar": "Tablas De Multiplicar",
    "dividir": "Tabla de dividir"
};


var en = {
    "tituloP": "Final Project - Interpreter",
    "labeltxArea": "Write your code here:",
    "btnValidar": "Validate",
    "btnEjecutar": "Run",
    "lenguaje": "Language",
    "salida": "Output",
    "ejemplo": "Example code:",
    "español": "Spanish",
    "ingles": "English",
    "portugues": "Portuguese",
    "atencion": "Attention:",
    "txAreaVacio": "Please enter your code in the editor before validating or running.",
    "txvalidarOk": "The code has been processed, everything is fine.",
    "txvalidarMal": "The code is not valid.",
    "txEjecutar": "The code has been executed, check the output.",
    "lblvoz": "Voice",
    "tablas": "Multiplication tables",
    "vacio": "empty",
    "suma": "Sum Tables",
    "multiplicar": "Multiplication Tables",
    "dividir": "Division Table",
    "codigoEjemplo": "Example Codes:"
};

var pt = {
    "tituloP": "Projeto Final - Intérprete",
    "labeltxArea": "Escreva seu código aqui:",
    "btnValidar": "Validar",
    "btnEjecutar": "Corre",
    "lenguaje": "Linguagem",
    "salida": "Partida",
    "ejemplo": "Código de exemplo:",
    "español": "Espanhol",
    "ingles": "Inglês",
    "portugues": "Português",
    "atencion": "Atenção:",
    "txAreaVacio": "Insira seu código no editor antes de validar ou executar.",
    "txvalidarOk": "O código foi processado, está tudo bem.",
    "txvalidarMal": "O código não é válido.",
    "txEjecutar": "O código foi executado, verifique a saída.",
    "lblvoz": "Voz",
    "tablas": "Tabuadas de multiplicação",
    "vacio": "vazio",
    "suma": "Tabelas de Soma",
    "multiplicar": "Tabuadas de multiplicação",
    "dividir": "Tabela de Divisão",
    "codigoEjemplo": "Códigos de Exemplo:"
};



$(function () {
    $("#language").change(function (e) { 
        cambiarIdioma($("#language").val())
    });
});

function cambiarIdioma(lang) {
    //cambiando idioma, español = 1, ingles = 2, portugés = 3
    let lg
    if(lang == 1){
        lg = es
    }else if(lang == 2){
        lg = en
    }else if(lang == 3){
        lg = pt
    }

    $("#tituloP").text(lg.tituloP)
    $(".creditos").text(lg.creditos)
    $("#tituloCodigo").empty()
    $("#tituloCodigo").append('<i class="fa-solid fa-code"></i> '+lg.labeltxArea)
    $("#expls").empty()
    $("#expls").append('<i class="fa-solid fa-note-sticky"></i> '+lg.ejemplo)
    $("#lenguaje").text(lg.lenguaje)
    $("#ES").text(lg.español)
    $("#EN").text(lg.ingles)
    $("#PT").text(lg.portugues)
    $("#btnVerificar").empty()
    $("#btnVerificar").append('<i class="fa-solid fa-glasses"></i> '+lg.btnValidar)
    $("#btnEjecutar").empty()
    $("#btnEjecutar").append('<i class="fa-solid fa-play"></i> '+lg.btnEjecutar)
    $("#salida").empty()
    $("#salida").append('<i class="fa-solid fa-outdent"></i> '+lg.salida)
    $("#lblVoz").text(lg.lblvoz)
    $("#tablas").text(lg.tablas)
    $("label[for='opciones']").text(lg.codigoEjemplo);
    $("#opciones option[value='vacio']").text(lg.vacio);
    $("#opciones option[value='suma']").text(lg.suma);
    $("#opciones option[value='multiplicar']").text(lg.multiplicar);
    $("#opciones option[value='dividir']").text(lg.dividir);
    
    atencion = lg.atencion
    txAreaVacio = lg.txAreaVacio
    txvalidarOk = lg.txvalidarOk
    txvalidarMal = lg.txvalidarMal
    txEjecutar = lg.txEjecutar
}