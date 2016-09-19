(function() {

	function load(){
		var parents = document.querySelectorAll(".parent");
		var i = 0;
		window.slide_down = function (){
   			if (parents[i]){
		   		parents[i].classList.add("open");
		   		i++;
	   		}
	   	};
		window.slide_up = function (){
   			if (i > 0){
		   		i--;
		   		parents[i].classList.remove("open");
	   		}
	   	};
	   	window.setInterval(function(){
	   		if (parents[i]){
				slide_down();
	   		}else{
	   			var fix = i;
	   			for (var j = 0; j < fix; j++){
	   				slide_up();
	   			}
	   		}
	   	}, 3000);

		$("#btn-down").click(function() {
		    $('.content').animate({
		        scrollTop: 900
		    }, 1000);
		});
		(function() { 

			// how many milliseconds is a long press?
			var longpress = 2000;
			// holds the start time
			var start;

			jQuery( ".tec li" ).on( 'mousedown', function( e ) {
			    start = new Date().getTime();
			} );

			jQuery( ".tec li" ).on( 'mouseleave', function( e ) {
			    start = 0;
			} );

			jQuery( ".tec li" ).on( 'mouseup', function( e ) {
			    if ( new Date().getTime() >= ( start + longpress )  ) {
			       $(this).addClass("animated");
			       window.setTimeout(function (){
			       		$(this).removeClass("animated");
			       }.bind(this), 2000);
			    }
			} );

		}());
   	}
	document.addEventListener("DOMContentLoaded", load, false);
})();
