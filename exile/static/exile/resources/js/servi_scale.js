(function() {
    function funciones() {
        window.animando=false;
        window.item =null;
        window.coordenadas=null;
        window.scalar = function(event){
            if(window.animando){
                document.removeEventListener('transitionend', mostrarTexto);
                window.animando=false;
                event.preventDefault();
                event.stopImmediatePropagation();
                var ima = window.item.querySelectorAll('img');
                if (ima != undefined){
                    ima[0].className="des_scale"
                }
                var texto = window.item.querySelectorAll("span.act_complem");
                if (texto != undefined){
                    texto[0].className="des_complem";
                }
                //console.log("termino la animacion");
                var css = "z-index: 0;position: relative;-ms-transform: translate(50px,100px);/* IE 9 */";
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
                    css+="background-color: white;";
                    css+="width:"+window.coordenadas.w+"px";
                    //css+="height:"+window.coordenadas.h+"px";
                console.log("esto es el tamaño de y "+window.coordenadas.h);

                window.item.style.cssText= css;
                window.item.className ="modal";
            }
        };
        window.mostrarTexto = function(event){
            event.preventDefault();
            event.stopImmediatePropagation();

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
                var xf=0,yf=0;
                for(var i=0;i < abuelos.length;i++){
                    if(i===0){
                        altura = abuelos[i].offsetTop;
                        __x = abuelos[i].getBoundingClientRect().width;
                        xf = abuelos[i].getBoundingClientRect().width*0.8;
                        yf = abuelos[i].getBoundingClientRect().height*2;
                    }
                    __y = abuelos[i].getBoundingClientRect().height;
                }
                console.log(" los tamaños a escalar "+xf+"  "+yf);
                /* posicion central de la seccion*/
                __x=__x/2;
                total_h=__y;
                //console.log("este es la altuda del contenedor "+total_h);
                __y=altura+ __y/2;

                //console.log(altura,__y,__x,"jajaja");
                /*coordenadas del elemento*/
                var x_prima= this.offsetLeft,
                    y_prima=this.offsetTop,
                    x_prima_w=this.getBoundingClientRect().width,
                    x_prima_h=this.getBoundingClientRect().height;
                    //console.log("este es el valor para y : "+x_prima_h);
                    var y_retorno = x_prima_h;
                var mover_x=0,
                    mover_y=0;
                if(__x<x_prima){
                    mover_x = -x_prima + __x-150;
                    //console.log("valor x "+mover_x);
                }else if(__x==x_prima){
                    mover_x = -150;
                }else{
                    mover_x = -x_prima + __x-150;
                }
                if(__y>y_prima){
                    //console.log("entro en esta");
                    mover_y =  __y-y_prima;
                }else if(y_prima >= __y){
                    mover_y = __y-y_prima;
                }
                var ima = this.querySelectorAll('img');
                if (ima != undefined){
                    //ima[0].style.width="60%";
                }
                var ima = this.querySelectorAll('img');
                if (ima != undefined){
                    ima[0].className="act_scale"
                }
                window.animando=true;
                var texto = this.querySelectorAll("span.des_complem");
                if (texto != undefined && window.animando){
                    texto[0].className="act_complem";
                }
                //console.log("valores para y ( ",__y,y_prima," )");
                var abuelo = this.parentNode.parentNode;
                var css = "z-index: 10;position: relative;-ms-transform: translate("+mover_x+"px,"+(mover_y)+"px);/* IE 9 */";
                    css+="-webkit-transform: translate("+mover_x+"px,"+mover_y+"px);";
                    css+="transform: translate("+(mover_x+(-100))+"px,"+mover_y+"px)  ;";
                    css+="-webkit-transition-property: transform,width  ; /* Safari */";
                    css+="-webkit-transition-duration: 5s,2s; /* Safari */";
                    css+="-webkit-transition-delay: 2s,2s; /* Safari */";
                    css+="transition-property: transform,width ;";
                    css+="transition-duration: 5s,2s;";
                    css+="transition-delay: 2s,2s;";
                    css+="border-radius: 3px;";
                    css+="box-shadow: 0 0 12 #555;";
                    css+="-webkit-transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);";
                    css+="transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);";
                    css+="width:500px;";
                window.item =this;

                window.coordenadas = {x:mover_x,y:mover_y,w:this.getBoundingClientRect().width,h:y_retorno};
                this.style.cssText= css;
                this.className = "mod_temp";
                this.addEventListener('transitionend', mostrarTexto, false);
            }
        };
        var item = document.getElementsByClassName("modal");
        for(var i=0;i < item.length; i++){
            item[i].addEventListener("click",mover,false);
            item[i].addEventListener("click",scalar,false);
        }
        window.redireccionar = function(event){
            event.preventDefault();
            event.stopImmediatePropagation();
            window.location.href = this.getAttribute("href");
        }
        var redireccion = document.getElementsByClassName("action_btn");
        for(var i=0;i < redireccion.length; i++){
            redireccion[i].addEventListener("click",redireccionar,false);
        }
        //
    }
    document.addEventListener("DOMContentLoaded", funciones, false);
})();
