var in_the_interests_of_other = "Иное";


$( document ).ready(function() {
    'use strict';

    $( "ul[id*=id_in_the_interests_of] li").on( "click", function() {
        var value_str = String($(this).find("label").text());
      //  alert(value_str == in_the_interests_of_other);
        // alert($(this).find("label").text());
        if (value_str === in_the_interests_of_other) {
           // alert(value_str === in_the_interests_of_other);
        }
        //  var elem = $(this).find("label");
        // alert(elem.text());
    });

});