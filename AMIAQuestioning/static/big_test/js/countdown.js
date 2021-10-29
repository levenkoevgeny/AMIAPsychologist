$(document).ready(function () {

    let countdown = 5;

    function setNewTime() {
        $('#user_countdown').html(countdown);
        console.log(countdown);
        countdown--;
    }

    let timerId = setInterval(setNewTime, 1000);
    setTimeout(() => {
        clearInterval(timerId);
        window.location.href = '/big_test';
    }, 5000);
});