jQuery.fn.center = function () {
    this.css("position","absolute");
    this.css("top", Math.max(0, (($(window).height() - this.outerHeight()) / 2) + 
                $(window).scrollTop()) + "px");
    this.css("left", Math.max(0, (($(window).width() - this.outerWidth()) / 2) + 
                $(window).scrollLeft()) + "px");
    return this;
}

$(document).ready(function() {
    $('.show_request').click(function(){
        $('#request_form').center();
        $('#modal_background').fadeToggle();
        $('#request_form').fadeToggle();   
    });
    $('.make_offer').click(function(){
        $('#offer_form').center();
        $('#modal_background').fadeToggle();
        $('#offer_form').fadeToggle();   
    });
    $('#modal_background').click(function(){
        $(this).fadeToggle();
        $('#request_form:visible').toggle();
        $('#offer_form:visible').toggle();

    });
});
