"use strict";
$(document).ready(function() {
    // $('.theme-loader').addClass('loaded');
    $('.preloader').animate({
        'opacity': '0',
    }, 1200);
    setTimeout(function() {
        $('.preloader').remove();
    }, 2000);
    // $('.pcoded').addClass('loaded');
});
