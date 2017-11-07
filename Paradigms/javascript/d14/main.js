function changeText(args)
{
	text = args[0]
	label = args[1]
	label.setText(text)
}

Label.prototype = new Item();
lbl = new Label();
lbl.createLabel("Guess Who", "theLabel");
lbl.addToDocument();

Button.prototype = new Item();
btn = new Button();
btn.createButton("Click Here", "theButton");

var xhr = new XMLHttpRequest()

xhr.open("GET","http://student04.cse.nd.edu:51001/movies/32", true)

xhr.onload = function(e) {
	btn.addClickEventHandler(changeText, [xhr.responseText, lbl]);
}

xhr.onerror = function (e) {
	console.error( xhr.statusText );
}

btn.addToDocument();

xhr.send(null)

