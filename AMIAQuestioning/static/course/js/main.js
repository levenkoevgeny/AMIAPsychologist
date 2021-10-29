$(document).ready(function() {
    'use strict';

    init_page();

    $('.education').on('click', function () {
        var id = $(this).val();
        var year_inputs = $('#education_1_year_of_graduation, #education_2_year_of_graduation, #education_3_year_of_graduation, #id_specialty');
        year_inputs.prop('disabled', true).prop('required', false);
        switch (id) {
            case "1":
                $('#education_1_year_of_graduation').prop('disabled', false).prop('required', true);
                break;
            case "2":
                $('#education_2_year_of_graduation').prop('disabled', false).prop('required', true);
                break;
            case "3":
                $('#education_3_year_of_graduation, #id_specialty').prop('disabled', false).prop('required', true);
                break;
        }
    });

    $('.military').on('click', function () {
        var id = $(this).val();
        var year_inputs = $('#id_military_year_since, #id_military_year_till, #id_military_place, #id_type_of_army');
        year_inputs.prop('disabled', true).prop('required', false);
        switch (id) {
            case "1":
                year_inputs.prop('disabled', true).prop('required', false);
                break;
            case "2":
                year_inputs.prop('disabled', false).prop('required', true);
                break;
        }
    });

    $('.marriage').on('click', function () {
        var id = $(this).val();
        var year_inputs = $('#id_marriage_year_since, #id_marriage_year_till');
        year_inputs.prop('disabled', true).prop('required', false);
        switch (id) {
            case "1":
                year_inputs.prop('disabled', true).prop('required', false);
                break;
            case "2":
                year_inputs.prop('disabled', false).prop('required', true);
                break;
        }
    });

    $('[name|="children"]').on('click', function () {
        var id = $(this).val();
        var year_inputs = $('#id_children_info');
        year_inputs.prop('disabled', true).prop('required', false);
        switch (id) {
            case "1":
                year_inputs.prop('disabled', true).prop('required', false);
                break;
            case "2":
                year_inputs.prop('disabled', false).prop('required', true);
                break;
        }
    });

    $('#id_participation_in_education_11').on('change', function () {
        if ($(this).prop("checked")==true){
            $('#id_participation_in_education_other').prop('disabled', false).prop('required', true);
        } else {
            $('#id_participation_in_education_other').prop('disabled', true).prop('required', false);
        }
    });

    $('.parents').on('click', function () {
        var id = $(this).val();
        var year_inputs = $('.parents_1_radio, .parents_2_radio, .parents_3_radio, .parents_4_radio, .parents_5_radio, .parents_6_radio');
        year_inputs.prop('disabled', true).prop('required', false);
        $('[name|="guardian"]').prop('disabled', true);
        switch (id) {
            case "1":
                $('.parents_1_radio').prop('disabled', false).prop('required', true);
                break;
            case "2":
                $('.parents_2_radio').prop('disabled', false);
                break;
            case "3":
                $('.parents_3_radio').prop('disabled', false).prop('required', true);
                break;
            case "4":
                $('.parents_4_radio').prop('disabled', false).prop('required', true);
                break;
            case "5":
                $('.parents_5_radio').prop('disabled', false);
                break;
            case "6":
                $('.parents_6_radio').prop('disabled', false);
                break;
            case "7":
                $('[name|="guardian"]').prop('disabled', false);
                // $('.parents_7_radio').prop('disabled', false);
                break;
            default:
                $('.parents_1_radio, .parents_2_radio, .parents_3_radio, .parents_4_radio, .parents_5_radio, .parents_6_radio').prop('disabled', true).prop('required', false);
                $('[name|="guardian"]').prop('disabled', true);
        }
    });

    $('#id_relationship_8').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_relationship_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_relationship_other").prop( "disabled", true).prop('required', false);
        }
    });

    $('#id_interest_43').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_interest_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_interest_other").prop( "disabled", true).prop('required', false);
        }
    });

    $('#id_guardian_6').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_guardian_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_guardian_other").prop( "disabled", true).prop('required', false);
        }
    });

    $('[name|="is_chronic_diseases"]').on('click', function () {
        var id = $(this).val();
        switch (id) {
            case "2":
                $('#id_chronic_diseases').prop('disabled', false).prop('required', true);
                break;
            case "1":
                $('#id_chronic_diseases').prop('disabled', true).prop('required', false);
                break;
        }
    });

    $('[name|="is_injury"]').on('click', function () {
        var id = $(this).val();
        switch (id) {
            case "2":
                $('#id_injury').prop('disabled', false).prop('required', true);
                break;
            case "1":
                $('#id_injury').prop('disabled', true).prop('required', false);
                break;
        }
    });


    $('#id_particular_qualities_8').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_particular_qualities_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_particular_qualities_other").prop( "disabled", true).prop('required', false);
        }
    });

    $('#id_relatives_record_6').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_relatives_record_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_relatives_record_other").prop( "disabled", true).prop('required', false);
        }
    });

    $('[name|="living_conditions_premises"]').on('click', function () {
        var id = $(this).val();
        switch (id) {
            case "4":
                $("#id_living_conditions_premises_other").prop( "disabled", false).prop('required', true);
                break;
            default:
                $("#id_living_conditions_premises_other").prop( "disabled", true).prop('required', false);
        }
    });


    $('#id_activity_6').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_activity_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_activity_other").prop( "disabled", true).prop('required', false);
        }
    });

    $('#id_ability_10').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_ability_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_ability_other").prop( "disabled", true).prop('required', false);
        }
    });


    $('[name|="gaming"]').on('click', function () {
        var id = $(this).val();
        var inputs = $('#id_gaming_hours_1, #id_gaming_hours_2');
        inputs.prop( "disabled", true).prop('required', false);
        switch (id) {
            case "3":
                $("#id_gaming_hours_1").prop( "disabled", false).prop('required', true);
                break;
            case "4":
                $("#id_gaming_hours_2").prop( "disabled", false).prop('required', true);
                break;
        }
    });

    $('#id_messenger_10').on('click', function () {
        if ($(this).prop("checked")==true){
            $("#id_messenger_other").prop( "disabled", false).prop('required', true);
        } else {
            $("#id_messenger_other").prop( "disabled", true).prop('required', false);
        }

    });


    $('[name|="smoking"]').on('click', function () {
        var id = $(this).val();
        var inputs = $('#id_smoking_try_in_year, #id_smoking_beginning_in_year_1, #id_smoking_beginning_in_year_2, #id_smoking_beginning_in_year_3, #id_smoking_ending_in_year');
        inputs.prop( "disabled", true).prop('required', false);
        switch (id) {
            case "2":
                $("#id_smoking_try_in_year").prop( "disabled", false).prop('required', true);
                break;
            case "3":
                $("#id_smoking_beginning_in_year_1, #id_smoking_ending_in_year").prop( "disabled", false).prop('required', true);
                break;
            case "4":
                $("#id_smoking_beginning_in_year_2").prop( "disabled", false).prop('required', true);
                break;
            case "5":
                $("#id_smoking_beginning_in_year_3").prop( "disabled", false).prop('required', true);
                break;
        }
    });

});

function  init_page() {
    $('#education_1_year_of_graduation').prop('required', true);
    // alert('init');
    // alert($('#id_participation_in_education_11').prop("checked"));
    if ($('#id_participation_in_education_11').prop("checked") == true) {
        $('#id_participation_in_education_other').prop('disabled', false).prop('required', true);
    } else {
        $('#id_participation_in_education_other').prop('disabled', true).prop('required', false);
    }

    if ($('#id_guardian_6').prop("checked") == true) {
        $("#id_guardian_other").prop("disabled", false).prop('required', true);
    } else {
        $("#id_guardian_other").prop("disabled", true).prop('required', false);
    }

    if ($('#id_relationship_8').prop("checked") == true) {
        $("#id_relationship_other").prop("disabled", false).prop('required', true);
    } else {
        $("#id_relationship_other").prop("disabled", true).prop('required', false);
    }

    if ($('#id_interest_43').prop("checked")==true){
        $("#id_interest_other").prop( "disabled", false).prop('required', true);
    } else {
        $("#id_interest_other").prop( "disabled", true).prop('required', false);
    }

    if ($('#id_particular_qualities_8').prop("checked")==true){
        $("#id_particular_qualities_other").prop( "disabled", false).prop('required', true);
    } else {
        $("#id_particular_qualities_other").prop( "disabled", true).prop('required', false);
    }

    if ($('#id_relatives_record_6').prop("checked")==true){
        $("#id_relatives_record_other").prop( "disabled", false).prop('required', true);
    } else {
        $("#id_relatives_record_other").prop( "disabled", true).prop('required', false);
    }

    var id = $('[name|="living_conditions_premises"]:checked').val();
    if (id === "4"){
        $("#id_living_conditions_premises_other").prop( "disabled", false).prop('required', true);
    }

    if ($('#id_activity_6').prop("checked")==true){
        $("#id_activity_other").prop( "disabled", false).prop('required', true);
    } else {
        $("#id_activity_other").prop( "disabled", true).prop('required', false);
    }


    if ($('#id_ability_10').prop("checked")==true){
        $("#id_ability_other").prop( "disabled", false).prop('required', true);
    } else {
        $("#id_ability_other").prop( "disabled", true).prop('required', false);
    }

    if ($('#id_messenger_10').prop("checked")==true){
        $("#id_messenger_other").prop( "disabled", false).prop('required', true);
    } else {
        $("#id_messenger_other").prop( "disabled", true).prop('required', false);
    }


}

