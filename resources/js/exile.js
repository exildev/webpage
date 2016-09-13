(function(exile){
    exile.addEventListener( 'DOMContentLoaded', function () {
        setTimeout(function(){
            let body = exile.querySelector('body');
            body.classList.remove('hidden');
        }, 200);
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
    }, false );
})(document);
