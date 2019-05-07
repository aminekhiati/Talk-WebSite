// welcome section animate elemnts
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(window).scrollTop() >= 300) {
            $("#welcome-section .scroll-animations .animated").fadeIn(1000);
        }
    });
});
// change navbar background on scroll
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(window).scrollTop() >= 50) {
            $(".navbar").addClass("nav-change");
        } else {
            $(".navbar").removeClass("nav-change");
        }
    });
});
