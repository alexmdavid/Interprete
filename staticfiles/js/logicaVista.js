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

    $('#codigoDigitado').keydown(function (e) {
        if (e.keyCode === 9) {
            var start = this.selectionStart;
            end = this.selectionEnd;

            var $this = $(this);

            $this.val($this.val().substring(0, start)
                + " "
                + $this.val().substring(end));
            this.selectionStart = this.selectionEnd = start + 1;
            return false;
        }
    });

    $(".exItem").click(function (e) { 
        $("#codigoDigitado").val($("#ejemploAll").text())
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