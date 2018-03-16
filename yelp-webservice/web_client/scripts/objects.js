function Item() {
	this.addToDocument = function(){
		document.body.appendChild(this.item);
	}
}

function RateForm(id){
	this.createForm = function(id){
		this.item = document.createElement("form");
		this.item.setAttribute("id", id); 
	},
	this.createRadio = function(label, name){
		for(i = 0; i < label.length; i++)
		{
			radio = document.createElement("input");
			radio.type = "radio";
			radio.name = name; 
			radio.id = name + label[i];
			radio.value = label[i];
			text = document.createTextNode(label[i]);
			this.item.appendChild(radio);
			this.item.appendChild(text);
			this.item.appendChild(document.createElement("br"));
		}
		
	},
	this.createSearch = function(id){
		search = document.createElement("input");
		search.type = "text";
		search.name = "text";
		search.id = id; 
		search.placeholder = "Enter Zipcode";
		this.item.appendChild(search);
		this.item.appendChild(document.createElement("br"));
	},
	this.createSubmit = function(id, val, fcn){
		submit = document.createElement("input");
		submit.type = "submit";
		submit.name = val;
		submit.value = val;
		submit.id = id;
		submit.setAttribute("onClick", fcn) 
		this.item.appendChild(submit);
		this.item.appendChild(document.createElement("br"));
	}
}

function Div(){
	this.createDiv = function(id, clas){
		this.item = document.createElement("div");
		this.item.setAttribute("id", id);
		this.item.setAttribute("class", clas);
	},
	this.appendChild = function(child){
		this.item.appendChild(child);
	}
	this.addText = function(text){
		this.item.innerHTML=text;
	}
}

function Label() {
	this.createLabel = function(id){
		this.item = document.createElement("p");
		this.item.setAttribute("id",id);
	},

	this.setText = function(text){
		this.item.innerHTML=text;
	},

	this.addText = function(text){
		oldtext = this.item.innerHTML;
		this.item.innerHTML = oldtext + "<br>" + text;
	},

	this.appendText = function(text){
		oldtext = this.item.innerHTML;
		this.item.innerHTML = oldtext + text;
	}
}

function Button() {
	this.createButton = function(text, id){
		this.item = document.createElement("button");
		this.item.setAttribute("id", id);
		this.item.innerHTML = text;
	},

	this.addClickEventHandler = function(handler, args){
		this.item.onmouseup = function(){
			handler(args);
		};
	}
}







