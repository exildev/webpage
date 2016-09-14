(function(exile){
    exile.addEventListener( 'DOMContentLoaded', function () {
        setTimeout(function(){
            var body = exile.querySelector('body');
            body.classList.remove('hidden');
        }, 200);
        function menuOnClick(e){

            e.preventDefault();
        }
        var c = exile.querySelector('.content');
        var h = exile.querySelector('.header');
        c.addEventListener('scroll', function(e){
            if(c.scrollTop === 0){
                h.classList.add('top');
            }else{
                if(h.classList.contains('top')){
                    h.classList.remove('top');
                }
            }
        }, false);
        var menu_li = exile.querySelectorAll('.header nav > ul > li');
        for (var i = 0; i < menu_li.length; i++){
            menu_li[i].addEventListener('click', menuOnClick, false);
            window._li = li;
        }
    }, false );
})(document);
