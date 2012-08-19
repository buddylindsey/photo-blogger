jQuery.fn.center = function () {
  this.css("position","absolute");
  this.css("top", ( $(window).height() - this.height() ) / 2+$(window).scrollTop() + "px");
  this.css("left", ( $(window).width() - this.width() ) / 2+$(window).scrollLeft() + "px");
  return this;
}

var default_lat = 36.14342011686289;
var default_lng = -96.00540148632808;

$(document).ready(function() {
  $('.show_request').click(function(){
    $('#request_form').center();
    $('#modal_background').toggle();
    $('#request_form').show();
    $('#id_expiration').datepicker({showOn: "button",
      buttonImage: "/static/img/calendar.png",
      buttonImageOnly: true,
      onSelect: function(dateText, inst) {
        $('#id_expiration_label').html(dateText);
      }
    });
    $('#id_expiration_label').remove();
    $('#id_expiration').after("<p id='id_expiration_label'>(Optional) Select an Expiration Date</p>");
    $('#id_location').after($('#request_map'));
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
  $('#id_expiration').click(function(){
    $('.id_expiration_trigger').click();
  });
  $('#submit_request_button').click(function(){

    if($('#id_description').val().length == 0)
  {
    alert('please enter a description');
    $('#id_description').focus();
  }
    else
  {
    if($('#id_location').val().length == 0)
  {
    $('#id_location').val("Not location specific");  
  }
  $('#submit_request').submit();
  }
  });
  $('#map_toggle').click(function(){
    $('#map_canvas').toggle();
    initializeMap($("#map_canvas"),default_lat,default_lng);
    $('#map_toggle').remove();
    $('#id_latitude').val(default_lat);
    $('#id_longitude').val(default_lng);
  });
  $('.location-review').click(function(){
    $('.location-details').center();
    $('#modal_background').fadeToggle();
    $('.location-details').fadeToggle();
    $.ajax({
      url: '/image/request/' + $(this).data('request-id') + "/",
      success: function(data){
        //var html = "<h2>" + data[0].fields.location + "</h2>";
        var html = "<div class='offers'>"
      html += "</div>"
      $('.location-details').html(html);
    $.ajax({
      url: '/image/request/' + data[0].pk + '/offers/',
      success: function(data){
        var html = "";
        for(i in data){
          html += "<div class='preview-popup'><center><img src='http://dash-media.s3.amazonaws.com" + data[i].fields.image + "' /></center></div>"   
        }
        $(".location-details .offers").html(html);
      }
    });
      }
    });

  });
  $('.list_map').each(function(){
    if($(this).data("lat") != "0" && $(this).data("lng") != "0" &&
      $(this).data("lat") != "None" && $(this).data("lng") != "None")
    {
      initializeMap($(this),$(this).data("lat"),$(this).data("lng"));
    }
    else {
      $(this).remove();
    }
  });
  $('.req_expiration').each(function(){
    if($(this).data("expiration") == "None")
  {
    $(this).remove();
  }
  });
});



function initializeMap(mapidname,lat,lng) {
  var myLatlng = new google.maps.LatLng(lat,lng);
  var myOptions = {
    zoom: 4,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(mapidname[0], myOptions);

  var marker = new google.maps.Marker({
    position: myLatlng, 
      map: map,
      draggable:true
  });
  google.maps.event.addListener(
      marker,
      'drag',
      function() {
        $('#id_latitude').val(marker.position.lat());
        $('#id_longitude').val(marker.position.lng());
      }
      );
}

this.imagePreview = function(){	
	/* CONFIG */
		
		xOffset = 10;
		yOffset = 30;
		
		// these 2 variable determine popup's distance from the cursor
		// you might want to adjust to get the right result
		
	/* END CONFIG */
	$("a.preview").hover(function(e){
		this.t = this.title;
		this.title = "";	
		var c = (this.t != "") ? "<br/>" + this.t : "";
		$("body").append("<p id='preview'><img src='"+ this.href +"' alt='Image preview' />"+ c +"</p>");								 
		$("#preview")
			.css("top",(e.pageY - xOffset) + "px")
			.css("left",(e.pageX + yOffset) + "px")
			.fadeIn("fast");						
    },
	function(){
		this.title = this.t;	
		$("#preview").remove();
    });	
	$("a.preview").mousemove(function(e){
		$("#preview")
			.css("top",(e.pageY - xOffset) + "px")
			.css("left",(e.pageX + yOffset) + "px");
	});			
};

