// toggle menu sidebar via sidebar.css
$(".navbar-brand").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});


function load_contents(url){
	//alert('will call '+ '/contents/'+url);
	$.ajax({
	  url: '/contents/'+url
	}).done(function(data) {
		console.log(data);
		borrar = data;
		if (data.result == 'OK'){
			$("#page-wrapper").html(data.contents);
			attach_submit_handler();
			attach_test_launch_handler();
		} else {
			alert('Error loading contents');
		}


	});
}