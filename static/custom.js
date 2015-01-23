$(function() {
	Webcam.attach( '#my_camera' );

	$('#snapshot').on('click', function(event) {  		
		Webcam.snap( function(data_uri) {
                	document.getElementById('my_result').innerHTML = '<img src="'+data_uri+'"class="img-responsive center-block" alt="Photobooth image">';
            	} );
	});

	$('#snapshot').on('click', function(event) {
		Webcam.freeze();
	});

	$('#dropit').on('click', function(event) {
  		Webcam.unfreeze();
	});

});
