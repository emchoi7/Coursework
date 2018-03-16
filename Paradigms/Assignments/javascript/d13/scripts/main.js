function changeText(args)
{
	args[1].setText(args[0]);
}

var Item = {
	addToDocument: function(){
		document.body.appendChild(this.item);
	}
};

var Label = {
	createLabel: function(text, id){
		this.item = document.createElement("p");
		this.item.setAttribute("id",id);
		this.item.innerHTML = text;
	},

	setText: function(text){
		this.item.innerHTML=text;
	}
};

var Button = {
	createButton: function(text, id){
		this.item = document.createElement("button");
		this.item.setAttribute("id",id);
		this.item.innerHTML = text;
	},

	addClickEventHandler: function(handler, args){
		this.item.onmouseup = function(){
			handler(args);
		};
	}
};

Label.__proto__ = Item;
Label.createLabel("Guess Who", "theLabel");
Label.addToDocument();
Button.__proto__ = Item;
Button.createButton("Click Here", "theButton");
args = [ "Maru Choi", Label ];
Button.addClickEventHandler(changeText, args);
Button.addToDocument();



