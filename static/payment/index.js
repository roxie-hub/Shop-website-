
$(document).ready(function(){
  $('#submit').click(function(ev){ 
  ev.preventDefault();
    $.ajax({
      type: "POST",
      url: 'http://127.0.0.1:8000/orders/add/',
      data: {
        csrfmiddlewaretoken: CSRF_TOKEN,
        action: "post",
      },
      success: function (json) {
        console.log(json.success)
        window.location.replace("http://127.0.0.1:8000/account/dashboard/");
      },
      error: function (xhr, errmsg, err) {},
    });

  });

});