console.log("started create");

create_button = document.getElementById("Create");
create_button.onmouseup = submitHero;

function getValuesFromForm(){

	var name = document.getElementById('input-hero-name').value;
	var align = "";
	var alive = "";
	var sex = "";
	var iden = "";

	if (document.getElementById('radio-good').checked){
		align = "good characters";
	}
	else{
		align = "bad characters";
	}
	if (document.getElementById('radio-alive').checked){
		alive = "alive characters";
	}
	else{
		alive = "dead characters";
	}
	if (document.getElementById('radio-female').checked){
		sex = "female characters";
	}
	else{
		sex = "male characters";
	}
	if (document.getElementById('radio-secret').checked){
		iden = "secret identity";
	}
	else{
		iden = "public identity";
	}

	var parameters = [name, align, alive, sex, iden];

}

function submitHero(){

	var params = getValuesFromForm();
	var xhr = new XMLHttpRequest();
	var url = "http://student04.cse.nd.edu:51027/heroes/";
	xhr.open("POST", url, true)

	xhr.onload = function(e) {
		console.log(xhr.responseText);
		console.log(params);

	}

	xhr.onerror = function(e) {
		console.error(xhr.statusText);
	}

	xhr.send();
}



