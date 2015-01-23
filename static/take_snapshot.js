var sendButton;
var freezeButton;
freezeButton = document.createElement("input");

function webcamConfigure(){
	Webcam.set({
        width: 640,
        height: 480,
        dest_width: 640,
        dest_height: 480,
        image_format: 'jpeg',
        jpeg_quality: 100,
        force_flash: false
    });
}

function attach(){
	Webcam.attach( '#my_camera' );
}


function createStoreButton(){
	$(document).ready(function() {var button='<button class="btn btn-primary">button</button>&nbsp;';
          $("#send-button").append(button);}
  	sendButton.onclick = function store(){
	  
	  	Webcam.snap( function(data_uri) {
        // snap complete, image data is in 'data_uri'

		  Webcam.upload( data_uri, 'http://raoulschorer.com/scripts/test.php', function (code, text){
			alert("Your picture was sent to the database. Thank you very much for your contribution!");
		  });
    	});
	  	freezeButton.value = "Capture snapshot!";
		sendButton.disabled = true;
  	}
}

function createFreezeButton(){
	//freezeButton = document.createElement("input");
	freezeButton.type = "button";
	freezeButton.value = "Capture snapshot!";
	freezeButton.onclick = function freeze(){

		if (freezeButton.value=="Capture snapshot!") {
			freezeButton.value = "Discard snapshot!";
			Webcam.freeze();
			sendButton.disabled = false;
		}
		else {
			freezeButton.value = "Capture snapshot!";
			Webcam.unfreeze();
			sendButton.disabled = true;
		}
	}
	placeHolder2 = document.getElementById("freezeButton");
	placeHolder2.appendChild(freezeButton);
}
