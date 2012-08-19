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
    initializeMap(36.14342011686289,-96.00540148632808);
  });
  $('.make_offer').click(function(){
    $('#offer_form').center();
    $('#modal_background').fadeToggle();
    $('#offer_form').fadeToggle();   
    $('#request').val($(this).data('request-id'));
  });
  $('#modal_background').click(function(){
    $(this).fadeToggle();
    $('#request_form:visible').toggle();
    $('#offer_form:visible').toggle();
    $('.location-details:visible').toggle();
  });

  $('.location-review').click(function(){
    $('.location-details').center();
    $('#modal_background').fadeToggle();
    $('.location-details').fadeToggle();
    $.ajax({
        url: '/image/request/' + $(this).data('request-id') + "/",
        success: function(data){
            var html = "<h2>" + data[0].fields.location + "</h2>";
            html += "<div class='offers'>"
            html += "</div>"
            $('.location-details').html(html);
            $.ajax({
                url: '/image/request/' + data[0].pk + '/offers/',
                success: function(data){
                    var html = "<h3>All Offers</h3>";
                    for(i in data){
                        html += "<div class='preview-popup' style='max-width: 250px;'><img src='http://dash-media.s3.amazonaws.com" + data[i].fields.image + "' /></div>"   
                    }
                    $(".location-details .offers").html(html);
                }
            });
        }
    });
    
  });
    
});



function initializeMap(lat,lng) {
  var myLatlng = new google.maps.LatLng(lat,lng);
  var myOptions = {
    zoom: 4,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

  var marker = new google.maps.Marker({
    position: myLatlng, 
      map: map,
      draggable:true
  });
  google.maps.event.addListener(
      marker,
      'drag',
      function() {
        $('#id_latitude').val(marker.position.lat().toFixed(7));
        $('#id_longitude').val(marker.position.lng().toFixed(7));
      }
      );
}
