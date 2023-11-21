$(function () {
    $("#btnVerificar").click(function (e) {
        let codigo = $("#codigoDigitado").val().trim();
        $("#textico").empty()
        if (codigo != "") {
            $.ajax({
                url: "validar/",
                method: "GET",
                dataType: "json",
                data:{
                    'codigo': codigo
                },
                success: function (respuesta) {
                    validarOk()
                    console.log(respuesta)
                },
                error: function () {
                    validarMal()
                }
            });
        } else {
            campoVacio()
        }
    });

    $("#btnEjecutar").click(function (e) {
        let codigo = $("#codigoDigitado").val().trim();
        $("#textico").empty()
        if (codigo != "") {
            $.ajax({
                url: "ejecutar/",
                method: "GET",
                dataType: "json",
                data:{
                    'codigo': codigo
                },
                success: function (respuesta) {
                    ejecutarOk()
                    $("#textico").append(respuesta.resultado.replaceAll("\n", "<br>"))
                    console.log(respuesta)
                },
                error: function () {
                    validarMal()
                }
            });
        } else {
            campoVacio()
        }
    });

    
    // Escucha el evento de cambio en las opciones del menú desplegable
    $("#opciones").change(function() {
        // Obtiene el valor seleccionado
        var seleccion = $(this).val();
        
        // Obtiene el contenido del pre correspondiente a la opción seleccionada
        var contenido = $("#" + seleccion).text();
        
        // Muestra el contenido en el textarea con ID "codigoDigitado"
        $("#codigoDigitado").val(contenido);
    });
   
      
});

function deselect() {
    $('.form-select').attr("disabled", true);
    $('.form-select').attr("disabled", false);
}

//Alertas

function campoVacio() {
    Swal.fire({
        title: atencion,
        text: txAreaVacio,
        icon: 'warning'
    })

    speak(txAreaVacio)
}

function validarOk() {
    Swal.fire({
        title: atencion,
        text: txvalidarOk,
        icon: 'success'
    })

    speak(txvalidarOk)
}

function validarMal() {
    Swal.fire({
        title: atencion,
        text: txvalidarMal,
        icon: 'error'
    })

    speak(txvalidarMal)
}

function ejecutarOk() {
    Swal.fire({
        title: atencion,
        text: txEjecutar,
        icon: 'success'
    })

    speak(txEjecutar)
}