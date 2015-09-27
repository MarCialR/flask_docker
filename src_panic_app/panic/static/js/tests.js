





var icon_OK = $('<i></i>');
icon_OK.addClass('fa').addClass('fa-thumbs-o-up');
var icon_KO = $('<i></i>');
icon_KO.addClass('fa').addClass('fa-thumbs-o-down');

var data;
function launch_ajax(btn){
	btn.addClass( "disabled" );
	$.ajax({
	  url: btn.attr('data')
	}).done(function(data) {
		if (data.result == 'OK'){
			btn.removeClass('btn-primary')
		  		.addClass( "btn-success" )
		  		.html(icon_OK.clone())
		  		.parent().next().next().html(data.info);
		} else {
		 	btn.removeClass('btn-primary')
		  		.addClass( "btn-danger" )
		  		.html(icon_KO.clone())
		  		.parent().next().next().html(data.info);
		}


	});
}

function attach_test_launch_handler(){
	$(".btn-primary").click(function(){
		launch_ajax($(this));	
	});
	$("#launch_all").click(function(){
		$(this).addClass( "disabled" );
		$(".btn-primary").click();
	});
}

function attach_toggle_info_handler(){
	$("#toggle_info").click(function(){
		$(".toggle_info").toggle();
	});
}

function attach_submit_handler(){
	// Attach a submit handler to the form
	$( "#runcommand_form" ).submit(function( event ) {
	 
		// Stop form from submitting normally
		event.preventDefault();
		// Get some values from elements on the page:
		var $form = $( this ),
		url = $form.attr( "action" );
		// Send the data using post
		var posting = $.post( url, $form.serialize() );
		// Put the results in a div
		posting.done(function( data ) {
			//var content = $( data ).find( "#content" );
			$( "#result" ).html( data.info.replace('\r\n', '<br/>') );
		});
	});
}

$(function(){
	attach_submit_handler();
	attach_test_launch_handler();
	attach_toggle_info_handler();
})




/*$("#runcommand_btn").click(function(){
	alert('yeah');//$.post( "/runcommand", $( "#runcommand_form" ).serialize() );	
})*/


