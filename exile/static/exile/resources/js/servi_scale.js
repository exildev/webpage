(function() {
    function funciones() {
        console.log("1");
        window.contentDelay = 400;
        window.isOpen = false;
        window.w = window;
        window.item=document.getElementsByClassName('item');
        window.close = function(event) {

            event.preventDefault();
            event.stopImmediatePropagation();

            var target = event.target;
            var div = document.getElementById('modal__temp');

            /**
             * make sure the modal__bg or modal__close was clicked, we don't want to be able to click
             * inside the modal and have it close.
             */

            if (isOpen && target.classList.contains('modal__bg') || target.classList.contains('modal__close')) {
                // make the hidden div visible again and remove the transforms so it scales back to its original size
                console.log(div);
                div.style.opacity = '1';
                div.removeAttribute('style');
                /**
                 * iterate through the modals and modal contents and triggers to remove their active classes.
                 * remove the inline css from the trigger to move it back into its original position.
                 */
                 div.style.visibility = 'hidden';
                 div.addEventListener('transitionend', removeDiv, false);
                 document.getElementById('modal').classList.remove('modal--active');
                 var contenidos = document.getElementsByClassName("modal__content");
                 for (var i = 0; i < contenidos.length; i++) {
                     contenidos[i].classList.add("desaparecer");
                     contenidos[i].classList.remove('modal__content--active');
                 }
                var item = document.getElementsByClassName('item');
                for (var i = 0; i < item.length; i++) {
                    //modals[i].classList.remove('modal--active');
                    //content[i].classList.remove('modal__content--active');
                    item[i].style.transform = 'none';
                    item[i].style.webkitTransform = 'none';
                    item[i].classList.remove('modal__trigger--active');
                }

                // when the temporary div is opacity:1 again, we want to remove it from the dom


                isOpen = false;

            }

            function removeDiv() {
                //alert("jajaja");
                setTimeout(function() {
                    window.requestAnimationFrame(function() {
                        // remove the temp div from the dom with a slight delay so the animation looks good
                        div.remove();
                    });
                }, window.contentDelay - 50);
            }

        };
        window.open = function(m, div) {

            if (!isOpen) {
                // select the content inside the modal
                var content = m.querySelector('.modal__content');
                // reveal the modal
                m.classList.add('modal--active');
                // reveal the modal content
                content.classList.add('modal__content--active');
                content.addEventListener('transitionend', hideDiv, false);

                isOpen = true;
            }

            function hideDiv() {
                div.style.opacity = '0';
                content.removeEventListener('transitionend', hideDiv, false);
            }
        };
        window.moverDiv = function(trig, modal, div) {
            var trigProps = trig.getBoundingClientRect();
            var m = modal;
            var mProps = m.querySelector('.modal__content').getBoundingClientRect();
            var transX, transY, scaleX, scaleY;
            var xc = window.w.innerWidth / 2;
            var yc = window.w.innerHeight / 2;

            // this class increases z-index value so the button goes overtop the other buttons
            trig.classList.add('modal__trigger--active');

            // these values are used for scale the temporary div to the same size as the modal
            scaleX = mProps.width / trigProps.width;
            scaleY = mProps.height / trigProps.height;

            scaleX = scaleX.toFixed(3); // round to 3 decimal places
            scaleY = scaleY.toFixed(3);


            // these values are used to move the button to the center of the window
            transX = Math.round(xc - trigProps.left - trigProps.width / 2);
            transY = Math.round(yc - trigProps.top - trigProps.height / 2);

            // if the modal is aligned to the top then move the button to the center-y of the modal instead of the window
            if (m.classList.contains('modal--align-top')) {
                transY = Math.round(mProps.height / 2 + mProps.top - trigProps.top - trigProps.height / 2);
            }
            // translate button to center of screen
            trig.style.transform = 'translate(' + transX + 'px, ' + transY + 'px)';
            trig.style.webkitTransform = 'translate(' + transX + 'px, ' + transY + 'px)';
            // expand temporary div to the same size as the modal
            div.style.transform = 'scale(' + scaleX + ',' + scaleY + ')';
            div.style.webkitTransform = 'scale(' + scaleX + ',' + scaleY + ')';

            window.setTimeout(function() {
                window.requestAnimationFrame(function() {
                    open(m, div);
                });
            }, window.contentDelay);
        }
        window.crearDiv = function(self, modal) {
            var tem_div = document.getElementById('tem_mod');
            if (tem_div === null) {
                var div = document.createElement('div');
                div.id = 'modal__temp';
                self.appendChild(div);
                moverDiv(self, modal, div);
            }
        };
        window.getIdentificador = function(event) {
            console.log("llego");
            event.preventDefault();
            var modal = document.getElementById('modal');
            crearDiv(this, modal);
        };
        console.log("1");
        var item = window.item;
        console.log(item.length);
        for (var i = 0; i < item.length; i++) {
            item[i].addEventListener('click', getIdentificador, false);
        }
        var mod = document.getElementsByClassName("modal_bg");

        for (var i = 0; i < mod.length; i++) {
            mod[i].addEventListener('click', close, false);
        }
    }
    document.addEventListener("DOMContentLoaded", funciones, false);
})();
