/*
  Framento tomado de :
  Joe Harry
  https://twitter.com/joeharry__/
  http://codepen.io/woodwork/
  http://codepen.io/woodwork/pen/pgLvEr
*/
var formContainer = $('#form-container');

bindFormClick();
//Opening the form
function bindFormClick(){
  $(formContainer).on('click', function(e) {
    e.preventDefault();
    toggleForm();
    //Ensure container doesn't togleForm when open
    $(this).off();
  });
}

//Closing the form
$('#form-close').click(function(e) {
  e.stopPropagation();
  e.preventDefault();
  toggleForm();
  bindFormClick();
});

function toggleForm(){
  $(formContainer).toggleClass('expand');
  $(formContainer).children().toggleClass('expand');
  $('.form-contacto').toggleClass('show-form-overlay');
  $('.form-submitted').removeClass('form-submitted');
}

var options = {
    url: "/contacto/",
    type: "POST",
    dataType: "json",
    success: showResponse,
    error: showError,
    resetForm: true
};

//Form validation
$('form').submit(function() {
  var form = $(this);
  form.find('.form-error').removeClass('form-error');
  var formError = false;

  form.find('.input').each(function() {
    if ($(this).val() === '') {
      $(this).addClass('form-error');
      $(this).select();
      formError = true;
      return false;
    }
    else if ($(this).hasClass('email') && !isValidEmail($(this).val())) {
      $(this).addClass('form-error');
      $(this).select();
      formError = true;
      return false;
    }
  });

  if (!formError) {
    $('.form-contacto').addClass('form-submitted');
    $('#form-head').addClass('form-submitted');
    $(this).ajaxSubmit(options);
  }
  return false;
});

// post-submit callback
function showResponse(responseText, statusText, xhr, $form)  {
    $('.thank').fadeIn(300);
    setTimeout(function(){
      toggleForm();
      bindFormClick();
      //$('form').trigger("reset");
    }, 1000);
}

function showError(response){
    $('.form-contacto').removeClass('form-submitted');
    $('#form-head').removeClass('form-submitted');
    console.log(response);
    if (response.status == 400) {
          if (response.responseJSON.nombre) {
              $('input[name="nombre"]').addClass('form-error');
              $('input[name="nombre"]').select();
          } else if (response.responseJSON.email) {
              $('input[name="email"]').addClass('form-error');
              $('input[name="email"]').select();
          } else if (response.responseJSON.asunto) {
              $('input[name="asunto"]').addClass('form-error');
              $('input[name="asunto"]').select();
          }else if (response.responseJSON.telefono) {
              $('input[name="telefono"]').addClass('form-error');
              $('input[name="telefono"]').select();
          } else if (response.responseJSON.mensaje) {
              $('input[name="mensaje"]').addClass('form-error');
              $('input[name="mensaje"]').select();
          }
    }else if (response.status == 500) {
      console.log("Error 500");
    }

}

function isValidEmail(email) {
    var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    return pattern.test(email);
}
