// main_script.js

// add reaction to Search button
search_button = document.getElementById("search-button");
search_text = document.getElementById("search-text");
filter_select = document.getElementById("filter-select");
filter_button = document.getElementById("filter-button");

var filter = "";
var key = "";

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
    if (filter == "good characters" || filter == "bad characters"){
        key = "align";
    }else if(filter == "secret identity" || filter == "public identity"){
        key = "iden";
    }else if(filter == "male" || filter == "female"){
        key = "sex";
    }else{
        filter = "";
        key = "";
    }
}

function makeSearchRequest() {
    console.log("started make search request");

    var url = "http://student04.cse.nd.edu:51031/heroes/query/" + search_text;

    var xhr = new XMLHttpRequest();

    xhr.open(GET, url, true);

    xhr.onload = function(e) {
        if (xhr.readyState === 4){
            var query_json = JSON.parse(xhr.responseText);
            i = 0
            for (hero in query_json['hero_list']){
                if (hero[key] == filter){
                    var id = hero['id'];
                    var name = hero['name'];
                    var align = hero['align'];
                    var alive = hero['alive'];
                    var iden = hero['iden'];
                    var sex = hero['sex'];



                    frontend_string = "name: " + name + ", aligns with: " + align + ", life status: " + alive + ", identity: " + iden + ", sex: " + sex;
                    var label = new Label();
                    label_id = "label-key-" + str(i);
                    label.createLabel(frontend_string, label_id);
                    label.addAtPositionById("div-for-label");
                }
            }
        }
    }

    xhr.onerror = function(e) {
		console.error(xhr.statusText);
	}

    xhr.send("?");


}
