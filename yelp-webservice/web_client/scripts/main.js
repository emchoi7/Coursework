

//4. Fetch & Display review
//   Fetch & Display biz
//5. Create buttons for rating (funny, cool, useful)
//6. Submit rating
//7. DELETE REQUEST!!
//8. Put up next req; if empty, put up message
//9. Fetch & update display



var URL = 'http://student04.cse.nd.edu:51022'
var ATT = '/attribute/'
var ATT_URL = URL + ATT
var LOC_URL = '/location/'
var BIZ_URL = URL + '/business/'
var REV_URL = URL + '/reviews/'
var BIZ_REV_URL = URL + '/business_reviews/'
var attributes = ["funny","cool","useful"]

var attribute;
var zipcode;
var business_id;
var rate = 0;
var rate_zip = 0;
var rate_biz = 0;

var header = document.createElement("h2")
header.innerHTML = "Yelp Reviews"
document.body.appendChild(header)

/////////ITEM////////
RateForm.prototype = new Item()
Div.prototype = new Item()
Label.prototype = new Item()
Button.prototype = new Button()

////////LABEL////////
var rev_text = new Label()
rev_text.createLabel("rev_text")

var star = new Label()
star.createLabel("star")

var r_funny = new Label()
r_funny.createLabel("r_funny")

var r_cool = new Label()
r_cool.createLabel("r_cool")

var r_useful = new Label()
r_useful.createLabel("r_useful")

var biz_text = new Label()
biz_text.createLabel("biz_text")

var lbl = new Label()
lbl.createLabel("lbl")

var biz_star = new Label()
biz_star.createLabel("biz_star")

////////RATING BUTTONS///////
var funny_btn = new Button()
funny_btn.createButton("funny", "funny_btn")

var cool_btn = new Button()
cool_btn.createButton("cool", "cool_btn")

var useful_btn = new Button()
useful_btn.createButton("useful", "useful_btn")

////////DIV for FORM////////
var div_form = new Div()
div_form.createDiv("form", "top")
text = document.createElement('hi')
div_form.appendChild(text)
document.body.appendChild(div_form.item)

////////DIV for REVIEW////////
var div_text = new Div() //review text div
div_text.createDiv("text", "review")
div_text.appendChild(rev_text.item)

var div_lbl = new Div() //says what you're viewing reviews for
div_lbl.createDiv("div_lbl", "review")
div_lbl.appendChild(lbl.item)

var div_star = new Div() //review star div
div_star.createDiv("div_star", "review")
div_star.appendChild(star.item)

var div_funny = new Div() //funny rates div
div_funny.createDiv("div_funny", "rating")
div_funny.appendChild(r_funny.item)

var div_cool = new Div() //cool rates div
div_cool.createDiv("div_cool", "rating")
div_funny.appendChild(r_cool.item)

var div_useful = new Div() //useful rates div
div_useful.createDiv("div_useful", "rating")
div_funny.appendChild(r_useful.item)

var div_rates = new Div() //attribute rates div
div_rates.createDiv("rates", "review")
div_rates.appendChild(div_funny.item)
div_rates.appendChild(div_cool.item)
div_rates.appendChild(div_useful.item)

var div_btn_f = new Div() //funny rating button div
div_btn_f.createDiv("div_btn_f", "review")
div_btn_f.appendChild(funny_btn.item)

var div_btn_c = new Div() //cool rating button div
div_btn_c.createDiv("div_btn_c", "review")
div_btn_c.appendChild(cool_btn.item)

var div_btn_u = new Div() //funny rating button div
div_btn_u.createDiv("div_btn_u", "review")
div_btn_u.appendChild(useful_btn.item)

var div_btn = new Div() //rating buttons div
div_btn.createDiv("div_btn", "review")
div_btn.appendChild(div_btn_f.item)
div_btn.appendChild(div_btn_c.item)
div_btn.appendChild(div_btn_u.item)

var div_rev = new Div() //big review div
div_rev.createDiv("rev", "review")
div_rev.appendChild(div_lbl.item)
div_rev.appendChild(div_star.item)
div_rev.appendChild(div_text.item)
div_rev.appendChild(div_rates.item)
document.body.appendChild(div_rev.item)

////////DIV for BIZ///////
var div_biz_form = new Div()
div_biz_form.createDiv("div_biz_form", "business")

var div_biz = new Div() //big biz div
div_biz.createDiv("biz", "business")
div_biz.appendChild(biz_text.item)
div_biz.appendChild(biz_star.item)
document.body.appendChild(div_biz.item)

////////FORM////////
var r_form = new RateForm()
r_form.createForm('r_form')
r_form.createSearch('search')
r_form.createRadio(attributes, 'rate')
r_form.createSubmit('submit', 'Submit', "showRev(); return false;")
div_form.appendChild(r_form.item)

var biz_form = new RateForm()
biz_form.createForm('b_form')
biz_form.createRadio(attributes, 'b_rate')
biz_form.createSubmit('b_submit_loc', 'Rate For This Location', "bizLocClick(); return false;")
biz_form.createSubmit('b_sumbit', 'Rate For This Business', "bizClick(); return false;")

//////FUNCTIONS////////
function showRev()
{
    window.zipcode = document.getElementById("search").value
    window.attribute = ""
    for(att in attributes){
        if(document.getElementById('rate' + attributes[att]).checked)
            window.attribute = document.getElementById('rate' + attributes[att]).value;

    }
    //access reviews
    if(window.attribute == "")
    {
        window.lbl.setText("")
        window.r_funny.setText("")
        window.r_cool.setText("")
        window.r_useful.setText("")
        window.star.setText("")
        window.rev_text.setText("You have to at least select an attribute...")

    }
    else if(window.zipcode!="" && window.attribute!="")
    {
        var rate = 0;
        var rate_zip = 1;
        var rate_biz = 0;
        fetchTopReviewLocation(window.zipcode, window.attribute)
    }

    else if(window.attribute != "")
    {
        var rate = 1;
        var rate_zip = 0;
        var rate_biz = 0;
        fetchTopReview(window.attribute)
    }


}

function addReview(response)
{
    //update label
    if(window.rate_zip > 0)
        lbl_text = "Currently viewing reviews by: " + "location"
    else if(window.rate > 0)
        lbl_text = "Currently viewing reviews by: " + "attribute"
    else if(window.rate_biz > 0)
        lbl_text = "Currently viewing reviews by: " + "business"
    else
        lbl_text = ""
    window.lbl.setText(lbl_text)

    //add rating buttons
    funny_btn.addClickEventHandler(rateClick,[response['review_id'], 'funny'])
    cool_btn.addClickEventHandler(rateClick,[response['review_id'], 'cool'])
    useful_btn.addClickEventHandler(rateClick,[response['review_id'], 'useful'])
    div_rev.appendChild(div_btn.item)
    //add text
    window.rev_text.setText(response['text'])
    //add stars
    window.star.setText('')
    stars = parseInt(response['stars'])
    for(i=0; i<stars; i++ )
    {
        window.star.appendText('☆')
    }
    //add ratings
    window.r_funny.setText('funny: ' + response['funny'])
    window.r_cool.setText('cool: ' + response['cool'])
    window.r_useful.setText('useful: ' + response['useful'])
}

function addBiz(response)
{
    window.biz_text.setText("")
    window.biz_text.addText("\n")
    window.biz_text.addText("Name: " + response['name'])
    window.biz_text.addText("\n")
    window.biz_text.addText("Address: ")
    window.biz_text.addText(response['address'])
    window.biz_text.addText("\t" + response['city'] + ", " + response['state'] + " " + response['postal_code'])
    window.biz_text.addText("\n")
    window.biz_text.addText("Number of Reviews: " + response['review_count'])
    
    window.biz_star.setText('')
    stars = parseInt(response['stars'])
    for(i=0; i<stars; i++ )
    {
        window.biz_star.appendText('☆')
    }

    div_biz_form.appendChild(biz_form.item)
    div_biz.appendChild(div_biz_form.item)
}

function emptyRev()
{
    window.star.setText("")
    window.r_funny.setText("")
    window.r_cool.setText("")
    window.r_useful.setText("")
    window.biz_text.setText("")
    window.rev_text.setText("Congratulations, you've rated all available reviews with these parameters!")
}

function fetchTopReviewLocation(zipcode, attribute)
{
    window.rate_zip = 1;
    window.rate = 0;
    window.rate_biz = 0;
    var URL = ATT_URL + attribute + LOC_URL + zipcode
    var xhr_zip = new XMLHttpRequest()
    xhr_zip.open("GET", URL, true)
    xhr_zip.onload = function(e){
        response = JSON.parse(xhr_zip.responseText);
        if(Object.keys(response).length > 1)
        {
            window.zipcode = response['postal_code']
            addReview(response);
            fetchBiz(response['business_id']);
        }
        else emptyRev();

        
    }
    xhr_zip.onerror = function (e) {
        console.error( xhr_zip.statusText );
    }
    xhr_zip.send(null)
}

function fetchTopReview(attribute)
{
    window.rate_zip = 0;
    window.rate = 1;
    window.rate_biz = 0;
    var URL = ATT_URL + attribute
    var xhr_top = new XMLHttpRequest()
    xhr_top.open("GET", URL, true)
    xhr_top.onload = function(e){
        response = JSON.parse(xhr_top.responseText);
        if(Object.keys(response).length > 1)
        {
            window.zipcode = response['postal_code']
            addReview(response);
            fetchBiz(response['business_id']);
        }
        else emptyRev();
    }
    xhr_top.onerror = function (e){
        console.error(xhr_top.statusText);
    }
    xhr_top.send(null)
}

function fetchBiz(bid)
{
    var URL = BIZ_URL + bid
    var xhr_biz = new XMLHttpRequest()
    xhr_biz.open("GET", URL, true)
    xhr_biz.onload = function(e){
        response = JSON.parse(xhr_biz.responseText)
        addBiz(response)
        window.business_id = response['business_id']
        window.zipcode = response['postal_code']
    }
    xhr_biz.onerror = function(e){
        console.error(xhr_biz.statusText);
    }
    xhr_biz.send(null)
}

function fetchBizRev(bid, attribute)
{
    window.rate_zip = 0;
    window.rate = 0;
    window.rate_biz = 1;
    var URL = BIZ_REV_URL + bid + ATT + attribute
    var xhr_brev = new XMLHttpRequest
    xhr_brev.open("GET", URL, true)
    xhr_brev.onload = function(e){
        response = JSON.parse(xhr_brev.responseText)
        addReview(response)
        window.business_id = response['business_id']
    }
    xhr_brev.onerror = function(e){
        console.error(xhr_brev.statusText);
    }
    xhr_brev.send(null)
}

function rateClick(args)
{
    rid = args[0]
    attribute = args[1]
    rateRev(rid, attribute)
}

function rateRev(rid, attribute)
{
    var URL = REV_URL + rid
    var xhr_rev = new XMLHttpRequest()
    xhr_rev.open("PUT", URL, true)
    xhr_rev.onload = function(e){
        deleteRev(rid)
    }
    xhr_rev.onerror = function(e) {
        console.error(xhr_rev.statusText)
    }
    xhr_rev.send(JSON.stringify({"attribute":attribute}))
}

function deleteRev(rid)
{
    var URL = REV_URL + rid
    var xhr_del = new XMLHttpRequest()
    xhr_del.open("DELETE", URL, true)
    xhr_del.onload = function(e){
        if(window.rate_zip>0) bizLocClick();
        else if(window.rate_biz>0) bizClick();
        else if(window.rate>0) showRev();
    }
    xhr_del.onerror = function(e){
        console.error(xhr_del.statusText)
    }
    xhr_del.send(null)
}

function bizLocClick()
{
    for(att in attributes){
        if(document.getElementById('b_rate' + attributes[att]).checked)
            window.attribute = document.getElementById('b_rate' + attributes[att]).value;

    }
    window.rate_zip = 1;
    window.rate = 0;
    window.rate_biz = 0;
    fetchTopReviewLocation(window.zipcode, window.attribute)

}

function bizClick()
{
    for(att in attributes){
        if(document.getElementById('b_rate' + attributes[att]).checked)
            window.attribute = document.getElementById('b_rate' + attributes[att]).value;
    }
    window.rate_zip = 0;
    window.rate = 0;
    window.rate_biz = 1;
    fetchBizRev(window.business_id, window.attribute)
}