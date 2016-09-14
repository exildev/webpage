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
   	}


	document.addEventListener("DOMContentLoaded", load, false);
})();
