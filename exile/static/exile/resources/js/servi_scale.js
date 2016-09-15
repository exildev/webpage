(function() {
    function funciones() {
        window.animando=false;
        window.item =null;
        window.coordenadas=null;
        window.scalar = function(event){
            if(window.animando){
                window.animando=false;
                event.preventDefault();
                event.stopImmediatePropagation();
                console.log("termino la animacion");
                var css = "z-index: 10;position: relative;-ms-transform: translate(50px,100px);/* IE 9 */";
                    css+="-webkit-transform: translate("+(-1*window.coordenadas.mover_x)+"px,"+(-1*window.coordenadas.mover_y)+"px);/*Safari */";
                    css+="transform: translate("+(-1*window.coordenadas.mover_x)+"px,"+(-1*window.coordenadas.mover_y)+"px); /* Standard syntax */";
                    css+="-webkit-transition-property: transform ; /* Safari */";
                    css+="-webkit-transition-duration: 5s; /* Safari */";
                    css+="-webkit-transition-delay: 2s; /* Safari */";
                    css+="transition-property: transform;"
                    css+="transition-duration: 5s;"
                    css+="transition-delay: 2s;"
                    css+="-webkit-transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);";
                    css+="transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);";
                    css+="background-color: lightblue;";
                    css+="width:"+window.coordenadas.w+"px";
                    //css+="height:"+window.coordenadas.h+"px";
                    console.log("esto es el tamaño de y "+window.coordenadas.h);
                window.item.style.cssText= css;
                window.item.className ="modal";
            }
        };
        window.mover = function(event){
            if(!window.animando){
                event.preventDefault();
                event.stopImmediatePropagation();
                var abuelos = document.getElementsByClassName("servi");
                var altura = 0,
                    __y=0,
                    __x =0,
                    total_h=0;
                for(var i=0;i < abuelos.length;i++){
                    if(i===0){
                        altura = abuelos[i].offsetTop;
                        __x = abuelos[i].getBoundingClientRect().width;
                    }
                    __y = abuelos[i].getBoundingClientRect().height;
                }
                /* posicion central de la seccion*/
                __x=__x/2;
                total_h=__y;
                console.log("este es la altuda del contenedor "+total_h);
                __y=altura+ __y/2;

                console.log(altura,__y,__x,"jajaja");
                /*coordenadas del elemento*/
                var x_prima= this.offsetLeft,
                    y_prima=this.offsetTop,
                    x_prima_w=this.getBoundingClientRect().width,
                    x_prima_h=this.getBoundingClientRect().height;
                    console.log("este es el valor para y : "+x_prima_h);
                    var y_retorno = x_prima_h;
                var mover_x=0,
                    mover_y=0;
                if(__x<x_prima){
                    mover_x = -x_prima + __x-150;
                    console.log("valor x "+mover_x);
                }else if(__x==x_prima){
                    mover_x = -150;
                }else{
                    mover_x = -x_prima + __x-150;
                }
                if(__y>y_prima){
                    console.log("entro en esta");
                    mover_y =  __y-y_prima;
                }else if(y_prima >= __y){
                    mover_y = __y-y_prima;
                }
                console.log("valores para y ( ",__y,y_prima," )");
                var abuelo = this.parentNode.parentNode;
                var css = "z-index: 10;position: relative;-ms-transform: translate("+mover_x+"px,"+mover_y+"px);/* IE 9 */";
                    css+="-webkit-transform: translate("+mover_x+"px,"+mover_y+"px) scaley(5);/*Safari */";
                    css+="transform: translate("+mover_x+"px,"+mover_y+"px)  scaley(5); /* Standard syntax */";
                    css+="-webkit-transition-property: transform ; /* Safari */";
                    css+="-webkit-transition-duration: 5s; /* Safari */";
                    css+="-webkit-transition-delay: 2s; /* Safari */";
                    css+="transition-property: transform;"
                    css+="transition-duration: 5s;"
                    css+="transition-delay: 2s;"
                    css+="-webkit-transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);";
                    css+="transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);";
                    css+="background-color: lightblue;";
                    css+="width:300px";
                window.item =this;
                window.animando=true;
                window.coordenadas = {x:mover_x,y:mover_y,w:this.getBoundingClientRect().width,h:y_retorno};
                this.style.cssText= css;
                this.className = "mod_temp";
            }
        };
        var item = document.getElementsByClassName("modal");
        for(var i=0;i < item.length; i++){
            item[i].addEventListener("click",mover,false);
            item[i].addEventListener("click",scalar,false);
        }
        //this.addEventListener('transitionend', scalar, false);
    }
    document.addEventListener("DOMContentLoaded", funciones, false);
})();
