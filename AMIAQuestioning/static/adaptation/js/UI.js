$(document).ready(function() {

    init();

    $('#id_tension_29').on('click', function () {
        let status = $('#id_tension_29').prop("checked");

        $("#id_tension_other").prop( "disabled", !status).prop("required", status);
    });


    function init(){

        let status = $('#id_tension_29').prop("checked");
        $("#id_tension_other").prop( "disabled", !status).prop("required", status);

    }

    $('.conversation_theme').on('change', function () {
        $('#id_need_a_conversation_theme').prop( "disabled", true).prop("required", false);
        let id = $(this).val();
        if (id == 2){
            $('#id_need_a_conversation_theme').prop( "disabled", false).prop("required", true);
        }
    });

});