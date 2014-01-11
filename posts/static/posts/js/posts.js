var userName = "YLC (for test)";

function init() {
  // $('.submit_button').click(submit_click);
  $('#datetimepicker1').datetimepicker({
    format: 'yyyy-MM-dd hh:mm:ss',
    language: 'en'
  });
  $('#datetimepicker2').datetimepicker({
    format: 'yyyy-MM-dd hh:mm:ss',
    language: 'en'
  });
}

function submit_click(e) {
  e.preventDefault();
  $(this).attr("disabled");
  $(this).hide();
/*  
  $.ajax({
    type:'POST',
    url:'create/',
    data : $("form").serialize(),
    success: submit_success
  });
*/
}

function submit_success(e) {
  $('.submit_button').removeAttr("disabled");
          
  if (e.length == 0) {
    console.log("POST failed");
    $("#error").fadeIn('slow').html("<h2><strong>Invalid Post!!</strong></h2>").delay(1000).fadeOut('slow');
  }
  else {
    console.log("POST succeeded");
    $("#post_table").find("tbody").append(e);
    postID = e.match(/<tr id=\"tr_(\d+)\">/)[1];
    $('#tr_' + postID).hide().fadeIn(1000);
  }

  $("form")[0].reset();
  $('.submit_button').show();
}

function edit(id) {
  var tr = $('#tr_' + id);
  var td_name = tr.find('.name');
  var td_msg = tr.find('.msg');
  var td_pubTime = tr.find('.pubTime');
  var td_delTime = tr.find('.delTime');
  var name_text = td_name.find('.not_editing').text();
  var msg_text = td_msg.find('.not_editing').text();
  var pubTime = td_pubTime.find('.not_editing').text();
  var delTime = td_delTime.find('.not_editing').text();

  td_name.find('.editing').html('<input type="text" class="editing_name" size="30" value="' + name_text + '" />');
  td_msg.find('.editing').html('<textarea cols="30" rows="5" class="editing_msg">' + msg_text + '</textarea>');
  td_pubTime.find('.editing').html('<div class="input-append date"><input type="text" class="editing_pubTime" size="30" value="' + pubTime + '" /><span class="add-on"><i data-time-icon="icon-time" data-date-icon="icon-calendar"></i></span></div>');
  td_delTime.find('.editing').html('<div class="input-append date"><input type="text" class="editing_delTime" size="30" value="' + delTime + '" /><span class="add-on"><i data-time-icon="icon-time" data-date-icon="icon-calendar"></i></span></div>');
  
  td_pubTime.find('.editing').find('div').datetimepicker({
    format: 'yyyy-MM-dd hh:mm:ss',
    language: 'en'
  });
  td_delTime.find('.editing').find('div').datetimepicker({
    format: 'yyyy-MM-dd hh:mm:ss',
    language: 'en'
  });

  tr.find('.not_editing').hide();
  tr.find('.editing').show();
}

function done(id) {
  var tr = $('#tr_' + id);
  var td_name = tr.find('.name');
  var td_msg = tr.find('.msg');
  var td_pubTime = tr.find('.pubTime');
  var name_text = td_name.find('.editing_name').val();
  var msg_text = td_msg.find('.editing_msg').val();
  var pubTime = td_pubTime.find('.editing_pubTime').val();

  $.ajax({
    type: 'POST',
    url: 'update/',
    data: { _method: 'PUT', 'id': id, 'name': name_text, 'msg': msg_text, 'pubTime': pubTime, csrfmiddlewaretoken: getCookie('csrftoken') },
    success: function(e) {
      if (e.length == 0) {
        console.log("PUT failed");
        $("#error").fadeIn('slow').html("<h2><strong>Invalid Update!!</strong></h2>").delay(1000).fadeOut('slow');
      }
      else {
        console.log("PUT succeeded");
        $('#tr_' + id).html(e);
      }
    }
  });
}

function discard(id) {
  var tr = $('#tr_' + id);
  var td_name = tr.find('.name');
  var td_msg = tr.find('.msg');
  var td_pubTime = tr.find('.pubTime');
  
  td_name.find('.editing').html('');
  td_msg.find('.editing').html('');
  td_pubTime.find('.editing').html('');

  tr.find('.editing').hide();
  tr.find('.not_editing').show();
}

function destroy(id) {
  if ( confirm("Delete this post?") ) {
    $.ajax({
      type: 'POST',
      url: 'destroy/',
      data: { _method: 'DELETE', 'id': id, csrfmiddlewaretoken: getCookie('csrftoken') },
      success: function(e) {
        $('#tr_' + id).fadeOut();
      }
    });
  }
}

/* HELPERS */

function QQ() {
   alert("QQ");
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(document).ready(init);
