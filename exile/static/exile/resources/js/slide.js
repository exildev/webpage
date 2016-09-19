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
			var longpress = 1000;
			// holds the start time
			var start;

			jQuery( ".tec li" ).on( 'mousedown', function( e ) {
			    start = new Date().getTime();
			    this.scale = 1;
			    this.interval = window.setInterval(function (){
			    	$(this).css({transform: 'scale(' + this.scale + ')'});
			    	if (this.scale < 4){
			    		this.scale += 0.9999;
			    	}
			    }.bind(this), 100);
			});

			jQuery( ".tec li" ).on( 'mouseleave', function( e ) {
				window.clearTimeout(this.interval);
				$(this).removeAttr("style");
				console.log($(this));
			    start = 0;
			});

			jQuery( ".tec li" ).on( 'mouseup', function( e ) {
				window.clearTimeout(this.interval);
				console.log($(this));
				$(this).removeAttr("style");
				console.log(new Date().getTime() , ( start + longpress )  , new Date().getTime() >= ( start + longpress )  );
			    if ( new Date().getTime() >= ( start + longpress )  ) {
			       $(this).addClass("animated");
			       window.setTimeout(function (){
			       		$(this).removeClass("animated");
			       }.bind(this), 1000);
			    }
			} );

		}());
   	}
	document.addEventListener("DOMContentLoaded", load, false);
})();
