// main_script.js
console.log("started main_script");

// add reaction to Search button
search_button = document.getElementById("search-button");
search_button.onmouseup = makeSearchRequest;

// add reaction to apply filter button
filter_button = document.getElementById("apply-filter");
filter_button.onmouseup = applyFilter;

// function to make a search query when search button clicked
function makeSearchRequest() {
    console.log("started make search request");

    var url = "http://student04.cse.nd.edu:51031/";
    var xhr = new XMLHttpRequest();

    // xhr.open()

}

function applyFilter() {
    
}
