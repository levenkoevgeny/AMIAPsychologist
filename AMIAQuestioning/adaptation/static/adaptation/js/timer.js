$(document).ready(function() {

    let now1 = new Date();

    function setNewTime() {
        let t = new Date() - now1;
        let t1 = Math.round(t/1000);

        let whole_h = 0;

        if (t1 >= 3600) {
            whole_h = Math.trunc(t1/3600);
        }

        let whole_m = 0;

        if ((t1-whole_h*3600) >= 60){
            whole_m = Math.trunc((t1-whole_h*3600)/60);
        }

        let whole_s = 0;

        whole_s = (t1 - (whole_h*3600 + whole_m*60));

        setReadableFormat(whole_h, whole_m, whole_s, t1)

    }

    function setReadableFormat(h,m,s, whole_time) {

        let str_h = h;
        let str_m = m;
        let str_s = s;

        if (h>=0 && h<10) {
            str_h = '0' + h;
        }

        if (m>=0 && m<10) {
            str_m = '0' + m;
        }
        if (s>=0 && s<10) {
            str_s = '0' + s;
        }

        time_str = str_h + ':' + str_m + ':' + str_s;

        $('#user_timer').html(time_str);
        $('#id_timer').val(whole_time);
    }



    setInterval(setNewTime, 1000);

});