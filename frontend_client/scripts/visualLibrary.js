// Jack Bigej, Chris Hunt, Andrew Rocks

function Item() {
	this.addToDocument = function() {
		document.body.appendChild(this.item);
	}

	this.addAtPositionById = function(id){
		document.getElementById(id).appendChild(this.item);
	}
}

function Label() {
	this.createLabel =  function(text, id) {
		this.item = document.createElement("p");
		this.item.setAttribute("id", id);
		this.setText(text);
	}

	this.setText = function(text) {
		this.item.innerHTML = text;
	}
}

function InputText(){
	this.createInput = function(id){
		this.item = document.createElement("input");
		this.item.setAttribute("id", id);
		this.item.setAttribute("name", "text-input");
		this.item.setAttribute("type", "text");
		this.item.setAttribute("class", "form-control");
	}; // end of createInput
} // end of InputText class

function Button() {
	this.createButton = function(text, id) {
		this.item = document.createElement("button");
		this.item.setAttribute("id", id);
		var itemText = document.createTextNode(text);
		this.item.appendChild(itemText);
		// the innerHTML trick doesn't work for buttons
	};

	this.addClickEventHandler = function(handler, args) {
		this.item.onmouseup = function() {
			handler(args); // closure allows this function to access handler and args, even though these are not passed to it.
		};
	};
} // end of Button class

function Dropdown() {
	this.createDropdown = function(dict, id, selected) {
		this.item = document.createElement("select");
		this.item.setAttribute("id", id);

		for (var key in dict) {
			listItem = document.createElement("option");
			listItem.setAttribute("value", key);
			listItem.innerHTML = dict[key];

			if (key === selected) {
				listItem.setAttribute("selected", "selected");
			}
			this.item.appendChild(listItem);
		} // end of for
	}; // end of createDropdown

	this.getSelected = function() {
		selidx = this.item.selectedIndex;
		return this.item.options[selidx].value;
	};
} // end of Dropdown class

// inheritance code - uses prototypical inheritance
Label.prototype 	= new Item();
InputText.prototype = new Item();
Button.prototype 	= new Item();
Dropdown.prototype 	= new Item();
