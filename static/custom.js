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

	$('#my-file-selector').change(function(){
		var file_name = $('#my-file-selector').val();
		$('#file_uploader').append('<span class="form-control-static">File chosen: ' + file_name + '</span>');
		//$("label[for='my-file-selector']").text("Chosen: " + file_name);
	});

});
