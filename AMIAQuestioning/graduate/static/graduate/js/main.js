$(document).ready(function() {
    'use strict';

    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    });

    $('.marital_status').on('click', function () {
        $('#id_married_from').prop('disabled', true).prop('required', false);
        let id = $(this).val();
        if (id === "2") {
            $('#id_married_from').prop('disabled', false).prop('required', true);
        }
    });

    $('#id_has_children_0, #id_has_children_1').on('click', function () {
        $('#id_children_data').prop('disabled', true).prop('required', false);
        let id = $(this).val();
        if (id === "1") {
            $('#id_children_data').prop('disabled', false).prop('required', true);
        }
    });

    $('.parents').on('click', function () {
        // $('#id_children_data').prop('disabled', true).prop('required', false);
        $('#id_divorced_from, #id_mother_only_father_died_in, #id_mother_only_father_died_other, #id_father_only_mother_died_in, #id_father_only_mother_died_other, #id_guardians_other, #id_guardians').prop('disabled', true).prop('required', false);
        $('#id_divorced_live').find('input').prop('disabled', true).prop('required', false);
        $('#id_stepfather_stepmother_marriage').find('input').prop('disabled', true).prop('required', false);
        $('.stepfather_stepmother_marriage_1').find('input').prop('disabled', true).prop('required', false);
        $('.stepfather_stepmother_marriage_2').find('input').prop('disabled', true).prop('required', false);
        $('#id_mother_father_data').find('input').prop('disabled', true).prop('required', false);
        $('#id_guardians').find('input').prop('disabled', true).prop('required', false);
        $('#id_divorced_live_0').prop('checked', false);
        $('#id_stepfather_stepmother_marriage_mother_0').prop('checked', false);
        $('#id_stepfather_stepmother_marriage_father_0').prop('checked', false);
        $('#id_mother_father_data_0').prop('checked', false);
        let id = $(this).val();
        switch (id) {
            case "2":
                $('#id_divorced_from, #id_divorced_live').prop('disabled', false).prop('required', true);
                $('#id_divorced_live').find('input').prop('disabled', false).prop('required', true);
                $('#id_divorced_from').focus();
                $('#id_divorced_live_0').click();
                break;
            case "3":
                $('#id_mother_only_father_died_in, #id_mother_only_father_died_other').prop('disabled', false);
                break;
            case "4":
                $('#id_father_only_mother_died_in, #id_father_only_mother_died_other').prop('disabled', false);
                break;
            case "5":
                $('.stepfather_stepmother_marriage_1').find('input').prop('disabled', false);
                $('#id_stepfather_stepmother_marriage_mother_0').click();
                break;
            case "6":
                $('.stepfather_stepmother_marriage_2').find('input').prop('disabled', false);
                $('#id_stepfather_stepmother_marriage_father_0').click();
                break;
            case "7":
                $('#id_mother_father_data').find('input').prop('disabled', false);
                $('#id_mother_father_data_0').click();
                break;
            case "8":
                $('#id_guardians').find('input').prop('disabled', false);
                $('#id_guardians_other').prop('disabled', false);
                break;
        }
    });

    $('#id_sport_is_only_by_program').on('click', function () {
        $('#id_sport_kind, #id_sport_period, #id_sport_achievements').prop('disabled', true).prop('required', false);
        $('#id_sport_level').find('input').prop('disabled', true).prop('required', false);
        let id = $(this).val();
        if (id === "1") {
            $('#id_sport_kind, #id_sport_period, #id_sport_achievements').prop('disabled', false).prop('required', true);
            $('#id_sport_level').find('input').prop('disabled', false).prop('required', true);
        }
    });

    $('input.induce_to_quit').on('click', function () {
        let id = $(this).val();

        if (id === "24") {
            if ($('#id_what_induce_to_quit_other').prop('disabled') == true){
                $('#id_what_induce_to_quit_other').prop('disabled', false).prop('required', true);
            } else {
                $('#id_what_induce_to_quit_other').prop('disabled', true);
            }
        }
    });

    $('input.what_keeps').on('click', function () {
        let id = $(this).val();

        if (id === "23") {
            if ($('#id_what_keeps_other').prop('disabled') == true){
                $('#id_what_keeps_other').prop('disabled', false).prop('required', true);
            } else {
                $('#id_what_keeps_other').prop('disabled', true);
            }
        }
    });

    $('#id_need_conversation').find('input').on('click', function () {
        $('#id_need_conversation_theme').prop('disabled', true).prop('required', false);
        let id = $(this).val();
        if (id === "2") {
            $('#id_need_conversation_theme').prop('disabled', false).prop('required', true);
        }
    });

    $( "#graduate_form").submit(function(event) {
    event.preventDefault();
    event.stopPropagation();

    var form = document.getElementsByClassName('needs-validation');

    if (form[0].checkValidity() === true) {
        form[0].submit();
    }
    else {
       alert('Пропущен один или несколько ответов (вопросы обозначены красным цветом)!');
    }

    form[0].classList.add('was-validated');
});

});