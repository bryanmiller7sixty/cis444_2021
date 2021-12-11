var jwt = null
var mon_am = 0;
var mon_pm = 0;
var tues_am = 0;
var wed_am = 0;
var wed_pm = 0;
var tues_pm = 0;
var thurs_am = 0;
var thurs_pm = 0;
var fri_am = 0;
var fri_pm= 0;

function secure_get_with_token(endpoint, data_to_send, on_success_callback, on_fail_callback){
	xhr = new XMLHttpRequest();
	function setHeader(xhr) {
		xhr.setRequestHeader('Authorization', 'Bearer:'+jwt);
	}
	function get_and_set_new_jwt(data){
		console.log(data);
		jwt  = data.token
		on_success_callback(data)
	}
	$.ajax({
		url: endpoint,
		data : data_to_send,
		type: 'GET',
		datatype: 'json',
		success: on_success_callback,
		error: on_fail_callback,
		beforeSend: setHeader
	});
}
