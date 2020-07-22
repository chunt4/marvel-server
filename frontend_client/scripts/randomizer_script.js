// randomizer_page.js
console.log("started randomizer_script");

// add reactivity to button
random_button = document.getElementById("random-button");
response = document.getElementById("response-h4")
random_button.onmouseup = makeRandomRequest;

function makeRandomRequest() {
    console.log("started make random request");
    id = Math.floor((Math.random() * 16389));
    console.log("random id = " + id);

    var url = "http://student04.cse.nd.edu:51031/heroes/" + id.toString();

    var xhr = new XMLHttpRequest();

    console.log("sending GET request at URL: " + url);
    xhr.open("GET", url, true);

    xhr.onload = function(e) {
        response.innerHTML = xhr.responseText;
    }

    xhr.onerror = function(e) {
        console.error(xhr.statusText);
    }

    xhr.send(null);


}
