var raw_image_data
$(function() {
	Webcam.attach( '#my_camera' );
	$('#snapshot').on('click', function(event) {  		
		Webcam.snap( function(data_uri) {
                	document.getElementById('my_result').innerHTML = '<img src="'+data_uri+'"class="img-responsive center-block" alt="Photobooth image">';			
			raw_image_data = data_uri.replace(/^data\:image\/\w+\;base64\,/, '');
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
		//$('#file_uploader').append('<span class="form-control-static">File chosen: ' + file_name + '</span>');
		//$("label[for='my-file-selector']").text("Chosen: " + file_name);
		$('#filename').text(file_name);
	});

	$('#webcam').on('click', function(event){
		$('#webcam').val(raw_image_data);
        	$('#webcam_form').submit();
		//alert(raw_image_data);
	});

	$('#PhotoModal').on('hide.bs.modal', function (e) {
		Webcam.unfreeze();
	});

});
