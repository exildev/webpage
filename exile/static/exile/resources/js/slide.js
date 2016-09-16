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
   	}
	$("#btn-down").click(function() {
	    $('html, body').animate({
	        scrollTop: 1070
	    }, 1000);
	});
	document.addEventListener("DOMContentLoaded", load, false);
})();
