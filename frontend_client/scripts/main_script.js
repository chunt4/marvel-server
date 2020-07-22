// main_script.js
console.log("started main_script");

// add reaction to Search button
search_button = document.getElementById("search-button");
search_text = document.getElementById("search-text");
filter_select = document.getElementById("filter-select");
filter_button = document.getElementById("filter-button");

var filter = "";
var key = "";
var num_labels = -1;

search_button.onmouseup = makeSearchRequest;

filter_button.onmouseup = applyFilter;

function createLabelsDynamically(){
    var label = new Label();
}

function applyFilter(){
    console.log("applying filter");
    var selidx = filter_select.selectedIndex;
    filter = filter_select.options[selidx].value;
    console.log(filter);
    if (filter == "good characters" || filter == "bad characters" || filter == "neutral characters"){
        key = "align";
    }else if(filter == "secret identity" || filter == "public identity"){
        key = "iden";
    }else if(filter == "male characters" || filter == "female characters" || filter == "agender characters"){
        key = "sex";
    }else if(filter == "living characters" || filter == "deceased characters"){
		key = "alive";
	}else{
        filter = "";
        key = "";
    }

	console.log("key: " + key);
	console.log("filter: " + filter);
}

function reset_labels(max){
	for (var i = 0; i <= max; i++) {
		label_id = "label-" + i;
		label = document.getElementById(label_id);
		label.parentNode.removeChild(label);
		num_labels--;
	}
}

function makeSearchRequest() {
    console.log("started make search request");

	reset_labels(num_labels);
	console.log("resetting labels ... num_labels: " + num_labels);

	console.log("key: " + key);
	console.log("filter: " + filter);

    var url = "http://student04.cse.nd.edu:51031/heroes/query/" + search_text.value;

    var xhr = new XMLHttpRequest();

    xhr.open("GET", url, true);

    xhr.onload = function(e) {
        if (xhr.readyState === 4){
            var query_json = JSON.parse(xhr.responseText);
			console.log(xhr.responseText);
			console.log(query_json['hero_list'][0]['name'])
			var hero_list = query_json['hero_list'];
           for(i = 0; i < hero_list.length; i++){
				console.log("here");
				console.log(hero_list[i][key]);
				hero = hero_list[i];
                if (filter == "" || hero[key] == filter){
					num_labels++;

                    var id = hero['id'];
                    var name = hero['name'];
                    var align = hero['align'];
                    var alive = hero['alive'];
                    var iden = hero['iden'];
                    var sex = hero['sex'];

                    frontend_string = "name: " + name + ", aligns with: " + align + ", life status: " + alive + ", identity: " + iden + ", sex: " + sex;
					console.log(frontend_string);
                    var label = new Label();
                    label_id = "label-" + num_labels;
					console.log(label_id);
                    label.createLabel(frontend_string, label_id);
                    label.addAtPositionById("div-for-label");
                }
            }
        }
    }

    xhr.onerror = function(e) {
		console.error(xhr.statusText);
	}

    xhr.send();


}
