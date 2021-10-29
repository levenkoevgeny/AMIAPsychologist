$( "#test_form").submit(function(event) {
    event.preventDefault();
    event.stopPropagation();

    var form = document.getElementsByClassName('needs-validation');

    if (form[0].checkValidity() === true) {
        form[0].submit();
    }
    else {
        alert('Пропущен один или несколько ответов (вопросы обозначены красным цветом)!');
        form[0].classList.add('was-validated');
        let invalids = $('input:invalid');
        let firstInp = invalids.filter(':first');
        firstInp[0].scrollIntoView();
    }

    form[0].classList.add('was-validated');
});